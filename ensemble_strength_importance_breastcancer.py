
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:03:45 2019

@author: Arpan Dam
"""
# importing csv module 
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from binarytree import Node


importance =1
mclass1=0
sortedmargin=[]
sortedimportance=[]
error=1
margin=0
mclass2=0
counttest=0
keyerror=0
countkey=0
totalrow=0
Accurate=0
Accuratei=0
sumofmargin=0
testingnumber=0
testkey=0
histo=[]
histo1=[]
mcc1={}
mcc2={}
finalsecondclass={}
finalsecondclassi={}
finalfirstclass={}
sumofweight=0
finalfirstclassi={}
firstfinal={}
firstfinali={}
secondfinal={}
secondfinali={}
for i1 in range(139):
    firstfinal[i1+1]=0
    firstfinali[i1+1]=0
for i2 in range(139):
    secondfinal[i2+1]=0
    secondfinali[i2+1]=0
index=0
totalclass=0
accurate=0
storefirstclass=[]
storesecondclass=[]
listtostoreimportanceandstrength=[]
finallisttostoreimportanceandstrength=[]
storefirstclassprobabilityforimportance=[]
storesecondclassprobabilityforimportance=[]
keytostoreentry={}
sortedentry={}
probabilityofsecondclass={}
probabilityoffirstclass={}
probabilityoffirstclasssorted={}
probabilityofsecondclasssorted={}


    


def gamma(x):
    x=x-1
    factorial = 1
    if int(x) >= 1:
        for i in range (1,int(x)+1):
            factorial = factorial * i
    return factorial




# this function will execute for each leaf node, v is the leaf node
def importanceweight(mv1,mv2,key):
    t=gamma(mv1+1)*gamma(mv2+1) # assume alpha is 1 and number of class is 2
    t=t*gamma(2)
    t1=gamma((mv1+1)+(mv2+1))
    t1=t1*(gamma(1)*gamma(1))
    fraction=t/t1
    global importance
    importance=fraction * importance














def train_split(mcctrain1={},mcctrain2={},m={},m1={}):
    m1trainreverse={}
    global totalrow
    global index
    global accurate
    global margin
    for key1 in sorted(m1.keys()):
        m1trainreverse[key1] = m1[key1]
    mtrainreverse={}
    for key2 in sorted(m.keys()):
        mtrainreverse[key2] = m[key2] 
    op=list(mtrainreverse.keys())
    jk=0
   
    with open('Breastcancertesting.csv', encoding='utf-8-sig') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for key in mtrainreverse:
            if(key != op[len(mtrainreverse)-1]):
                left, right = list(), list()
                #jk=0
                opo=0
                for row in readCSV:
                    
                   
                    opo=opo+1
                    for opl in range (len(op)):
                        if op[opl]==key and op[opl]!=op[-1]:
                            key2=op[opl+1]
                            m23=checkleftrightnode(root,key,key2)
                            #print(m23)
                            if m23 == 1:
                                if float((row[m1trainreverse[key]])) < mtrainreverse[key]:
                                    left.append(row)
                             #   readCSV=left
                                    jk=1
                                   
                            if m23 == 2:
                                if float((row[m1trainreverse[key]])) > mtrainreverse[key]:
                                    right.append(row)
                            #readCSV=right
                                    jk=2
                                   
                               
                if jk==1:
                    readCSV=left
                if jk==2:
                    readCSV=right
            else:
                
                firstclassprobability=(mcctrain1[key]+1)/562
                
                secondclassprobability=(mcctrain2[key]+1)/562
                global sortedentry
                global storefirstclass
                global storesecondclass
                global storefirstclassprobabilityforimportance
                global storesecondclassprobabilityforimportance
                for row2 in readCSV:
                    index1=0                    
                    with open('Breastcancertesting.csv', encoding='utf-8-sig') as csvfile:
                        readCSV1 = csv.reader(csvfile, delimiter=',')
                        for row1 in readCSV1:
                            index1=index1+1
                            if row1 == row2:
                                sortedentry[index1]=row2
                                probabilityoffirstclass[index1]=firstclassprobability
                                probabilityofsecondclass[index1]=secondclassprobability
                        
                storefirstclass.append(readCSV)
                storesecondclass.append(readCSV)
                storefirstclassprobabilityforimportance.append(firstclassprobability)
                storesecondclassprobabilityforimportance.append(secondclassprobability)
                for readCSVlength in readCSV:                     
                     if(readCSVlength[9]) == '0.2' and (secondclassprobability > firstclassprobability):
                        accurate=accurate+1
                     if(readCSVlength[9]) == '0.4' and (firstclassprobability > secondclassprobability):
                        accurate=accurate+1
                     totalrow=totalrow+1
                     if mcctrain1[key]==0:
                         probability_of_1st_class = 0
                         if mcctrain2[key]!=0:
                             probability_of_2nd_class = mcctrain2[key]/(mcctrain1[key]+mcctrain2[key])
                         else:
                             probability_of_2nd_class=0
                     if mcctrain2[key]==0:
                         probability_of_2nd_class = 0
                         if mcctrain1[key]!=0:
                             probability_of_1st_class = mcctrain1[key]/(mcctrain1[key]+mcctrain2[key])
                         else:
                             probability_of_1st_class = 0
                     else:    
                         probability_of_1st_class = mcctrain1[key]/(mcctrain1[key]+mcctrain2[key])
                         probability_of_2nd_class = mcctrain2[key]/(mcctrain1[key]+mcctrain2[key])       
                     margin=margin + abs(probability_of_1st_class - probability_of_2nd_class)
                    
                    
                         
                

















    
def test_split(m={},m1={}):
    
    global countkey
    global keyerror
    global totalclass
    global counttest
    global error
    global testkey
    #print(root)
    global mcc1
    global mcc2
   
    jk=0
    m1reverse={}
    for key1 in sorted(m1.keys()):
        m1reverse[key1] = m1[key1]
    mreverse={}
    for key2 in sorted(m.keys()):
        mreverse[key2] = m[key2]  
        #checkleftrightnode(root,x,y)
        
    
    op=list(mreverse.keys())
   # left, right = list(), list()
    with open('Breastcancertraining.csv', encoding='utf-8-sig') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for key in mreverse:
            #jk=0
            countkey=countkey+1
            if(key != op[len(mreverse)-1]):
                left, right = list(), list()
                #jk=0
                for row in readCSV:
                    counttest=counttest+1
                    n=0 
                    #jk=0
                    for opl in range (len(op)):
                        if op[opl]==key and op[opl]!=op[-1]:
                            key2=op[opl+1]
                            m23=checkleftrightnode(root,key,key2)
                            #print(m23)
                            if m23 == 1:
                                if float((row[m1reverse[key]])) < mreverse[key]:
                                    left.append(row)
                             #   readCSV=left
                                    jk=1
                                    a1=np.array(left)
                            if m23 == 2:
                                if float((row[m1reverse[key]])) > mreverse[key]:
                                    right.append(row)
                            #readCSV=right
                                    jk=2
                                    b=np.array(right)
                if jk==1:
                    readCSV=left
                if jk==2:
                    readCSV=right
            if jk==0 and (key == op[len(mreverse)-1]) :
                #print("data on leaf node")
                #print(key)
                keyerror=0
                
                if bool(mcc1) is False :
                    mcc1[key]=0
                if bool(mcc2) is False :
                    mcc2[key]=0
               
                mcc1[key]=0
                mcc2[key]=0
                importanceweight(0,0,key)
                        
            if jk!=0 and (key == op[len(mreverse)-1]):
                secondclass=0
                firstclass=0
                
                global mclass1
                global mclass2
                for readCSVlength in readCSV:
                    if(readCSVlength[9]) == '0.2':
                        secondclass=secondclass+1
                    else:
                        firstclass=firstclass+1
                      
                    jk=0
                
                totalclass=totalclass+secondclass+firstclass
                mcc1[key]=firstclass
                mcc2[key]=secondclass
                mclass2=mclass2+secondclass
                mclass1=mclass1+firstclass
                keyerror=2
                importanceweight(firstclass,secondclass,key)
                    
                        
                        
            
 

matrix1 = [] 
g=[]  

#dyarr1 = []

matrix2 = [] 

       
g=[]
test=[]
testfeature=[]
test1={}
g1={}        
s = np.random.uniform(1,0)
root = Node(1)
#print(root);
string_lengths = {}
string_length = {}
store={}
storefeature={}
notree=0;
number_of_trees= int(input("Enter number of trees"))
val = int(input("Enter height of the tree:"))
lamb = float(input("Enter  the value of lambda"))
Dimension =int(input("Input number of dimension:"))
kl=0
 
j=0
result1 =[]
result2=[]
def countNonleaf(root,dyarr1 = [],dyarr2 = []): 
      
    # Base cases.  
    if (root == None or (root.left == None and 
                         root.right == None)):  
        return 0
    string_lengths[root.value] = np.random.uniform(1,0)
    string_length[root.value] = np.random.randint(0,Dimension-1)
    # The below code is for assuming all features are following normal distribution
    '''if string_length[root.value] == 0:
        string_lengths[root.value] = np.random.normal(0.454383, 0.291292, 1)
    if string_length[root.value] == 1:
        string_lengths[root.value] = np.random.normal(0.320751, 0.301309, 1)
    if string_length[root.value] == 3:
        string_lengths[root.value] = np.random.normal(0.286225, 0.287381, 1)
    if string_length[root.value] == 4:
        string_lengths[root.value] = np.random.normal(0.330948, 0.231617, 1)
    if string_length[root.value] == 5:
        string_lengths[root.value] = np.random.normal(0.377102, 0.371732, 1)
    if string_length[root.value] == 6:
        string_lengths[root.value] = np.random.normal(0.349195, 0.23263, 1)
    if string_length[root.value] == 7:
        string_lengths[root.value] = np.random.normal(0.3, 0.309526, 1)
    if string_length[root.value] == 8:
        string_lengths[root.value] = np.random.normal(0.164758, 0.178784, 1)
    if string_length[root.value] == 2:
        string_lengths[root.value] = np.random.normal(0.328265, 0.297381, 1) '''   
    global store
    global storefeature
    store=string_lengths
    storefeature=string_length
    dyarr1.append(string_lengths[root.value])
    dyarr2.append(string_length[root.value])
    
    global result1
    global result2
    result1=dyarr1
    result2=dyarr2
    
    return (1 + countNonleaf(root.left,dyarr1,dyarr2) + 
                countNonleaf(root.right,dyarr1,dyarr2)) 
def checkleftrightnode(node,x,y):
    if node.height>0:
        if node.value == x:
            #print("inside outer for")
            if node.left.value == y:
                #print("inside inner for")
                #print(1)
                return 1
            else:
                #print("inside inner else")
                #print(0)
                return 2
        else:
            #print("inside outer else")
            return checkleftrightnode(node.left,x,y) + checkleftrightnode(node.right,x,y) 
    else:
        return 0
          
def getLeafCount(node): 
    if node is None: 
        return 0 
    if(node.left is None and node.right is None): 
        return 1 
    else: 
        return getLeafCount(node.left) + getLeafCount(node.right)   
def print_arr(arr):
   # i=0
    if not arr or arr.__len__() == 0:
            return
    #g1    
    counter = arr.__len__() -2
    global test
    global g
    global g1
    global gfeature
   
    g=[]
    g1={}
    gfeature={}
    g1[arr[arr.__len__() -1]]=0
    gfeature[arr[arr.__len__() -1]]=0
    
    while counter >= 0:
        g1[arr[counter]]=store[arr[counter]]
        gfeature[arr[counter]]=storefeature[arr[counter]]
        g.append(store[arr[counter]])
        
        counter = counter-1
   
    test_split(g1,gfeature)
    train_split(mcc1,mcc2,g1,gfeature)
    test.append(g1)
    testfeature.append(gfeature)
    #print(arr[0])
def checkLeafCount(node): 
    if node is None: 
        return 0 
    if(node.left is None and node.right is None): 
        return 1 
    else: 
        return 0
def print_leaf_to_root_paths(root , arr):
	if not root:
		return
	
	arr.append(root.value)
   # root.
	
	if checkLeafCount(root):
		print_arr(arr)
	
	if root.left:
		print_leaf_to_root_paths(root.left, arr)
	
	if root.right:
		print_leaf_to_root_paths(root.right, arr)

	
	arr.pop()
def buildtree(r):
    
    global i  
    r1=np.random.random();
    if float(r1)<lamb:
         i=i+1
         r.left=Node(i)
         i=i+1
         r.right=Node(i)
   
def fringe(root):

    if root.left or root.right:
        if root.left:
            yield from fringe(root.left)
        if root.right:
            yield from fringe(root.right)
    else:
        yield root


rows, cols = (10, 5) 
matrix1 = [[0]*cols]*rows
indexofkey=1 
with open('Breastcancertraining.csv', encoding='utf-8-sig') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            keytostoreentry[indexofkey]=row
            indexofkey=indexofkey+1
while notree < number_of_trees:

    
    i=1
    root = Node(1)
    notree=notree+1
    while root.height<=val-1:
        for i1 in list(fringe(root)): 
            buildtree(i1)
        fringe(root)
    countNonleaf(root,matrix1,matrix2)
    string_lengths = {}
    string_length = {}
    #print(root)
    root1=root
    print_leaf_to_root_paths(root , [])
    g=[]
    test=[]
    testfeature=[]
    
    for key in sorted(probabilityoffirstclass.keys()) :
        finalfirstclass[key]=probabilityoffirstclass[key]
        finalfirstclassi[key]=probabilityoffirstclass[key]
    for key in sorted(probabilityofsecondclass.keys()) :
        finalsecondclass[key]=probabilityofsecondclass[key]
        finalsecondclassi[key]=probabilityofsecondclass[key]
    for key in finalfirstclass.keys():
        finalfirstclass[key]=finalfirstclass[key]*((margin/139))
        firstfinal[key]=finalfirstclass[key]+firstfinal[key]
    for key in finalsecondclass.keys():
        finalsecondclass[key]=finalsecondclass[key]*((margin/139))
        secondfinal[key]=finalsecondclass[key]+secondfinal[key]
    for key in finalfirstclassi.keys():
        finalfirstclassi[key]=finalfirstclassi[key]*importance
        firstfinali[key]=finalfirstclassi[key]+firstfinali[key]
    for key in finalsecondclassi.keys():
        finalsecondclassi[key]=finalsecondclassi[key]*importance
        secondfinali[key]=finalsecondclassi[key]+secondfinali[key]    
    print("\n")
    print("For tree ")
    print(notree)
    print("strength is")
    print(margin/139)
    print(" and importance weight is" )
    print(importance)
    #print("accuracy is")
    #print(accurate)    
    histo1.append(margin/139)
    histo.append(np.log(importance))
    
    
    
    sortedimportance.append((importance))
    sortedimportance.sort(reverse=True)
    sortedmargin.append((margin))
    sortedmargin.sort(reverse=True)
    highestmargin2=margin
    logofhighestimportanceweight2=np.log(importance)
    if margin == sortedmargin[0]:
        highestmargin=margin
    
    if importance == sortedimportance[0]:
        highestimportanceweight=importance
        logofhighestimportanceweight=np.log(importance)    
    
    
    
    listtostoreimportanceandstrength.append(margin)
    listtostoreimportanceandstrength.append(np.log(importance))
    finallisttostoreimportanceandstrength.append(listtostoreimportanceandstrength)
    listtostoreimportanceandstrength=[]
    margin=0
    importance=1
    
    accurate=0
    error=1
    mcc1={}
    mcc2={}
    g=[]
    g1={}
    gfeature={}
    string_lengths = {}
    string_length = {}
    
indexof=0
indexofi=0
with open('Breastcancertesting.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            indexof=indexof+1
            if(row[9]) == '0.2' and (secondfinal[indexof] > firstfinal[indexof]):
                        Accurate=Accurate+1
            if(row[9]) == '0.4' and (firstfinal[indexof] > secondfinal[indexof]):
                        Accurate=Accurate+1
with open('Breastcancertesting.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            indexofi=indexofi+1
            if(row[9]) == '0.2' and (secondfinali[indexofi] > firstfinali[indexofi]):
                        Accuratei=Accuratei+1
            if(row[9]) == '0.4' and (firstfinali[indexofi] > secondfinali[indexofi]):
                        Accuratei=Accuratei+1                        

print("\n")
print("Ensemble Accuracy for strength is")
#print(Accurate)
print(Accurate/139 *100)  # 139 is the number of test data in breast cancer database
print("\n")
print("Ensemble Accuracy for importance weight is")
#print(Accurate)
print(Accuratei/139 *100)




for count in range(number_of_trees):
    sumofmargin = sumofmargin + finallisttostoreimportanceandstrength[count][0]
    sumofweight = sumofweight + finallisttostoreimportanceandstrength[count][1]
# plot between 2 attributes
for count1 in range(number_of_trees):
    finallisttostoreimportanceandstrength[count1][0] = finallisttostoreimportanceandstrength[count1][0]/highestmargin
    finallisttostoreimportanceandstrength[count1][1] = logofhighestimportanceweight/finallisttostoreimportanceandstrength[count1][1]
df = pd.DataFrame(finallisttostoreimportanceandstrength, columns = ['Strength', 'Log Importance_weight'  
                                    ] )





print("\n")
print("Histogram of strength of tree")
plt.hist(histo1, bins=20)
plt.ylabel('No of times')
plt.show()

print("\n")
print("Histogram of log of importance weight")
plt.hist(histo, bins=20)
plt.ylabel('No of times')
plt.show()                       

print("\n")
print("Comparison between strength and importance weight")           
df.plot.bar(figsize=(23,5))

plt.xlabel("Trees") 
plt.ylabel("Height") 
plt.show() 

print("End")     