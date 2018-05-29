import os
from datetime import datetime 
os.system('python server.py')
t1 = datetime.now()
# receive a packet
while (datetime.now()-t1).seconds <= 4:
	pass
# os.system('python client.py')
