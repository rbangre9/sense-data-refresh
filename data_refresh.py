import sys
import pandas as pd
import hashlib

'''
Computes if two datasets are the same, consumes two command line arguments which are the paths to the datasets. 

Example 1: 

command-line input: py data_refresh.py ./example-data/dataset1.csv ./example-data/dataset2.csv 
ouput: Duplicate Datasets

Example 2:

command-line input: py data_refresh.py ./example-data/dataset1.csv ./example-data/dataset2.csv 
output: Not Duplicate Datasets
'''

def hash(df):
    data_bytes = df.to_string()
    encoded_data = data_bytes.encode('utf-8')
    hasher = hashlib.sha256()
    hasher.update(encoded_data)
    return hasher.hexdigest()

def check_duplicate(ds1, ds2): 
    ds1_hash = hash(ds1)
    ds2_hash = hash(ds2)

    if ds1_hash == ds2_hash: return 1
    return 0

def main(dp_1, dp_2):
    dataset1 = pd.read_csv(dp_1)
    dataset2 = pd.read_csv(dp_2)

    dataset1.columns = dataset1.columns.str.strip()
    dataset2.columns = dataset2.columns.str.strip()

    isDuplicate = check_duplicate(dataset1, dataset2)

    if isDuplicate: print('Duplicate Datasets')
    else: print('Not Duplicate Datasets')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])






