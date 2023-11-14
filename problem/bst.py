#이진 검색 트리 구현

from __future__ import annotations
from typing import Any, Type

class Node:

    def __init__(self, key: Any, value: Any, left: Node = None,
                right: Node = None):

        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        self.root = None # 루트
        
    def search(self, key: Any) -> Any:
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right
                