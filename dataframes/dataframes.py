from tabulate import tabulate
from typing import List
import pandas as pd
import matplotlib.pyplot as plt


def print_table(df):
    """Print table using tabulate"""

    # Print dataframe info in a tuple (number of rows, number of columns)
    print(df.shape)
    
    print(tabulate(df.head(), headers = 'keys', tablefmt = 'psql'))

def read_csv(url="../datasets/Students_Grading_Dataset.csv"):
    """
    Load data from CSV file
    
    """
    df = pd.read_csv("../datasets/Students_Grading_Dataset.csv")

    print(df.head())

def data_inspection():
    data = [
        {"id": 1, "Name": "Ana", "Age": 25, "Salary": 1000},
        {"id": 2, "Name": "Ana", "Age": 25, "Salary": 1000},
        {"id": 3, "Name": "Luis", "Age": 30, "Salary": 2000},
        {"id": 4, "Name": "Carlos", "Age": 22, "Salary": 6000},
        {"id": 5, "Name": "Juan", "Age": 35, "Salary": 2500},
        {"id": 6, "Name": "Camilo", "Age": 31, "Salary": 3500}
    ]

    df = pd.DataFrame(data)

    print(df.head()) # Show first 5 rows
    print(df.tail(2)) # Show last 2 rows
    print(df.info()) # Show data types and not null values
    print(df.describe()) # Show Basic statistics (median, min, max, etc..)


def data_selection():
    data = [
        {"id": 1, "Name": "Ana", "Age": 25, "Salary": 1000},
        {"id": 2, "Name": "Ana", "Age": 25, "Salary": 1000},
        {"id": 3, "Name": "Luis", "Age": 30, "Salary": 2000},
        {"id": 4, "Name": "Carlos", "Age": 22, "Salary": 6000},
        {"id": 5, "Name": "Juan", "Age": 35, "Salary": 2500},
        {"id": 6, "Name": "Camilo", "Age": 31, "Salary": 3500}
    ]

    df = pd.DataFrame(data)

    print(df["Name"]) # One column
    print(df[["Name", "Salary"]]) # Multiple columns
    print(df.iloc[2]) # By position
    print(df[df["Age"] > 25]) # By condition
    print(df[(df["Age"] > 25) & (df["Salary"] > 2000)]) # By multiple condition

def data_modification():
     data = [
        {"id": 1, "Name": "Ana", "Age": 25, "Salary": 1000},
        {"id": 2, "Name": "Ana", "Age": 25, "Salary": 1000},
        {"id": 3, "Name": "Luis", "Age": 30, "Salary": 2000},
        {"id": 4, "Name": "Carlos", "Age": 22, "Salary": 6000},
        {"id": 5, "Name": "Juan", "Age": 35, "Salary": 2500},
        {"id": 6, "Name": "Camilo", "Age": 31, "Salary": 3500}
    ]
     
     df = pd.DataFrame(data)

     df['Discounts'] = df['Salary']*0.08
     df['Total'] = df['Salary'] - df['Discounts']
     print(df)

def data_sorting():
    data = [
        {"id": 1, "Name": "Ana", "Age": 25, "Salary": 1000},
        {"id": 2, "Name": "Ana", "Age": 25, "Salary": 1000},
        {"id": 3, "Name": "Luis", "Age": 30, "Salary": 2000},
        {"id": 4, "Name": "Carlos", "Age": 22, "Salary": 6000},
        {"id": 5, "Name": "Juan", "Age": 35, "Salary": 2500},
        {"id": 6, "Name": "Camilo", "Age": 31, "Salary": 3500}
    ]
     
    df = pd.DataFrame(data)
    print(df.sort_values(by="Salary", ascending=False))

def group_data():
    data = [
        {"id": 1, "Name": "Ana", "Age": 25, "Salary": 1000, "department": "HR"},
        {"id": 2, "Name": "Ana", "Age": 25, "Salary": 1000, "department": "IT"},
        {"id": 3, "Name": "Luis", "Age": 30, "Salary": 2000, "department": "Legal"},
        {"id": 4, "Name": "Carlos", "Age": 22, "Salary": 6000, "department": "Legal"},
        {"id": 5, "Name": "Juan", "Age": 35, "Salary": 2500, "department": "IT"},
        {"id": 6, "Name": "Camilo", "Age": 31, "Salary": 3500, "department": "HR"}
    ]
     
    df = pd.DataFrame(data)
    
    print(df.groupby('department')['Salary'].mean())

def calculations():
    data = [
        {"id": 1, "Name": "Ana", "Age": 25, "Salary": 1000, "department": "HR"},
        {"id": 2, "Name": "Ana", "Age": 25, "Salary": 1000, "department": "IT"},
        {"id": 3, "Name": "Luis", "Age": 30, "Salary": 2000, "department": "Legal"},
        {"id": 4, "Name": "Carlos", "Age": 22, "Salary": 6000, "department": "Legal"},
        {"id": 5, "Name": "Juan", "Age": 35, "Salary": 2500, "department": "IT"},
        {"id": 6, "Name": "Camilo", "Age": 31, "Salary": 3500, "department": "HR"}
    ]
     
    df = pd.DataFrame(data)
    calculations = [f"MIN : {df['Age'].min()}", # Minimum 
                f"MAX : {df['Age'].max()}", # Maximum
                f"MEAN : {df['Age'].mean()}", # Average, sum and divide for the total
                f"MEDIAN : {df['Age'].median()}", # Median, medium value 50% of the values are greater and 50% of the values are less
                f"NUNIQUE : {df['Age'].nunique()}", # Number of unique entries
                f"SUM : {df['Age'].sum()}" # Sum of values
            ] 


def drop_dupl():
    data = [
        {"id": 1, "Name": "Ana", "Age": 25, "Salary": 1000},
        {"id": 2, "Name": "Ana", "Age": 25, "Salary": 1000},
        {"id": 3, "Name": "Luis", "Age": 30, "Salary": 2000},
        {"id": 4, "Name": "Carlos", "Age": 22, "Salary": 6000}
    ]

    df = pd.DataFrame(data)

    print_table(df)

    print_table(df.drop_duplicates(subset=['Name', 'Age', 'Salary']))

def merge():
    data = [
        {"id": 1, "Name": "Ana", "Age": 25, "Salary": "Madrid"},
        {"id": 2, "Name": "Ana", "Age": 25, "City": "Madrid"},
        {"id": 3, "Name": "Luis", "Age": 30, "City": "Barcelona"},
        {"id": 4, "Name": "Carlos", "Age": 22, "City": "Sevilla"}
    ]

    data2 = [
        {"person_id": 1, "Address": "Kra 62"}
    ]

    df = pd.DataFrame(data)

    df2 = pd.DataFrame(data2)

    print_table(df.merge(df2, left_on='id', right_on='person_id'))
    
def data_visualization():
    data = [
        {"id": 1, "Name": "Ana", "Age": 25, "Salary": 1000},
        {"id": 2, "Name": "Ana", "Age": 25, "Salary": 1000},
        {"id": 3, "Name": "Luis", "Age": 30, "Salary": 2000},
        {"id": 4, "Name": "Carlos", "Age": 22, "Salary": 6000}
    ]

    df = pd.DataFrame(data)

    df.plot(kind="line")
    plt.show()


data_visualization()