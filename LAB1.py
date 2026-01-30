def LAB1():

    bai1()

    bai2()

    bai3()


#bài 1
def bai1():
 #float:số thực
 a= float(input("điểm môn Toán: " ))
 b= float(input("điểm môn Văn: " ))
 print("điểm trung bình: ", (a+b)/2)
 print("*******************************************")
#bài 2
def bai2():
 #ty_gia: tỷ giá USD/VND
 ty_gia= 26000
 tien_usd= int(input("nhập số tiền USD cần đổi: " ))
 tien_vnd= tien_usd * ty_gia
 print("số tiền VND sau quy đổi: ", tien_vnd)  
 print("*******************************************")
#bài 3
def bai3():
 can_nang= float(input("cân nặng của bạn là (kg): " ))
 chieu_cao= float(input("chiều cao của bạn là (m): " ))
 BMI= can_nang / (chieu_cao ** 2)
 print("chỉ số BMI của bạn là :",BMI)
