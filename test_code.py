import pytest
from check_graduation import calculate_probability


@pytest.mark.test
def test_method1():
    assert calculate_probability(5) == '14/29'


@pytest.mark.test
def test_method2():
    assert calculate_probability(10) == '372/773'
