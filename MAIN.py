# -*- coding: utf-8 -*-
"""Created on Sat Apr 27 05:58:01 2019
@author: yasin"""

import pandas as pd
import numpy as np

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

root = Tk()
root.title('Accident Prediction system')
root.geometry('850x650')
root.configure(background="white")

var = StringVar()
label = Label( root, textvariable = var,font=('arial',20,'bold'),bd=20,background="white")
var.set("Accident Prediction system")
label.grid(row=0,columnspan=6)


def risk_file():
     root1=Tk()
     root1.title("login page")
     root1.geometry('600x500')
     root1.configure(background="white")
     def login():
         user = E.get()
         password = E1.get()
         admin_login_risk(user,password)
     L=Label(root1, text = "Username",bd=8,background="white",height=1,padx=16,pady=16,font=('arial',16,'bold'),width=10,).grid(row = 0,column=0)
     E=Entry(root1)
     E.grid(row = 0, column = 1)
     L1=Label(root1, text = "Password",bd=8,background="white",height=1,padx=16,pady=16,font=('arial',16,'bold'),width=10,).grid(row = 1,column=0)
     E1=Entry(root1,show="*")
     E1.grid(row = 1, column = 1)
     B1=Button(root1,text="Login",width=4,height=1,command=login,bd=8,background="white")
     B1.grid(row = 2, column = 1)
     root1.mainloop()

def admin_login_risk(user,password):
    if user == "admin" and password == "admin":
        risk_predict()
        
def rule_file():
     root1=Tk()
     root1.title("login page")
     root1.geometry('600x500')
     root1.configure(background="white")
     def login():
         user = E.get()
         password = E1.get()
         admin_login(user,password)
     L=Label(root1, text = "Username",bd=8,background="white",height=1,padx=16,pady=16,font=('arial',16,'bold'),width=10,).grid(row = 0,column=0)
     E=Entry(root1)
     E.grid(row = 0, column = 1)
     L1=Label(root1, text = "Password",bd=8,background="white",height=1,padx=16,pady=16,font=('arial',16,'bold'),width=10,).grid(row = 1,column=0)
     E1=Entry(root1,show="*")
     E1.grid(row = 1, column = 1)
     B1=Button(root1,text="Login",width=4,height=1,command=login,bd=8,background="white")
     B1.grid(row = 2, column = 1)
     root1.mainloop()


    
def admin_login(user,password):
    if user == "admin" and password == "admin":
        Rule_display()
        



def Rule_display():
    root1=Tk()
    root1.title("Rules")
    root1.geometry('800x800')
    root1.configure(background="white")
    

    
    label_6 = ttk.Label(root1, text = 'support',font=("Helvetica", 16),background="white")
    label_6.grid(row=1,column=0)
    
    Entry_6 = Entry(root1)
    Entry_6.grid(row=1,column=1)
    
    
    
    label_7 = ttk.Label(root1, text = 'confidence',font=("Helvetica", 16),background="white")
    label_7.grid(row=2,column=0)
    
    Entry_7 = Entry(root1)
    Entry_7.grid(row=2,column=1)
    
    def ruleplot():
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm
        from apyori import apriori  
        import pandas as pd
        import numpy as np
        df=pd.read_csv('3g.csv')
        df.shape
        df.columns
        del df['SrNo'] 
        del df['Fatal']
        del df['Grevious']
        del df['Minor']
        del df['Injured']
        del df['Date']
        del df['a']
        
        records = []  
        for i in range(0, 807):  
            records.append([str(df.values[i,j]) for j in range(0, 10)])
        association_rules = apriori(records, min_support=float(Entry_6.get()), min_confidence=float(Entry_7.get()), min_lift=1.0)
        association_results = list(association_rules)
        for item in association_results:
        
            # first index of the inner list
            # Contains base item and add item
            pair = item[0] 
            items = [x for x in pair]
        import random
        import matplotlib.pyplot as plt
         
        support=[]
        confidence=[]
        lift=[]
        color=[]
        for a in association_results:
            support.append(a[1])
            confidence.append(a[2][0][2])
            lift.append(a[2][0][3])
            color.append(a[2][0][3]*20.0)
            
        print(len(support))
        rules = []
        for item in association_results:
            # first index of the inner list
            # Contains base item and add item
            pair = item[0] 
            items = [x for x in pair]
            rules.append("Rule: " + str(items)+"->"+ items[0]+"\n")
            #print("Rule: " + str(items)+"->"+ items[0])
            print(rules)
        rules = "".join(x for x in rules)
        Text_rule.delete('1.0',END)
        Text_rule.insert(INSERT,rules)
        
    Text_rule = Text(root1)
    Text_rule.grid(row=3,column=1)
    
    B3 = Button(root1, text = "mine",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=ruleplot)
    B3.grid(row=4,column=1)
    
    root1.mainloop()


