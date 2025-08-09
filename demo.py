a=10
print(a)

a_1=20
print(a_1)

a='hello'
b="hi"
c='''python'''
d=10.4
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#type casting
a=10
b='20'
c=int(b)
print(a+c)

#string operation
s1="hello world"
s2="hello"
s3="world"
result=s1+" "+s2
print(result)

s="python"
print(s[0])
print(s[4])
print(s[-3])
print(s[1:4])
str1="hello world"
print(str1.lower())
print(str1.upper())
print(str1.capitalize())
print(str1.title())

a=10
b=20
print(a+b)
print(a*b)
print(a-b)
print(a/b)
print(a%b)
print(a//b)

#list
list1=[1,2,3,4,5]
print(list1)
#index
fruits=["apple","banana","cherry"]
print(fruits[0][1])
print(fruits[1][4])
print(fruits[2][4])
list2=[2,4,6]
list2.append([8,10])
print(list2)

list3=[1,2,3,[4,5],6,8,[7,8,9],"apple"]
print(list3[6][2])
print(list3[7][4])
list3=[10,20,30]
list3.extend([40,50])
print(list3)
print(list3[3])

list4=[1,2,3]
list4.insert(1,4)
print(list4)
list5=[1,2,3,4,5]
list5.remove(3)
print(list5)
list7=[1,2,3,4,5]
print(list7.pop())
list8=[1,2,3,4,5]
print(list8[1:3])

#tuple
tup1=(1,2,3,4,5)
print(tup1)
print(tup1[0])
print(tup1[1:3])

tup2=(45,50,65,85,90,25)
print(tup2[1:4])

#set
my_set={10,20,30,20}
print(my_set)

#dict
dict1={"name":"alice","age":25,"marks":88}
print(dict1)
print(dict1["name"])
print(dict1["age"])
dict1["age"]=24
dict1["contact no"]=3365424552
print(dict1)

#conditional statement
age=15
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

marks=82
if marks>=90:
    print("garde A")
elif marks>=75:
    print("garde B")
elif marks>=60:
    print("garde c")
else:
    print("garde D")

#loops
for i in range(1,6):
    print(i)

name="python"
for ch in name:
    print(ch)

#while loop
i=1
while i<=5:
    print("count is",i)
    i+=1

for n in range(10):
    if (n==5):
        break
    print(n)

for i in range(0,10):
    if (i==5):
        print('five')
        continue
    if(i==9):
        print('nine')
        continue
    print(i)

n=5
if(n>=0):
    print("number is +ve")
else:
    print("number is -ve")


n=2
if (n%2==0):
    print("even")
else:
    print("odd")


for i in range(2,21,2):
    print(i)


for i in range(1,6):
    print(f'square of {i}={i**2}')


n=5
if n%3==0:
    print("divide by 3")
elif n%5==0:
    print("divide by 5")
else:
    print('enter valid no')

#function
def add(a,b):
    return a+b
result=add(5,3)
print("sum is",result)   



def check_even(number):
    if number%2==0:
        return "even"
    else:
        return "odd"
print(check_even(4))

#lambda function
square= lambda x:x*x
print(square(5))

add= lambda a,b:a+b
print(add(5,5))

max_of_two=lambda a,b:a if a>b else b
print("maximum is",max_of_two(10,20))

even_or_odd=lambda a:"even"if a%2==0 else "odd"
print("no is",even_or_odd(10))



def greater_or_not(a,b):
    if a>b:
        return "a is greater"
    else:
        return "b is greater"
print(greater_or_not(4,5))


greater_or_not=lambda a,b:"a greater" if a>b else "b greater"
print("value is",greater_or_not(60,50))










