#########################Ex 1################################
def frequency(l):
    dct = {}
    for item in l:
        if item in dct:
            dct[item] += 1
        else:
            dct[item] = 1
    return dct
#print(frequency(['abc','def','abc','pdq','abc']))

def histogram(l):
    dct = frequency(l)
    for key in dct:
        print(key + ' ' + '*'*dct[key])
        
#histogram(['abc','def','abc','pdq','abc'])
###########################################################

#########################Ex 2a##############################
def even(num):
    return num % 2   
   
def pos(l2,func):
    result = []
    for i in range(len(l2)):
        if func(i) == 0:
            result.append(l2[i])
    return result         
#print(pos([1,2,3,4,5,6],even))   
###########################################################

#########################Ex 2b##############################
def evenFilter(data):
    result = []
    for i in data:
        if i % 2 == 0:
            result.append(data[i])
    return result
data = {1:"one",2:"two",5:"five",6:"six"}
#print(evenFilter(data))
###########################################################

#########################Ex 2c##############################
def diff(l1,l2):
    result = []
    for i in l1:
        if i not in l2:
            result.append(i)
#    return result
###########################################################

#########################Ex 2d##############################        
def union(l1,l2):
    a = l1 if len(l1) > len(l2) else l2
    b = l2 if len(l1) > len(l2) else l1
    return diff(a,b) + b
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [2,4,6,8,10]
#print(union(l1,l2))
###########################################################

#########################Ex 3a##############################
import pickle
def load_data(file):
    dct = {}
    f = open(file,'rb')
    dct = pickle.load(f)
    return dct

def query(prof_name):
    dct = load_data('dept-prof.pydata')
    result = []
    for department in dct:
        if prof_name in dct[department]:
           result.append(department) 
    return result

def update():
    dct = load_data('dept-prof.pydata')
    del dct['Artificial Intelligence']
    dct['Space Engineering'] = ['Musk','Andy','Jane']
    f = open('dept-prof-updated.pydata','wb')
    pickle.dump(dct,f)
    
def get_depts_size():
    dct = load_data('dept-prof-updated.pydata')
    result = {}
    for de in dct:
        result[de] = len(dct[de])
    return result
###########################################################
