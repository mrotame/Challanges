'''Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.'''

#Result

class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = ''
        for i in range(len(s)):
            if len(x := self.checkPalindrome(s, i, i)) > len(longest): longest = x
            if len(x := self.checkPalindrome(s, i, i+1)) > len(longest): longest = x
        return longest

    def returnPalindrome(self, s: str, leftIndex:int, rightIndex:int):
        while(leftIndex>=0 and rightIndex<len(s) and s[leftIndex] == s[rightIndex]):
            leftIndex -= 1
            rightIndex += 1
        return s[leftIndex+1:rightIndex]
