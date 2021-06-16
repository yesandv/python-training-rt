def role_list_to_str(role_1, role_2, role_3, separator):
    roles = role_1 + separator + role_2 + separator + role_3
    return roles


if __name__ == "__main__":
    prefix = 'Who is John Galt?\nJohn Galt is:\n'
    role_1 = input()
    role_2 = input()
    role_3 = input()
    sep = input()
    print(prefix + role_list_to_str(role_1, role_2, role_3, sep))
