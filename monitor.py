from cocotb.triggers import *
from transactions import *
import cocotb
import cocotb.queue

class monitor ():
   t_monitor    = transactions()
   mon_mail_s   = cocotb.queue.Queue()
   mon_mail_su  = cocotb.queue.Queue()
   def __int__(self,name = "MONITOR"):
        self.name= name
      
   async def run_monitor (self,dut_monitor):
      cocotb.log.info("[Monitor] STARTING.")
      await RisingEdge(dut_monitor.clk)
      while(True):
        cocotb.log.info("[Monitor] waiting for item ...")
        await RisingEdge(dut_monitor.clk)
        await ReadOnly()
        self.t_monitor.inn              =   int(dut_monitor.inn)
        self.t_monitor.key              =   int(dut_monitor.key)    
        self.t_monitor.out              =   int(dut_monitor.out.value )    
        self.t_monitor.display("MONITOR")  
        await self.mon_mail_s.put(self.t_monitor)  
        await self.mon_mail_su.put(self.t_monitor)
