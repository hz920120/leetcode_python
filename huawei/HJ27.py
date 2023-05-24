while True:
    try:
        data = list(map(str, input().split()))
        words = data[1:-2]
        word = data[-2]
        n = int(data[0])
        k = int(data[-1])
        total = 0
        set = [0] * 26
        brothers = []
        for ch in word:
            set[ord(ch)-ord('a')] += 1

        for i in range(n):
            if words[i] == word or len(word) != len(words[i]):
                continue
            temp = set.copy()
            for ch in words[i]:
                if temp[ord(ch)-ord('a')] != 0:
                    temp[ord(ch)-ord('a')] -= 1
            if sum(temp) == 0:
                total += 1
                brothers.append(words[i])
        brothers.sort()
        print(len(brothers))
        print(brothers[k-1])

    except:
        break