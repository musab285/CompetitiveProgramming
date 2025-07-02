while True:
    try:
        n = int(input())
        facts = set()
        facts.add(1)
        for i in range(1, int(n**0.5)+1):
            if n%i==0 and (i!=n and n//i!=n) :
                facts.add(i)
                facts.add(n//i)
        if sum(facts) == n:
            print(f"{n} perfect")
        elif abs(sum(facts) - n) <= 2:
            print(f"{n} almost perfect")
        else:
            print(f"{n} not perfect")
    except EOFError:
        break