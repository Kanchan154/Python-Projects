import csv
def HighestMarks():
    try:
        hm=0
        with open("student_records_100.csv","r")as f1:
            reader= csv.DictReader(f1)
            for row in reader:
                if(int(row["Marks"]) > hm):
                    hm=int(row["Marks"])
            print(f" Highest marks: {hm}")
    except Exception as error:
        print(error)
# HighestMarks()                
            
def LowestMarks():
    try:
        lm=100
        with open("student_records_100.csv","r")as f1:
            reader= csv.DictReader(f1)
            for row in reader:
                if (int(row["Marks"])<lm):
                    lm=int(row["Marks"])
            print(f"Lowest marks:{lm}")
    except Exception as error:
        print(error)
# LowestMarks()

def AverageMarks():
    try:
        summ=0
        count=0
        with open("student_records_100.csv","r")as f1:
            reader= csv.DictReader(f1)
            for row in reader:
                count+=1
                summ+=int(row["Marks"])
            print(f"Average marks of students are:{summ/count}")
            print(f"Number of Students are : {count}")
    except Exception as error:
        print(error)
# AverageMarks()

def greaterthan80():
    try:
        count=0
        with open("student_records_100.csv","r")as f1:
            reader=  csv.DictReader(f1)
            for row in reader:
                if (int(row["Marks"])>80):
                    count+=1
            print(f"number of students whose marks are greater than 80 are {count}")
    except Exception as error:
        print(error)
# greaterthan80()

def greaterthan90():
    try:
        with open("student_records_100.csv","r")as f1:
            reader=  csv.DictReader(f1)
            for row in reader:
                if (int(row["Marks"])>90):
                    print(row["Name"])
    except Exception as error:
        print(error)
# greaterthan90()

def SearchStudents():
    try:
        rollno=input("enter the roll number:")
        with open("student_records_100.csv","r")as f1:
            reader=csv.DictReader(f1)
            for row in reader:
                if (rollno==row["Roll No"]):
                    print(row)
                    break
            else:
                print("student not found")
    except Exception as error:
        print(error)
# SearchStudents()

def printInTable():
    try:
        with open("student_records_100.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(f"{row[0]:<10} {row[1]:<20} {row[2]:<10} {row[3]:<10} {row[4]:<10} {row[5]:<10}")
        
    except Exception as error:
        print(error)
# printInTable()

def UpdateMarks():
    try:
        rollNo = int(input("Enter the Roll No."))
        marks = int(input("Enter the marks"))
        l1 = []
        # read file
        with open("student_records_100.csv", "r") as f1:
            reader = csv.DictReader(f1)
            for row in reader:
                if(rollNo == int(row["Roll No"])):
                    row["Marks"] = marks
                l1.append(row)
        
        # write the file 
        with open("student_records_100.csv", "w", newline="") as f1:
            fields = ["Roll No","Name","Gender","Branch","Semester","Marks"]
            writer = csv.DictWriter(f1,fieldnames=fields)
            writer.writeheader()
            writer.writerows(l1)
            print("File Updated Successfully")
    except Exception as error:
        print(error)    
# UpdateMarks()

def DeleteRecord():
    try:
        rollNo = int(input("Enter the Roll No."))
        l1 = []
        # read file
        with open("student_records_100.csv", "r") as f1:
            reader = csv.DictReader(f1)
            for row in reader:
                if(rollNo == int(row["Roll No"])):
                    continue
                l1.append(row)
        
        # write the file 
        with open("student_records_100.csv", "w", newline="") as f1:
            fields = ["Roll No","Name","Gender","Branch","Semester","Marks"]
            writer = csv.DictWriter(f1,fieldnames=fields)
            writer.writeheader()
            writer.writerows(l1)
            print("Student Deleted Successfully")
    except Exception as error:
        print(error)   
DeleteRecord()