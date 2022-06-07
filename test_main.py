from main import solution

def test_solution_1():
    assert solution("asdfadsf") == ['as', 'df', 'ad', 'sf']

def test_solution_2():
    assert solution("asdfads") == ['as', 'df', 'ad', 's_']
    
def test_solution_3():    
    assert solution("") == []
    
def test_solution_4():    
    assert solution("x") == ["x_"]