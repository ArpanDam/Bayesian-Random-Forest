# -*- coding: utf-8 -*-
"""
Created on May 16 2020

@author: Arpan Dam
"""


# importing csv module 
import csv
import math 




import numpy as np


from binarytree import Node


importance =1
mclass1=0
error=1
finalerrorforregression=0

mclass2=0
counttest=0
keyerror=0
countkey=0
totalrow=0
totalstrengthofforest=0
Accurate=0
testingnumber=0
testkey=0
finalaverage={}
histo=[]
finalerror={}
histo1=[]
mcc1={}
mcc2={}
finalsecondclass={}
finalfirstclass={}
firstfinal={}
secondfinal={}
predicted={}
finalprediction={}
for i1 in range(677):
    predicted[i1+1]=0
    finalprediction[i1+1]=0

index=0
totalclass=0
weighted_error=0
average={}
keyvalue=[]
accurate=0
storefirstclass=[]
testingregression=[]
storesecondclass=[]
storefirstclassprobabilityforimportance=[]
storesecondclassprobabilityforimportance=[]
keytostoreentry={}
sortedentry={}
probabilityofsecondclass={}
probabilityoffirstclass={}
probabilityoffirstclasssorted={}
probabilityofsecondclasssorted={}
















def train_split(mcctrain1={},mcctrain2={},m={},m1={}):
    m1trainreverse={}
    global totalrow
    global testingregression
    global index
    global average
    global finalaverage
    global accurate
    #global margin
    for key1 in sorted(m1.keys()):
        m1trainreverse[key1] = m1[key1]
    mtrainreverse={}
    for key2 in sorted(m.keys()):
        mtrainreverse[key2] = m[key2] 
    op=list(mtrainreverse.keys())
    jk=0
   
    with open('regression_wine_quality_testing.csv', encoding='utf-8-sig') as csvfile:
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
    
                countaverage=0
                sum=0
                for key1 in average[key]:
                    countaverage=countaverage+1
               
                for i in range(countaverage):
                    sum=float(sum)+float(average[key][i])
                ave=float(sum/countaverage)    
                
                for row2 in readCSV:
                    index1=0                    
                    with open('regression_wine_quality_testing.csv', encoding='utf-8-sig') as csvfile:
                        readCSV1 = csv.reader(csvfile, delimiter=',')
                        for row1 in readCSV1:
                            index1=index1+1
                            if row1 == row2:
                                finalaverage[index1]=ave
                                break
                               
              
                    
                    
                         
                

















    
def test_split(m={},m1={}):
    
    global countkey
    global keyerror
    global totalclass
    global counttest
    global keyvalue
    global average
    global testingregression
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
       
        
    keyvalue=[]
    op=list(mreverse.keys())
  
    with open('regression_wine_quality_train.csv', encoding='utf-8-sig') as csvfile:
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
                                    
                            if m23 == 2:
                                if float((row[m1reverse[key]])) > mreverse[key]:
                                    right.append(row)
                            #readCSV=right
                                    jk=2
                                    
                if jk==1:
                    readCSV=left
                if jk==2:
                    readCSV=right
                testingregression=readCSV    
            if jk==0 and (key == op[len(mreverse)-1]) :
                
                keyerror=0
               
                if bool(mcc1) is False :
                    mcc1[key]=0
                if bool(mcc2) is False :
                    mcc2[key]=0
               
                mcc1[key]=0
                mcc2[key]=0
                average[key]=[0,0]
                #importanceweight(0,0,key)
                        
            if jk!=0 and (key == op[len(mreverse)-1]):
               
                global mclass1
                global mclass2
                for readCSVlength in testingregression:
                    keyvalue.append(readCSVlength[11])
                     
                      
                    jk=0
                
                average[key]=keyvalue
                keyerror=2
                if len(average[key])==0:
                    average[key]=[0,0]
               
                        
                        
            
                            


matrix1 = [] 
g=[]  



matrix2 = [] 

       
g=[]
test=[]
strength={}
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
            
            if node.left.value == y:
                
                return 1
            else:
                
                return 2
        else:
            
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
    #print(i)
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
with open('regression_wine_quality_train.csv', encoding='utf-8-sig') as csvfile:
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
    
    root1=root
   
    print_leaf_to_root_paths(root , [])
    g=[]
    
    test=[]
    testfeature=[]
    
   
    
    importance=1
    strengthoftreee1=0
    accurate=0
    
    average={}
    rownumber=1
    strengthoftreee=0
   
    with open('regression_wine_quality_testing.csv',encoding='utf-8-sig') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            predicted[rownumber]=finalaverage[rownumber]
            margin=float(abs(float(row[11])-finalaverage[rownumber]))
            margin1=margin*9
            resedual=margin
                        
            resedual=resedual*resedual
            resedual1=margin1
                        
            resedual1=resedual1*resedual1
            
            rownumber=rownumber+1
            conf=float(1/float(math.exp(margin)))
            strengthoftreee=strengthoftreee+conf
            conf1=float(1/float(math.exp(margin1)))
            strengthoftreee1=strengthoftreee1+conf1
    strengthoftreee=strengthoftreee/(677)
    strengthoftreee1=strengthoftreee1/(677)        
    #strength[notree]=strengthoftreee
   # error=error/60
    rownumberr=1
    with open('regression_wine_quality_testing.csv',encoding='utf-8-sig') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            predicted[rownumberr]=predicted[rownumberr] * strengthoftreee
            rownumberr=rownumberr+1
    rownumber_prediction=1
    with open('regression_wine_quality_testing.csv',encoding='utf-8-sig') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            finalprediction[rownumber_prediction]=finalprediction[rownumber_prediction] + predicted[rownumber_prediction]
            rownumber_prediction = rownumber_prediction +1
    print("\n")
    print("For tree")
    print(notree)
    print("Strength is")
    print(strengthoftreee1)
   
    totalstrengthofforest=totalstrengthofforest+strengthoftreee1
    finalerror[notree]=error
  
    finalaverage={}
    mcc1={}
    mcc2={}
    g=[]
    g1={}
    gfeature={}
    string_lengths = {}
    string_length = {}
   
indexof=1
error=0
with open('regression_wine_quality_testing.csv',encoding='utf-8-sig') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            finalprediction[indexof]=finalprediction[indexof]/number_of_trees
            margin=float(abs(float(row[11])*9)-(finalprediction[indexof] *9))
            resedual=margin
            resedual=resedual*resedual
            error=error+resedual
            indexof=indexof+1
final_error=error/677
totalstrengthofforest=totalstrengthofforest/number_of_trees
print("\n")
print("Total strength of the forest is")
print(totalstrengthofforest)
print("\n")
print("FInal ensemble  mean square error is")
print(final_error)
print("END")