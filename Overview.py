# Imports
import datetime as dt
import pandas as pd
import pandas_datareader.data as data
import matplotlib.pyplot as plt
from matplotlib import style
import os
from tkinter import *
import tkinter.messagebox as box
import random
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#  Declarations of variables

files=['Amazon.csv','Apple.csv','Facebook.csv','Google.csv','HCL.csv','Infosys.csv','Microsoft.csv','Paypal.csv','TCS.csv','Tesla.csv']
direct="I:\\Project\\Company Data\\"
Attributes=['High','Low','Open','Close','Adj Close','Volume']
Plot_Types=['Line','Bar','Fill','Scatter']

#  Data Collection from internet

def Save_Data(dat):
    inp=str(input("Press y to save data as csv file:"))
    if inp=='y':
        name=str(input("Enter name of file:"))
        files.append(name+'.csv')
        dat.to_csv("I:\\Project\\Company Data\\"+name+".csv")
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
    opt=str(input("Press y to display data:"))
    if opt=='y':
        sample_num=int(input("Enter how many records are needed"))
        print()
        print(df.head(sample_num))
    return df


#  Data Collection From existing files

def Read_Data(n1,n2):
    df=pd.read_csv(direct+files[n1-1], parse_dates=True, index_col=0)
    print(df.head(n2))
    return df

#  Simpler Plots

def Style_Choose():
    print("Available Styles:")
    print()
    print(style.available[0:5])
    print(style.available[5:10])
    print(style.available[10:15])
    print(style.available[15:20])
    print(style.available[20:26])
    print()
    stylec=str(input("Enter desired style: "))
    style.use(stylec)

def Dat_plot(dat,n,plotnum):
    if plotnum==1:
      dat[Attributes[n-1]].plot()
    elif plotnum==2:
      plt.bar(dat.index,dat[Attributes[n-1]])
    elif plotnum==3:
        plt.fill_between(dat.index,dat[Attributes[n-1]])
    elif plotnum==4:
        plt.scatter(dat.index,dat[Attributes[n-1]])
    plt.title(Attributes[n-1]+" vs Years")
    plt.show()

def Compare_plot(dat,attr):
    for i in attr:
       dat[Attributes[i-1]].plot(label=str(Attributes[i-1]))
    plt.title("Comparitive graph of Attributes")
    plt.legend()
    plt.show()

def Mega_plot(dat,plotnum):
    grid=(2,3)
    
    cast1=plt.subplot2grid(grid,(0,0))
    cast2=plt.subplot2grid(grid,(0,1))
    cast3=plt.subplot2grid(grid,(0,2))
    cast4=plt.subplot2grid(grid,(1,0))
    cast5=plt.subplot2grid(grid,(1,1))
    cast6=plt.subplot2grid(grid,(1,2))
    if plotnum==1:
        cast1.plot(dat[Attributes[0]],label='High',color='violet')
        cast2.plot(dat[Attributes[1]],label='Low',color='green')
        cast3.plot(dat[Attributes[2]],label='Open',color='black')
        cast4.plot(dat[Attributes[3]],label='Close',color='orange')
        cast5.plot(dat[Attributes[4]],label='Adj Close',color='red')
        cast6.plot(dat[Attributes[5]],label='Volume',color='blue')
    elif plotnum==2:
        cast1.bar(dat.index,dat[Attributes[0]],label='High',color='violet')
        cast2.bar(dat.index,dat[Attributes[1]],label='Low',color='green')
        cast3.bar(dat.index,dat[Attributes[2]],label='Open',color='black')
        cast4.bar(dat.index,dat[Attributes[3]],label='Close',color='orange')
        cast5.bar(dat.index,dat[Attributes[4]],label='Adj Close',color='red')
        cast6.bar(dat.index,dat[Attributes[5]],label='Volume',color='blue')
    elif plotnum==3:
        cast1.fill_between(dat.index,dat[Attributes[0]],label='High',color='violet')
        cast2.fill_between(dat.index,dat[Attributes[1]],label='Low',color='green')
        cast3.fill_between(dat.index,dat[Attributes[2]],label='Open',color='black')
        cast4.fill_between(dat.index,dat[Attributes[3]],label='Close',color='orange')
        cast5.fill_between(dat.index,dat[Attributes[4]],label='Adj Close',color='red')
        cast6.fill_between(dat.index,dat[Attributes[5]],label='Volume',color='blue')
    elif plotnum==4:
        cast1.scatter(dat.index,dat[Attributes[0]],label='High',color='violet')
        cast2.scatter(dat.index,dat[Attributes[1]],label='Low',color='green')
        cast3.scatter(dat.index,dat[Attributes[2]],label='Open',color='black')
        cast4.scatter(dat.index,dat[Attributes[3]],label='Close',color='orange')
        cast5.scatter(dat.index,dat[Attributes[4]],label='Adj Close',color='red')
        cast6.scatter(dat.index,dat[Attributes[5]],label='Volume',color='blue')

    cast1.legend()
    cast2.legend()
    cast3.legend()
    cast4.legend()
    cast5.legend()
    cast6.legend()

    plt.show()    



