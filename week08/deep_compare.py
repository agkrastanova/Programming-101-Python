from deep_find import dictionary_to_list


def deep_compare(obj1, obj2):
    obj1_list = dictionary_to_list(obj1)
    obj2_list = dictionary_to_list(obj2)

    return obj1_list == obj2_list
