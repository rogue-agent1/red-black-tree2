#!/usr/bin/env python3
"""red_black_tree2 - Red-black tree with insert and search."""
import sys
RED,BLACK=True,False
class Node:
    def __init__(s,key,color=RED):s.key=key;s.color=color;s.left=s.right=s.parent=None
class RBTree:
    def __init__(s):s.NIL=Node(0,BLACK);s.root=s.NIL
    def insert(s,key):
        n=Node(key);n.left=n.right=s.NIL;p=None;c=s.root
        while c!=s.NIL:
            p=c;c=c.left if key<c.key else c.right
        n.parent=p
        if not p:s.root=n
        elif key<p.key:p.left=n
        else:p.right=n
        s._fix_insert(n)
    def _fix_insert(s,z):
        while z.parent and z.parent.color==RED:
            if z.parent==z.parent.parent.left:
                y=z.parent.parent.right
                if y.color==RED:z.parent.color=BLACK;y.color=BLACK;z.parent.parent.color=RED;z=z.parent.parent
                else:
                    if z==z.parent.right:z=z.parent;s._left_rotate(z)
                    z.parent.color=BLACK;z.parent.parent.color=RED;s._right_rotate(z.parent.parent)
            else:
                y=z.parent.parent.left
                if y.color==RED:z.parent.color=BLACK;y.color=BLACK;z.parent.parent.color=RED;z=z.parent.parent
                else:
                    if z==z.parent.left:z=z.parent;s._right_rotate(z)
                    z.parent.color=BLACK;z.parent.parent.color=RED;s._left_rotate(z.parent.parent)
        s.root.color=BLACK
    def _left_rotate(s,x):
        y=x.right;x.right=y.left
        if y.left!=s.NIL:y.left.parent=x
        y.parent=x.parent
        if not x.parent:s.root=y
        elif x==x.parent.left:x.parent.left=y
        else:x.parent.right=y
        y.left=x;x.parent=y
    def _right_rotate(s,y):
        x=y.left;y.left=x.right
        if x.right!=s.NIL:x.right.parent=y
        x.parent=y.parent
        if not y.parent:s.root=x
        elif y==y.parent.right:y.parent.right=x
        else:y.parent.left=x
        x.right=y;y.parent=x
    def search(s,key):
        n=s.root
        while n!=s.NIL:
            if key==n.key:return True
            n=n.left if key<n.key else n.right
        return False
    def inorder(s,n=None):
        if n is None:n=s.root
        if n==s.NIL:return[]
        return s.inorder(n.left)+[n.key]+s.inorder(n.right)
if __name__=="__main__":
    t=RBTree();data=[7,3,18,10,22,8,11,26,2,6,13]
    for d in data:t.insert(d)
    print(f"Inserted: {data}");print(f"Inorder: {t.inorder()}")
    for k in[10,15,22]:print(f"Search {k}: {'found' if t.search(k) else 'not found'}")