# Moving average Analysis

def Daily_Avg(dat,n):
    Days_Specs=int(input("Enter number of previous days to calculate Moving Average:"))
    dat[str(Days_Specs)+' Mov_Avg']=dat[Attributes[n-1]].rolling(window=Days_Specs,min_periods=0).mean()
    sample=int(input("Enter number of sample days are required:"))
    print()
    print(dat.head(sample))
    print()
    inp=str(input("press y to enable a subplot:"))
    if inp=='y':
        num=int(input("Enter Attribute num(1-5):"))
        grid=eval(input("Enter grid size as tuple:"))        
        top_row=round(0.6*int(grid[0]))
        bottom_row=round(0.4*int(grid[0]))
        top=plt.subplot2grid(grid,(0,0),rowspan=top_row,colspan=int(grid[1]))
        bottom=plt.subplot2grid(grid,(top_row,0),rowspan=bottom_row,colspan=int(grid[1]),sharex=top)
        top.plot(dat.index,dat[Attributes[num-1]],label=Attributes[num-1],color='red')
        top.plot(dat.index,dat[str(Days_Specs)+' Mov_Avg'],label=str(Days_Specs)+' Mov_Avg',color='green')
        top.plot([],[],color='blue',label='Volume')
        top.legend()
        print("1.Plot Volume as Barplot")
        print("2.Plot Volume as fillplot")
        plotinp=int(input("Press 1 for barplot of volume and press 2 for fill plot of volume:"))
        if plotinp==1:
           bottom.bar(dat.index,dat['Volume'],color='blue')
        else:
           bottom.fill_between(dat.index,dat['Volume'],color='blue')  
    else:
        plt.plot(dat.index,dat[Attributes[n-1]])
        plt.plot(dat.index,dat[str(Days_Specs)+'Mov_Avg'])
    plt.show()

# Predicitive Analysis

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
  start_date=eval(input("Enter a Monday as a tuple in the format(Year,Month,Date):"))
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

  df=pd.read_csv('I:\\Project\\Company Data\\Microsoft.csv', index_col=0)

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
             print("Predicting Dates:")
             for j in range(Time_Frame-1,Time_Frame+4):
               Current_data.append(datafeed[i+j])
               print(datadate[i+j])
             Current_data.append(datafeed[i+Time_Frame+4])
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

# 


