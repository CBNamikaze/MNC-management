print('Loading!!')
import pandas as pd
import datetime as dt
import os
from tkinter import *
import tkinter.messagebox as box
import random
#INFORMATION TECHNOLOGY,0,50
#HUMAN RESOURCES,0,30
#MARKETING,0,25
#LEGAL CONSULTANTS,0,5
#PUBLIC RELATIONS,0,15
#MANUFACTURING,0,100
#CUSTOMER SERVICE,0,50
#FINANCE,0,20
#LABOR,0,10
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
            prote=prote.split('@')
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
            if choice==2:
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
            if choice==3:
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
    if option==4:
        break
