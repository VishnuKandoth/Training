class department:

	def dept(self):
		print " " 
		print "Fill In the Details Form"
		self.dept_id=int(input("Department ID: "))
		self.dept=raw_input("Department: ")
	
	def deptdetails(self):
		print " " 
		print "Department Details:"
		print " "
		print "\t Department ID: ",self.dept_id
		print "\t Department: ",self.dept		


class employee(department):
	def details(self):
		self.emp_name=raw_input("Employee Name: ")
		self.emp_id=int(input("Employee ID: "))
		self.emp_addr=raw_input("Address: ")	
						
	def status(self):
		self.emp_status=raw_input("Status: Active/InActive(A/I) ")
		print " "
	
	def empdetails(self):		
		print " "
		print "Employee Details: "
		print " "
		print "\t Name: ",self.emp_name
		print "\t Emp_ID: ",self.emp_id
		print "\t Dept_ID: ",self.dept_id
		print "\t Address: ",self.emp_addr
		print "\t Employee Status: ",
		if self.emp_status=='a' or self.emp_status=='A':
			print "Active"
		elif self.emp_status=='i' or self.emp_status=='I':
			print "Inactive"
		else:
			print "Not Valid"


class leave(employee):
	date=[]
	no=0
	def applyleave(self):
		print " "
		self.no=int(input("No.of Leave Required: "))
		if self.no<= 5:
			print "Enter the Dates for Leave:[dd/mm/yyyy]"
			for i in range (0,self.no):
				self.dat=raw_input(" ")
				self.date.insert(i,self.dat)
		else:
			print " "
			print "\t Maximum of Only 5 Leaves Can be Applied"
		
	def leavestatus(self):
		print " "
		if self.no== 0:
			print "\t No Leaves Applied"
		else:
			print "\t Leave applied for ",self.no," Days"
			print " "	
			print "\t Dates: "		
			for i in range (0,self.no):
				print "\t\t",self.date[i]
	

ob=leave()
ob.dept()
ob.details()
ob.status()	
loop=0
while(loop!=1):
	print " "	
	print "-----------------Please select an Option-----------------"
	print " "	
	print "1.Employee Details"
	print "2.Department Details"
	print "3.Apply Leave"
	print "4.Leave Status"
	print "5.Exit"
	print " "
	print "Option: "
	choice=int(input())
	if choice== 1:
		ob.empdetails()
	elif choice== 2:
	    	ob.deptdetails()
	elif choice== 3:
	   	ob.applyleave()
	elif choice== 4:
		ob.leavestatus()
	elif choice== 5:
		break

print "------------------------Thank You------------------------"
print "                     Have A Nice Day                     "	
print " "		
