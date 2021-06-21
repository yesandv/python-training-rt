def list_to_list_of_tuples(general_list):
    list_of_tuples = []
    del general_list[0]
    flowers = general_list[0:len(general_list):2]
    quantities = general_list[1:len(general_list):2]
    for i in range(0, len(flowers)):
        flower_tuple = (flowers[i], quantities[i])
        list_of_tuples.append(flower_tuple)
    return list_of_tuples
