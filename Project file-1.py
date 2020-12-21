#Author: Ekta Solanki

import pandas as pd
import operator
import numpy as np                                                               
import matplotlib.pyplot as plt
import matplotlib.pyplot as plot

BBS = pd.read_csv("bus-breakdown-and-delays.csv")

del BBS['Incident_Number']


BusDelayed15 = (BBS.School_Year=='2015-2016').sum()
BusDelayed16 = (BBS.School_Year=='2016-2017').sum()
BusDelayed17 = (BBS.School_Year=='2017-2018').sum()
BusDelayed18 = (BBS.School_Year=='2018-2019').sum()

print 
print 
print "   Total", BusDelayed15 , "buses faced delay/breakdown in school year 2015-16 "
print "   Total", BusDelayed16 , "buses faced delay/breakdown in school year 2016-17 "
print "   Total", BusDelayed17 , "buses faced delay/breakdown in school year 2017-18 "
print "   Total", BusDelayed18 , "buses faced delay/breakdown in school year 2018-19 "

#Running late or Breakdown counts per year

print("\n*******Table for school year, and count of running late or breakdown********\n")
print BBS.groupby(['School_Year','Breakdown_or_Running_Late']).size().reset_index().rename(columns={0:'count'})


#################age of student stuck in bus

StudentsOnBus = pd.DataFrame(BBS.groupby(by='School_Age_or_PreK')['Number_Of_Students_On_The_Bus'].sum())
print'\n''\n'
print "\n  Total" ,StudentsOnBus['Number_Of_Students_On_The_Bus'].iloc[1] , "were School age kids and", StudentsOnBus['Number_Of_Students_On_The_Bus'].iloc[0] , "were Pre KG kids during the break down and delay.\n\n"


#########################bus number and incident graph

BusNoDictionary = BBS['Bus_No'].value_counts().to_dict()

BusNoSorted = sorted(BusNoDictionary.items(), key=operator.itemgetter(1), reverse=True) 
Top20BusNo= BusNoSorted[:20]
#print Top20BusNo

#BusNoTable = pd.DataFrame(BusNoSorted).head(20)
#BusNoTable.columns = ['BUS-NUMBER','INCIDENTS']
#BusNoTable.index = range(1,21)
#print BusNoTable
#labels=['Bus-number']

labels, ys = zip(*Top20BusNo)
xs = np.arange(len(labels)) 

color=['fuchsia','violet','darkviolet','rebeccapurple','slateblue','darkblue','slategrey','dodgerblue','skyblue','cadetblue','c','darkslategrey'
                ,'mediumturquoise','mediumseagreen','g','lightgreen','lawngreen','olive','khaki','goldenrod']
plt.bar(xs, ys, width=0.5, align='center',color=color)
plt.xlabel("Bus Number")
plt.ylabel("No of Incident")
plt.rcParams.update({'font.size': 18})
plt.xticks(xs, labels)


##############top companies to faulty buses
#after cleaning bus names manualy in excel, using find and replce

BusCompnyDictionary = BBS['Bus_Company_Name'].value_counts().to_dict()
BusCompnySorted_dict= sorted(BusCompnyDictionary.items(), key=operator.itemgetter(1), reverse=True) 

                                                                                   
print"**********TOP-10 BUS VENDORS TO CAUSE MOST NUMBER OF BREAKDOWNS AND DELAYS ARE*********"
WorstComanies=pd.DataFrame(BusCompnySorted_dict).head(10)#
WorstComanies.columns = ['||BUS COMPANY||','      ||NUMBER OF INCIDENTS||']
WorstComanies.index = range(1,11)
print 
print WorstComanies

ReliableCompanies= pd.DataFrame(BusCompnySorted_dict).tail(10)
print'\n''\n'
ReliableCompanies.columns = ['||BUS COMPANY||','      ||NUMBER OF INCIDENTS||']
ReliableCompanies.index = range(1,11)
print 
print "*************Top-10 Most reliable Companies are*************"
print ReliableCompanies


########Top borough to have incidents
Borough = BBS['Boro'].value_counts().to_dict()
Borough_sorted = sorted(Borough.items(), key=operator.itemgetter(1), reverse=True) 

Top_Borough = pd.DataFrame(Borough_sorted)
Top_Borough.columns = ['||BOROUGH||','    ||INCIDENTS||']
Top_Borough.index = range(1,12)
print'\n'
print"Borough and incident numbers Table"
print
print Top_Borough

########Top reasons to have incidents
Reason = BBS['Reason'].value_counts().to_dict()
Reason_sorted = sorted(Reason.items(), key=operator.itemgetter(1), reverse=True) 

#pie chart of reasons and incdents
x= pd.Series(Reason)
y = pd.Series.sort_values(x)
z = pd.DataFrame(y)
fig, axes = plot.subplots(nrows=1)
z.plot(y=0,kind = 'pie',fontsize=8,autopct='%0.1f%%')
plot.show()

###########  How many times contractor notified the school

CNotifiedS = pd.DataFrame(BBS['Has_Contractor_Notified_Schools'].value_counts())

CNotifiedS.columns = ['SchoolNotified']
print 
print"Number of times Contractor notified School"
print'\n', CNotifiedS

#############Has_Contractor_Notified_Parents
CNotifiedP = pd.DataFrame(BBS['Has_Contractor_Notified_Parents'].value_counts())
CNotifiedP.columns = [' Parents Notified']
print 
print"Number of times Contractor notified Parents"
print'\n', CNotifiedP

###########Have_Driver_Alerted_OPT
DNotifiedOPT = pd.DataFrame(BBS['Have_You_Alerted_OPT'].value_counts())
DNotifiedOPT.columns = [' OPT Notified']
print
print "Number of times Contractor notified OPT"
print'\n', DNotifiedOPT


############When school bus are delayed
Runtype = pd.DataFrame(BBS['Run_Type'].value_counts())
print
print"Runtypes and Delay Table"
print '\n', Runtype


############redefined time in excel using VB and calculating average delay time

time_reason=pd.DataFrame(BBS.groupby(by=['Reason','Breakdown_or_Running_Late'])['Filtered_Time'].mean())
time_reason.columns=['Time taken']

print
print"Reasons and mean delay time"
print time_reason









