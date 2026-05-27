"""LeetCode 100. Same Tree.

https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if
they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    _ = (p, q)
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)