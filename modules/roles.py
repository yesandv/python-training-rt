def role_list(role_1, role_2, role_3, separator):
    john = 'Who is John Galt?\nJohn Galt is:\n'
    roles = john + role_1 + separator + role_2 + separator + role_3
    return roles


if __name__ == "__main__":
    role_1 = input()
    role_2 = input()
    role_3 = input()
    sep = input()
    print(role_list(role_1, role_2, role_3, sep))
