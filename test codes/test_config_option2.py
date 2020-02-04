
import pytest

def test_input_correct_coor():
    input_row = "3"
    input_col = "3"
    assert datafile[3][3] == "O"
    
def test_input_incorrect_coor():
    input_row = "3.3"
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
    input_row = "P"
    input_col = ""
    assert "Invalid input, please enter a valid input of either “B/M” or coordinate in the correct format"

