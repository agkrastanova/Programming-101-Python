data = {'A': [1, 2, 3],
        'dict_B': {'B': 11,
                   'C': 12}}


data2 = {'dict_B': {'B': 11,
                    'C': 12},
         'A': [1, 2, 3]}


data3 = {'dict_C': {'A': 1,
                    'dict_D': {'B': 12,
                               'C': 13}},
         'dict_E': {'D': 21,
                    'E': 22}}


data4 = {'dict_C': {'A': 1,
                    'dict_D': {'B': 12,
                               'dict_C': {'F': 31,
                                          'G': 32}}},
         'dict_E': {'D': 21,
                    'E': 22}}


def dictionary_to_list(data):  # DFS
    list_of_dictionary = []

    for key, value in data.items():
        if type(value) is dict:
            list_of_dictionary.append((key, value))
            inside_values = take_dict_keys_and_values(value)
            for elem in inside_values:
                list_of_dictionary.append(elem)
        else:
            list_of_dictionary.append((key, value))

    return list_of_dictionary


def take_dict_keys_and_values(data):
    list_of_tuples = []
    for key, value in data.items():
        list_of_tuples.append((key, value))
        if type(value) is dict:
            values_list = take_dict_keys_and_values(value)
            for elem in values_list:
                list_of_tuples.append(elem)

    return list_of_tuples


def deep_find(data, key):
    list_of_dictionary = dictionary_to_list(data)

    for i in range(len(list_of_dictionary)):
        if list_of_dictionary[i][0] == key:
            return 'key: {}\n   value: {}'.format(list_of_dictionary[i][0], list_of_dictionary[i][1])


# print(dictionary_to_list(data))
# print(dictionary_to_list(data2))
# print(dictionary_to_list(data3))
# print(dictionary_to_list(data4))
# print(deep_find(data, 'dict_B'))
# print(deep_find(data, 'B'))
# print(deep_find(data, 'C'))
# print(deep_find(data3, 'C'))
