import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
import tkinter
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
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
Attributes=['High','Low','Open','Close','Adj Close','Volume']
Plot_Types=['Line','Bar','Fill','Scatter']
df=pd.read_csv('C:\\Users\\gaisundar\\Desktop\\Project\\Company Data\\Microsoft.csv',parse_dates=True,index_col=0)

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

def Mega_plot(dat):
    grid=(2,3)
    cast1=plt.subplot2grid(grid,(0,0))
    cast2=plt.subplot2grid(grid,(0,1))
    cast3=plt.subplot2grid(grid,(0,2))
    cast4=plt.subplot2grid(grid,(1,0),sharex=cast1)
    cast5=plt.subplot2grid(grid,(1,1),sharex=cast2)
    cast6=plt.subplot2grid(grid,(1,2),sharex=cast3)
    cast1.plot(dat[Attributes[0]],label='High',color='violet')
    cast2.plot(dat[Attributes[1]],label='Low',color='green')
    cast3.plot(dat[Attributes[2]],label='Open',color='black')
    cast4.plot(dat[Attributes[3]],label='Close',color='orange')
    cast5.plot(dat[Attributes[4]],label='Adj Close',color='red')
    cast6.plot(dat[Attributes[5]],label='Volume',color='blue')
    cast1.legend()
    cast2.legend()
    cast3.legend()
    cast4.legend()
    cast5.legend()
    cast6.legend()
    plt.show()               
    
    
while True:    
 print("1.Compare 1 Attribute versus time")
 print("2.Compare 2 or more Attributes versus time")
 print("3.Overall View")
 choice=int(input("Enter your choice(1-3):"))
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
    Compare_plot(df,Attrs,plot)
 elif choice==3:
     Mega_plot(df)



