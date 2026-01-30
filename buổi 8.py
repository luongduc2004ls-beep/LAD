#bài 1
for i in range(1,50):
    if i%3 and i%5 :    
        print("FizzBuzz")
    elif i%3:
        print("Fizz")
    elif i%5:
        print("Buzz")
    else:
        print(i)             
print("-------------------------------------------")
#bài 2
print("--------------TRÒ CHƠI ĐOÁN SỐ-------------")
a=69
while True:
    b= int(input("hãy nhập con số mà bạn cho là đúng :"))
    if b>a:
        print("Số bạn đoán lớn quá! Vui lòng thử lại =))")
    elif b<a:
        print("Số bạn đoán quá nhỏ! vui lòng nhập lại =))")
    elif b==a:
        print("Bạn đã đoán đúng rồi")
        break
    else:
        print("chơi lại")
        
        




