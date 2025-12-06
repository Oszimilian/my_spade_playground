#top = MyState::MyState

import cocotb
from spade import SpadeExt
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, Timer  # ← Timer fehlt!

@cocotb.test()
async def test(dut):
    s = SpadeExt(dut)
    clk = dut.clk_i
    
    # Clock starten (100MHz, 10ns Periode)
    await cocotb.start(Clock(clk, period=10, units='ns').start())
    
    # Reset-Sequenz (wichtig für MyState)
    await FallingEdge(clk)
    s.i.rst = True
    await FallingEdge(clk)
    await FallingEdge(clk)
    s.i.rst = False
    await FallingEdge(clk)
    
    # 100ms = 100.000ns warten (10.000 Takte @100MHz)
    await Timer(100_000, units='ns')  # Jetzt funktioniert es!

    await FallingEdge(clk)