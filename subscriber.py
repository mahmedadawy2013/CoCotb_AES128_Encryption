from transactions import * 
from cocotb.triggers import * 
import cocotb
import cocotb.queue
from cocotb_coverage.coverage import *


@CoverPoint("top.out"      , vname="out"      , bins=list(range(0, 2 ** 16  ))) 
def sample(out):
    pass

class subscriber() :
   
    def __init__(self ,name = "SUBSCRIBER"): 
       self.name               = name
       self.t_sub              = transactions()
       self.sub_mail           = cocotb.queue.Queue()

    async def run_subscriber (self) : 
        while(True):
            self.t_sub = transactions()
            cocotb.log.info("[subscriber] receiving from monitor..... ") 
            self.t_sub = await self.sub_mail.get() 
            self.t_sub.display("SUBSCRIBER")
            cocotb.log.info("[subscriber] receiving from monitor..... ") 
            sample(self.t_sub.out)
 
                