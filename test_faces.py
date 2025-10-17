import pytest
from faces import convert

def main():
    test_convert()

def test_convert():
    assert convert("hello :)") == "hello 🙂"
    assert convert(":(") == "☹️"