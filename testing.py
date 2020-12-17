import numpy as np 
import pandas as pd 
import pickle
import rule
import testing


def runner_(path):

 rule.rules_preprocessing()
  
 testing.rules_balancing()  
  
 rules = pickle.load(open('rules.pkl','rb'))

 label = list()
 fr = pd.DataFrame(pd.read_csv(path))
 idd = fr['id']
 del fr['id']
 fr = np.array(fr)
 c = 1

 for x in fr:
    flag = False
    for i in range(len(rules)):
       count = 0
       for j in range(len(rules[i])-1):
           if rules[i][j] in x:
               count = count + 1
       if count == len(rules[i])-1:
           c = c + 1
           l = int(rules[i][len(rules[i])-1])
           label.append(l)
           flag = True
           break 
    if flag == False:
           label.append(4) 

 fr = pd.DataFrame(columns=['id','Label'])
 fr['id'] = idd
 fr['Label'] = label
 fr.to_csv('result.csv', index=False)

runner('~/Desktop/test.csv')
