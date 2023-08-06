# ==============================================================================
# Author:              Süleyman Yasin Peker
#
# Cocotb Testbench:     For Car Parking System
#
# Description:
# ------------------------------------
# Test-bench for Car Parking System
#
# License: MIT License
# ==============================================================================

# Import necessary libraries
import random
import warnings
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

@cocotb.test()
async def Car_Parking_System_test1(dut):

    # 	input clk, reset,
    # 	input entrance_sensor, exit_sensor,
    # 	input [1:0] password_user1, password_user2,
    # 	output wire green_light, red_light,
    # 	output reg [6:0] hex1, hex2
    #   reg [2:0] current_state, next_state;
    # 	reg [31:0] counter;
    # 	reg green_light_tmp, red_light_tmp;

    await cocotb.start(Clock(dut.clk, 10, 'us').start(start_high=False))

    clkedge = RisingEdge(dut.clk)

    await clkedge
    dut.reset.value = 1
    dut.entrance_sensor.value = 0
    dut.exit_sensor.value = 0
    dut.password_user1.value = 0b00
    dut.password_user2.value = 0b00

    await clkedge

    dut._log.info("######### IDLE STATE  #########")
    dut._log.info("Current State     : %s  <-  Next State: %s", dut.current_state.value, dut.next_state.value)
    dut._log.info("Green Light       : %s    ||  Red Light : %s", dut.green_light.value, dut.red_light.value)
    dut._log.info("7-Segment Display1: %s", dut.hex1.value)
    dut._log.info("7-Segment Display2: %s", dut.hex2.value)
    dut._log.info("Counter           : %s", hex(dut.counter.value))

    assert dut.next_state.value == 0b000

    await clkedge

    dut.entrance_sensor.value = 1
    dut.exit_sensor.value = 0

    await clkedge

    dut._log.info("######### WAIT PASSWORD STATE  #########")
    dut._log.info("Current State     : %s  <-  Next State: %s", dut.current_state.value, dut.next_state.value)
    dut._log.info("Green Light       : %s    ||  Red Light : %s", dut.green_light.value, dut.red_light.value)
    dut._log.info("7-Segment Display1: %s", dut.hex1.value)
    dut._log.info("7-Segment Display2: %s", dut.hex2.value)
    dut._log.info("Counter           : %s", hex(dut.counter.value))

    assert dut.next_state.value == 0b001

    dut.password_user1.value = 1
    dut.password_user2.value = 3

    await clkedge
    await clkedge
    await clkedge
    await clkedge


    dut._log.info("######### CORRECT PASSWORD STATE  #########")
    dut._log.info("Current State     : %s  <-  Next State: %s", dut.current_state.value, dut.next_state.value)
    dut._log.info("Green Light       : %s    ||  Red Light : %s", dut.green_light.value, dut.red_light.value)
    dut._log.info("7-Segment Display1: %s", dut.hex1.value)
    dut._log.info("7-Segment Display2: %s", dut.hex2.value)
    dut._log.info("Counter           : %s", hex(dut.counter.value))

    assert dut.next_state.value == 0b011

    dut.entrance_sensor.value = 0
    dut.exit_sensor.value = 1

    await clkedge

    dut._log.info("######### CAR EXITS AND IDLE STATE STARTS  #########")
    dut._log.info("Current State     : %s  <-  Next State: %s", dut.current_state.value, dut.next_state.value)
    dut._log.info("Green Light       : %s    ||  Red Light : %s", dut.green_light.value, dut.red_light.value)
    dut._log.info("7-Segment Display1: %s", dut.hex1.value)
    dut._log.info("7-Segment Display2: %s", dut.hex2.value)
    dut._log.info("Counter           : %s", hex(dut.counter.value))

    assert dut.next_state.value == 0b000

    await clkedge


@cocotb.test()
async def Car_Parking_System_test2(dut):

    await cocotb.start(Clock(dut.clk, 10, 'us').start(start_high=False))

    clkedge = RisingEdge(dut.clk)

    await clkedge
    dut.reset.value = 1
    dut.entrance_sensor.value = 0
    dut.exit_sensor.value = 0
    dut.password_user1.value = 0b00
    dut.password_user2.value = 0b00

    await clkedge

    dut._log.info("######### IDLE STATE  #########")
    dut._log.info("Current State     : %s  <-  Next State: %s", dut.current_state.value, dut.next_state.value)
    dut._log.info("Green Light       : %s    ||  Red Light : %s", dut.green_light.value, dut.red_light.value)
    dut._log.info("7-Segment Display1: %s", dut.hex1.value)
    dut._log.info("7-Segment Display2: %s", dut.hex2.value)
    dut._log.info("Counter           : %s", hex(dut.counter.value))

    assert dut.next_state.value == 0b000

    await clkedge

    dut.entrance_sensor.value = 1
    dut.exit_sensor.value = 0

    await clkedge

    dut._log.info("######### WAIT PASSWORD STATE  #########")
    dut._log.info("Current State     : %s  <-  Next State: %s", dut.current_state.value, dut.next_state.value)
    dut._log.info("Green Light       : %s    ||  Red Light : %s", dut.green_light.value, dut.red_light.value)
    dut._log.info("7-Segment Display1: %s", dut.hex1.value)
    dut._log.info("7-Segment Display2: %s", dut.hex2.value)
    dut._log.info("Counter           : %s", hex(dut.counter.value))

    assert dut.next_state.value == 0b001

    dut.password_user1.value = 2
    dut.password_user2.value = 2

    await clkedge
    await clkedge
    await clkedge
    await clkedge

    dut._log.info("######### WRONG PASSWORD STATE  #########")
    dut._log.info("Current State     : %s  <-  Next State: %s", dut.current_state.value, dut.next_state.value)
    dut._log.info("Green Light       : %s    ||  Red Light : %s", dut.green_light.value, dut.red_light.value)
    dut._log.info("7-Segment Display1: %s", dut.hex1.value)
    dut._log.info("7-Segment Display2: %s", dut.hex2.value)
    dut._log.info("Counter           : %s", hex(dut.counter.value))

    assert dut.next_state.value == 0b010

    dut.password_user1.value = 1
    dut.password_user2.value = 3

    await clkedge
    await clkedge
    await clkedge
    await clkedge

    dut._log.info("######### CORRECT PASSWORD STATE  #########")
    dut._log.info("Current State     : %s  <-  Next State: %s", dut.current_state.value, dut.next_state.value)
    dut._log.info("Green Light       : %s    ||  Red Light : %s", dut.green_light.value, dut.red_light.value)
    dut._log.info("7-Segment Display1: %s", dut.hex1.value)
    dut._log.info("7-Segment Display2: %s", dut.hex2.value)
    dut._log.info("Counter           : %s", hex(dut.counter.value))

    assert dut.next_state.value == 0b011

    await clkedge

    dut.entrance_sensor.value = 0
    dut.exit_sensor.value = 1

    await clkedge

    dut._log.info("######### CAR EXITS AND IDLE STATE STARTS  #########")
    dut._log.info("Current State     : %s  <-  Next State: %s", dut.current_state.value, dut.next_state.value)
    dut._log.info("Green Light       : %s    ||  Red Light : %s", dut.green_light.value, dut.red_light.value)
    dut._log.info("7-Segment Display1: %s", dut.hex1.value)
    dut._log.info("7-Segment Display2: %s", dut.hex2.value)
    dut._log.info("Counter           : %s", hex(dut.counter.value))

    assert dut.next_state.value == 0b000

    await clkedge