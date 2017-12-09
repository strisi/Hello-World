# content of test_helloWorld.py
"""Test pytest"""

import helloworld

def test_hi():
    """check"""
    assert helloworld.say_hi() == 'Hello WOrld'
