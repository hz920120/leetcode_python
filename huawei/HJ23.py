import sys

while True:
    try:
        s = input()

        bucket = [0]*26
        for c in s:
                bucket[ord(c) - ord('a')] += 1
        min = sys.maxsize
        for i, count in enumerate(bucket):
            if bucket[i] < min and count != 0:
                min = bucket[i]
        for i, count in enumerate(bucket):
            if count == min:
                s = s.replace(chr(ord('a') + i), '')
        print(s)

    except:
        break