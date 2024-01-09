import cocotb 
import random
from cocotb_coverage.crv import *

"""***************************************************************************************************************
* Check This Important Link For Coverage And Constraints 
https://cocotb-coverage.readthedocs.io/en/latest/reference.html#cocotb_coverage.crv.Randomized.randomize_with

* This The Source Code With Examples 
https://cocotb-coverage.readthedocs.io/en/latest/_modules/cocotb_coverage/crv.html#Randomized.add_constraint

* Check This Link For Extra Information about Constraints 
https://cocotb-coverage.readthedocs.io/en/latest/introduc

tion.html#constrained-random-verification-features-in-systemverilog
* Another link but it is so important 
https://cocotb-coverage.readthedocs.io/en/latest/tutorials.html

*****************************************************************************************************************"""
class  transactions(Randomized):
    def __init__(self ,name = "TRANSACTIONS"):
        Randomized.__init__(self)
        self.name = name
        self.inn           =  0  
        self.out           =  0
        self.key           =  0

        self.add_rand("inn"        , list(range(0,2**16)       )   ) 
        self.add_rand("key"        , list(range(0,2**16)       )   ) 



    def display(self,name = "TRANSACTION"):
        cocotb.log.info("******************"+str(name)+"*******************")
        cocotb.log.info("the Value of inn           is   " + str(self.inn      ))
        cocotb.log.info("the Value of key           is   " + str(self.key      ))
        cocotb.log.info("the Value of out           is   " + str(self.out      ))
        cocotb.log.info("**************************************************")


