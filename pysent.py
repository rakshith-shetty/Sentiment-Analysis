import pandas as pd
pos=["good","amazing","superb","best"]
neg=["bad","average","worst","boring"]
r=input("Enter your sentence: ")
words=r.split()
for i in words:

    if i.lower() in pos:
        print (1);
        
    elif i.lower() in neg:
        print (0);