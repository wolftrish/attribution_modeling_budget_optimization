# define a fucntion for reading the dataset

def Import(path):
    import pandas as pd
    data = pd.read_csv(path)
    return data