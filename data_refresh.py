import sys
import pandas as pd

'''
Computes if two datasets are the same, consumes two command line arguments which are the paths to the datasets. 

Example 1: 

command-line input: py data_refresh.py ./example-data/smalldata1.csv ./example-data/smalldata2.csv 
ouput: {0: 'Not Matched', 1: 'Not Matched', 2: 'Not Matched', 3: 'Not Matched', 4: 'Not Matched', 5: 'Not Matched', 6: 'Not Matched', 
    7: 'Not Matched', 8: 'Not Matched', 9: 'Not Matched', 10: 'Not Matched', 11: 'Not Matched', 12: 'Not Matched', 13: 'Not Matched', 
    14: 'Not Matched', 15: 'Not Matched', 16: 'Not Matched'}

Example 2:

command-line input: py data_refresh.py ./example-data/smalldata2.csv ./example-data/smalldata3.csv 
output: {0: 'Match', 1: 'Not Matched', 2: 'Match', 3: 'Not Matched', 4: 'Match', 5: 'Match', 6: 'Match', 7: 'Match', 8: 'Not Matched', 
    9: 'Match', 10: 'Match', 11: 'Match', 12: 'Match', 13: 'Match', 14: 'Match', 15: 'Match', 16: 'Match'}
'''

def check_duplicate_column(col1, col2):
    return col1.equals(col2)

def main(dp_1, dp_2):
    dataset1 = pd.read_csv(dp_1)
    dataset2 = pd.read_csv(dp_2)

    dataset1.columns = dataset1.columns.str.strip()
    dataset2.columns = dataset2.columns.str.strip()

    numColumns = dataset1.shape[1]
    if dataset1.shape[1] != dataset2.shape[1]:  
        print('Invalid Dataset Shape')
        return

    res = {i : "Match" if check_duplicate_column(dataset1.iloc[:, i], dataset2[:, i]) 
           else "Not Matched" for i in range(numColumns)}

    print(res)
    return res

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
