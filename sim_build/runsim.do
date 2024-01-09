# Autogenerated file
onerror {
	quit -f -code 1
}
vmap -c
if [file exists sim_build/work] {vdel -lib sim_build/work -all}
vlib sim_build/work
vmap work sim_build/work
vlog -work work +define+COCOTB_SIM -sv -timescale 1ns/1ps -mfcu +acc  E:/Digital_Verf/Linkdin/AES/RTL/AES.sv E:/Digital_Verf/Linkdin/AES/RTL/AES_Decrypt.sv E:/Digital_Verf/Linkdin/AES/RTL/AES_Decrypt_tb.sv E:/Digital_Verf/Linkdin/AES/RTL/AES_Encrypt.sv E:/Digital_Verf/Linkdin/AES/RTL/AES_Encrypt_tb.sv E:/Digital_Verf/Linkdin/AES/RTL/AES_tb.sv E:/Digital_Verf/Linkdin/AES/RTL/addRoundKey.sv E:/Digital_Verf/Linkdin/AES/RTL/addRoundKey_tb.sv E:/Digital_Verf/Linkdin/AES/RTL/decryptRound.sv E:/Digital_Verf/Linkdin/AES/RTL/encryptRound.sv E:/Digital_Verf/Linkdin/AES/RTL/inverseMixColumns.sv E:/Digital_Verf/Linkdin/AES/RTL/inverseMixColumns_tb.sv E:/Digital_Verf/Linkdin/AES/RTL/inverseSbox.sv E:/Digital_Verf/Linkdin/AES/RTL/inverseShiftRows.sv E:/Digital_Verf/Linkdin/AES/RTL/inverseShiftRows_tb.sv E:/Digital_Verf/Linkdin/AES/RTL/inverseSubBytes.sv E:/Digital_Verf/Linkdin/AES/RTL/inverseSubBytes_tb.sv E:/Digital_Verf/Linkdin/AES/RTL/keyExpansion.sv E:/Digital_Verf/Linkdin/AES/RTL/keyExpansion_tb.sv E:/Digital_Verf/Linkdin/AES/RTL/mixColumns.sv E:/Digital_Verf/Linkdin/AES/RTL/mixColumns_tb.sv E:/Digital_Verf/Linkdin/AES/RTL/sbox.sv E:/Digital_Verf/Linkdin/AES/RTL/shiftRows.sv E:/Digital_Verf/Linkdin/AES/RTL/shiftRows_tb.sv E:/Digital_Verf/Linkdin/AES/RTL/subBytes.sv E:/Digital_Verf/Linkdin/AES/RTL/subBytes_tb.sv
vsim  -onfinish exit -pli C:/ProgramData/Anaconda3/lib/site-packages/cocotb/libs/cocotbvpi_modelsim.dll   sim_build/work.AES_Encrypt
onbreak resume
run -all
quit