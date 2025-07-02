n, k = list(map(int, input().split()))
blue = (8*n)/k
red = (2*n)/k
green = (5*n)/k
if blue>int(blue):
    blue= int(blue)+1
if red > int(red):
    red = int(red)+1
if green > int(green):
    green = int(green)+1

print(int(red+blue+green))