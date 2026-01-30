#bài 1
danh_sach_cong_viec=[]
while True:
    print("\n >>>>>>>>>>>>>>>Menu<<<<<<<<<<<<<<<<<<<<")
    print("1.xem danh sách tất cả công việc")
    print("2.thêm công việc mới")
    print("3.đánh dấu một công việc đã hoàn thành")
    print("0.thoát chương trình")
    lua_chon=input("mời nhập lựa chọn của bạn:")
    if lua_chon=="1":
        if not danh_sach_cong_viec:
            print("chưa có công việc")
        else:
            print("danh sách công việc:")
            for i in range(len(danh_sach_cong_viec)):
                print(f"{i+1}. {danh_sach_cong_viec[i]['ten_cong_viec']} ")

            
    elif lua_chon=="2":
        ten_cong_viec=input("nhập tên công việc mới:")
        danh_sach_cong_viec.append({"ten_cong_viec": ten_cong_viec, "hoan_thanh": False}) 
        print("đã thêm công việc")
    elif lua_chon=="3":
        cong_viec_da_hoan_thanh=input("nhập số thứ tự công việc đã hoàn thành:")
        so_thu_tu=int(cong_viec_da_hoan_thanh)
        if 1 <= so_thu_tu <= len(danh_sach_cong_viec):
            danh_sach_cong_viec[so_thu_tu-1]["hoan_thanh"] = True
            print("đã đánh dấu công việc đã hoàn thành")
        else:
            print("số thứ tự không hợp lệ")
    elif lua_chon=="0":
        print("thoát chương trình")
        break
    else:
        print("hãy thử lại")  
# BÀI 2
day_so= input("nhập dãy số cách nhau bởi dấu phẩy:")
number =day_so.split(",")
max_number=float(number[0])
for num in number:
    if float(num)>max_number:
        max_number=float(num)
print("số lớn nhất là :",max_number)
#bài 3
print("=========================================")
grade_book=[
    ["an",8.0,7.5,9.0],
    ["binh",9.5,9.0,9.5],
    ["cuong",5.0,6.0,7.0],
]
#điểm trung bình
for i in range(len(grade_book)):
    diem_tb=(grade_book[i][1]+grade_book[i][2]+grade_book[i][3])/3
    print("điểm trung bình ",diem_tb)
#điểm trung bình cao nhất
max_diem_tb=9
for i in range(len(grade_book)):
    diem_tb=(grade_book[i][1]+grade_book[i][2]+grade_book[i][3])/3
    if diem_tb>max_diem_tb:
        max_diem_tb=diem_tb
print("điểm trung bình cao nhất là :",max_diem_tb)       
        