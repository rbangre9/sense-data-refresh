import sys
import pandas as pd
import hashlib

'''
Computes how similar 2 given datasets are. Consumes 3 command line arguments (datapath1, datapath2, minimum difference threshold)

'''

MINIMUM_THRESHOLD = sys.argv[3] 

def hash(df):
    data_bytes = df.to_string()
    hasher = hashlib.sha256()
    hasher.update(data_bytes)
    return hasher.hexdigest()

def check_duplicate(ds1, ds2): 
    ds1_hash = hash(ds1)
    ds2_hash = hash(ds2)

    if ds1_hash == ds2_hash: return 0
    return 1

def check_similarity(ds1, ds2):
    pass

def main(dp_1, dp_2):
    dataset1 = pd.read_csv(dp_1)
    dataset2 = pd.read_csv(dp_2)

    dataset1.columns = dataset1.columns.str.strip()
    dataset2.columns = dataset2.columns.str.strip()

    if not check_duplicate(dataset1, dataset2): 
        print('Duplicate Datasets Found')
        return

    check_similarity(dataset1, dataset2)


    

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])






