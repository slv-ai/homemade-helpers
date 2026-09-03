def count(my_collection, target):
    if not my_collection:
        return None
    count_value = 0
    for value in my_collection:
        if value == target:
            count_value += 1
    return count_value 
    pass
    

def test_count_empty_list():
    assert count([], 7) == None

def test_count_no_instances_of_target():
    assert count([1, 3, 5, 2, 3], 8) == 0

def test_count_multiple_instances_of_targe():
    assert count([4, 5, 8, 3, 9, 5, 5, 5], 5) == 4

def count_tests():
    test_count_empty_list()
    test_count_no_instances_of_target()
    test_count_multiple_instances_of_targe
    print("All count tests passing.")