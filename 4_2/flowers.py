def list_to_list_of_tuples(general_list):
    # Not being used
    list_of_tuples = []
    del general_list[0]
    flowers = general_list[0:len(general_list):2]
    quantities = general_list[1:len(general_list):2]
    for i in range(0, len(flowers)):
        flower_tuple = (flowers[i], quantities[i])
        list_of_tuples.append(flower_tuple)
    return list_of_tuples


def sort_list_of_tuples(list_of_tuples):
    sorted_list_of_tuples = sorted(list_of_tuples, key=lambda flowers: flowers[1], reverse=True)
    return sorted_list_of_tuples


def list_of_tuples_to_list_of_flowers(sorted_list_of_tuples):
    list_of_flowers = []
    for flower_tuple in sorted_list_of_tuples:
        flower = flower_tuple[0]
        list_of_flowers.append(flower)
    return list_of_flowers


def find_frequent_flowers(list_of_tuples):
    sorted_list = sort_list_of_tuples(list_of_tuples)
    tuples_to_flowers = list_of_tuples_to_list_of_flowers(sorted_list)
    frequent_flowers = tuples_to_flowers[:3]
    return frequent_flowers


if __name__ == "__main__":
    list_of_tuples = []
    all_sort_of_flowers = int(input("Введите кол-во видов цветов: "))
    for k in range(all_sort_of_flowers):
        flowers = input("Введите название цветка: ")
        amount = int(input("Введите кол-во цветов: "))
        flower_tuple = (flowers, amount)
        list_of_tuples.append(flower_tuple)
    flowers = find_frequent_flowers(list_of_tuples)
    print(flowers)