data_new = []
from sklearnn import kmf2label
def new_data():
    root10 = Tk()
    root10.title('Predict Heart DETECTOR')
    root10.geometry('400x400')
    root10.configure(background="white")
    
    """var = StringVar()
    label = Label( root, textvariable = var,font=('arial',20,'bold'),bd=20,background="Powderblue")
    var.set("Predict STRESS DETECTOR")
    label.grid(row=0,columnspan=6)
    """
    label_1 = ttk.Label(root10, text ='Date',font=("Helvetica", 16),background="white")
    label_1.grid(row=0,column=0)
    
    Entry_1 = Entry(root10)
    Entry_1.grid(row=0,column=1)
    
    label_2 = ttk.Label(root10, text = 'Time',font=("Helvetica", 16),background="white")
    label_2.grid(row=1,column=0)
    
    Entry_2 = Entry(root10)
    Entry_2.grid(row=1,column=1)
    
    label_3 = ttk.Label(root10, text = 'Location',font=("Helvetica", 16,),background="white")
    label_3.grid(row=2,column=0)
    
    Entry_3 = Entry(root10)
    Entry_3.grid(row=2,column=1)
    
    label_4 = ttk.Label(root10, text = 'Type of vehicle' ,font=("Helvetica", 16),background="white")
    label_4.grid(row=3,column=0)
    
    Entry_4 = Entry(root10)
    Entry_4.grid(row=3,column=1)
    
    label_5 = ttk.Label(root10, text = 'Type of accident',font=("Helvetica", 16),background="white")
    label_5.grid(row=4,column=0)
    
    Entry_5 = Entry(root10)
    Entry_5.grid(row=4,column=1)
    
    label_6 = ttk.Label(root10, text = 'No of Casualities',font=("Helvetica", 16),background="white")
    label_6.grid(row=5,column=0)
    
    Entry_6 = Entry(root10)
    Entry_6.grid(row=5,column=1)
    
    label_7 = ttk.Label(root10, text = 'Vehicle Number',font=("Helvetica", 16),background="white")
    label_7.grid(row=6,column=0)
    
    Entry_7 = Entry(root10)
    Entry_7.grid(row=6,column=1)
    
    global model,labelText
    
    def predout_knn():
        global model,labelText
        
        data_new.append(Entry_1.get()+","+Entry_2.get()+","+Entry_3.get()+","+Entry_4.get()+","+Entry_5.get()+","+Entry_6.get()+","+Entry_7.get()+"\n")
        
        file = open('data.csv','w')
        file.writelines(data_new)
        file.close()
        
    label_7 = Button(root10, text = 'submit',font=("Helvetica", 16),background="white",command = predout_knn)
    label_7.grid(row=7,column=0)
    


