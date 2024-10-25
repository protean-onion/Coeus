"""
Visualise a binary tree with each node being indexed by a position that progresses from left to right,
starting with 0 for the root level.

This module contains a set of functions for traversing the tree based on such position indices.
"""

def calculate_level(p):
    level = 0
    while not p in return_positions_of_level(level):
        level += 1
    return level

def return_last_index_of_level(level):
        return sum([2 ** i for i in range(level)]) - 1
        
def return_positions_of_level(level):
    return [i for i in range(return_last_index_of_level(level - 1) + 1, return_last_index_of_level(level) + 1)]

def calculate_segment(p):
    level = calculate_level(p)

    first_position = return_positions_of_level(level)[0]

    segment = 0
    
    check = first_position + 1
    while p > check:
        segment += 1
        check += 2

    return segment

def calculate_local_position(p):
    return return_positions_of_level(calculate_level(p)).index(p)

def return_segments(level):
    elements = return_positions_of_level(level)
    return [[elements[i], elements[i + 1]] for i in range(0, len(elements), 2)]

def return_parent(p):
    segment = calculate_segment(p)
    return return_positions_of_level(calculate_level(p) - 1)[(segment) // 2]

def left_child(p):
    level = calculate_level(p)
    node_position = calculate_local_position(p)

    child_segments = return_segments(level + 1)

    return child_segments[node_position][0]

def right_child(p):
    level = calculate_level(p)
    node_position = calculate_local_position(p)

    child_segments = return_segments(level + 1)

    return child_segments[node_position][1]
