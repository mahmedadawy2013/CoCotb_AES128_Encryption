from transactions import * 
from cocotb.triggers import * 
import cocotb
import cocotb.queue

class driver ():

   def __int__(self,name = "DRIVER"):
      self.name = name
      self.driv_mail      = cocotb.queue.Queue()
      self.t_drive        = transactions()
      self.driv_handover  = Event(name=None) 
      
   async def run_driver (self,dut_driver):
      cocotb.log.info("[Driver] STARTING.")
      while(True):
         cocotb.log.info("[Driver] waiting for item ...")
         self.t_drive = await self.driv_mail.get()
         cocotb.log.info("[Driver] Recieved items is  ...")
         await FallingEdge(dut_driver.clk)
         self.t_drive.display("DRIVER")
         dut_driver.inn.value        = self.t_drive.inn
         dut_driver.key.value        = self.t_drive.key
         self.driv_handover.set() 
