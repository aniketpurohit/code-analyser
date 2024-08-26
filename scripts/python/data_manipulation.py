# data_manipulation.py

import pandas as pd


def create_dataframe():
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [24, 27, 22],
        "City": ["New York", "Los Angeles", "Chicago"],
    }
    df = pd.DataFrame(data)
    return df


def save_to_csv(df, file_name):
    df.to_csv(file_name, index=False)


if __name__ == "__main__":
    df = create_dataframe()
    print(df)
    save_to_csv(df, "people.csv")
    print("Data saved to 'people.csv'")
