import import_functions as my_imports

def test_multiply_4_nums() :
    assert my_imports.multiply_4_nums(1, 1, 1, 4) == 4
    assert my_imports.multiply_4_nums(1, 1, 5, 5) == 25
    assert my_imports.multiply_4_nums(1, 1, 1, 5) == 8
    assert my_imports.multiply_4_nums(1, 1, 3, 5) == 150
    

