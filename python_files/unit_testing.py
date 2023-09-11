
import pytest 
from python_files.all_que import sum_func


def test_cases():
    assert sum_func(10,20) == 30
    assert sum_func(20,20) == 40
    assert sum_func(1,-1) == 0
    # return True 