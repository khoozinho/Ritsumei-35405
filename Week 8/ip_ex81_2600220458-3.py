num_lst = [[1,1,4,66],[-55,7],[-1,43,55,-6,12,12,4]]

even = []
odd = []

def flatten_list(a_list):
    """Flattens the list - makes a normal lsit from a nested list."""
    flat_num_lst = []
    for lst in a_list:
        for element in lst:
            flat_num_lst.append(element)

    return flat_num_lst