def risk_predict():
    root11 = Tk()
    root11.title('RISK PREDICTION')
    root11.geometry('400x400')
    root11.configure(background="white")
    
    var = StringVar()
    label = Label( root11, textvariable = var,font=('arial',20,'bold'),bd=20,background="white")
    var.set("RISK PREDICTION")
    label.grid(row=0,columnspan=6)
    
    label_1 = ttk.Label(root11, text ='Area',font=("Helvetica", 16),background="white")

    label_1.grid(row=1,column=0)
    tkvar = StringVar(root11)
    choices = ['A Narayanapura','Agaram','Banasavadi','Basavanapura','Bellanduru','Benniganahalli','Bharathi Nagar','BTM Layout','C V Raman Nagar','Chickpete','Devasandra','Dharmaraya Swamy Temple','Dodda Nekkundi','Domlur','Garudachar Playa','Gurappanapalya','Hagadur','HAL Airport','Halsoor','Hemmigepura','Horamavu','Hoysala Nagar','HSR Layout','Hudi','J P Nagar','Jaraganahalli','Jayanagar East','Jeevanbhima Nagar','Jogupalya','K R Puram','Kacharkanahalli','Kadugodi','Kammanahalli','Konena Agrahara','Madivala','Marathahalli','New Tippasandara','Other','other','Ramamurthy Nagar','Sampangiram Nagar','Sarakki','Shantala Nagar','Singasandra','Sudham Nagara','Varthuru','Vasanthpura','Vijnana Nagar','Vijnanapura','Yelchenahalli']
     
    popupMenu = OptionMenu(root11, tkvar, choices[1], *choices)
    #Label(root, text="select area",background="purple2").grid(row=0,column=0)
    popupMenu.grid(row=1,column=1)
    tkvar.set('Select area')

    def pass1():
        import pandas as pd
        import numpy as np
        
        print()
        bdf = pd.read_excel('bangalore-cas-alerts.xlsx')
        bdf.info()
        bdf = bdf.rename(columns = {'deviceCode_time_recordedTime_$date':'timestamp'})
        bdf['timestamp'] = pd.to_datetime(bdf['timestamp'])
        bdf['eventDate'] = pd.to_datetime(bdf['timestamp'])
        bdf['eventDate'] = bdf['eventDate'].dt.strftime('%Y%m%d')
        bdf['e_hour'] = pd.to_datetime(bdf['timestamp'], format = '%H:%M:%S').dt.hour
        bdf['ehourCat'] = 0
        bdf['ehourCat'] = np.where((bdf['e_hour'] >= 0) & (bdf['e_hour'] < 6), 1, bdf['ehourCat'])
        bdf['ehourCat'] = np.where((bdf['e_hour'] >= 6) & (bdf['e_hour'] < 10), 2, bdf['ehourCat'])
        bdf['ehourCat'] = np.where((bdf['e_hour'] >= 10) & (bdf['e_hour'] < 16), 3, bdf['ehourCat'])
        bdf['ehourCat'] = np.where((bdf['e_hour'] >= 16) & (bdf['e_hour'] < 21), 4, bdf['ehourCat'])
        bdf['ehourCat'] = np.where((bdf['e_hour'] >= 21) & (bdf['e_hour'] < 24), 5, bdf['ehourCat'])
        
        bwdf = pd.read_excel('bangalore-weather.xlsx')
        bwdf['w_hour'] = pd.to_datetime(bwdf['time'], format= '%H:%M').dt.hour
        bwdf['hourCat'] = 0
        bwdf['hourCat'] = np.where((bwdf['w_hour'] >= 0) & (bwdf['w_hour'] < 6), 1, bwdf['hourCat'])
        bwdf['hourCat'] = np.where((bwdf['w_hour'] >= 6) & (bwdf['w_hour'] < 10), 2, bwdf['hourCat'])
        bwdf['hourCat'] = np.where((bwdf['w_hour'] >= 10) & (bwdf['w_hour'] < 16), 3, bwdf['hourCat'])
        bwdf['hourCat'] = np.where((bwdf['w_hour'] >= 16) & (bwdf['w_hour'] < 21), 4, bwdf['hourCat'])
        bwdf['hourCat'] = np.where((bwdf['w_hour'] >= 21) & (bwdf['w_hour'] < 24), 5, bwdf['hourCat'])
        bwdf = bwdf.drop_duplicates(subset = ['weatherDate', 'hourCat'], keep = 'first')
        bwdf['ehourCat'] = bwdf['hourCat']
        bwdf['weatherDate'] = bwdf['weatherDate'].astype(str)
        bdf['weatherDate'] = bdf['eventDate']
        bdf['weatherDate'] = bdf['weatherDate'].astype(str)
        b1 = pd.merge(bdf, bwdf, on = ['weatherDate', 'ehourCat'], how = 'left')
        b1 = b1.rename(columns = {'deviceCode_location_wardName':'Area'})
        badf = pd.read_excel('bangalore-accident-zones.xlsx')
        b = pd.merge(b1, badf, on = ['Area'], how = 'left')
        b = b.rename(columns = {'deviceCode_pyld_alarmType':'Alarm_Type'})
        b = b.rename(columns = {'deviceCode_pyld_speed':'Plying_Speed'})
        b['hasOversped'] = np.where(b.Plying_Speed > 60, 1, 0)
        b['hasOversped'] = np.where(b.Alarm_Type == 'Overspeed', 1, b['hasOversped'])
        for column in ['temperature', 'visibility', 'condition']:
            b[column].fillna(b[column].mode()[0], inplace=True)
        b['visibility'] = np.where(b['visibility'] < 10, 0, 1)
        df = b.copy()
        df['hasOversped'] = np.where(b.hasOversped == 1, 'Yes', 'No')
        df['visibility'] = np.where(b.visibility == 0, 'Low', 'High')
        df['ehourCat'] = b['ehourCat'].map({1: 'Early', 2: 'PeakM', 3: 'RegularM'})
        b['Accident_Severity'] = b['Accident_Severity'].map({'High': 3, 'Medium': 2, 'Low': 1})
        b['Pothole_Severity'] = b['Pothole_Severity'].map({'High': 3, 'Medium': 2, 'Low': 1})
        b['Alarm_Type'] = b['Alarm_Type'].map({'PCW': 1, 'FCW': 2, 'Overspeed': 3, 'HMW': 4, 'UFCW': 5, 'LDWL': 6, 'LDWR': 7})
        b['condition'] = b['condition'].map({'Clear': 1, 'Sunny': 2, 'Passing clouds': 3,
               'Broken clouds': 4, 'Scattered clouds': 5, 'Fog': 6, 'Haze': 7, 'Partly cloudy': 8,
               'Mild': 9, 'Drizzle. Broken clouds': 10})
        b['Area'] = b['Area'].map({'Kadugodi': 1, 'Garudachar Playa': 2, 'Hudi': 3, 'Other': 4, 'Devasandra': 5,
               'Hagadur': 6, 'Bellanduru': 7, 'Marathahalli': 8, 'Dodda Nekkundi': 9, 'Varthuru': 10,
               'HAL Airport': 11, 'Vijnana Nagar': 12, 'Konena Agrahara': 13, 'A Narayanapura': 14,
               'C V Raman Nagar': 15, 'Jeevanbhima Nagar': 16, 'HSR Layout': 17, 'Domlur': 18, 'Jogupalya': 19,
               'Hoysala Nagar': 20, 'New Tippasandara': 21, 'Benniganahalli': 22, 'Singasandra': 23,
               'Basavanapura': 24, 'Halsoor': 25, 'Agaram': 26, 'Shantala Nagar': 27, 'Sampangiram Nagar': 28,
               'Sudham Nagara': 29, 'Dharmaraya Swamy Temple': 30, 'Chickpete': 31, 'Banasavadi': 32,
               'Horamavu': 33, 'Kacharkanahalli': 34, 'Kammanahalli': 35, 'Vijnanapura': 36, 'Ramamurthy Nagar': 37,
               'K R Puram': 38, 'BTM Layout': 39, 'Madivala': 40, 'Gurappanapalya': 41, 'J P Nagar': 42, 'Sarakki': 43,
               'Jaraganahalli': 44, 'Vasanthpura': 45, 'Hemmigepura': 46, 'Yelchenahalli': 47,
               'Jayanagar East': 48, 'Bharathi Nagar': 49, 'other': 4})
        
        #writer = pd.ExcelWriter('bangalore-consolidated-data.xlsx')
        #b.to_excel(writer, index = False, sheet_name = 'Sheet1')
        #df.to_excel(writer, index = False, sheet_name = 'Sheet2')
        #writer.save()
        
        del b['deviceCode_deviceCode'], b['deviceCode_location_latitude'], b['deviceCode_location_longitude']
        del b['w_hour'], b['Mapped_Location'], b['timestamp'], b['e_hour'], b['weatherDate']
        del b['hourCat'], b['time'], b['temperature'], b['eventDate'], b['Plying_Speed']
        
        del df['deviceCode_deviceCode'], df['deviceCode_location_latitude'], df['deviceCode_location_longitude']
        del df['w_hour'], df['Mapped_Location'], df['timestamp'], df['e_hour'], df['weatherDate']
        del df['hourCat'], df['time'], df['temperature'], df['eventDate'], df['Plying_Speed']
                
        from sklearn.cluster import KMeans
        X = b.values.astype(np.float)
        kmeans = KMeans(n_clusters = 2, max_iter = 2000, algorithm = 'full').fit(X)
        kmf2labels = kmeans.labels_
        kmf2labels = kmf2labels.tolist()
        print('Finished clustering using K-Means')
        
        b['labels'] = kmf2labels
        df['labels'] = kmf2labels
        df['labels'] = df['labels'].map({0: 'High', 1: 'Low'})
        
        Entry_11.delete(0,END)
        Entry_11.insert(0,'Finished clustering using K-Means')
        
    def main_risk_predict():
        area = tkvar.get()
        if kmf2label['Area'][tkvar.get()] == 1:
            Entry_12.delete(0,END)
            Entry_12.insert(0,'HIGH')
        else :
            Entry_12.delete(0,END)
            Entry_12.insert(0,'LOW')
            
        
                
    label_7 = Button(root11, text = 'submit',font=("Helvetica", 16),background="white",command = main_risk_predict)
    label_7.grid(row=2,column=0)
        
   
            
    Entry_12 = Entry(root11)
    Entry_12.grid(row=2,column=1)

    Entry_11 = Entry(root11)
    Entry_11.grid(row=0,column=1)    

    label_8 = Button(root11, text = 'train',font=("Helvetica", 16),background="white",command = pass1)
    label_8.grid(row=0,column=0) 
    
    
