import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
style.use('ggplot')
Attributes=['High','Low','Open','Close','Adj Close','Volume']
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
def Daily_Avg(dat,n):
    Days_Specs=int(input("Enter number of previous days to calculate Moving Average:"))
    dat[str(Days_Specs)+' Mov_Avg']=dat[Attributes[n-1]].rolling(window=Days_Specs,min_periods=0).mean()
    sample=int(input("Enter number of sample days are required:"))
    print(dat.head(sample))
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
print(Attributes)
AttriNum=int(input("Enter Attribute number of choice:"))
df=pd.read_csv('C:\\Users\\gaisundar\\Desktop\\Project\\Company Data\\Microsoft.csv',parse_dates=True,index_col=0)
Daily_Avg(df,AttriNum)
    
