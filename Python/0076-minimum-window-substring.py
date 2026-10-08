class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target = {}

        for ch in t:
            target[ch] = target.get(ch, 0) + 1

        left = 0
        have = 0
        need = len(target)

        window = {}
        result = ""
        result_len = float("inf")

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in target and window[ch] == target[ch]:
                have += 1

            # Contract left while window is valid
            while have == need:
                if right - left + 1 < result_len:
                    result_len = right - left + 1
                    result = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in target and window[left_char] < target[left_char]:
                    have -= 1

                left += 1

        return result
