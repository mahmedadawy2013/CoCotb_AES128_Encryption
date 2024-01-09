SIM ?= questa
TOPLEVEL_LANG ?= verilog
PWD=$(shell pwd)
VERILOG_SOURCES = $(PWD)/RTL/*.sv 
TOPLEVEL := AES_Encrypt
MODULE=tb
include $(shell cocotb-config --makefiles)/Makefile.sim