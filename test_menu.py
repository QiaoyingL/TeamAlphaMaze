import pytest
import builtins
from Maze import *

result = ""
    
def  test_invalid_option_input():
    result = option("5")
    assert result == "Invalid Option. Try Again"
  
def  test_alphabet_input():
    result = option("abc")
    assert result == "Invalid Option. Try Again"
    
def  test_symbols_input(): 
    result = option("@")
    assert result == "Invalid Option. Try Again"
    
def  test_double_digits_input():
    result = option("92")
    assert result == "Invalid Option. Try Again"
    
def test_option1(): 
    result = option("1")
    assert result == "Option 1 selected"
    
def test_option2(): 
    result = option("2")
    assert result == "Option 2 selected"
    
def test_option3():
    result = option("3")
    assert result == "Option 3 selected"
    
def test_option4():
    result = option("4")
    assert result == "Option 4 selected"
    
def test_option0():
    result = option("0")
    assert result == False
