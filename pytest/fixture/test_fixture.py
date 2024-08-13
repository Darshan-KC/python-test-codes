import pytest

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