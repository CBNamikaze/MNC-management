import datetime as dt
import pandas as pd
import pandas_datareader.data as data

def Save_Data(dat):
    inp=str(input("Press y to save data as csv file:"))
    if inp=='y':
        name=str(input("Enter name of file:"))
        dat.to_csv("C:\\Users\\gaisundar\\Desktop\\Project\\Company Data\\"+name+".csv")
def Acquire_data():
    start_date=eval(input("Enter tuple containing numbers of (year,month,date) start:"))
    end_date=eval(input("Enter tuple containing numbers of (year,month,date) end:"))
    a,b,c=start_date
    start_date=dt.datetime(a,b,c)
    a,b,c=end_date
    end_date=dt.datetime(a,b,c)
    source=str(input("Enter data source:"))
    Comp=str(input("Enter company code:"))
    df=data.DataReader(Comp,source,start_date,end_date)
    Save_Data(df)
    sample_num=int(input("Enter how many records are needed"))
    print(df.head(sample_num))
    return df
Acquire_data()

    
