import re


def split_tag_to_parts(string, join_index=False):
    # Seperating string into list of elements. Seperation is made by '.' and '[]' with text inside brackets. join_index
    #  joins left and right bracket with text inside if true, else it seperates into diferent elements.
    first_splitted = string.split(".")
    splitted = list()
    pattern = r"(\[)([\w\.\[\]]+)(\])"
    for element in first_splitted:
        match = re.search(pattern, element)
        if match:
            splitted.append(element[:match.start()])
            if join_index:
                splitted.append(match.group())
            else:
                [splitted.append(match.group(i)) for i in range(1, 4)]
            if len(element[match.end():]):
                splitted.append(element[match.end():])
        else:
            splitted.append(element)
    return splitted
