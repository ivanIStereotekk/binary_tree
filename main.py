from binarytree import build
import re

exemp = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

data = (4,5,7,3,9,7,4,123,7,789,2,5,4,34,1,4,1)

def binary_tree_builder(*args):
    #cleaned = re.findall("[\d{9}]", str(*args))
    binary_tree = build(*args)
    print('Binary tree from list :\n',
      binary_tree)


#binary_tree_builder(data)

def binary_tree_values(*args):
    #cleaned = re.findall("[\d{9}]", str(*args))
    binary_tree = build(*args)
    print('\nList from binary tree :',
          binary_tree.values)


#binary_tree_values(data)



