
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

def Percent_Check(data,index,check_val,arc,arcdate):
  outnum={'Buy':0,'Sell':0,'Hold':0}
  outval={'Mon':[],
          'Tue':[],
          'Wed':[],
          'Thur':[],
          'Fri':[]}
  Days=['Mon','Tue','Wed','Thur','Fri']
  for i in range(len(data)-1):
    refer_index=arc.index(data[i])
    currdate=arcdate[refer_index]
    year=int(currdate[0:4])
    month=int(currdate[5:7])
    day=int(currdate[8:])
    currdate=dt.date(year,month,day)
    currday=Days[dt.date.weekday(currdate)]
    pct=((data[i+1][index]-data[i][index])/data[i][index])*100
    if pct>=check_val:
      outnum['Sell']+=1
      outval[str(currday)].append('Sell')
    elif pct<=-check_val:
      outnum['Buy']+=1
      outval[str(currday)].append('Buy')
    else:
      outnum['Hold']+=1
      outval[str(currday)].append('Hold')
  return outnum,outval
def Remove_Void(datdict):
  outdict={}
  for i in datdict:
    if datdict[i]:
      outdict[i]=datdict[i]
  return outdict

def Find_Max(datdict):
  for i in datdict:
    CurrSet=datdict[i]
    freq={}
    for j in CurrSet:
      if j in freq:
        freq[j]+=1
      else:
        freq[j]=1
    freq=max(freq)
    datdict[i]=freq
  return datdict
  

def Next_day(date):
    date=str(date)
    Month=[1,2,3,4,5,6,7,8,9,10,11,12]
    day=int(date[8:])
    month=int(date[5:7])
    year=int(date[0:4])
    if (year%400==0) or (year%4==0 and year%100!=100):
      Days=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
      Days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if day<Days[Month.index(month)]:
      day+=1
    elif day==Days[Month.index(month)] and month!=12:
      day=1
      month+=1
    elif day==Days[Month.index(month)] and month==12:
      day=1
      month=1
      year+=1
    out=dt.date(year,month,day)
    return out
    
      
  
def Analyze_data(datfield):
  Time_Frame=int(input("Enter no of days:"))
  start_date=eval(input("Enter a tuple in the format(Year,Month,Date):"))
  a,b,c=start_date
  start_date=dt.date(a,b,c)
  var_date=dt.date(a,b,c)

  print("1.Press to Check validity and Accuracy of stock projections(For existing dates)")
  print("2.Press to find values for future dates")
  Condition=int(input("Enter your Choice:"))

  
  local_check_count=0
  while local_check_count<Time_Frame:
    Next=Next_day(var_date)
    if dt.date.weekday(Next)==5 or dt.date.weekday(Next)==6:
      var_date=Next
    else:
      var_date=Next
      local_check_count+=1

  df=pd.read_csv('C:\\Users\\gaisundar\\Desktop\\Project\\Company Data\\Microsoft.csv', index_col=0)

  fields=df.columns.values.tolist()
  field_index=fields.index(datfield)

  datafeed=df.values.tolist()
  datadate=df.index.values.tolist()

  Analyser_data=[]
  Current_data=[]
  Current_dates=[]
  
  Percent_Change=float(input("Enter Percent Change required for action:"))

  for i in range(len(datadate)):
      if str(datadate[i]) == str(start_date):
         for j in range(Time_Frame+1):
             Analyser_data.append(datafeed[i+j])
         else:
           if Condition==1:
             for j in range(Time_Frame-1,Time_Frame+4):
               Current_data.append(datafeed[i+j])
               print(datadate[i+j])

             Actual_Stock,Actual_DayStock=Percent_Check(Current_data,field_index,Percent_Change,datafeed,datadate)
             Actual_DayStock=Remove_Void(Actual_DayStock)
             Actual_DayStock=Find_Max(Actual_DayStock)
             print("Actual Values:",Actual_DayStock)

  Stock,Day_Stock=Percent_Check(Analyser_data,field_index,Percent_Change,datafeed,datadate)
  print("Analysis of Data:",Stock)
  Day_Stock=Find_Max(Day_Stock)
  

  Predictive_dates=[]
  Predictive_days=[]
  Predictive_dates.append(var_date)

  local_check_count=0
  while local_check_count<=3:
    Next=Next_day(var_date)
    if dt.date.weekday(Next)==5 or dt.date.weekday(Next)==6:
      var_date=Next
    else:
      var_date=Next
      Predictive_dates.append(Next)
      local_check_count+=1

  Days=['Mon','Tue','Wed','Thur','Fri']

  for i in Predictive_dates:
    Predictive_days.append(Days[dt.date.weekday(i)-1])

  Predictive_days_Stock={}

  for i in Predictive_dates:
    Predictive_days_Stock[i]=Day_Stock[Predictive_days[Predictive_dates.index(i)]]

  Predictive_days_Stock=Find_Max(Predictive_days_Stock)
  for i in Predictive_days_Stock:
    if Predictive_days_Stock[i]=='o':
      Predictive_days_Stock[i]='Hold'
    elif Predictive_days_Stock[i]=='l':
      Predictive_days_Stock[i]='Sell'
    elif Predictive_days_Stock[i]=='y':
      Predictive_days_Stock[i]='Buy'
  print("Projection:")
  for i in Predictive_days_Stock:
    print(i,Predictive_days_Stock[i])
Analyze_data('Adj Close')
