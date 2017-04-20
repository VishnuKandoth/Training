student={101:'Vishnu',102:'Vikas',103:'Nithin',104:'Jishnu',105:'Sravan',106:'Soman',107:'Sajeesh',108:'Jyothish',109:'Arun',110:'Jithin'}
subject=[['Pearl','Python','Ruby'],['Java','Dotnet','Networking'],['Oracle','SQLite','MySQL'],['Android','IOS']]
dept=('Open-Source','Domain','Database','Mobile Technology')

def addstud():
	stuname=raw_input("Student Name: ")
	stuid=int(input("Student ID: "))	
	student[stuid]=stuname
	print " "
	print "\t Student Data Entered !!"
	print " " 	


def studdetails():
	option=raw_input("Do you want the details of all students:[y/n] ")
	if option=='y' or option=='Y': 
		print " "
		print "STUDENT DETAILS: "
		print " "
		print "\t",student
		print " "
	elif option=='n' or option=='N':
		print " "
		stuid=int(input("Student_ID: "))
		print " "
		print "\t",student[stuid]
		print " "	
	else: 
		print " "
		print "\t Not a Valid Input !!"
		print " "


def studedit():
	optio=int(input("Student ID of Student to be Edited: "))
	print " "
	print "Select Option to be Edited: "
	print "1.Name"
	print "2.ID"
	edit=int(input("Option"))
	if edit== 1: 	
		stdname=raw_input("Enter New Student Name: ")
		student[optio]=stdname
		print " "
		print "Student Data Updated"
		print " "
	elif edit== 2:
		stname=student[optio]
		del student[optio]
		stid=int(input("Enter the New Student ID: "))	
		student[stid]=stname
		print " "
		print "\t Student Data Entered !!"
		print " " 	
	else:
		print " "
		print "Invalid Entry"


def studremove():
	stid=int(input("Student ID: "))
	delop=raw_input("Are You Sure To Delete the Entry:[y/n] ")	
	if delop=='y' or delop=='Y':
		del student[stid]
		print " "
		print "\t Student Removed"
		print " "
	elif delop=='n' or delop=='N':
		print " "
		print "\t Cancelled "
		print " "
	else:
		print " "
		print "\t Unable to Process"
		print " "


def deptsub():
	loop=0
	while(loop!=1):
		print " "
		print "\t -------------Select the Option-------------"
		print "\t 1.Departments "
		print "\t 2.All Subjects"
		print "\t 3.Add Subject"
		print "\t 4.Subject of Particular Department"
		print "\t 5.Exit to Main Menu"
		print "\t-------------------------------------------"
		print " "
		op=int(input("\t Option: "))
		if op== 1:
			print dept
			print " "
		elif op== 2:
			print subject
			print " "
		elif op== 3:
			loop=0
			while(loop!=1):
				print " "
				print "\t --------Choose Department--------"
				print "\t 1.Open-Source"
				print "\t 2.Domain"
				print "\t 3.Database"
				print "\t 4.Mobile Technology"
				print "\t ------------------------------------"
				print " "
				op2=int(input("\t Department No: "))
				subname=raw_input("\t Enter the Subject: ")
				if op2== 1:
					subject[0].append(subname)
					break
				elif op2== 2:
					subject[1].append(subname)
					break
				elif op2== 3:
					subject[2].append(subname)
					break
				elif op2== 4:
					subject[3].append(subname)
					break	
				else:
					print "\tWrong Dept No"
			print " "
			print "\t successfully added",subname
			print " "
		elif op==4:
			loop=0
			while(loop!=1):
				print " "
				print "\t --------Choose Department No--------"
				print "\t 1.Open-Source"
				print "\t 2.Domain"
				print "\t 3.Database"
				print "\t 4.Mobile Technology"
				print "\t 5.Exit to Previous Menu"
				print "\t ------------------------------------"
				print " "
				op1=int(input("\t Department No: "))
				print " "
				if op1== 1:print subject[0]
				elif op1== 2:print subject[1]
				elif op1== 3:print subject[2]
				elif op1== 4:print subject[3]
				elif op1== 5:break	
				else:print "\t Wrong Dept No"
		elif op==5:
			break		
		else:
			print "\t Invalid Data Input"
	
loop=0
while(loop!=1):
	print "--------------Select the Option--------------"
	print "|  1.Add Student                            |"
	print "|  2.Students Detail                        |"
	print "|  3.Edit/Update Student                    |"
	print "|  4.Delete Student                         |"
	print "|  5.Departments & Subject                  |"
	print "|  6.Exit                                   |" 
	print "---------------------------------------------"
	
	choice=int(input("Option: "))
	if choice== 1:
		addstud()
	elif choice== 2:
		studdetails()
	elif choice== 3:
		studedit()
	elif choice== 4:
		studremove()
	elif choice== 5:
		deptsub()
	elif choice== 6:	
		break
	else:	
		print " "
		print "\t Sorry..Wrong Input!! Visit Again"
		break	

print" "
print "--------------------Thank You--------------------"
print "                 Have A Nice Day                 "
print " "
