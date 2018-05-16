import collections
from collections import deque



result = []
count = 0

def setLen(len_result):
	global result
	result = [None]*len_result

def replaceData(result, val_data, count):
	if count < len(result):
		result[count] = val_data
	else:
		count = 0	
		result[count] = val_data

def getValue(list_data):
	global result
	for index_data, val_data in enumerate(list_data):
		print 'index: ', index_data, ' value: ', val_data
		if index_data < len(result):
			result[index_data] = val_data
			print 'result ', result
		else:
			if val_data in result:
				print 'result ', result
				continue
			global count
			replaceData(result, val_data, count)
			count +=1
			print 'result ', result


print("Enter the number of process: ")
setLen(int(input()))
print("Enter the burst time of the processes: \n")
list_value =list(map(int, raw_input().split()))
print list_value
getValue(list_value)