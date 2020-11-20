import os
import time
while True :
    check = input("Want to shutdown your computer ? (y/n): ");
    if check == 'n':
        for c in range(1 , 31):
            print(c, end=' ')
            time.sleep(1) #Hen gio tat may (30s)
    else:
        os.system("shutdown /s /t 1");
        break