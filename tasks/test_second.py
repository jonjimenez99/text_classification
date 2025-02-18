import pandas as pd

def create_dataframe():
    data = {
        'name': ['John', 'Anna', 'Peter', 'Linda'],
        'location': ['New York', 'Paris', 'Berlin', 'London'],
        'age': [24, 13, 53, 33]
    }
    return pd.DataFrame(data)

def test_create_dataframe():
    assert create_dataframe().shape == (4, 3)
    assert type(create_dataframe()) == pd.core.frame.DataFrame