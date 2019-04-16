#author k163710

# coding=utf8
import os
from nltk.tokenize import word_tokenize
import re
import json
from collections import defaultdict

file = open(r"C:\Users\SHAIKH\.spyder-py3\Assign1\list.txt", "r")
stop_words = []
for w in file:
    stop_words.extend(word_tokenize(w))   
    
    

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 


def PositionalQuery():
    query=input("Enter 2 keywords followed by a number\n")
    worda= query.casefold()
    worda = re.sub('-', ' ', worda)
    worda = re.sub('/', ' ', worda)
    worda = re.sub(r"\W", " ", worda)
        # result = re.sub(r"\d", " ", result)
        # result = re.sub(r"\s+[a-z]\s+", " ", result)
    worda = re.sub(r"\s+", " ", worda)
    worda = re.sub(r"^\s", "", worda)
    worda = re.sub(r"\s$", "", worda)
    wordf = worda.split()
    wordf=removestop(wordf)
    word1=data.get(wordf[0])
    l1=word1.keys()
    word2=data.get(wordf[1])
    l2=word2.keys()
    finallist=[]
    word1docs=[]
    word2docs=[]
    list2iterator=0
    list1iterator=0
    for nk in l1:  
     word1docs.append(nk)
   
    for n in l2:
     word2docs.append(n) 

    positionlist1=[]  
    positionlist2=[]
    k=int(wordf[2])
    k = k + 1
    i=0 
    j=0
    while (i < len(word1docs) and j < len(word2docs)):
     positionlist1.clear()
     positionlist2.clear()
     if word1docs[i]==word2docs[j]:
       templist=[]
       for x,n in word1.items():
          if x==word1docs[i]:   
           positionlist1.extend(n)
       for x,n in word2.items():
          if x==word2docs[j]:
           positionlist2.extend(n)
       list1iterator=0
       while list1iterator < len(positionlist1):
           list2iterator=0
           while list2iterator < len(positionlist2):
               if abs(positionlist1[list1iterator]-positionlist2[list2iterator]) <= k:
                   templist.append(list2iterator)
               elif positionlist2[list2iterator] > positionlist1[list1iterator]:
                   break
               list2iterator = list2iterator+1
           
           for item in templist:
                distance=abs(positionlist2[item]-positionlist1[list1iterator])
                if distance > k:
                    
                    templist.remove(item)
           for item in templist:
                 finallist.append({ "Document_ID" : word1docs[i],  "Postion 1 " : positionlist1[list1iterator]  ,  "Postion 2" : positionlist2[item] })
        
           list1iterator=list1iterator+1 
       i = i +1
       j= j + 1
       
     elif word1docs[i] < word2docs[j] :
        i = i + 1
     else:
        j= j + 1
        
    
     
            
               
               
    return finallist
               

          


def Union(lst1, lst2): 
    final_list = list(set(lst1) | set(lst2)) 
    return final_list     

operates=["and", "or","not"]

def removestop(list1):
    list2=[]
    for i in  list1:
        if not i in stop_words or i in operates:
                list2.append(i)
                
                
                         
    return list2       
                
    
        


totaldocs=['1.txt','2.txt','3.txt','4.txt','5.txt','6.txt','7.txt','8.txt','9.txt','10.txt','11.txt','12.txt','13.txt','14.txt','15.txt','16.txt','17.txt','18.txt','19.txt','20.txt','21.txt','22.txt','23.txt','24.txt','25.txt','26.txt','27.txt','28.txt','29.txt','30.txt','31.txt','32.txt','33.txt','34.txt','35.txt','36.txt','37.txt','38.txt','39.txt','40.txt','41.txt','42.txt','43.txt','44.txt','45.txt','46.txt','47.txt','48.txt','49.txt','50.txt']

