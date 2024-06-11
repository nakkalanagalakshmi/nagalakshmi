import pandas as pd
s=[]
def data(name,roll,marks,total):
    student={
        'name':name,
        'rollnumber':roll,
        'marks':marks,
        'total':total
    }
    s.append(student)
n=int(input())    
for i in range(n):
    name=input("enter student name:")
    roll=int(input("enter roll number:"))
    marks=list(map(int,input("enter marks:").split()))
    total=sum(marks)
    data(name,roll,marks,total)    
df=pd.DataFrame(s)
print(df)
b=[]    
for j in range(n):
    a=s[j]['total']
    b.append(a)
print('max total=:',max(b))
print('min total=:',min(b))
b.sort()
print('sort total=:',b)
print(set(b))
c=[]
for k in range(n):
    d=s[k]['marks']
    c.append(d)
for p in range(n):
    print(f'maximum score of student{p+1}:',max(c[p]))
    print(f'minimum score of student{p+1}:',min(c[p]))
    print(f'total score of student{p+1}:',sum(c[p]))
    print(f'average score of student{p+1}:',sum(c[p])/len(c[p]))
    c[p].sort()
    print(f'sort of all marks {p+1}:',c[p])
    print(f'score of each subject without duplicates:',set(c[p]))
m=[]
for j in range(len(marks)):
    for i in range(n):
        m.append(s[i]['marks'][j])
    print(f'maximum marks in subject {j+1}:',max(m))
    m.clear()


    

