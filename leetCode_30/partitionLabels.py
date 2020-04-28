class Solution:
    def partitionLabels_(self, S):
        last_seen_d = {}
        for i, char in enumerate(S):
            last_seen_d[char] = i

        last_seen = 0
        count = 0
        res = []
        for i, char in enumerate(S):
            last_seen = max(last_seen, last_seen_d[char])
            count += 1
            if last_seen == i:
                res.append(count)
                count = 0

        print(res)

    def partitionLabels(self, S):
        char_ranges = {}
        for i, char in enumerate(S):
            if char_ranges.get(char):
                char_ranges[char][1] = i
            else:
                char_ranges[char] = [i, i]

        ranges = []
        res = []
        for char, r in char_ranges.items():
            ranges.append(r)

        ranges.sort()

        start, end = None, None
        for r in ranges:
            current_start, current_end = r
            if start == None:
                start, end = r
            else:
                if start <= current_start <= end or start <= current_end <= end:
                    start = min(start, current_start)
                    end = max(end, current_end)
                else:
                    res.append(end-start+1)
                    start, end = r
        res.append(end-start+1)

        print(res)


sol = Solution()
s = 'ababcbacadefegdehijhklij'
sol.partitionLabels(s)
