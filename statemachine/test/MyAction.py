#top = MyAction::MyAction

import cocotb
from spade import SpadeExt
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, Timer

@cocotb.test()
async def test(dut):
    s = SpadeExt(dut)
    clk = dut.clk_i
    

    await cocotb.start(Clock(clk, period=10, units='ns').start())
    
    
    await FallingEdge(clk)
    s.i.rst = True
    await FallingEdge(clk)
    await FallingEdge(clk)
    s.i.rst = False
    await FallingEdge(clk)
    
    
    await Timer(100_000, units='ns')

    await FallingEdge(clk)