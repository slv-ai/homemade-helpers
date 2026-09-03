def max(my_collection):
    max_value = my_collection[0] if my_collection else None
    for value in my_collection:
        if value > max_value:
            max_value = value
    return max_value
    pass

def test_max_empty_list():
    assert max([]) == None

def test_max_single_list():
    assert max([1]) == 1

def test_max_many_list():
    assert max([4, 5, 8, 3, 9]) == 9

def max_tests():
    test_max_empty_list()
    test_max_single_list()
    test_max_many_list()
    print("All max tests passing.")