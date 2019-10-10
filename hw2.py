import pandas as pd
import numpy as np


def read_from_url(url):
    return pd.read_csv(url)


def test_create_dataframe(test_df, list_column_names):
    result = True
    test_df_col = test_df.columns.values
    # The DataFrame contains only the columns that you specified as the second argument
    if not set(list_column_names) == set(test_df_col):
        print(f'Elements present in list of columns names given but not in dataframe: '
              f'{set(list_column_names) - set(test_df_col)} \n'
              f'Elements present in dataframe but not in list of columns names given: '
              f'{set(test_df_col) - set(list_column_names)}')
        result = False
    # The values in each column have the same python type
    sets_of_type_in_column = [set(map(type, test_df[c])) for c in test_df_col]
    lengths_of_type_set_in_column = [len(t) for t in sets_of_type_in_column]
    if any(l > 1 for l in lengths_of_type_set_in_column):
        column_idx_different_type = np.where(np.array(lengths_of_type_set_in_column) > 1)[0]
        print(f'Values in these columns do not have the same python type: '
              f'{test_df_col[column_idx_different_type]}')
        result = False
    # There are at least 10 rows in the DataFrame
    if test_df.shape[0] < 10:
        print(f'There are {test_df.shape[0]} rows in the DataFrame')
        result = False
    return result


url = "https://raw.githubusercontent.com/UWSEDS/LectureNotes/master/Data/" \
      "Fremont_Bridge_Hourly_Bicycle_Counts_by_Month_October_2012_to_present.csv"
# df = read_from_url(url)
df = pd.DataFrame({'float': [1.0, 2],
                   'int': [1, 1],
                   'string': ['foo', 'st']})
print(test_create_dataframe(df, ['float', 'int', 'str', 'string']))
