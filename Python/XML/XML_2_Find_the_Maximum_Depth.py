# Easy Level Problem

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    
    # Make the root match level 0
    if level == -1:
        level = 0
        
    # Update max depth first
    if level > maxdepth:
        maxdepth = level
        
    # Apply Recursion
    for child in elem:
        depth(child, level+1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)