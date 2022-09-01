"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

"""
class Solution:
    def connect(self, root):
        head = root
        while root:
            cur, root = root, root.left
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                    if cur.next: 
                        cur.right.next = cur.next.left
                else: 
                    break
                cur = cur.next
                
        return head
