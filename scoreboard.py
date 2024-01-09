from transactions import * 
from cocotb.triggers import * 
import cocotb
import cocotb.queue
from Crypto.Cipher import AES
import binascii

class Scoreboard() :
   
    def __init__(self ,name = "SCOREBOARD"): 
       self.name                = name
       self.t_score             = transactions()
       self.score_mail          = cocotb.queue.Queue()
       self.Golden_out          = 0
       self.passed_test_cases   = 0
       self.failed_test_cases   = 0


    async def run_scoreboard (self) : 
        while(True):
            self.t_score = transactions()
            cocotb.log.info("[Scoreboard] receiving from monitor..... ") 
            self.t_score = await self.score_mail.get() 
            self.t_score.display("SCOREBOARD")
            """**************************  TEST CASES **************************"""
            self.Golden_out =  self.Golden_AES( self.t_score.key ,  self.t_score.inn ) 
            cocotb.log.info(self.Golden_out)
            if (self.t_score.out == self.Golden_out):
                self.passed_test_cases += 1 
            else :
                self.failed_test_cases += 1 
            """******************************************************************"""

    def Golden_AES (int_key,int_input) :
        h1 = hex(int_key)[2:].zfill(32)
        h2 = hex(int_input)[2:].zfill(32)
        key_hex  = str(h1)
        data_hex = str(h2)
        data = bytes.fromhex(data_hex)
        key = bytes.fromhex(key_hex)

        cipher = AES.new(key, AES.MODE_ECB)

        ciphertext = cipher.encrypt(data)

        hex_representation = binascii.hexlify(ciphertext).decode()

        resulting_integer = int(hex_representation, 16)

        return(resulting_integer)


    def report_test_cases(self):
        self.total_test_cases = self.passed_test_cases + self.failed_test_cases
        cocotb.log.info("The Number Of Total  Test Cases is :  " + str(self.total_test_cases)) 
        cocotb.log.info("The Number Of Passed Test Cases is :  " + str(self.passed_test_cases))  
        cocotb.log.info("The Number Of Failed Test Cases is :  " + str(self.failed_test_cases))   

            


