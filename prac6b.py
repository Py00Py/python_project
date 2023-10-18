dict={}
n=int(input("enter no of entries"))
for i in range(n):
    roll=int(input("enter roll no. ="))
    grade=input("enter grade (A,B,C,D,E,F)")
    dict[roll]=grade
for i in dict:
    print(i , dict[i])