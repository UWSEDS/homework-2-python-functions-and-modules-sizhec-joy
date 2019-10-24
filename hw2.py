import pandas as pd
import numpy as np


def read_from_url(url):
    return pd.read_csv(url)


def test_create_dataframe(test_df, list_column_names):
    result = True
    test_df_col = test_df.columns.values
    # The DataFrame contains only the columns that you specified as the second argument
    if not set(list_column_names) == set(test_df_col):
        result = False
    # The values in each column have the same python type
    sets_of_type_in_column = [set(map(type, test_df[c])) for c in test_df_col]
    lengths_of_type_set_in_column = [len(t) for t in sets_of_type_in_column]
    if any(l > 1 for l in lengths_of_type_set_in_column):
        result = False
    # There are at least 10 rows in the DataFrame
    if test_df.shape[0] < 10:
        result = False
    return result

