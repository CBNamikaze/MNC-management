import datetime as dt
import pandas as pd
import pandas_datareader.data as dat

direct="C:\\Users\\gaisundar\\Desktop\\Project\\Company Data\\"
def Read_names():
    f=open("C:\\Users\\gaisundar\\Desktop\\Project\\Company Names.txt",'r+')
    names=f.readlines()
    out=[]
    for i in names:
        if i!=names[-1]:
           out.append(i[:-1])
    return out
def Read_Data(n1,n2):
    df=pd.read_csv(direct+files[n1-1], parse_dates=True, index_col=0)
    print(df.head(n2))
    return df

files=Read_names()
print(files)
filenum=int(input("Enter file no to read:"))
records=int(input("Enter no of records required:"))
Read_Data(filenum,records)
