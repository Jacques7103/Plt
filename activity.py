import csv
import datetime as dt
import statistics as st
import matplotlib.pyplot as plt
import pygal
import os

os.chdir("C:/Users/ferdi/OneDrive/Desktop/Binus/1st Semester/Algorith And Programming/12th/Task")

file = "activity.csv"

dictDate = {}
dictInterval = {}

with open(file,"r") as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    print(headerRow)

    for row in reader:
        steps = row[0]
        # Ignore NA step values
        if steps != "NA":
            date = row[1]
            date2 = int(dt.datetime.strptime(date, '%Y-%m-%d').day)

            interval = int(row[2])

            # Populate the dictionary
            # if the date exists, nothing happens
            # else, add new key in the dictionary
            dictDate.setdefault(str(date), [])
            # Populate the lsit with the numebr of steps
            # Taken in teh specific date
            dictDate[str(date)].append(int(steps))

            dictInterval.setdefault(interval,[])
            dictInterval[interval].append(int(steps))
            # print(dictInterval)
            # print(dictDate)
    
    listDate = []   # Store dates
    listTotal = []  # Store total number of steps in a day
    listAve = []    # Store avg # of steps in a day

    for i in dictDate.keys():
        listDate.append(i)
        listTotal.append(sum(dictDate.get(i)))
        listAve.append(st.mean(dictDate.get(i)))
        
    date_step = {listDate[i]: listTotal[i] for i in range(len(listDate))}
    
    weekDay = []
    weekEnd = []
    
    for day, step in date_step.items():
        day = day.split("-")
        day = (", ".join(day))
        (year, month, date) = [int(x) for x in day.split(",")]
        day = dt.datetime(year, month, date)
        if day.weekday() > 4:
            weekEnd.append(step)
        else:
            weekDay.append(step)
            
    hist = pygal.Bar()
    hist._title = "Average per interval (WeekEnds)"
    hist._x_title = "Intervals"
    hist._y_title = "Frequency"
    hist.x_labels = dictInterval.keys()
    hist.add("Average number of steps", weekEnd)
    hist.render_to_file("weekends1.svg")

    plt.hist(weekEnd)
    plt.title("Total steps taken per day (WeekEnds)")
    plt.xlabel("Steps per day")
    plt.ylabel("Frequency")
    plt.tick_params(axis = "both", which = "major", labelsize = 6)
    plt.savefig("weekends2.svg")
    plt.show()
    plt.close()
    
    hist = pygal.Bar()
    hist._title = "Average per interval (WeekDays)"
    hist._x_title = "Intervals"
    hist._y_title = "Frequency"
    hist.x_labels = dictInterval.keys()
    hist.add("Average number of steps", weekDay)
    hist.render_to_file("weekdays1.svg")

    plt.hist(weekDay)
    plt.title("Total steps taken per day (WeekDays)")
    plt.xlabel("Steps per day")
    plt.ylabel("Frequency")
    plt.tick_params(axis = "both", which = "major", labelsize = 6)
    plt.savefig("weekdays2.svg")
    plt.show()
    plt.close()