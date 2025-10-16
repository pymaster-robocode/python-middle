from tree import BinarySearchTree

tree = BinarySearchTree()

students = [
    {"name": "Alice Johnson", "class": "5A", "score": 88},
    {"name": "Benjamin Smith", "class": "5B", "score": 74},
    {"name": "Charlotte Lee", "class": "5A", "score": 92},
    {"name": "Daniel Brown", "class": "5C", "score": 67},
    {"name": "Emma Davis", "class": "5B", "score": 85},
    {"name": "Felix Wilson", "class": "5A", "score": 79},
    {"name": "Grace Taylor", "class": "5C", "score": 90},
    {"name": "Henry Moore", "class": "5B", "score": 73},
    {"name": "Isabella Martin", "class": "5C", "score": 95},
    {"name": "Jack Thompson", "class": "5A", "score": 81},
]

for n in students:
    tree.insert(n)

tree.print_inorder()

