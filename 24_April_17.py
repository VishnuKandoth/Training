file1="file1.txt"
file2="file2.txt"



f=open("file1.txt" ,"w")
write_data=raw_input("Enter the data to be Written in file1: ")
f.write(write_data)
f.close()

print " " 
print "Written Data: ",file("file1.txt").read()
print " " 

f1="file2.txt"
file2_data=raw_input("Enter the Addon Data of file2: ")
file(f1,"a").write(file2_data)
print " "
print "Append Mode: ",file(f1).read()
print " "


s = '100 NORTH MAIN ROAD'
print "Replaced Value: ",s.replace('ROAD', 'RD.')               

s = '100 NORTH BROAD ROAD'
print "Replaced Value: ",s.replace('ROAD', 'RD.')               

print "Replaced Value: ",s[:-4] + s[-4:].replace('ROAD', 'RD.') 


#email verification
import re
def email():
    email = raw_input("enter the mail address::")
    match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)

    if match:
        print " " 
        print "valid email", match.group()
        print " "
    else:
    	print " "
        print "email not valid"
        print " "

def phone():
	phone=raw_input("Enter the mobile number")
	match1=re.search('[789]\d{9}$',phone)
	if match1:
		print " "  
		print "Phone_no is matching:::",match1.group()
		print " "
	else:
		print " "
		print "not a valid phone_no ... not matching the regex"
		print " " 

email()
phone()