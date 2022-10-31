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
    numRows: int
    table: list
    activeCol = 0
    activeRow = 0
    letter = 0
    
    def convert(self, s: str, numRows: int) -> str:
        self.numRows = numRows
        self.table = [['' for i in s] for i in range(numRows)]
        while self.letter <= len(s)-1:
            if self.activeRow == 0:
                self.allWayDown(s)
            if self.activeRow == self.numRows:
                self.stairUp(s)
        return ''.join([''.join(i) for i in self.table])

    def allWayDown(self, s:str)->None:
        while self.activeRow < self.numRows and self.letter <= len(s)-1:
            self.table[self.activeRow][self.activeCol] = s[self.letter]
            self.letter += 1
            self.activeRow += 1
        self.activeCol += 1
    
    def stairUp(self, s:str)->None:
        self.activeRow -= 1
        while self.activeRow > 1 and self.letter <= len(s)-1:
            self.activeRow -= 1
            self.table[self.activeRow][self.activeCol] = s[self.letter]
            self.activeCol += 1
            self.letter += 1
        self.activeRow = 0
    
