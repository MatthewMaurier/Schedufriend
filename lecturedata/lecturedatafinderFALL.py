import csv
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd


def obtainlecturedata(df, df2, row):
    
    url = df.iloc[row, 2] 
    print(url)
    response = requests.get(url)
    coursesoup = BeautifulSoup(response.content, 'html.parser')
    #print(coursesoup)
    return df2

df = pd.read_csv('coursedatafinder/coursedata.csv',encoding='ISO-8859-1').drop_duplicates().reset_index(drop=True)
lectures_df_headers = ['Department', 'Course Code', 'Lecture code', 'dates', 'timeframe', 'location', 'prof' ]

testdata = [["math","100","LECTURE EA1 (82051)","2023-09-05 - 2023-12-08","11:00:00 - 11:50:00","T B-95"," Vladyslav Yaskin"]]
df2 = pd.DataFrame(testdata, columns=lectures_df_headers) #df2 is to be the new dataframe which contains only info 
df2 = obtainlecturedata(df, df2, 0)
print(df2)

#NEXT STEP: run obtainlecture data to create a list of strings with the ['Department', 'Course Code', 'Lecture code', 'dates', 'timeframe', 'location', 'prof' ] value from each url, then append that to df2 for each class with fall lectures