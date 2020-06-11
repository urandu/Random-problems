"""
check for balanced brackets [{(
[]
solution not working. use stack instead
"""

lookup_dict = {
    "[":1,
    "{":2.1,
    "(":3,
    "]":-1,
    "}":-2,
    ")":-3,
}

def is_balanced(input_string):
    status = 0
    if(len(input_string) % 2 != 0):
        return False

    for character in input_string:
        status += lookup_dict[character]

    if status == 0:
        return True

    return False
