
import pytest
from config_current_maze import *

#def test_input_option1():
#def test_input_option2():
#def test_input_option3():
#def test_input_option4():
#def test_input_option0():
#def test_input_option5():

def test_display_config_menu():
    display_menu = config_menu()
    assert display_menu == "Configuration Menu is displayed"
