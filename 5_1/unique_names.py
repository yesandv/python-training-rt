def get_unique_names_from_a_list(list_of_names):
    unique_names_list = []
    for name in list_of_names:
        if name not in unique_names_list:
            unique_names_list.append(name)
    return unique_names_list


if __name__ == "__main__":
    number_of_names = int(input("Укажите кол-во муми: "))

    list_of_names = []

    for i in range(number_of_names):
        moomin_name = input("Введите фамилию муми: ")
        list_of_names.append(moomin_name)

    unique_names = get_unique_names_from_a_list(list_of_names)
    print(unique_names)
