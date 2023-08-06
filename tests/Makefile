CWD=$(shell pwd)

SIM ?= icarus
TOPLEVEL_LANG ?=verilog


VERILOG_SOURCES =$(CWD)/../*.v


TOPLEVEL = Car_Parking_System
MODULE := Car_Parking_System_cocotb_test
#COCOTB_HDL_TIMEUNIT=1us
#COCOTB_HDL_TIMEPRECISION=1us

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
