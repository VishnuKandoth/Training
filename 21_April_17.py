#Type Function
print type(1)           

li = []
print type(li)          


#string functions
import string
print string.join("vishnu",'_')



#getattribute
li = ["Sravan", "Kailash"]       
print getattr(li, "append")("Nithin") 
print li
print getattr({}, "clear")         
  

#List Filtering
li = ["a", "vishnubalachandran", "nithin", "b", "c", "b", "d", "d"]
print [elem for elem in li if len(elem) > 10]       
print [elem for elem in li if elem != "b"]         
print [elem for elem in li if li.count(elem) == 1] 


#and-or Trick
a = "first"
b = "second"
print 1 and a or b 
print 0 and a or b 


#lambda Function
def f(x):
	return x*2     
print f(3)
g = lambda x: x*2  
print g(4)
print (lambda x: x*2)(5) 


#split WithOut arguement
s = "Hai   how\nare\tyou"  
print s
print "simple split:",s.split()           
print "Join Split: "," ".join(s.split()) 


#ljust
s = 'this is left padding'
print s.ljust(30,'*') 
