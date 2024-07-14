class TreeNode:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class DirectoryTree:
    def __init__(self, root_name):
        self.root = TreeNode(root_name)

    def insert(self, path):
        parts = path.strip('/').split('/')
        current_node = self.root
        for part in parts:
            # Check if the current part is already a child
            found = False
            for child in current_node.children:
                if child.name == part:
                    current_node = child
                    found = True
                    break
            if not found:
                # Create a new node if the part isn't found
                new_node = TreeNode(part, current_node)
                current_node.add_child(new_node)
                current_node = new_node 

from graphviz import Digraph

import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'

def build_tree_from_directory(directory_path):
    tree = DirectoryTree('/')
    for dirpath, dirnames, filenames in os.walk(directory_path):
        # Get relative path to the root directory path
        rel_path = os.path.relpath(dirpath, directory_path)
        if rel_path == '.':
            rel_path = '/'
        else:
            rel_path = '/' + rel_path.replace('\\', '/')
        for dirname in dirnames:
            tree.insert(os.path.join(rel_path, dirname))
        for filename in filenames:
            tree.insert(os.path.join(rel_path, filename))
    return tree

def visualize_tree(tree):
    dot = Digraph(comment='Directory Tree')
    nodes = []
    edges = []

    def traverse(node):
        if node not in nodes:
            dot.node(node.name, node.name)
            nodes.append(node)
        for child in node.children:
            if child not in nodes:
                dot.node(child.name, child.name)
                nodes.append(child)
            dot.edge(node.name, child.name)
            traverse(child)

    traverse(tree.root)
    for node in nodes:
        print(node.name)
    dot.render('directory_tree.gv', view=False)  # Saves and opens the graph

# Usage
dir_path = 'C:/Users/kostas/Documents/pythonForGithub'
tree = build_tree_from_directory(dir_path)
visualize_tree(tree)