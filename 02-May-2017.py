class ToRomanBadInput(unittest.TestCase):                            
    def testTooLarge(self):                                          
        """toRoman should fail with large input"""                   
        print self.assertRaises(roman.OutOfRangeError, roman.toRoman, 4000) 

    def testZero(self):                                              
        """toRoman should fail with 0 input"""                       
        print self.assertRaises(roman.OutOfRangeError, roman.toRoman, 0)    

    def testNegative(self):                                          
        """toRoman should fail with negative input"""                
        print self.assertRaises(roman.OutOfRangeError, roman.toRoman, -1)  

    def testNonInteger(self):                                        
        """toRoman should fail with non-integer input"""             
        print self.assertRaises(roman.NotIntegerError, roman.toRoman, 0.5)  




from SOAPpy import SOAPProxy
url = 'http://services.xmethods.net:80/soap/servlet/rpcrouter'
n = 'urn:xmethods-Temperature'
server = SOAPProxy(url, namespace=n)     
server.config.dumpSOAPOut = 1            
server.config.dumpSOAPIn = 1
temperature = server.getTemp('27502')  



from SOAPpy import WSDL          
wsdlFile = ('http://www.xmethods.net/sd/2001/TemperatureService.wsdl')
server = WSDL.Proxy(wsdlFile)
server.methods.keys() 