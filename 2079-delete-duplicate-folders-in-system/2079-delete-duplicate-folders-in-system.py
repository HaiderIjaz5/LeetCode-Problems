from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()

        # Step 1: Build the Trie from paths
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]

        # Step 2: Serialize each subtree to find duplicates
        subtree_map = defaultdict(list)

        def serialize(node: TrieNode) -> str:
            if not node.children:
                return ""
            serialized_parts = []
            for name in sorted(node.children.keys()):
                child_serial = serialize(node.children[name])
                serialized_parts.append(name + "(" + child_serial + ")")
            serial = "".join(serialized_parts)
            subtree_map[serial].append(node)
            return serial

        serialize(root)

        # Step 3: Mark all duplicate subtrees
        for nodes in subtree_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.is_deleted = True

        # Step 4: Collect all remaining paths (not deleted)
        res = []

        def dfs(node: TrieNode, path: List[str]):
            for folder, child in node.children.items():
                if not child.is_deleted:
                    new_path = path + [folder]
                    res.append(new_path)
                    dfs(child, new_path)

        dfs(root, [])
        return res
