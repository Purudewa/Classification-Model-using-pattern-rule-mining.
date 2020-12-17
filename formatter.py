import pickle

file=open('iptr19.txt','r+')
rules=list()
for l in file.readlines():
    rules.append(l.strip().split(' ')[:-5])
labels=[]*(len(rules)-2)
rules_mod=[list()]*(len(rules)-2)
cols=['Elevation', 'Aspect', 'Slope', 'Wilderness', 'Soil_Type','Horizontal_Distance_To_Hydrology',
       'Vertical_Distance_To_Hydrology', 'Horizontal_Distance_To_Fire_Points',]
jj=0
for r in rules[:-2]:
    temp=list()
    for t in r[1:-3]:
        if len(t)==0:
            continue
        te=t.split('=')
        temp.append(te[1])
    labels.append(int(r[-1].split('=')[1]))
    temp.append(int(r[-1].split('=')[1]))
    rules_mod[jj]=temp
    jj+=1

pickle.dump(rules_mod,open('rules19.pkl','wb'))



