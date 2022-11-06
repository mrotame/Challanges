2. Add Two Numbers
Medium
22.4K
4.4K
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Result

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.returnNode(str(int(''.join(self.returnList(l1))) + int(''.join(self.returnList(l2)))))

    def returnList(self, node):
        array = [node.val]
        next = node.next
        while next is not None:
            array.append(next.val)
            next = next.next
        return reversed([str(i) for i in array])

    def returnNode(self, array):
        last_node = None
        for i in range(len(array)):
            last_node = ListNode(int(array[i]), last_node)
        print(last_node)
        return(last_node)
