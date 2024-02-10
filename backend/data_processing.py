import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
data = pd.read_csv(os.getenv("SOURCELOCATION"))

def get_data():
    return data

def get_count_companies():
    temp = data[['Company Name']].dropna()
    return temp.value_counts()

def get_comments(Company_Name):
    temp = data[data['Company Name'] == Company_Name].dropna()
    return temp[['Why it is bad?']]

if __name__ == '__main__':
    print(get_data())
    print(get_count_companies())
    print(get_comments("Accenture"))