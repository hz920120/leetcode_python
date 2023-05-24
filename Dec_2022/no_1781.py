import sys


class Solution(object):
    def cal_beauty(self, str):
        char_freq = {}
        for i in range(len(str)):
            if str[i] in char_freq:
                freq = char_freq.get(str[i])
                char_freq[str[i]] = freq + 1
            else:
                char_freq[str[i]] = 1

        min, max = sys.maxsize, 0
        for key in char_freq.keys():
            freq = char_freq.get(key)
            if freq < min:
                min = freq
            if freq > max:
                max = freq
        return max - min

    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        # key: sub word, value: beauty value
        sub_map = {}
        # slide window
        total = 0
        for window_size in range(len(s)+1, 3, -1):
            l_index = 0
            r_index = l_index + window_size
            while r_index <= len(s):
                if s[l_index:r_index] in sub_map:
                    total += sub_map.get(s[l_index:r_index])
                if s[l_index:r_index] not in sub_map:
                    v = self.cal_beauty(s[l_index:r_index])
                    total += v
                    sub_map[s[l_index:r_index]] = v
                l_index += 1
                r_index += 1
        return total


if __name__ == '__main__':
    # for i in range(6, 3, -1):
    #     print(i)
    s = Solution()

    str = 'kcgdnprqxcmpcavjzjgvgekzsvoejxwrdsidzitpzcegxrrrnayndadtqwqswuinzyhdewzzvukqbzobylcporryqpurrzzmidrjcgtfoeyycrsbpbinbzweirmlamaajudtaermybbopxknkwalbnowfsevnodehzdalgailizfvnenmfuatxieorjaybxilmjsslalgeecmsbqwdjntfoaizbpmxekrtesrguepsevaymfwetnddblkbrirhrxrxvrpnqtazyurmwmlxtxczsypiycedwdgyzelbyapgfmedpzbfjfmbtydaqnshncgciqhatuzzpjklomxxqkdvrcwpotadandkwkfnrgiugpxyfjzzwkfdlvytfufxpsdwgmrqzufghuyq'
    print(s.beautySum(str))
    # print(s[0:3])