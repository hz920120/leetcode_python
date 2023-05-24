while True:
    try:
        inp = input()
        is_ip = True
        if len(inp.split('.')) == 1:
            is_ip = False

        def fill_zero(x, l):
            while len(x) < l:
                x = '0' + x
            return x

        def to_ip(s):
            # s:长整形
            bin_32 = fill_zero(bin(int(s)).replace('0b', ''), 32)
            ip = ''
            for i in range(0,32,8):
                ip_t = str(int(bin_32[i:i+8], 2))
                ip += ip_t + '.'
            return ip[:-1]

        def to_int(x):
            # X:ip address
            ip_list = x.split('.')
            res = ''
            for ip in ip_list:
                res += fill_zero(bin(int(ip)).replace('0b',''), 8)
            return int(res, 2)

        if is_ip:
            print(to_int(inp))
        else:
            print(to_ip(inp))
    except:
        break


if __name__ == '__main__':
    print('10.0.3.193'.split('.'))