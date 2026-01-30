#bài 1
import math
n = float(input("Nhập số n: "))
#số chẵn hay lẻ
if n%2==0:
    print(n,"là số chẵn")   
else:
    print(n,"là số lẻ")
#số nguyên
if n==int(n):
    print(n,"là số nguyên")
else:
    print(n,"không phải số nguyên")
#số chính phương
if math.sqrt (n)==int(math.sqrt(n)):
    print(n,"là số chính phương")   
else:
    print(n,"không phải số chính phương")    
#số hoàn hảo 
if n>0:
    sum=0
    for i in range(1,int(n)):
        if n%i==0:
            sum=sum+i
    if sum==n:
        print(n,"là số hoàn hảo")   
    else:
        print(n,"không phải số hoàn hảo")
#bài 2
#hai số
a=int(input("nhập số a: "))
b=int(input("nhập số b: "))
def tinh_tong(a,b):
    print(a+b)
def tinh_hieu(a,b):
    print(a-b)
def tinh_tich(a,b):
    print(a*b)
def tinh_thuong(a,b):
    if b!=0:
        print(a/b)
   
        
tinh_tong(a,b)
tinh_hieu(a,b)
tinh_tich(a,b)  
tinh_thuong(a,b)
#ba số
a=int(input("nhập số a: "))
b=int(input("nhập số b: "))
c=int(input("nhập số c: "))
def tinh_tong(a,b,c):
    print(a+b+c)
def tinh_hieu(a,b,c):
    print(a-b-c)
def tinh_tich(a,b,c):
    print(a*b*c)
def tinh_thuong(a,b,c):
    if c!=0:
        print(a/b/c)
    
tinh_tong(a,b,c)
tinh_hieu(a,b,c)
tinh_tich(a,b,c)  
tinh_thuong(a,b,c)