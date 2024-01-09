from transactions import * 
from cocotb.triggers import * 
import cocotb
import cocotb.queue


class generator() :
   
    def __init__(self ,join_any,name = "GENERATOR"): 
       self.name             = name
       self.t_gen            = transactions()
       self.gen_mail         = cocotb.queue.Queue()
       self.gen_handover     = Event(name=None) 
       self.join_any         = join_any

    async def run_generator (self,dut_generator) : 
        iteration_number = 1000 ; 
        for i in range(iteration_number): 
            self.gen_handover.clear() 
            await self.randoum_sequence()

        await FallingEdge(dut_generator.clk)
        self.join_any.set()

    """ ************* **************** Sequence Generation ****************** ***************"""
    async def randoum_sequence (self):
        self.t_gen = transactions()
        self.t_gen.randomize() ; 
        #self.t_gen.display("GENERATOR")
        cocotb.log.info("[Generator] Sending To The Driver..... ") 
        await self.gen_mail.put(self.t_gen)  
        await self.gen_handover.wait()      
