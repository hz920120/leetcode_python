while True:
    try:
        s = input()
        m = []
        se = set()
        for ch in [*s]:
            if ch not in se:
                se.add(ch)
                m.append(ch)
            else:
                if ch in m:
                    m.remove(ch)

        print(-1 if len(m) == 0 else m[0])
    except:
        break