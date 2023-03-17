import math
import pytest

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def test_square():
    num = 7
    assert num*num == 40

def test_camparison():
    assert 10 == 11
    
            