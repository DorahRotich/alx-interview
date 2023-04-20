#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = _import_('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if _name_ == "_main_":
    print_triangle(pascal_triangle(5))
