def take_dict_keys_and_values(data):
    list_of_tuples = []
    for key, value in data.items():
        list_of_tuples.append((key, value))
        if type(value) is dict:
            key_values_list = take_dict_keys_and_values(value)
            for elem in key_values_list:
                list_of_tuples.append(elem)

    return list_of_tuples


def dictionary_to_list(data):  # DFS
    list_of_dictionary = []

    for key, value in data.items():
        if type(value) is dict:
            list_of_dictionary.append((key, value))
            key_values_list = take_dict_keys_and_values(value)
            for elem in key_values_list:
                list_of_dictionary.append(elem)
        else:
            list_of_dictionary.append((key, value))

    return list_of_dictionary


def deep_find_all(data, key):
    list_of_dictionary = dictionary_to_list(data)
    list_of_all = []

    for i in range(len(list_of_dictionary)):
        if list_of_dictionary[i][0] == key:
            list_of_all.append(list_of_dictionary[i][1])

    return list_of_all
