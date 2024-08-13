import pytest

""" 
@pytest.fixture is a decorator in Pytest that is used to create and manage fixtures. Fixtures are functions that provide a fixed baseline or setup that can be used in your tests. They are typically used to create resources that your tests need, such as initializing objects, setting up databases, preparing test data, or configuring environments.
"""

@pytest.fixture
def sample_data():
    data = [1,2,3,4,5]
    return data

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_len(sample_data):
    assert len(sample_data) == 5

def test_contains(sample_data):
    assert 3 in sample_data
    assert 6 in sample_data