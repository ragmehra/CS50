from fuel import convert, gauge
import pytest


def test_convert(): 
    assert convert("2/3") == 67
    with pytest.raises(ValueError): 
        convert("10/4")
    with pytest.raises(ValueError): 
        convert("-10/4")
    with pytest.raises(ZeroDivisionError): 
        convert("10/0")

def test_gauge():
    assert gauge(67) == "67%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"