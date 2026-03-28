#!/usr/bin/env python3
"""Red-Black Tree — zero-dep."""
BLACK=0; RED=1

class RBNode:
    def __init__(self, key, color=RED):
        self.key=key; self.color=color; self.left=self.right=self.parent=None

class RBTree:
    def __init__(self):
        self.NIL=RBNode(None,BLACK); self.root=self.NIL
    def insert(self, key):
        z=RBNode(key); z.left=z.right=self.NIL; y=None; x=self.root
        while x!=self.NIL:
            y=x; x=x.left if key<x.key else x.right
        z.parent=y
        if y is None: self.root=z
        elif key<y.key: y.left=z
        else: y.right=z
        self._fix_insert(z)
    def _fix_insert(self, z):
        while z.parent and z.parent.color==RED:
            if z.parent==z.parent.parent.left:
                u=z.parent.parent.right
                if u.color==RED:
                    z.parent.color=BLACK; u.color=BLACK; z.parent.parent.color=RED; z=z.parent.parent
                else:
                    if z==z.parent.right: z=z.parent; self._left_rotate(z)
                    z.parent.color=BLACK; z.parent.parent.color=RED; self._right_rotate(z.parent.parent)
            else:
                u=z.parent.parent.left
                if u.color==RED:
                    z.parent.color=BLACK; u.color=BLACK; z.parent.parent.color=RED; z=z.parent.parent
                else:
                    if z==z.parent.left: z=z.parent; self._right_rotate(z)
                    z.parent.color=BLACK; z.parent.parent.color=RED; self._left_rotate(z.parent.parent)
        self.root.color=BLACK
    def _left_rotate(self, x):
        y=x.right; x.right=y.left
        if y.left!=self.NIL: y.left.parent=x
        y.parent=x.parent
        if x.parent is None: self.root=y
        elif x==x.parent.left: x.parent.left=y
        else: x.parent.right=y
        y.left=x; x.parent=y
    def _right_rotate(self, y):
        x=y.left; y.left=x.right
        if x.right!=self.NIL: x.right.parent=y
        x.parent=y.parent
        if y.parent is None: self.root=x
        elif y==y.parent.right: y.parent.right=x
        else: y.parent.left=x
        x.right=y; y.parent=x
    def inorder(self):
        result=[]
        def _in(n):
            if n!=self.NIL: _in(n.left); result.append((n.key,"R" if n.color==RED else "B")); _in(n.right)
        _in(self.root); return result
    def search(self, key):
        n=self.root
        while n!=self.NIL:
            if key==n.key: return True
            n=n.left if key<n.key else n.right
        return False
    def height(self):
        def _h(n): return 0 if n==self.NIL else 1+max(_h(n.left),_h(n.right))
        return _h(self.root)

if __name__=="__main__":
    t=RBTree()
    for k in [7,3,18,10,22,8,11,26,2,6,13]:
        t.insert(k)
    print(f"Inorder: {t.inorder()}")
    print(f"Root: {t.root.key} ({'R' if t.root.color==RED else 'B'})")
    print(f"Height: {t.height()}")
    print(f"Search 10: {t.search(10)}, Search 99: {t.search(99)}")
