"""
# ##################################################################################################################
#חוברת פיתון עמוד 38 שאלה 3.2
word=input("insert street, house number and city")
word=word.split()
word2=""
num=0
for i in range(len(word)):
    if not word[i].isnumeric():
      word2=word2+" "+word[i]
    if word[i].isnumeric():
        print(f"you live in :{word2} street")
        num=int(word[i])
        print(f"you house number is: {num}")
        num=i
        word2=""
        for x in range(num+1,len(word)):
          word2=word2+" "+word[x]
        print(f"you live in city:{word2}")
"""


"""
#חוברת פיתון עמוד 38 שאלה 3.2
word=input("insert street, house number and city")
count=0
string=""
# word=word.split()
for i in word:
    if i.isnumeric():
        print(word[0:word.index(i)])
        word=word[word.index(i):]
        break
for i in word:
    if i.isnumeric():
        string+=str(i)
        count+=1
print(string)
word=word[count:]
print(word)
"""

"""
##################
#תרגילים מחרוזות פיתון תרגיל 3
word1=input("insert sentence")
word2=input("insert sentence")
count=0
newsen=""
for i in word1:
    for x in word2:
        if x==i:
            if i not in newsen:
             newsen+=x+" "
             count+=1
print(f"the leters are {newsen} \n there are {count} same chars")

"""


"""
#תרגילים מחרוזות פיתון תרגיל 2
import random

word1=input("insert ID")
while len(word1)>7:
    word1 = input("insert ID")
# word1=word1.split()
password=""
for i in range(6):
    x=random.randrange(0,5)
    password+=word1[x]
print(password)
"""


"""
# פעולה ששמה במילה חדשה את האותיות הקטנות לפני האותיות הגדולות
word1=input("insert input")
newword=""
for i in word1:
    if 97<ord(i)<122:
        newword+=i
for i in word1:
    if 65<ord(i)<90:
        newword+=i

print(newword)
"""




#w= 'arhateh aehaerhea'
# print(w)
# w=list(w)
# print(w)
# stri=""
# w=w[9:14]
# for i in range(len(w)):
#     stri+=str(w[i])
# print(stri)



"""
#תרגילי רשימה 5.1 במצגת
max=0
sum=0
lowest=100
l=[]
x=input("insert grade")
while x != "":
    if not x.isnumeric():
        x = input("insert fine value")
    if x.isnumeric():
        l.append(x)
        x = input("insert grade")
for i in range(len(l)):
    sum+=int(l[i])
    if max<int(l[i]):
        max=int(l[i])
    if int(l[i])<lowest:
        lowest=int(l[i])
avg=sum/len(l)
print(f" the lowest grade is {lowest}\n the highest grade is {max}\n the avarage is {avg}")
"""
"""
#תרגילי רשימה 5.6 במצגת
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)
list2=list1[-3:]
print(list2)
list3=list1[::-1]
print(list3)
list4=list1[1::2]
print(list4)
list5=[]
for i in list1:
    if i%2!=0:
        list5.append(i)
print(list5)
list6=list1.copy()
x=int(input("insert num"))
y=int(input("insert num"))
z=int(input("insert num"))
list6[4:6]=[x,y]
list6.append(z)
print(list6)
list7=[]
for i in range(10):
    list7.append(int(list1[i])*2)
print(list7)
list8=[list1[0],list1[-1]]
print(list8)
"""

"""
#אנגלית רשימות שאלה 14
number=int(input("insert number"))
list=[]
for i in range(1,number):
    if number%i==0:
        list.append(i)
print(list)
"""

# פעולה שאמורה לבדוק איזה ספרות זהות יש בין 2 מספרים בלי כפילויות
# counter=0
# number=input("insert number")
# list1=[]
# while number!="":
#     if number.isnumeric():
#         list1.append(number)
#     number=input("insert number")
# for i in list1:
#     for x in list1:
#         if (int(list1[i])==int(list1[x])) and (counter==0):
#             counter=1
#         if (int(list1[i])==int(list1[x])) and (counter==1):
#             list1.remove(x)
# print(list1)
#



# import random
# list1=[random.randrange(1,100) for i in range(10)]
# t=()
# for i in list1:
#     t+=(i,)
# print(t)
# num=int(input("insert number"))
# t+=(num,)
# t2=t[0:4]+t[-4:]
# t3=t2[1:]
# print(t)
# print(t2)
# print(t3)

# t5=()
# for i in range(5):
#     t5+=(i,)
# str1=""
# for i in t5:
#     str1+=str(i)
# print(str1)


"""
#תרגילי מילון 7.2 וגם 7.3
d = {}
list1 = []
x = input("insert key")
y = input("insert value")
while x != "" and y != "":
    d1 = {x: y}
    d.update(d1)
    list1 = list(d.keys())
    x = input("insert key")
    y = input("insert value")
    if x == "" and y == "":
        break
    if x in list1:
        x = input("the key is already exist. insert different key")

print(d)

d3 = {}
listkeys = list(d.keys())
listvalue = list(d.values())
for i in range(len(listkeys)):
    d4 = {listvalue[i]: listkeys[i]}
    d3.update(d4)
print(d3)
"""
"""
#תרגילי מילון 7.4
d = {}
num = int(input("insert number"))
for i in range(1, num+1):
    d1 = {i: i*i}
    d.update(d1)
print(d)
"""

"""
#איש תלוי צריך לשנות את המילון לטיפוס נתונים אחר למשל רשימה
import  random
d={}
d1={}
x=input("insert words")
while x!="":
    len1=len(d)
    d1={len1+1:x}
    d.update(d1)
    x = input("insert words")
k=""
number=random.randint(1,len(d))
for i in d[number]:
    if i!=" ":
        k+="_"
    else:
        k+=" "
print(" the chosen value is:"+k)

anothevalue=""
fuckinganothervalue=""
where=0
counter=1
guess=input("guess char in the word above")
while guess!="" and 0<=counter<8:
    if len(guess)!=1:
        guess = input("guess char in the word above")
    else:
             if guess in d[number]:
                 # where=str(d[number]).find(guess)
                anothevalue=list(d[number])
                k=list(k)
                for i in range(len(anothevalue)):
                    if guess==anothevalue[i]:
                      k[i]=guess
                for i in k:
                    fuckinganothervalue+=i
                k=fuckinganothervalue
             else:
                 counter += 1
                 print("wrong answer")
             fuckinganothervalue=""
             if "_" not in k:
                 print("congratulations!!!! \n the word is", k)
                 del d[number]
                 break

             print(k)
             guess = input("guess char in the word above")
else:
    print("you fail! rerun the program to play again")
"""


"""
def does_it_filandrom (sentenc):
    'the fuction check if the sentense is filondrom'
    s1=sentenc
    s2=sentenc[::-1]
    if s1==s2:
        return 1
    else:
        return -1

def even_sum(list_1):
    'the function do sum of the even numbers'
    sum=0
    for i in range(0,len(list_1)-1,2):
        sum+=list_1[i]
    return  sum

def does_it_rishoni (number):
    'the function check if the number is prime'
    counter=0
    for i in range(1,number+1,1):
         if number/i==number//i:
              counter+=1
    if counter<=2:
        return  1
    else:
        return -1

def without_doubel_int(list_1):
    set1=set(list_1)
    return  set1


def upper_lower (sentencs):
    x=list(sentencs)
    upper=0
    lower=0
    for i in range(len(x)):
        if ascii('a')<=ascii(x[i])<=ascii('z'):
            lower+=1
        if ascii('A')<=ascii(x[i])<=ascii('Z'):
            upper+=1
    return {'upper':upper,'lower':lower}

"""



















































