import pandas as pd

def read_csv_file(filename):
    data = pd.read_csv(filename)
    return data.values.tolist()

filename = 'praeferenzen.csv'
csv_data = read_csv_file(filename)

