#!/usr/bin/env python3
"""red_black_tree2 — Red-Black tree with insert and balancing. Zero deps."""

RED, BLACK = True, False

class Node:
    __slots__ = ('key','color','left','right','parent')
    def __init__(self, key, color=RED):
        self.key, self.color = key, color
        self.left = self.right = self.parent = None

class RBTree:
    def __init__(self):
        self.NIL = Node(None, BLACK)
        self.root = self.NIL

    def insert(self, key):
        node = Node(key)
        node.left = node.right = self.NIL
        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            current = current.left if key < current.key else current.right
        node.parent = parent
        if not parent: self.root = node
        elif key < parent.key: parent.left = node
        else: parent.right = node
        self._fix_insert(node)

    def _fix_insert(self, z):
        while z.parent and z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                uncle = z.parent.parent.right
                if uncle.color == RED:
                    z.parent.color = uncle.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent; self._rotate_left(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rotate_right(z.parent.parent)
            else:
                uncle = z.parent.parent.left
                if uncle.color == RED:
                    z.parent.color = uncle.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent; self._rotate_right(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rotate_left(z.parent.parent)
        self.root.color = BLACK

    def _rotate_left(self, x):
        y = x.right; x.right = y.left
        if y.left != self.NIL: y.left.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y

    def _rotate_right(self, x):
        y = x.left; x.left = y.right
        if y.right != self.NIL: y.right.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.right: x.parent.right = y
        else: x.parent.left = y
        y.right = x; x.parent = y

    def inorder(self):
        result = []
        def _io(n):
            if n == self.NIL: return
            _io(n.left); result.append((n.key, 'R' if n.color == RED else 'B')); _io(n.right)
        _io(self.root)
        return result

    def black_height(self, node=None):
        if node is None: node = self.root
        if node == self.NIL: return 1
        return self.black_height(node.left) + (1 if node.color == BLACK else 0)

def main():
    tree = RBTree()
    for x in [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]:
        tree.insert(x)
    print(f"Red-Black Tree (black-height={tree.black_height()}):")
    print(f"  Root: {tree.root.key} ({('R' if tree.root.color == RED else 'B')})")
    for key, color in tree.inorder():
        print(f"  {key:>3} [{color}]")

if __name__ == "__main__":
    main()