def plot_graph():
    root10 = Tk()
    root10.title('GRAPHS')
    root10.geometry('400x400')
    root10.configure(background="white")
    
    """var = StringVar()
    label = Label( root, textvariable = var,font=('arial',20,'bold'),bd=20,background="Powderblue")
    var.set("Predict STRESS DETECTOR")
    label.grid(row=0,columnspan=6)
    """
    
    from PIL import ImageTk,Image
    def graph1():
        image = Image.open("graph1.png")
        image = image.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)  
        panel1 = Label(root, image=img)
        panel1.image = img
        panel1.grid(row=3,column=0)
    
    def graph2():
        image = Image.open("graph2.png")
        image = image.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)  
        panel2 = Label(root, image=img)
        panel2.image = img
        panel2.grid(row=3,column=1)
    
    def graph3():
        image = Image.open("graph3.png")
        image = image.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)  
        panel3 = Label(root, image=img)
        panel3.image = img
        panel3.grid(row=3,column=2)
    
    def graph4():
        import numpy as np # linear algebra
        import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
        import os
        
        import matplotlib.pyplot as plt
        import seaborn as sns
        # Input data files are available in the "../input/" directory.
        # For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
        from pandas import DataFrame , read_csv
        df=pd.read_csv('Details_of_road_accident_deaths_by_situation_state.csv')
        ncount=df['STATE/UT'].value_counts()
        ap=df[df['STATE/UT']=='ANDHRA PRADESH']
        ap1=ap[ap['Year']==2001]
        a=ap1.head(14)
        ap=df[df['STATE/UT']=='KARNATAKA']
        ap1=ap[ap['Year']==2001]
        a=ap1.head(14)
        t=df[df['CAUSE']=='Total Truck/Lorry']
        t.head()
        r=t[t['STATE/UT']== tkvar.get()]
        fig = plt.figure(figsize=(20,10))
        ax = plt.axes()
        
        x = np.linspace(0, 10, 1000)
        ax.plot(r['Year'],r['Total'])
        plt.title('NO OF ACCIDENTS DUE TO TRUCK AND LORRY')
        plt.xlabel('year')
        plt.ylabel('no of accidents')
        plt.savefig('graph4.png',dpi=199)
        
        image = Image.open("graph4.png")
        image = image.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)  
        panel3 = Label(root, image=img)
        panel3.image = img
        panel3.grid(row=3,column=3)
        
    label_1 = ttk.Label(root10,background="white")
    label_1.grid(row=1,column=0)    
    
    var = StringVar()
    label = Label( root10, textvariable = var,font=('arial',20,'bold'),bd=20,background="white")
    var.set("RISK PREDICTION")
    label.grid(row=0,columnspan=6)
    
    label_1 = ttk.Label(root10, text ='Area',font=("Helvetica", 16),background="white")
    label_1.grid(row=1,column=0)
    tkvar = StringVar(root10)
    choices = ['ANDHRA PRADESH','ASSAM','BIHAR','CHHATTISGARH','GOA','GUJARAT','HARYANA','HIMACHAL PRADESH','JAMMU & KASHMIR','JHARKHAND','KARNATAKA','KERALA','KERALA','MADHYA PRADESH','MAHARASHTRA','MANIPUR','MEGHALAYA','MIZORAM','NAGALAND','ODISHA','PUNJAB','RAJASTHAN','SIKKIM','TAMIL NADU','TRIPURA','UTTAR PRADESH','UTTARAKHAND','WEST BENGAL','TOTAL (STATES)','A & N ISLANDS','CHANDIGARH','D & N HAVELI','DAMAN & DIU','DELHI (UT)','LAKSHADWEEP','PUDUCHERRY','TOTAL (UTs)','TOTAL (ALL INDIA)',]
     
    popupMenu = OptionMenu(root10, tkvar, choices[1], *choices)
    #Label(root, text="select area",background="purple2").grid(row=0,column=0)
    popupMenu.grid(row=1,column=1)
    tkvar.set('Select area')
    
    B_rule = Button(root10, text = "graph1",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=graph1)
    B_rule.grid(row=2,column=0) 
    
    B = Button(root10, text = "graph2",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=graph2)
    B.grid(row=3,column=0)
    
    B1 = Button(root10, text = "graph3",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=graph3)
    B1.grid(row=2,column=4)
    
    B3 = Button(root10, text = "graph4",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=graph4)
    B3.grid(row=3,column=4)
        


label_0 = ttk.Label(root,background="white")
label_0.grid(row=1,column=0)
    
B_rule = Button(root, text = "Rules",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=rule_file)
B_rule.grid(row=1,column=1) 

B = Button(root, text = "Risk prediction",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=risk_file)
B.grid(row=2,column=1)

label_00 = ttk.Label(root,background="white")
label_00.grid(row=1,column=3)

B1 = Button(root, text = "Plot Graph",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=plot_graph)
B1.grid(row=1,column=3)

B3 = Button(root, text = "entry new data",height=1,padx=16,pady=16,bd=8,font=('arial',16,'bold'),width=10,bg="white",command=new_data)
B3.grid(row=2,column=3)

root.mainloop()

