
import pytest
from config_current_maze import *

def test_input_correct_coor():
    input_row = "2"
    input_col = "4"
    assert datafile[2][4] == "X"
    
def test_input_incorrect_coor():
    input_row = "2.4"
    input_col = ""
    assert "Invalid input, please enter in the correct format"
    
def test_input_return_config():
    input_row = "B"
    input_col = ""
    return config_menu()

def test_input_return_main():
    input_row = "M"
    input_col = ""
    return MainMenu()

def test_input_invalid():
    input_row = "O"
    input_col = ""
    assert "Invalid input, please enter a valid input of either “B/M” or coordinate in the correct format"
