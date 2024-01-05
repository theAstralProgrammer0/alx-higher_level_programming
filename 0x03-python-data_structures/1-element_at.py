def element_at(my_list, idx):
    if len(my_list) < idx < 0:
        return (None)
    for item in my_list:
        if my_list.index(item) == idx:
            return (item)
