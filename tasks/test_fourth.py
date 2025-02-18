import pandas as pd

def concat_dataframes(df1, df2):
    return pd.concat([df1, df2])

def test_concat_dataframes():
    data1 = {
        'name': ['John', 'Anna', 'Peter', 'Linda'],
        'location': ['New York', 'Paris', 'Berlin', 'London'],
        'age': [24, 13, 53, 33]
    }
    data2 = {
        'name': ['Tom', 'Jerry', 'Mickey', 'Donald'],
        'location': ['Los Angeles', 'Tokyo', 'Beijing', 'Moscow'],
        'age': [44, 23, 43, 53]
    }
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    assert concat_dataframes(df1, df2).shape == (8, 3)
    assert type(concat_dataframes(df1, df2)) == pd.core.frame.DataFrame