#----------------------------------------------------------------------------------------------------
while True:
  print("1.Stock Data Management")
  print("2.Employee Data Management")
  Mode_out=int(input("Enter your choice(1-2):"))
  if Mode_out==1:
    while True:
        print("1.Data Collection")
        print("2.Simple Comparisions")
        print("3.Moving Average Analysis")
        print("4.Predictive analysis")
        print("5.Bankruptcy Simulator")
        print("6.Back")
        Mode=int(input("Enter your choice(1-6):"))
        if Mode==1:
            print(files)
            Exist=str(input("Press y if desired company exisits in Above data:"))
            if Exist=='y':
                filenum=int(input("Enter file no to read:"))
                records=int(input("Enter no of records required:"))
                print()
                df=Read_Data(filenum,records)
                print()
            else:
                df=Acquire_data()
                print()
        elif Mode==2:
            Style_Choose()
            while True:    
                print("1.Compare 1 Attribute versus time")
                print("2.Compare 2 or more Attributes versus time")
                print("3.Overall View")
                print("4.Back")
                choice=int(input("Enter your choice(1-4):"))
                if choice==1:
                    print(Attributes)
                    num=int(input("Enter desired Attribute vs Time graph(1-6):"))
                    print(Plot_Types)
                    plot=int(input("Enter desired plot Type:"))
                    Dat_plot(df,num,plot)
                elif choice==2:
                    print(Attributes)
                    Attrs=[]
                    num=int(input("Enter number of Attributes to compare:"))
                    for i in range(num):
                        Attrinum=int(input("Enter desired Attribute(1-6)"))
                        Attrs.append(Attrinum)
                    Compare_plot(df,Attrs)
                elif choice==3:
                    print(Plot_Types)
                    plot=int(input("Enter desired plot Type:"))
                    Mega_plot(df,plot)
                else:
                    break
        elif Mode==3:
            Style_Choose()
            print(Attributes)
            AttriNum=int(input("Enter Attribute number of choice:"))
            Daily_Avg(df,AttriNum)
        elif Mode==4:
            Analyze_data('Adj Close')
        elif Mode==6:
            print("End of Program")
            break
  elif Mode_out==2:
      while True:
        print('PRESS 1 TO ADD AN NEW EMPLOYEE')
        print('PRESS 2 TO GET THE PORTFOLIO OF AN EMPLOYEE')
        print('PRESS 3 FOR EMPLOYMENT EXCHANGE PROGRAM')
        print('PRESS 4 TO EXIT')
        option=int(input('ENTER YOUR OPTION'))
        if option==1:
          def dialog1():
                  #password check
                  username=entry1.get()
                  password = entry2.get()
                  if (username == 'ADMIN' and  password == 'ADMIN'):
                      getchoice='y'
                      while getchoice in ['y','Y']:
                          #checking vacancy
                          vaclis=open('vaclis.txt','r')
                          vacantlist=vaclis.read()
                          vaclis.close()
                          vacantlist=vacantlist.split('\n')
                          vaclis=[]
                          #converting to list
                          for i in vacantlist:
                              i=i.split(',')
                              if i!='':
                                  vaclis+=[i]
                          #incase of blankspace in next line
                          if vaclis[-1]==['']:
                              vaclis=vaclis[::-1]
                              vaclis=vaclis[1:]
                              vaclis=vaclis[::-1]
                          #converting str to int
                          for i in vaclis:
                              i[1]=int(i[1])
                              i[2]=int(i[2])
                          vaclist=vaclis
                          #availability checker
                          avail={}
                          for i in vaclist:
                              avail[i[0]]=i[2]-i[1]
                          print('Departments:')
                          print('INFORMATION TECHNOLOGY\nHUMAN RESOURCES\nMARKETING\nLEGAL CONSULTANTS\nPUBLIC RELATIONS\nMANUFACTURING\nCUSTOMER SERVICE\nFINANCE\nLABOR')
                          q=input('ENTER YOUR DEPARTMENT:')
                          if q.upper() not in avail:
                              print('No Such Department Found!')
                          if avail[q.upper()]>0:                  
                              for i in vaclist:
                                  if i[0]==q.upper():
                                      i[1]+=1                    
                              vaclis=open('vaclis.txt','w')
                              save=''
                              for i in vaclist:
                                  save+=i[0]+','+str(i[1])+','+str(i[2])
                                  save+='\n'
                              vaclis.write(save)
                              vaclis.close()
                              path=os.path.abspath('DATA.xlsx')
                              xfl=pd.read_excel(path)
                              w=pd.ExcelWriter('DATA.xlsx',engine='xlsxwriter')
                              val=xfl.values.tolist()
                              #date of join
                              dojoin=str(dt.date.today())
                              dojoin=dojoin[-2:]+'-'+dojoin[-5:-3]+'-'+dojoin[:4]
                              p=input('ENTER YOUR NAME:')
                              p=p.upper()
                              q=q.upper()
                              r=input('ENTER YOUR SALARY:')
                              s=input('ENTER YOUR WORKING HOURS:')
                              t=input('ENTER YOUR DESIGNATION:')
                              t=t.upper()
                              u=input('ENTER YOUR DATE OF BIRTH:')
                              sn=[]
                              n=[]
                              dept=[]
                              sal=[]
                              woho=[]
                              desig=[]
                              dob=[]
                              do=[]
                              pa=[]
                              #password generator
                              pas=(str(random.randint(1,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
                              paswrds=open('paswrd.txt','r')
                              pasgen=paswrds.read()
                              pasgen=pasgen.split(' ')
                              while pas in pasgen:
                                  pas=(str(random.randint(1,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
                              paswrds.close()
                              paswrds=open('paswrd.txt','a')
                              paswrds.write(pas+' ')
                              paswrds.close()
                              prot=open('pasdat.txt','a')
                              prot.write(p+','+pas+'@')
                              prot.close()
                              for i in val:
                                  sn+=[i[1]]
                                  n+=[i[2]]
                                  dept+=[i[3]]
                                  sal+=[i[4]]
                                  woho+=[i[5]]
                                  desig+=[i[6]]
                                  dob+=[i[7]]
                                  do+=[i[8]]
                                  pa+=[i[9]]                   
                              if len(sn)>0:
                                  sn+=[(sn[-1]+1)]
                              else:
                                  sn+=[1]
                              n+=[p]
                              dept+=[q]
                              sal+=[r]
                              woho+=[s]
                              desig+=[t]
                              dob+=[u]
                              do+=[dojoin]
                              pa+=[pas]
                              df=pd.DataFrame({'SNO.':sn,'NAME':n,'DEPARTMENT':dept,'SALARY':sal,'WORKING HOURS':woho,'DESIGNATION':desig,'DATE OF BIRTH':dob,'DATE OF JOIN':do,'PASSWORD':pa})
                              df.to_excel(w,sheet_name='Sheet1')
                              w.save()
                              getchoice=input('Do You Want To Continue?(y/n):')
                              while len(getchoice)>1 or getchoice not in 'yYnN':
                                  print('Enter A Valid Option!')
                                  getchoice=input('Do You Want To Continue?(y/n):')
                          else:
                              print('NO JOB AVAILABLE IN THIS DEPARTMENT')
                  else:
                      box.showinfo('info','Invalid Login\nenter correct username or password')
          window = Tk()
          window.title('AUTHENTICATION')
          frame = Frame(window)
          Label1 = Label(window,text = 'Username:')
          Label1.pack(padx=15,pady= 5)
          entry1 = Entry(window,bd =5)
          entry1.pack(padx=15, pady=5)
          Label2 = Label(window,text = 'Password: ')
          Label2.pack(padx = 15,pady=6)
          entry2 = Entry(window, bd=5)
          entry2.pack(padx = 15,pady=7)
          btn = Button(frame, text = 'Check Login',command = dialog1)
          btn.pack(side = RIGHT , padx =5)
          frame.pack(padx=100,pady = 19)
          window.mainloop()
        if option==2:
            def dialog1():
                username=entry1.get()
                password = entry2.get()
                username=username.upper()
                password=password.upper()
                prot=open('pasdat.txt','r')
                prote=prot.read()
                prote=prote.split(' ')
                chk={}
                for i in prote:
                    l=i.split(',')
                    chk[l[0]]=l[-1]
                if (username == 'ADMIN' and  password == 'ADMIN'):
                    box.showinfo('info','ADMIN Login')
                    pth=os.path.abspath('DATA.xlsx')
                    j=pd.read_excel(pth)
                    j=j.values.tolist()
                    search=input('enter the name to search:')
                    search=search.upper()
                    lt=[]
                    for i in j:
                        lt+=[i[2]]
                    if search in lt:
                        for i in j:
                            if i[2]==search:
                                print('NAME:','-',i[2])
                                print('DEPARTMENT:','-',i[3])
                                print('SALARY:','-',i[4])
                                print('WORKING HOURS:','-',i[5])
                                print('DESIGNATION:','-',i[6])
                                print('DATE OF BIRTH:','-',i[7])
                                print('DATE OF JOIN:','-',i[8])
                                print('PASSWORD:','-',i[9])
                    else:
                        print('DATA NOT FOUND!!')
                elif (chk[username]==password):
                    box.showinfo('info','employee Login')
                    pth=os.path.abspath('DATA.xlsx')
                    j=pd.read_excel(pth)
                    j=j.values.tolist()
                    search=input('enter the name to search:')
                    search=search.upper()
                    lt=[]
                    for i in j:
                        lt+=[i[2]]
                    if search in lt:
                        for i in j:
                            if i[2]==search:
                                print('NAME:','-',i[2])
                                print('DEPARTMENT:','-',i[3])
                                print('DATE OF JOIN:','-',i[8])
                    else:
                        print('DATA NOT FOUND!!')
                else:
                    box.showinfo('info','Invalid Login\nenter correct username or password')
                    prot.close()
            window = Tk()
            window.title('AUTHENTICATION')
            frame = Frame(window)
            Label1 = Label(window,text = 'Username:')
            Label1.pack(padx=15,pady= 5)
            entry1 = Entry(window,bd =5)
            entry1.pack(padx=15, pady=5)
            Label2 = Label(window,text = 'Password: ')
            Label2.pack(padx = 15,pady=6)
            entry2 = Entry(window, bd=5)
            entry2.pack(padx = 15,pady=7)
            btn = Button(frame, text = 'Check Login',command = dialog1)
            btn.pack(side = RIGHT , padx =5)
            frame.pack(padx=100,pady = 19)
            window.mainloop()
        if option==3:
            while True:
                print('EMPLOYMENT EXCHANGE PROGRAM')
                print('PRESS 1 TO GET VACANCY LIST FOR EACH DEPARTMENT')
                print('PRESS 2 TO APPLY FOR JOB')
                print('PRESS 3 TO GET THE LEAST PRODUCTIVE EMPLOYEES AND TO FIRE')
                print('PRESS 4 TO GO BACK')
                choice=int(input('ENTER YOUR CHOICE:'))
                if choice==1:
                    vaclis=open('vaclis.txt','r')
                    vaclist=vaclis.readlines()
                    vacancy=[]
                    for i in vaclist:
                        vacancy+=[i.split(',')]
                    dicti={}
                    for i in vacancy:
                        dicti[i[0]]=int(i[2])-int(i[1])
                    for i in dicti:
                        print(i,':',dicti[i])
                    vaclis.close()
                elif choice==2:
                    vaclis=open('vaclis.txt','r')
                    vaclist=vaclis.read()
                    vaclist=vaclist.split('\n')
                    vaclis.close()
                    vaclis=[]
                    for i in vaclist:
                        i=i.split(',')
                        vaclis+=[i]
                    if vaclis[-1]==['']:
                        vaclis=vaclis[::-1]
                        vaclis=vaclis[1:]
                        vaclis=vaclis[::-1]
                    for i in vaclis:
                        i[1]=int(i[1])
                        i[2]=int(i[2])
                    vaclist=vaclis
                    avail={}
                    for i in vaclist:
                        avail[i[0]]=i[2]-i[1]
                    q=input('ENTER YOUR DEPARTMENT:')
                    if avail[q.upper()]>0:
                        def dialog1():
                            J='WE HAVE VACANCY IN '+q.upper()+' DEPARTMENT\nYOU CAN APPROACH US FOR AN INTERVIEW'
                            box.showinfo('INFO',J)
                        window = Tk()
                        window.title('INFO')
                        frame = Frame(window)
                        Label1 = Label(window,text = 'WE HAVE ACCEPTED YOUR APPLICATION')
                        Label1.pack(padx=15,pady= 5)
                        btn = Button(frame, text = 'MORE INFO',command = dialog1)
                        btn.pack(side = RIGHT , padx =5)
                        frame.pack(padx=100,pady = 19)
                        window.mainloop()
                    else:
                        def dialog1():
                            J='WE HAVE NO VACANCY IN '+q.upper()+' DEPARTMENT\nYOU CAN APPROACH US LATER '
                            box.showinfo('INFO',J)
                        window = Tk()
                        window.title('INFO')
                        frame = Frame(window)
                        Label1 = Label(window,text = 'YOUR APPLICATION IS REJECTED')
                        Label1.pack(padx=15,pady= 5)
                        btn = Button(frame, text = 'MORE INFO',command = dialog1)
                        btn.pack(side = RIGHT , padx =5)
                        frame.pack(padx=100,pady = 19)
                        window.mainloop()
                elif choice==3:
                    def dialog1():
                        username=entry1.get()
                        password = entry2.get()
                        if (username == 'ADMIN' and  password == 'ADMIN'):
                            path=os.path.abspath('DATA.xlsx')
                            xfl=pd.read_excel(path)
                            val=xfl.values.tolist()
                            k=[]
                            earning=int(input('enter earning of company per hour:'))
                            ndpm=int(input('enter number of days in current month:'))
                            for i in val:
                                woho=int(i[5])
                                sal=int(i[4])
                                f=((((earning)*(woho))-sal)/ndpm)*100
                                k+=[[i[3],i[2],f]]
                            dictio={}
                            listio=[]
                            tempchk={}
                            for i in k:
                                if i[0] not in listio:
                                    listio+=[i[0]]
                                    dictio[i[0]]=i[1]
                                    tempchk[i[0]]=i[2]
                                else:
                                    if tempchk[i[0]]>i[2]:
                                        dictio[i[0]]=i[1]                                
                            print('LEAST PRODUCTIVE EMPLOYEE IN EACH DEPARTMENT ARE AS FOLLOWS:')
                            for i in dictio:
                                print(i,'-',dictio[i])
                            while True:
                                fire=input('Do You Want to Fire Anyone?..(Y/N):')
                                if fire in 'yY':
                                    print('press enter if you want to quit')
                                    print('and restart the program')
                                    firedept=input('enter department to fire the person :')
                                    namefire=dictio[i] 
                                    path=os.path.abspath('DATA.xlsx')
                                    xfl=pd.read_excel(path)
                                    w=pd.ExcelWriter('DATA.xlsx',engine='xlsxwriter')
                                    val=xfl.values.tolist()
                                    n=[]
                                    for i in val:
                                        n+=[i[2]]
                                    index=0
                                    while n[index] != namefire:
                                        index+=1
                                    sn=[]
                                    n=[]
                                    dept=[]
                                    sal=[]
                                    woho=[]
                                    desig=[]
                                    dob=[]
                                    do=[]
                                    pa=[]
                                    filepd=open('pasdat.txt','r')
                                    listda=filepd.split(' ')
                                    listdi=[]
                                    for i in listda:
                                        listdi+=i.split[',']
                                    listda=[]
                                    delepas=''
                                    for i in listdi:
                                        if i[0]!=n[index]:
                                            listda+=[i]
                                        else:
                                            delepas=i[1]
                                    filepd.close()
                                    filepd=open('pasdat.txt','w')
                                    for i in listda:
                                        filepd.write(i[0]+','+i[1]+' ')
                                    filepd.close()
                                    filepd=open('paswrd.txt','r')
                                    reading=filepd.split(' ')
                                    filepd.close()
                                    filepd=open('paswrd.txt','w')
                                    for i in reading:
                                        if i!=delepas:
                                            filepd.write(i+' ')
                                    filepd.close()
                                    filepd=open('vaclis.txt','r')
                                    listda=filepd.readlines()
                                    listdi=[]
                                    for i in listda:
                                        listdi+=[i.split(',')]
                                    filepd.close()
                                    filepd=open('vaclis.txt','w')
                                    for i in listdi:
                                        if i[0]!=firedept:
                                            s=i[0]+','+i[1]+','+i[2]+'\n'
                                        else:
                                            s=i[0]+','+str(int(i[1])-1)+','+i[2]+'\n'
                                        filepd.write(s)
                                    for i in range (len(val)):
                                        if i != index:
                                            sn+=[val[i][0]]
                                            n+=[val[i][1]]
                                            dept+=[val[i][2]]
                                            sal+=[val[i][3]]
                                            woho+=[val[i][4]]
                                            desig+=[val[i][5]]
                                            dob+=[val[i][6]]
                                            do+=[val[i][7]]
                                            pa+=[val[i][8]]
                                    df=pd.DataFrame({'SNO.':sn,'NAME':n,'DEPARTMENT':dept,'SALARY':sal,'WORKING HOURS':woho,'DESIGNATION':desig,'DATE OF BIRTH':dob,'DATE OF JOIN':do,'PASSWORD':pa})
                                    df.to_excel(w,sheet_name='Sheet1')
                                    w.save()
                                    print('employee fired!')
                                elif fire in 'nN':
                                    break
                                else:
                                    print('enter a valid option!')
                        else:
                            box.showinfo('info','Invalid Login\nenter correct username or password')
                    window = Tk()
                    window.title('AUTHENTICATION')
                    frame = Frame(window)
                    Label1 = Label(window,text = 'Username:')
                    Label1.pack(padx=15,pady= 5)
                    entry1 = Entry(window,bd =5)
                    entry1.pack(padx=15, pady=5)
                    Label2 = Label(window,text = 'Password: ')
                    Label2.pack(padx = 15,pady=6)
                    entry2 = Entry(window, bd=5)
                    entry2.pack(padx = 15,pady=7)
                    btn = Button(frame, text = 'Check Login',command = dialog1)
                    btn.pack(side = RIGHT , padx =5)
                    frame.pack(padx=100,pady = 19)
                    window.mainloop()
                if choice==4:
                    break
        
