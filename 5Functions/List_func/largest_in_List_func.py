# def largest_in_list(lst):
#    if len(lst) == 0:
#       return None
#    large = lst[0]
#    for i in lst:
#       if i>large:
#          large = i
#    return large


# print(largest_in_list([]))


def largest_in_list(lst):
    return max(lst) if lst else None
print(largest_in_list([]) )