import os
import time
while True :
    check = input("Bạn có muốn tắt máy không? (y/n): "); 
    if check == 'n':
        for c in range(1 , 31): 
            print(c, end=' ')   #Hiển thị số giây
            time.sleep(1) #Hen gio tat may (30s)
    else:
        os.system("shutdown /s /t 1"); #Tắt máy trong 1s
        break
