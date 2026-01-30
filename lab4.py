#bài 1
n=int(input("nhập số nguyên:"))
giai_thua = 1
for i in range(1,n+1):
    giai_thua*=i
print(f"{n}={giai_thua}")    
# bài 2
while True:
    print("\n====menu====")
    print("1.tổng hai số")
    print("2.hiệu hai số")
    print("0.thoát chương trình")
    go=input("nhập lựa chọn :")
    if go == "1":
        a=float(input("nhập số thứ nhất:"))
        b=float(input("nhập số thứ hai:"))
        tong=a+b
        print("tổng hai số ",tong)
    elif go == "2":
        a=float(input("nhập số thứ nhất:"))
        b=float(input("nhập số thứ hai:"))
        hieu=a-b
        print("hiệu hai số ",hieu)
    elif go == "0":
        print("thoát chương trình")
        break
    else:
        print("quay lại từ đầu")

# bài 3

a=int(input("nhập số nguyên dương: "))
if a <=1:
    print(a,"không phải số nguyên tố")
else:
    so_nt=True
    for i in range(2,a):
        if a%i== 0: 
            so_nt=False
            break
    if so_nt:
        print(a,"là số nguyên tố") 
    else:
        print(a,"không phải số nguyên tố")           