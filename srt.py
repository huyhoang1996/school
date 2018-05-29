import datetime
import time
""" Results Should Be The Following: 
    arrive=[0,3,6,7,7,10,15,16]
    exe=[12,3,11,1,4,5,20,7]
Num  Process   Time     Time
      Time   Remaining   Now
0               12        0  added
0       3        9        3
1                3           added
1       3        0        6  #1 Finished
2               11           added
0       1        8        7
3                1           added
4                4           added
3       1        0        8  #3 Finished
4       2        2       10
5                5           added
4       2        0       12  #4 Finished
5                5
5       3        2       15
6               20           added
5       1        1
"""
result = ''
class ProcessUnit:
    def __init__(self, arrive, exe):
        global result
        unit_to_process = {}
        ctr = 0
        unit_number = 0
        time_now = 0
        next_start_time = 0
        add_ctr = 0
        stop = len(arrive) - 2
        ## add first unit to start the process
        unit_to_process[add_ctr] = [ arrive[add_ctr], exe[add_ctr] ]
        while add_ctr < stop:
            ctr += 1
            if ctr > 500:     ## limit to 500 cycles
                add_ctr = stop +1
            result+= "\n"+ "-"*60
            ## add next unit to the dictionary ?
            if arrive[add_ctr+1] <= time_now:
                add_ctr += 1
                unit_to_process[add_ctr] = [ arrive[add_ctr], exe[add_ctr] ]
                result+= "added #"+ str(add_ctr)
                next_start_time = arrive[add_ctr+1]
            result+="\n" + str(unit_to_process)
            ##  initialize stop time = next start time - time now
            stop_time = arrive[add_ctr+1] - time_now
##            print "initialize stop time", arrive[add_ctr+1], time_now
            if stop_time < 0:      ## two units arrive at same time
                stop_time = 99999
            ##  find smallest completion time and compare to
            ##  the current stop time (next arrive time)
            smallest = 99999
            for key in unit_to_process:
##               print "time remaining", unit_to_process[key][1], stop_time
               if unit_to_process[key][1] < smallest:
                   smallest = unit_to_process[key][1]
                   unit_number = key   # process smallest unit no matter how long the time is
            if smallest < stop_time:
                stop_time = smallest
            result+="\n" + "processing next unit, stop_time"+ str(stop_time)+ "unit number"+ str(unit_number)
            self.process_unit(stop_time)
            time_now += stop_time
            unit_to_process[unit_number][0] += stop_time
            unit_to_process[unit_number][1] -= stop_time
            ##  if completed, delete from dictionary
            if unit_to_process[unit_number][1] < 1:
                result+="\n" + "dictionary delete key"+ str(unit_number)
                del unit_to_process[unit_number]
        ## add last unit and process remaining in order received
        result+= "\n-------- processing remaining units ----------------"
        add_ctr += 1
        unit_to_process[add_ctr] = [ arrive[add_ctr], exe[add_ctr] ]
        result+=  "\n"+ str(unit_to_process)+ "\n"
        units = unit_to_process.keys()
        sorted(units)
        for key in units:
            result+="\n"+ "unit ="+ str(key)+ "  time ="+ str(unit_to_process[key][1])+"\n"
            self.process_unit(unit_to_process[key][1])
    def process_unit(self, time_to_process):
        global result
        result+= "\n"+ "     "
        for n in range(0, time_to_process):
            time.sleep(1.0)
            result+= str(n)
        print
##===================================================================
def process(a,b):
    global result
    arrive=a
    exe=b
    start_time = datetime.datetime.now()
    P = ProcessUnit(arrive, exe)
    result+= ("\n"+ str(datetime.datetime.now() - start_time))
    return result

