'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000'''

# Result

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        table = [['' for i in s] for i in range(numRows)]
        activeCol = 0
        activeRow = 0
        letter = 0
        while letter <= len(s)-1:
            if activeRow == 0:
                while activeRow < numRows and letter <= len(s)-1:
                    table[activeRow][activeCol] = s[letter]
                    letter += 1
                    activeRow += 1
                activeCol += 1
            
            if activeRow == numRows:
                activeRow -= 1
                while activeRow > 1 and letter <= len(s)-1:
                    activeRow -= 1
                    table[activeRow][activeCol] = s[letter]
                    activeCol += 1
                    letter += 1
                activeRow = 0
        return ''.join([''.join(i) for i in table])
