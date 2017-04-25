rom xml.dom import minidom
xmldoc = minidom.parse('russiansample.xml') 
title = xmldoc.getElementsByTagName('title')[0].firstChild.data
print title                                                                        
convertedtitle = title.encode('koi8-r')     
print convertedtitle



reflist = xmldoc.getElementsByTagName('ref')
bitref = reflist[0]
print bitref.toxml()
print bitref.attributes          
print bitref.attributes.keys()   
print bitref.attributes.values() 
print bitref.attributes["id"]    


#Accessing Individual Attributes
a = bitref.attributes["id"]
print a
print a.name 
print a.value 


#String IO
contents = "<grammar><ref id='bit'><p>0</p><p>1</p></ref></grammar>"
import StringIO
ssock = StringIO.StringIO(contents)   
print ssock.read()                          
print ssock.read()                          
ssock.seek(0)                         
print ssock.read(15)                        
print ssock.read(15)
print ssock.read()
ssock.close()   


#stdout and stderr
for i in range(3):
	print 'Dive in'             
import sys
print "stdout: "
for i in range(3):
	sys.stdout.write('Dive in')


print "\nstderr: "
for i in range(3):
	sys.stderr.write('Dive in') 

#Parsing XML from a File
from xml.dom import minidom
fsock = open('binary.xml')    
xmldoc = minidom.parse(fsock) 
fsock.close()                 
print xmldoc.toxml()          

#Redirecting Output
import sys

print 'Dive in'                                          
saveout = sys.stdout                                     
fsock = open('out.log', 'w')                             
sys.stdout = fsock                                       
print 'This message will be logged instead of displayed' 
sys.stdout = saveout                                     
fsock.close()       

#Reading From Standard Input
def openAnything(source):
    if source == "-":    1
        import sys
        return sys.stdin


#ref Element
def do_xref(self, node):
    id = node.attributes["id"].value
    self.parse(self.randomChildElement(self.refs[id]))
