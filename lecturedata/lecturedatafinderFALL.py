import csv
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd


def obtainlecturedata(df,row):
    
    url = df.iloc[row, 2] 
    print(url)
    response = requests.get(url)
    coursesoup = BeautifulSoup(response.content, 'html.parser')
    print(coursesoup)

df = pd.read_csv('coursedatafinder/coursedata.csv',encoding='ISO-8859-1').drop_duplicates().reset_index(drop=True)
obtainlecturedata(df,0)
