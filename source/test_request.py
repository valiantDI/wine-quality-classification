import requests
import pandas as pd
import random


if __name__ == '__main__':
    df = pd.read_csv('../data/winequality-red.csv', sep=';')
    num_examples = 3
    for i in range(num_examples):
        j = random.randint(0, len(df)-1)
        df_columns = [column.replace(' ', '_') for column in df.columns]
        test_data = {column: value for column, value in zip(df_columns, df.iloc[j].values)}
        target = test_data.pop('quality')
        resp = requests.post(
            'http://127.0.0.1:80/predict',
            json=test_data
        )
        print(f'Inpit features: {test_data}')
        print(f'Predicted: {resp.json()}')
        print(f'Expected: {target}')
        print('----')