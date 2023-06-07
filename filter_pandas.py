import pandas as pd

# 1. filter Series by loc
def filter_series_by_loc(data: pd.Series, min_length=5):
    data_long_word = data.loc[lambda x: x >= min_length]
    return data_long_word

# 2. filter Series by INDEX
def filter_series_by_index(series: pd.Series, min_length=5):
    filter = series.index[series.index.str.len() >= min_length]
    return series[filter]

# 3. filter DataFrame by loc
def need_to_work_better(df: pd.DataFrame):
    return df.loc[(df['maths'] <= 2) | (df['physics'] <= 2) | (df['computer science'] <= 2)] 

# 4. filter DataFrame by filter mask
def best(df: pd.DataFrame):
    filter_df = df['maths'].isin([4, 5]) & df['physics'].isin([4, 5]) & df['computer science'].isin([4, 5])
    return df[filter_df]

def main():
    # filter Series
    data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
    filtered = filter_series_by_loc(data, min_length=6)
    filtered_data = filter_series_by_index(data)

    print(data)
    print(filtered)
    print(filtered_data)

    # filter DataFrame
    columns = ['name', 'maths', 'physics', 'computer science']
    data2 = {
        'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
        'maths': [5, 4, 5, 2, 4],
        'physics': [4, 4, 4, 5, 5],
        'computer science': [5, 2, 5, 4, 3]
    }
    journal = pd.DataFrame(data2, columns=columns)
    filtered = best(journal)
    filtered2 = need_to_work_better(journal)
    print(journal)
    print(filtered)
    print(filtered2)

    
if __name__ == "__main__":
    main()