def Start():

 


 query=input("Enter a  query (write 'stopp' to exit) \n ")
 while query != "stopp" :
  worda= query.casefold()
  worda = re.sub('-', ' ', worda)
  worda = re.sub(r"\W", " ", worda)
        # result = re.sub(r"\d", " ", result)
        # result = re.sub(r"\s+[a-z]\s+", " ", result)
  worda = re.sub(r"\s+", " ", worda)
  worda = re.sub(r"^\s", "", worda)
  worda = re.sub(r"\s$", "", worda)
  wordf = worda.split()
  wordf=removestop(wordf)




  for i in wordf:  
     if i == "and":
         
        if len(wordf)==5:
            stopa=wordf.index(i)
            l1=wordf[stopa-1]
            l2=wordf[stopa+1]
            l3=wordf[stopa+3]
            seof=wordf[stopa+2]
            
            if l1 not in data or l2 not in data or l3 not in data:
                print("One of the query terms  not in Dictionary")
                break
            
            if seof=="and":
              la1=data.get(l1)
              list1=(la1.keys())
              la2=data.get(l2)
              list2=(la2.keys())
              la3=data.get(l3)
              list3=(la3.keys())
              loq1=(intersection(list1,list2))
              loq2=(intersection(loq1,list3))
              #loq2=((intersection(loq1,list3))
              print (loq2)
              print (len(loq2) , " documents retreievd" )
              break
              
              
            if seof=="or":
              la1=data.get(l1)
              list1=(la1.keys())
              la2=data.get(l2)
              list2=(la2.keys())
              la3=data.get(l3)
              list3=(la3.keys())
              loq1=(intersection(list1,list2))
              loq2=(Union(loq1,list3))
              #loq2=((intersection(loq1,list3))
              print (loq2)
              print (len(loq2) , " documents retreievd" )  
              break
              
            
        
         
        else: 
         stopa=wordf.index(i)
         l1=wordf[stopa-1]
         l2=wordf[stopa+1]
       
         if l2 == "not":
           l3=wordf[stopa+2]
           if l1 not in data or l3 not in data:
                print("One of the query terms  not in Dictionary")
                break
           
           lava=data.get(l1)
           lavaq=data.get(l3)
           list1=(lava.keys())
           tlist=list(set(totaldocs) - set(list1))
           list2=(lavaq.keys())
           print((intersection(tlist,list2)))            
           print(len(intersection(tlist,list2)) , " documents retreievd" ) 
           break
            
           
         else:  
          if l1 not in data or l2 not in data:
                print("One of the query terms  not in Dictionary")
                break
          else:       
           lava=data.get(l1)
           lavaq=data.get(l2)
           list1=(lava.keys())
           list2=(lavaq.keys())      
           print((intersection(list1,list2)))            
           print(len(intersection(list1,list2)) , " documents retreievd" ) 
           break
     if i == "or":
        
        if len(wordf)==5:
            stopa=wordf.index(i)
            l1=wordf[stopa-1]
            l2=wordf[stopa+1]
            l3=wordf[stopa+3]
            seof=wordf[stopa+2]
            
            if l1 not in data or l2 not in data or l3 not in data:
                print("One of the query terms  not in Dictionary")
                break
            
            if seof=="and":
              la1=data.get(l1)
              list1=(la1.keys())
              la2=data.get(l2)
              list2=(la2.keys())
              la3=data.get(l3)
              list3=(la3.keys())
              loq1=(Union(list1,list2))
              loq2=(intersection(loq1,list3))
              #loq2=((intersection(loq1,list3))
              print (loq2)
              print (len(loq2) , " documents retreievd" )
              break
              
              
            if seof=="or":
              la1=data.get(l1)
              list1=(la1.keys())
              la2=data.get(l2)
              list2=(la2.keys())
              la3=data.get(l3)
              list3=(la3.keys())
              loq1=(Union(list1,list2))
              loq2=(Union(loq1,list3))
              #loq2=((intersection(loq1,list3))
              print (loq2)
              print (len(loq2) , " documents retreievd" )  
              break 
         
        else:  
         
         stopa=wordf.index(i)
         l1=wordf[stopa-1]
         l2=wordf[stopa+1]
         if l2 == "not":
           l3=wordf[stopa+2]
           if l1 not in data or l3 not in data:
                print("One of the query terms  not in Dictionary")
                break
           
           lava=data.get(l1)
           lavaq=data.get(l3)
           list1=(lava.keys())
           tlist=list(set(totaldocs) - set(list1))
           list2=(lavaq.keys())
           print((Union(tlist,list2)))            
           print(len(Union(tlist,list2)) , " documents retreievd" ) 
           break
         if l1 not in data or l2 not in data:
                print("One of the query terms  not in Dictionary")
                break
         lava=data.get(l1)
         lavaq=data.get(l2)
         list1=(lava.keys())
         list2=(lavaq.keys())      
         print((Union(list1,list2)))            
         print(len(Union(list1,list2)) , " documents retreievd" ) 
         break
   
     if i =="not":
       if len(wordf) <  3 :
            stopa=wordf.index(i)
            l1=wordf[stopa+1]
            if l1 not in data:
                print("Word Not In Dictionary")
                break
            lava=data.get(l1)
            list1=(lava.keys())
            tlist=list(set(totaldocs) - set(list1))
            print(tlist)
            print(len((tlist)) , " documents retreievd" )
            break
        
       elif len(wordf) == 5 :
            stopa=wordf.index(i)
            l1=wordf[stopa+1]
            l2=wordf[stopa+4]
            l3=wordf[stopa+2]
            if l1 not in data or l2 not in data:
                print("One or more words not in Dictionary")
                break
            if l3=="and":
             lava=data.get(l1)
             list1=(lava.keys())
             tlist=list(set(totaldocs) - set(list1))
             lavaq=data.get(l2)
             list2=(lavaq.keys())
             tlist2=list(set(totaldocs) - set(list2))
             print(intersection(tlist,tlist2))
             print(len(intersection(tlist,tlist2)) , " documents retreievd" )
             break
            if l3=="or":
             lava=data.get(l1)
             list1=(lava.keys())
             tlist=list(set(totaldocs) - set(list1))
             lavaq=data.get(l2)
             list2=(lavaq.keys())
             tlist2=list(set(totaldocs) - set(list2))
             print(Union(tlist,tlist2))
             print(len(Union(tlist,tlist2)) , " documents retreievd" )
             break
           
        
           
       else:    
        stopa=wordf.index(i)
        l1=wordf[stopa+1]
        l2=wordf[stopa+2]
        l3=wordf[stopa+3]
     
        
        if l1 not in data or l3 not in data:
                print("One of the query terms  not in Dictionary")
                break
       
        if l2=="and":
         lava=data.get(l1)    
         lavaq=data.get(l3)
         list1=(lava.keys())
         tlist=list(set(totaldocs) - set(list1))
         list2=(lavaq.keys())      
         print((intersection(tlist,list2)))            
         print(len(intersection(tlist,list2)) , " documents retreievd" ) 
         break
        if l2=="or":
         lava=data.get(l1)
         lavaq=data.get(l3)
         list1=(lava.keys())
         tlist=list(set(totaldocs) - set(list1))
         list2=(lavaq.keys())      
         print((Union(tlist,list2)))            
         print(len(Union(tlist,list2)) , " documents retreievd" ) 
         break
        if l2=="not":
         lava=data.get(l1)
         lavaq=data.get(l3)
         list1=(lava.keys())
         tlist=list(set(totaldocs) - set(list1))
         list2=(lavaq.keys())
         tlist2=list(set(totaldocs) - set(list2))
         print((intersection(tlist,tlist2)))            
         print(len(intersection(tlist,tlist2)) , " documents retreievd" ) 
         break
     
  else:    
    for tocheck in wordf:
       if tocheck not in operates:
            lavaq=data.get(tocheck)
            list1=(set(lavaq.keys()))
            print(list1)
            print(len((list1)) , " documents retreievd" )
            break
       if tocheck not in data:
                print("Word Not In Dictionary")
                exit
            
           
       
      
  query=input("Enter a  query (write 'stopp' to exit) \n")


 
