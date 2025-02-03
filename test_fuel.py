import pytest
from fuel import convert, gauge

def test_convert_valid_inputs():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert("99/100") == 99

def test_convert_invalid_inputs():
    # Test invalid formats
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3")
    with pytest.raises(ValueError):
        convert("3/2/1")

    # Test invalid fractions
    with pytest.raises(ValueError):
        convert("5/4")  # X > Y
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Y = 0

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"