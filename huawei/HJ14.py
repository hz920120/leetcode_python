while True:
    try:
        n = int(input())
        vac = []
        for _ in range(n):
            word = input()
            vac.append(word)
        vac.sort()
        for w in vac:
            print(w)
    except:
        break