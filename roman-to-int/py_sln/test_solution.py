from .solution import romanToInt

def test_one():
    assert romanToInt("III") == 3
    

def test_two():
    assert romanToInt("LVIII") == 58
    

def test_three():
    assert romanToInt("MCMXCIV") == 1994