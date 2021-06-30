def get_unique_names_from_a_list(list_of_names):
    unique_names_list = []
    for name in list_of_names:
        if name not in unique_names_list:
            unique_names_list.append(name)
    return unique_names_list
