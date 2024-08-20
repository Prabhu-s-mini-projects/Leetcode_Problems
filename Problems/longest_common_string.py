# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for word in strs:
            prefix = prefix[: len(prefix) if len(prefix) < len(word) else len(word)]
            for i in range(len(prefix)):
                if prefix[i] == word[i]:
                    continue
                else:
                    prefix = prefix[:i]
                    break
        return prefix if prefix != "" else ""
