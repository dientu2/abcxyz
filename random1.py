from random import randint #
from time import sleep
from datetime import datetime
print("Chuong trinh lay gia tri ngau nhien")
try:
	while(1):
		temperature = randint(28, 30)
		humidity = randint(80, 90)
		time_now = datetime.now()
		print("Cap nhat luc %s" %(time_now))
		print("Nhiet do : %s" %(temperature))
		print("Do am : %s" %(humidity))
		print("------------------------")
		sleep(1)
except: #KeyboardInterrupt:
	print("Chuong trinh ket thuc") 