#cấu trúc vòng lặp 
#key range ( tham số)
#1 tham số
print(range(3)) #0,1,2
#range(3) là range(0,3) từu 0 dến 3 không bao gồm 3
# bắt đầu lặp
x=1
for i in range(3):
 #block -- khỏi lệnh
    print("lặp lần thứ ", x)
    print(i)
    x=x+1
#for (i =1; i<10 điều kiện thoát ,i++)    
#kêt thúc lặp
# lưu ý khi sử dụng vòng lặp tránh việc lặp vô hạn    
#lặp 7 lần từ 3
x=0
for i in range(3,9):
    print("lần lặp số ", x,"và i =",i)
    x=x+1
listp=[3,4,3,2,4,5,3]
sum=0
for i in listp:
   #sum=0
    sum=sum+i
print("tổng các phần tử trong listp =",sum)    

#biểu thức điều kiện
print(5>2) #True
#if đúng thì in 
if 5>2:
    print("chuẩn")
else:
    print("xem lại")    
#cách 2
print("khởi tạo a")
a=8
if a>2:
     print("chuẩn")
print("kết thúc")    

#rẽ nhiều nhánh hơn
numberA=1
if numberA==1:
    print("thứ hai")
elif numberA==2:
    print("thứ ba")
elif numberA==3:
    print("thứ tư")
else:
    print("chủ nhật")    
# trường hợp đặc biệt hay bị nhầm lẫn
#kiểm tra x có chia hết cho 2 và 5 hay không
x=100
if x%2==0:
#cú pháp 1    
    print ("chia hết cho 2 ")
#cú pháp 2    
if x%5==0:
    print("chia hết cho 5") 
else:
    print("không chia hết cho 5 và 2")   


##########
x=24
if x%10==0:
    print("chia hết cho 2 và 5")
else:
    print("không chia hết cho 2 và 5")  
if x%2==0:
    if x%5==0:
        print("ok")  
    else:
        print("chia hết cho 2 không chia hết cho 5")       
else:
    print("không")   

#tính tổng các số từ 1 đến 10
sum=0

for i in range(1,10):
    sum=sum+i
    print(i,",",sum)
print(sum) #trả về 66
#function-- hàm:cấu trúc block mà được đánh tên và sử dụng khi được gọi ra
#def ten_ham(tham số truyền vào nếu có):
#block --khối câu lệnh

#tinh tong
    def tong_hai_so(a,b):
        sum=a+b
        print("tổng hai số",a,b)
        print(a+b)
    tong_hai_so(3,4)
    tong_hai_so(10,20)