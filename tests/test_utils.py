from visual_sort.utils import hextodec, colordict, interpolateColor, interpolateColors

import pytest

@pytest.fixture
def red():
    return "#ff0000"

@pytest.fixture
def grn():
    return "#00FF00"

@pytest.fixture
def blu():
    return "#0000FF"

def test_hex_to_dec_rd(red):
    result = hextodec(red)
    assert result == (1,0,0)


def test_hex_to_dec_grn(grn):
    result = hextodec(grn)
    assert result == (0,1,0)


def test_hex_to_dec_blu(blu):
    result = hextodec(blu)
    assert result == (0,0,1)


def test_interpolateColors(red,blu):
    red = hextodec(red)
    blu = hextodec(blu)
    result = interpolateColors(red, blu, 500)
    print(result)
    assert result == blu
