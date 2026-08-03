from plates import is_valid
import pytest

def test_is_valid_start(): 
    assert is_valid("23") == False
    assert is_valid("AB") == True

def test_is_valid_max(): 
    assert is_valid("ABCDEFGH") == False
    assert is_valid("ABCDEG") == True

def test_is_valid_min(): 
    assert is_valid("A") == False

def test_is_valid_punct(): 
    assert is_valid("A,BCDE") == False
    assert is_valid("AB#CDE") == False


def test_is_valid_numbend(): 
    assert is_valid("AB23AB") == False
    assert is_valid("ABC123") == True
    assert is_valid("AB0123") == False
    assert is_valid("ABC102") == True