if os.path.isfile(r"C:\Users\SHAIKH\.spyder-py3\Assign1\SavedDictionary.json") :
  a1=input("Press 1 to enter query or Press 2 to print dictionary (with positional index) or 3 for positional query or 4 to exit\n\n")
  data = json.load(open(r"C:\Users\SHAIKH\.spyder-py3\Assign1\SavedDictionary.json"))
  while a1 != "4":
      if a1 =="1":
       Start()
      elif a1== "2":
       for wordname, docid in sorted(data.items()):
         for key in sorted(docid):
          print(wordname ,"--> ", key + ':', docid[key])

       print("Unique Words : ", len(data))
      elif a1=="3":
       finallist={}
       finallist=PositionalQuery()
       print(finallist)
       print(len(finallist), " Documents Retreived\n")
      
      elif a1=="4":
       exit
       
      a1=input("Press 1 to enter query or Press 2 to print dictionary (with positional index) or 3 for positional query or 4 to exit\n\n")  
      
        
   
  
else:  

 dictionary =defaultdict(lambda: defaultdict(list))

 file = open(r"C:\Users\SHAIKH\.spyder-py3\Assign1\list.txt", "r")
 directory = r"C:\Users\SHAIKH\.spyder-py3\Assign1\Stories"
 stop_words = []
 for w in file:
    stop_words.extend(word_tokenize(w))

# print(stop_words)

 for filename in sorted((os.listdir(directory))):
    f = os.fsdecode(filename)
    if f.endswith(".txt"):
        story = open(r'C:\Users\SHAIKH\.spyder-py3\Assign1\Stories\\' + filename)
        word = story.read();
        m = word.casefold()
        worda = re.sub('-', ' ', m)
        worda = re.sub(r"\W", " ", worda)
        # result = re.sub(r"\d", " ", result)
        # result = re.sub(r"\s+[a-z]\s+", " ", result)
        worda = re.sub(r"\s+", " ", worda)
        worda = re.sub(r"^\s", "", worda)
        worda = re.sub(r"\s$", "", worda)
        wordf = worda.split()
        wordf=removestop(wordf)
        for eachword in sorted(wordf):
                   dictionary[eachword][filename]=[]
                   for i, j in enumerate(wordf):
                       if j == eachword: 
                         dictionary[eachword][filename].append(i+1)
                 
                     
            

        

 json.dump(dictionary, open(r"C:\Users\SHAIKH\.spyder-py3\Assign1\SavedDictionary.json", 'w'))
 Start() 





       


  
 


           
            
            

