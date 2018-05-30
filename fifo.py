
def process(n , list_n):
	result = ''
	bt=[]     #bt stands for burst time
	n= n 
	processes=[]
	for i in range(0,n):
	 	processes.insert(i,i+1)
	bt= list_n
	wt=[]    #wt stands for waiting time
	avgwt=0  #average of waiting time
	tat=[]    #tat stands for turnaround time
	avgtat=0   #average of total turnaround time
	wt.insert(0,0)
	tat.insert(0,bt[0])
	for i in range(1,len(bt)):  
		wt.insert(i,wt[i-1]+bt[i-1])
		tat.insert(i,wt[i]+bt[i])
		avgwt+=wt[i]
		avgtat+=tat[i]
	avgwt=float(avgwt)/n
	avgtat=float(avgtat)/n
	result += ("\n")
	result +=("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time\n")
	for i in range(0,n):
		result +=(str(processes[i])+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
		result +=("\n")
	result +=("Average Waiting time is: "+str(avgwt))
	result +=("\n")
	result +=("Average Turn Arount Time is: "+str(avgtat))
	return result


