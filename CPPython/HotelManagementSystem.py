"""
Hotel Management System
Single-file Python application using Tkinter for GUI and SQLite for storage.
Features:
- Manage Rooms (add/edit/delete)
- Manage Guests (add/edit/delete)
- Create Bookings (new booking, check-in, check-out)
- Simple reports (occupancy, revenue) and CSV export
No external libraries required — runs with Python 3.x (tested on 3.8+)

Save this file as HotelManagementSystem.py and run: python HotelManagementSystem.py
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import sqlite3
from datetime import datetime, date
import csv

DB_NAME = 'hotel.db'

# ---------------------------- Database ----------------------------
class DB:
    def __init__(self, db_name=DB_NAME):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.ensure_schema()

    def ensure_schema(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number TEXT UNIQUE NOT NULL,
                type TEXT NOT NULL,
                price REAL NOT NULL,
                status TEXT NOT NULL DEFAULT 'available' -- available/booked/out
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS guests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                guest_id INTEGER NOT NULL,
                room_id INTEGER NOT NULL,
                checkin_date TEXT NOT NULL,
                checkout_date TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'booked', -- booked, checked-in, checked-out, cancelled
                total REAL DEFAULT 0,
                FOREIGN KEY(guest_id) REFERENCES guests(id),
                FOREIGN KEY(room_id) REFERENCES rooms(id)
            )
        ''')
        self.conn.commit()

    # Rooms
    def add_room(self, number, rtype, price):
        c = self.conn.cursor()
        c.execute('INSERT INTO rooms(number,type,price) VALUES (?, ?, ?)', (number, rtype, price))
        self.conn.commit()

    def update_room(self, room_id, number, rtype, price, status):
        c = self.conn.cursor()
        c.execute('UPDATE rooms SET number=?, type=?, price=?, status=? WHERE id=?', (number, rtype, price, status, room_id))
        self.conn.commit()

    def delete_room(self, room_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM rooms WHERE id=?', (room_id,))
        self.conn.commit()

    def get_rooms(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM rooms ORDER BY number')
        return c.fetchall()

    def get_available_rooms_between(self, checkin, checkout):
        # selects rooms that are not booked between dates
        c = self.conn.cursor()
        c.execute('''
            SELECT * FROM rooms r WHERE r.id NOT IN (
                SELECT room_id FROM bookings b
                WHERE b.status IN ('booked','checked-in')
                AND NOT (date(b.checkout_date) <= date(?) OR date(b.checkin_date) >= date(?))
            )
            ORDER BY number
        ''', (checkin, checkout))
        return c.fetchall()

    # Guests
    def add_guest(self, name, phone, email):
        c = self.conn.cursor()
        c.execute('INSERT INTO guests(name,phone,email) VALUES (?, ?, ?)', (name, phone, email))
        self.conn.commit()
        return c.lastrowid

    def update_guest(self, guest_id, name, phone, email):
        c = self.conn.cursor()
        c.execute('UPDATE guests SET name=?, phone=?, email=? WHERE id=?', (name, phone, email, guest_id))
        self.conn.commit()

    def delete_guest(self, guest_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM guests WHERE id=?', (guest_id,))
        self.conn.commit()

    def get_guests(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM guests ORDER BY name')
        return c.fetchall()

    # Bookings
    def add_booking(self, guest_id, room_id, checkin_date, checkout_date, total):
        c = self.conn.cursor()
        c.execute('INSERT INTO bookings(guest_id,room_id,checkin_date,checkout_date,total) VALUES (?,?,?,?,?)',
                  (guest_id, room_id, checkin_date, checkout_date, total))
        self.conn.commit()
        # set room status to booked
        c.execute('UPDATE rooms SET status=? WHERE id=?', ('booked', room_id))
        self.conn.commit()

    def update_booking_status(self, booking_id, status):
        c = self.conn.cursor()
        c.execute('UPDATE bookings SET status=? WHERE id=?', (status, booking_id))
        self.conn.commit()
        # adjust room status accordingly
        c.execute('SELECT room_id FROM bookings WHERE id=?', (booking_id,))
        row = c.fetchone()
        if row:
            rid = row['room_id']
            if status == 'checked-in':
                c.execute('UPDATE rooms SET status=? WHERE id=?', ('occupied', rid))
            elif status in ('checked-out','cancelled'):
                c.execute('UPDATE rooms SET status=? WHERE id=?', ('available', rid))
            elif status == 'booked':
                c.execute('UPDATE rooms SET status=? WHERE id=?', ('booked', rid))
            self.conn.commit()

    def get_bookings(self):
        c = self.conn.cursor()
        c.execute('''
            SELECT b.*, g.name as guest_name, r.number as room_number, r.type as room_type
            FROM bookings b
            JOIN guests g ON g.id=b.guest_id
            JOIN rooms r ON r.id=b.room_id
            ORDER BY b.checkin_date DESC
        ''')
        return c.fetchall()

    def get_bookings_between(self, start, end):
        c = self.conn.cursor()
        c.execute('''
            SELECT b.*, g.name as guest_name, r.number as room_number
            FROM bookings b
            JOIN guests g ON g.id=b.guest_id
            JOIN rooms r ON r.id=b.room_id
            WHERE date(b.checkin_date) >= date(?) AND date(b.checkin_date) <= date(?)
            ORDER BY b.checkin_date
        ''', (start, end))
        return c.fetchall()

    def close(self):
        self.conn.close()

# ---------------------------- GUI ----------------------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hotel Management System')
        self.geometry('1000x650')
        self.db = DB()
        self.create_widgets()

    def create_widgets(self):
        nb = ttk.Notebook(self)
        nb.pack(fill='both', expand=True)

        self.rooms_frame = ttk.Frame(nb)
        self.guests_frame = ttk.Frame(nb)
        self.bookings_frame = ttk.Frame(nb)
        self.reports_frame = ttk.Frame(nb)

        nb.add(self.rooms_frame, text='Rooms')
        nb.add(self.guests_frame, text='Guests')
        nb.add(self.bookings_frame, text='Bookings')
        nb.add(self.reports_frame, text='Reports')

        self.build_rooms_tab()
        self.build_guests_tab()
        self.build_bookings_tab()
        self.build_reports_tab()

    # ---------------- Rooms Tab ----------------
    def build_rooms_tab(self):
        top = ttk.Frame(self.rooms_frame)
        top.pack(fill='x', padx=10, pady=8)

        add_btn = ttk.Button(top, text='Add Room', command=self.room_add_dialog)
        edit_btn = ttk.Button(top, text='Edit Selected', command=self.room_edit_selected)
        del_btn = ttk.Button(top, text='Delete Selected', command=self.room_delete_selected)
        refresh_btn = ttk.Button(top, text='Refresh', command=self.rooms_load)

        add_btn.pack(side='left', padx=4)
        edit_btn.pack(side='left', padx=4)
        del_btn.pack(side='left', padx=4)
        refresh_btn.pack(side='left', padx=4)

        cols = ('id','number','type','price','status')
        self.rooms_tree = ttk.Treeview(self.rooms_frame, columns=cols, show='headings')
        for c in cols:
            self.rooms_tree.heading(c, text=c.title())
        self.rooms_tree.column('id', width=40)
        self.rooms_tree.pack(fill='both', expand=True, padx=10, pady=6)

        self.rooms_load()

    def rooms_load(self):
        for r in self.rooms_tree.get_children():
            self.rooms_tree.delete(r)
        for row in self.db.get_rooms():
            self.rooms_tree.insert('', 'end', values=(row['id'], row['number'], row['type'], f"{row['price']:.2f}", row['status']))

    def room_add_dialog(self):
        dlg = RoomDialog(self, title='Add Room')
        self.wait_window(dlg)
        if dlg.result:
            number, rtype, price = dlg.result
            try:
                self.db.add_room(number, rtype, float(price))
                self.rooms_load()
            except Exception as e:
                messagebox.showerror('Error', str(e))

    def room_edit_selected(self):
        sel = self.rooms_tree.selection()
        if not sel:
            messagebox.showinfo('Info', 'Select a room first')
            return
        item = self.rooms_tree.item(sel[0])
        rid, number, rtype, price, status = item['values']
        dlg = RoomDialog(self, title='Edit Room', initial=(number, rtype, price, status))
        self.wait_window(dlg)
        if dlg.result:
            number, rtype, price, = dlg.result
            try:
                self.db.update_room(rid, number, rtype, float(price), status)
                self.rooms_load()
            except Exception as e:
                messagebox.showerror('Error', str(e))

    def room_delete_selected(self):
        sel = self.rooms_tree.selection()
        if not sel:
            messagebox.showinfo('Info', 'Select a room first')
            return
        item = self.rooms_tree.item(sel[0])
        rid = item['values'][0]
        if messagebox.askyesno('Confirm', 'Delete selected room?'):
            try:
                self.db.delete_room(rid)
                self.rooms_load()
            except Exception as e:
                messagebox.showerror('Error', str(e))

    # ---------------- Guests Tab ----------------
    def build_guests_tab(self):
        top = ttk.Frame(self.guests_frame)
        top.pack(fill='x', padx=10, pady=8)

        add_btn = ttk.Button(top, text='Add Guest', command=self.guest_add_dialog)
        edit_btn = ttk.Button(top, text='Edit Selected', command=self.guest_edit_selected)
        del_btn = ttk.Button(top, text='Delete Selected', command=self.guest_delete_selected)
        refresh_btn = ttk.Button(top, text='Refresh', command=self.guests_load)

        add_btn.pack(side='left', padx=4)
        edit_btn.pack(side='left', padx=4)
        del_btn.pack(side='left', padx=4)
        refresh_btn.pack(side='left', padx=4)

        cols = ('id','name','phone','email')
        self.guests_tree = ttk.Treeview(self.guests_frame, columns=cols, show='headings')
        for c in cols:
            self.guests_tree.heading(c, text=c.title())
        self.guests_tree.column('id', width=40)
        self.guests_tree.pack(fill='both', expand=True, padx=10, pady=6)

        self.guests_load()

    def guests_load(self):
        for r in self.guests_tree.get_children():
            self.guests_tree.delete(r)
        for row in self.db.get_guests():
            self.guests_tree.insert('', 'end', values=(row['id'], row['name'], row['phone'] or '', row['email'] or ''))

    def guest_add_dialog(self):
        dlg = GuestDialog(self, title='Add Guest')
        self.wait_window(dlg)
        if dlg.result:
            name, phone, email = dlg.result
            try:
                self.db.add_guest(name, phone, email)
                self.guests_load()
            except Exception as e:
                messagebox.showerror('Error', str(e))

    def guest_edit_selected(self):
        sel = self.guests_tree.selection()
        if not sel:
            messagebox.showinfo('Info', 'Select a guest first')
            return
        item = self.guests_tree.item(sel[0])
        gid, name, phone, email = item['values']
        dlg = GuestDialog(self, title='Edit Guest', initial=(name, phone, email))
        self.wait_window(dlg)
        if dlg.result:
            name, phone, email = dlg.result
            try:
                self.db.update_guest(gid, name, phone, email)
                self.guests_load()
            except Exception as e:
                messagebox.showerror('Error', str(e))

    def guest_delete_selected(self):
        sel = self.guests_tree.selection()
        if not sel:
            messagebox.showinfo('Info', 'Select a guest first')
            return
        item = self.guests_tree.item(sel[0])
        gid = item['values'][0]
        if messagebox.askyesno('Confirm', 'Delete selected guest?'):
            try:
                self.db.delete_guest(gid)
                self.guests_load()
            except Exception as e:
                messagebox.showerror('Error', str(e))

    # ---------------- Bookings Tab ----------------
    def build_bookings_tab(self):
        top = ttk.Frame(self.bookings_frame)
        top.pack(fill='x', padx=10, pady=8)

        add_btn = ttk.Button(top, text='New Booking', command=self.booking_new_dialog)
        checkin_btn = ttk.Button(top, text='Check-in Selected', command=lambda: self.booking_change_status('checked-in'))
        checkout_btn = ttk.Button(top, text='Check-out Selected', command=lambda: self.booking_change_status('checked-out'))
        cancel_btn = ttk.Button(top, text='Cancel Selected', command=lambda: self.booking_change_status('cancelled'))
        refresh_btn = ttk.Button(top, text='Refresh', command=self.bookings_load)

        for b in (add_btn, checkin_btn, checkout_btn, cancel_btn, refresh_btn):
            b.pack(side='left', padx=4)

        cols = ('id','guest','room','checkin','checkout','status','total')
        self.bookings_tree = ttk.Treeview(self.bookings_frame, columns=cols, show='headings')
        for c in cols:
            self.bookings_tree.heading(c, text=c.title())
        self.bookings_tree.column('id', width=40)
        self.bookings_tree.pack(fill='both', expand=True, padx=10, pady=6)

        self.bookings_load()

    def bookings_load(self):
        for r in self.bookings_tree.get_children():
            self.bookings_tree.delete(r)
        for row in self.db.get_bookings():
            self.bookings_tree.insert('', 'end', values=(row['id'], row['guest_name'], row['room_number'], row['checkin_date'], row['checkout_date'], row['status'], f"{row['total']:.2f}"))

    def booking_new_dialog(self):
        dlg = BookingDialog(self, self.db)
        self.wait_window(dlg)
        if dlg.result:
            guest_id, room_id, checkin, checkout, total = dlg.result
            try:
                self.db.add_booking(guest_id, room_id, checkin, checkout, total)
                self.bookings_load()
                self.rooms_load()
            except Exception as e:
                messagebox.showerror('Error', str(e))

    def booking_change_status(self, new_status):
        sel = self.bookings_tree.selection()
        if not sel:
            messagebox.showinfo('Info', 'Select a booking first')
            return
        item = self.bookings_tree.item(sel[0])
        bid = item['values'][0]
        if messagebox.askyesno('Confirm', f'Change status to {new_status}?'):
            try:
                self.db.update_booking_status(bid, new_status)
                self.bookings_load()
                self.rooms_load()
            except Exception as e:
                messagebox.showerror('Error', str(e))

    # ---------------- Reports Tab ----------------
    def build_reports_tab(self):
        frm = ttk.Frame(self.reports_frame)
        frm.pack(fill='x', padx=10, pady=8)

        ttk.Label(frm, text='From (YYYY-MM-DD)').pack(side='left')
        self.rep_from = ttk.Entry(frm, width=12)
        self.rep_from.pack(side='left', padx=4)
        ttk.Label(frm, text='To (YYYY-MM-DD)').pack(side='left')
        self.rep_to = ttk.Entry(frm, width=12)
        self.rep_to.pack(side='left', padx=4)
        run_btn = ttk.Button(frm, text='Run Report', command=self.run_report)
        export_btn = ttk.Button(frm, text='Export CSV', command=self.export_report)
        run_btn.pack(side='left', padx=6)
        export_btn.pack(side='left', padx=6)

        cols = ('id','guest','room','checkin','checkout','status','total')
        self.report_tree = ttk.Treeview(self.reports_frame, columns=cols, show='headings')
        for c in cols:
            self.report_tree.heading(c, text=c.title())
        self.report_tree.column('id', width=40)
        self.report_tree.pack(fill='both', expand=True, padx=10, pady=6)

    def run_report(self):
        start = self.rep_from.get().strip()
        end = self.rep_to.get().strip()
        if not start or not end:
            messagebox.showinfo('Info', 'Please enter both dates')
            return
        try:
            rows = self.db.get_bookings_between(start, end)
        except Exception as e:
            messagebox.showerror('Error', str(e))
            return
        for r in self.report_tree.get_children():
            self.report_tree.delete(r)
        total_revenue = 0
        occupied = 0
        for row in rows:
            self.report_tree.insert('', 'end', values=(row['id'], row['guest_name'], row['room_number'], row['checkin_date'], row['checkout_date'], row['status'], f"{row['total']:.2f}"))
            total_revenue += row['total'] or 0
            if row['status'] == 'checked-in':
                occupied += 1
        messagebox.showinfo('Report Summary', f'Total bookings: {len(rows)}\nTotal revenue: {total_revenue:.2f}\nCurrently occupied (in range): {occupied}')

    def export_report(self):
        items = self.report_tree.get_children()
        if not items:
            messagebox.showinfo('Info', 'Run a report first')
            return
        path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV files','*.csv')])
        if not path:
            return
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id','guest','room','checkin','checkout','status','total'])
            for it in items:
                writer.writerow(self.report_tree.item(it)['values'])
        messagebox.showinfo('Exported', f'Exported to {path}')

# ---------------- Dialogs ----------------
class RoomDialog(tk.Toplevel):
    def __init__(self, parent, title='Room', initial=None):
        super().__init__(parent)
        self.title(title)
        self.result = None
        self.transient(parent)
        self.grab_set()
        ttk.Label(self, text='Room Number').grid(row=0, column=0, padx=8, pady=6)
        self.ent_number = ttk.Entry(self)
        self.ent_number.grid(row=0, column=1, padx=8, pady=6)
        ttk.Label(self, text='Type').grid(row=1, column=0, padx=8, pady=6)
        self.ent_type = ttk.Entry(self)
        self.ent_type.grid(row=1, column=1, padx=8, pady=6)
        ttk.Label(self, text='Price per night').grid(row=2, column=0, padx=8, pady=6)
        self.ent_price = ttk.Entry(self)
        self.ent_price.grid(row=2, column=1, padx=8, pady=6)
        btn = ttk.Button(self, text='OK', command=self.on_ok)
        btn.grid(row=3, column=0, columnspan=2, pady=8)
        if initial:
            num, rtype, price, status = initial
            self.ent_number.insert(0, num)
            self.ent_type.insert(0, rtype)
            self.ent_price.insert(0, price)

    def on_ok(self):
        number = self.ent_number.get().strip()
        rtype = self.ent_type.get().strip()
        price = self.ent_price.get().strip()
        if not number or not rtype or not price:
            messagebox.showinfo('Info', 'Fill all fields')
            return
        try:
            float(price)
        except:
            messagebox.showinfo('Info', 'Price must be a number')
            return
        self.result = (number, rtype, price)
        self.destroy()

class GuestDialog(tk.Toplevel):
    def __init__(self, parent, title='Guest', initial=None):
        super().__init__(parent)
        self.title(title)
        self.result = None
        self.transient(parent)
        self.grab_set()
        ttk.Label(self, text='Name').grid(row=0, column=0, padx=8, pady=6)
        self.ent_name = ttk.Entry(self)
        self.ent_name.grid(row=0, column=1, padx=8, pady=6)
        ttk.Label(self, text='Phone').grid(row=1, column=0, padx=8, pady=6)
        self.ent_phone = ttk.Entry(self)
        self.ent_phone.grid(row=1, column=1, padx=8, pady=6)
        ttk.Label(self, text='Email').grid(row=2, column=0, padx=8, pady=6)
        self.ent_email = ttk.Entry(self)
        self.ent_email.grid(row=2, column=1, padx=8, pady=6)
        btn = ttk.Button(self, text='OK', command=self.on_ok)
        btn.grid(row=3, column=0, columnspan=2, pady=8)
        if initial:
            name, phone, email = initial
            self.ent_name.insert(0, name)
            self.ent_phone.insert(0, phone)
            self.ent_email.insert(0, email)

    def on_ok(self):
        name = self.ent_name.get().strip()
        phone = self.ent_phone.get().strip()
        email = self.ent_email.get().strip()
        if not name:
            messagebox.showinfo('Info', 'Name required')
            return
        self.result = (name, phone, email)
        self.destroy()

class BookingDialog(tk.Toplevel):
    def __init__(self, parent, db: DB):
        super().__init__(parent)
        self.title('New Booking')
        self.result = None
        self.db = db
        self.transient(parent)
        self.grab_set()

        # Guest selection
        ttk.Label(self, text='Select Guest').grid(row=0, column=0, padx=8, pady=6)
        self.cmb_guest = ttk.Combobox(self, values=[f"{g['id']}: {g['name']}" for g in db.get_guests()], width=35)
        self.cmb_guest.grid(row=0, column=1, padx=8, pady=6)
        ttk.Button(self, text='Add Guest', command=self.add_guest_inline).grid(row=0, column=2, padx=6)

        # Dates
        ttk.Label(self, text='Check-in (YYYY-MM-DD)').grid(row=1, column=0, padx=8, pady=6)
        self.ent_checkin = ttk.Entry(self)
        self.ent_checkin.grid(row=1, column=1, padx=8, pady=6)
        ttk.Label(self, text='Check-out (YYYY-MM-DD)').grid(row=2, column=0, padx=8, pady=6)
        self.ent_checkout = ttk.Entry(self)
        self.ent_checkout.grid(row=2, column=1, padx=8, pady=6)

        ttk.Label(self, text='Available Rooms').grid(row=3, column=0, padx=8, pady=6)
        self.cmb_rooms = ttk.Combobox(self, values=[], width=35)
        self.cmb_rooms.grid(row=3, column=1, padx=8, pady=6)
        ttk.Button(self, text='Check Availability', command=self.check_availability).grid(row=3, column=2, padx=6)

        ttk.Label(self, text='Total (auto)').grid(row=4, column=0, padx=8, pady=6)
        self.ent_total = ttk.Entry(self)
        self.ent_total.grid(row=4, column=1, padx=8, pady=6)

        ttk.Button(self, text='Book', command=self.on_book).grid(row=5, column=0, columnspan=3, pady=10)

    def add_guest_inline(self):
        dlg = GuestDialog(self, title='Add Guest')
        self.wait_window(dlg)
        if dlg.result:
            name, phone, email = dlg.result
            gid = self.db.add_guest(name, phone, email)
            self.cmb_guest['values'] = [f"{g['id']}: {g['name']}" for g in self.db.get_guests()]
            # select new guest
            self.cmb_guest.set(f"{gid}: {name}")

    def check_availability(self):
        ci = self.ent_checkin.get().strip()
        co = self.ent_checkout.get().strip()
        try:
            ci_d = datetime.strptime(ci, '%Y-%m-%d').date()
            co_d = datetime.strptime(co, '%Y-%m-%d').date()
            if ci_d >= co_d:
                messagebox.showinfo('Info', 'Checkout must be after checkin')
                return
        except Exception as e:
            messagebox.showinfo('Info', 'Enter valid dates in YYYY-MM-DD')
            return
        rooms = self.db.get_available_rooms_between(ci, co)
        if not rooms:
            messagebox.showinfo('Info', 'No rooms available for these dates')
            return
        vals = [f"{r['id']}: {r['number']} ({r['type']}) - {r['price']:.2f}" for r in rooms]
        self.cmb_rooms['values'] = vals
        # default select first
        if vals:
            self.cmb_rooms.set(vals[0])
            # set total
            nights = (co_d - ci_d).days
            price = rooms[0]['price']
            self.ent_total.delete(0, tk.END)
            self.ent_total.insert(0, f"{(nights * price):.2f}")

    def on_book(self):
        guest_text = self.cmb_guest.get().strip()
        room_text = self.cmb_rooms.get().strip()
        ci = self.ent_checkin.get().strip()
        co = self.ent_checkout.get().strip()
        total_text = self.ent_total.get().strip()
        if not guest_text or not room_text or not ci or not co:
            messagebox.showinfo('Info', 'Fill all fields and check availability')
            return
        try:
            guest_id = int(guest_text.split(':')[0])
            room_id = int(room_text.split(':')[0])
            total = float(total_text)
        except Exception as e:
            messagebox.showinfo('Info', 'Invalid guest or room selection')
            return
        # store
        self.result = (guest_id, room_id, ci, co, total)
        self.destroy()

# ---------------------------- Run ----------------------------
if __name__ == '__main__':
    app = App()
    app.mainloop()
