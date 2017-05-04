#GNUPLOT script to plot constant velocity ensemble results
#Steven Large
#April 10th 2017
set term postscript landscape color enhanced lw 2 "Times-Roman,26"
set output "constVelocityMulti.ps"
set border lw 0.5
set style data l
set logscale y
set logscale x
set style circle radius graph 0.01

set format y "10^%T"
set format x "10^%T"

set xrange [1:500]
set yrange [10:60000]

unset key
set key off

POS = "at graph 0.15,0.85 font 'Helvetica'"

#TMARGIN = "set tmargin at screen 0.95; set bmargin at screen 0.575"
#BMARGIN = "set tmargin at screen 0.525; set bmargin at screen 0.15"
#LMARGIN = "set lmargin at screen 0.125; set rmargin at screen 0.525"
#RMARGIN = "set lmargin at screen 0.575; set rmargin at screen 0.975"

#TLMARGIN = "set tmargin at screen 0.95; set bmargin at screen 0.6834; set lmargin at screen 0.125; set rmargin at screen 0.4083"
#TMMARGIN = "set tmargin at screen 0.95; set bmargin at screen 0.6834; set lmargin at screen 0.4083; set rmargin at screen 0.6916"
#TRMARGIN = "set tmargin at screen 0.95; set bmargin at screen 0.6834; set lmargin at screen 0.6916; set rmargin at screen 0.975"

#MLMARGIN = "set tmargin at screen 0.6834; set bmargin at screen 0.4167; set lmargin at screen 0.125; set rmargin at screen 0.4083"
#MMMARGIN = "set tmargin at screen 0.6834; set bmargin at screen 0.4167; set lmargin at screen 0.4083; set rmargin at screen 0.6916"
#MRMARGIN = "set tmargin at screen 0.6834; set bmargin at screen 0.4167; set lmargin at screen 0.6916; set rmargin at screen 0.975"

#BLMARGIN = "set tmargin at screen 0.4167; set bmargin at screen 0.15; set lmargin at screen 0.125; set rmargin at screen 0.4083"
#BMMARGIN = "set tmargin at screen 0.4167; set bmargin at screen 0.15; set lmargin at screen 0.4083; set rmargin at screen 0.6916"
#BRMARGIN = "set tmargin at screen 0.4167; set bmargin at screen 0.15; set lmargin at screen 0.6916; set rmargin at screen 0.975"

#TLMARGIN = "set tmargin at screen 0.90; set bmargin at screen 0.6334; set lmargin at screen 0.100; set rmargin at screen 0.3833"
#TMMARGIN = "set tmargin at screen 0.90; set bmargin at screen 0.6334; set lmargin at screen 0.3833; set rmargin at screen 0.6666"
#TRMARGIN = "set tmargin at screen 0.90; set bmargin at screen 0.6334; set lmargin at screen 0.6666; set rmargin at screen 0.950"

#MLMARGIN = "set tmargin at screen 0.6334; set bmargin at screen 0.3667; set lmargin at screen 0.100; set rmargin at screen 0.3833"
#MMMARGIN = "set tmargin at screen 0.6334; set bmargin at screen 0.3667; set lmargin at screen 0.3833; set rmargin at screen 0.6666"
#MRMARGIN = "set tmargin at screen 0.6334; set bmargin at screen 0.3667; set lmargin at screen 0.6666; set rmargin at screen 0.950"

#BLMARGIN = "set tmargin at screen 0.3667; set bmargin at screen 0.1; set lmargin at screen 0.100; set rmargin at screen 0.3833"
#BMMARGIN = "set tmargin at screen 0.3667; set bmargin at screen 0.1; set lmargin at screen 0.3833; set rmargin at screen 0.6666"
#BRMARGIN = "set tmargin at screen 0.3667; set bmargin at screen 0.1; set lmargin at screen 0.6666; set rmargin at screen 0.950"

TLMARGIN = "set tmargin at screen 0.97; set bmargin at screen 0.68; set lmargin at screen 0.1; set rmargin at screen 0.3833"
TMMARGIN = "set tmargin at screen 0.97; set bmargin at screen 0.68; set lmargin at screen 0.3833; set rmargin at screen 0.666"
TRMARGIN = "set tmargin at screen 0.97; set bmargin at screen 0.68; set lmargin at screen 0.666; set rmargin at screen 0.97"

MLMARGIN = "set tmargin at screen 0.68; set bmargin at screen 0.39; set lmargin at screen 0.1; set rmargin at screen 0.3833"
MMMARGIN = "set tmargin at screen 0.68; set bmargin at screen 0.39; set lmargin at screen 0.3833; set rmargin at screen 0.666"
MRMARGIN = "set tmargin at screen 0.68; set bmargin at screen 0.39; set lmargin at screen 0.666; set rmargin at screen 0.97"

BLMARGIN = "set tmargin at screen 0.39; set bmargin at screen 0.1; set lmargin at screen 0.1; set rmargin at screen 0.3833"
BMMARGIN = "set tmargin at screen 0.39; set bmargin at screen 0.1; set lmargin at screen 0.3833; set rmargin at screen 0.666"
BRMARGIN = "set tmargin at screen 0.39; set bmargin at screen 0.1; set lmargin at screen 0.666; set rmargin at screen 0.97"

#NOYTICS = "set ytics 10000000; unset ylabel"
#NOXTICS = "set xtics 10000000; unset xlabel"

NOYTICS = "unset ytics; unset ylabel"
NOXTICS = "unset xtics; unset xlabel"

XTICS = "set xtics 10"
YTICS = "set ytics 10"

set label 3 "ProtocolTime (s)" at screen 0.40, -0.01
set label 4 "Work (units of k_BT)" at screen -0.01, 0.35 rotate by 90

set label 5 "k = 1" at screen 0.2166, 1.01
set label 6 "k = 4" at screen 0.4999, 1.01
set label 7 "k = 16" at screen 0.7833, 1.01

set label 8 "<{/Symbol D}{/ Symbol l}> = 20" at screen 0.99, 0.9167 rotate by 270
set label 9 "<{/Symbol D}{/Symbol l}> = 40" at screen 0.99, 0.6501 rotate by 270
set label 10 "<{/Symbol D}{/Symbol l}> = 80" at screen 0.99, 0.3734 rotate by 270

#set arrow from screen 0.1425,0.92 to screen 0.2275,0.92 nohead lw 5 lc rgb "purple"
#set arrow from screen 0.3125,0.92 to screen 0.3975,0.92 nohead lw 5 lc rgb "blue"
#set arrow from screen 0.4825,0.92 to screen 0.5675,0.92 nohead lw 5 lc rgb "green"
#set arrow from screen 0.6525,0.92 to screen 0.7375,0.92 nohead lw 5 lc rgb "orange"
#set arrow from screen 0.8225,0.92 to screen 0.9075,0.92 nohead lw 5 lc rgb "red"

#set arrow from screen 0.100, 0.98 to screen 0.950, 0.975 nohead lw 1 lc rgb "black"
#set arrow from screen 0.100, 0.975 to screen 0.100, 0.90 nohead lw 1 lc rgb "black"
#set arrow from screen 0.950, 0.975 to screen 0.950, 0.90 nohead lw 1 lc rgb "black"

#set label 11 "{/Symbol s}^2 = 0.5" at screen 0.1625, 0.95 font "Symbol, 14"
#set label 12 "{/Symbol s}^2 = 1" at screen 0.3325, 0.95 font "Symbol, 14"
#set label 13 "{/Symbol s}^2 = 2" at screen 0.5025, 0.95 font "Symbol, 14"
#set label 14 "{/Symbol s}^2 = 4" at screen 0.6725, 0.95 font "Symbol, 14"
#set label 15 "{/Symbol s}^2 = 8" at screen 0.8425, 0.95 font "Symbol, 14"

set label 11 "{/Symbol s}^2" at screen 0.730, 0.255 font "Symbol, 16"

set arrow from screen 0.7, 0.235 to screen 0.77, 0.235 nohead lw 1.5 lc rgb "black"
set arrow from screen 0.735, 0.235 to screen 0.735, 0.12 nohead lw 1.5 lc rgb "black"

set arrow from screen 0.740, 0.22 to screen 0.760, 0.22 nohead lw 3 lc rgb "purple"
set arrow from screen 0.740, 0.20 to screen 0.760, 0.20 nohead lw 3 lc rgb "blue"
set arrow from screen 0.740, 0.18 to screen 0.760, 0.18 nohead lw 3 lc rgb "green"
set arrow from screen 0.740, 0.16 to screen 0.760, 0.16 nohead lw 3 lc rgb "orange"
set arrow from screen 0.740, 0.14 to screen 0.760, 0.14 nohead lw 3 lc rgb "red"

set label 12 "0.5" at screen 0.71, 0.22 font "Symbol, 12"
set label 13 "1" at screen 0.715, 0.20 font "Symbol, 12"
set label 14 "2" at screen 0.715, 0.18 font "Symbol, 12"
set label 15 "4" at screen 0.715, 0.16 font "Symbol, 12"
set label 16 "8" at screen 0.715, 0.14 font "Symbol, 12"

set object circle at screen 0.42, 0.20 size scr 0.007 fc rgb "red" fs transparent solid 0.5 noborder
set arrow from screen 0.41, 0.17 to screen 0.43, 0.17 nohead lt 1 lw 3 lc rgb "red"
set arrow from screen 0.41, 0.14 to screen 0.43, 0.14 nohead lt 'dashed' lw 3 lc rgb "red"

set label 17 "Simulation" at screen 0.44, 0.20 font "Times-Roman,12"
set label 18 "Theoretical Prediction" at screen 0.44, 0.17 font "Times-Roman,12"
set label 19 "Exact Solution" at screen 0.44, 0.14 font "Times-Roman,12"

show arrow

set multiplot layout 3,3 rowsfirst

#set label 1 'a' @POS
#@TMARGIN; @LMARGIN
@TLMARGIN
@NOXTICS; @YTICS
plot "SimulationData/WorkTotal_L5_k1_05.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L5_k1_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L5_k1_2.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L5_k1_4.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L5_k1_8.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "WorkTheory/WorkTotalExact_5_k1_Var_0.5.dat" with line lt "dashed" lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalExact_5_k1_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalExact_5_k1_Var_2.dat" with line lt "dashed" lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalExact_5_k1_Var_4.dat" with line lt "dashed" lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalExact_5_k1_Var_8.dat" with line lt "dashed" lw 1.5 lc rgb "red", \
	 "WorkTheory/WorkTotalTheory_5_k1_Var_0.5.dat" with line lt 1 lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalTheory_5_k1_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalTheory_5_k1_Var_2.dat" with line lt 1 lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalTheory_5_k1_Var_4.dat" with line lt 1 lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalTheory_5_k1_Var_8.dat" with line lt 1 lw 1.5 lc rgb "red"

#set label 1 'b' @POS
#@TMARGIN; @RMARGIN
@TMMARGIN
@NOYTICS; @NOXTICS
plot "SimulationData/WorkTotal_L5_k4_05.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L5_k4_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L5_k4_2.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L5_k4_4.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L5_k4_8.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "WorkTheory/WorkTotalExact_5_k4_Var_0.5.dat" with line lt "dashed" lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalExact_5_k4_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalExact_5_k4_Var_2.dat" with line lt "dashed" lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalExact_5_k4_Var_4.dat" with line lt "dashed" lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalExact_5_k4_Var_8.dat" with line lt "dashed" lw 1.5 lc rgb "red" ,\
	 "WorkTheory/WorkTotalTheory_5_k4_Var_0.5.dat" with line lt 1 lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalTheory_5_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalTheory_5_k4_Var_2.dat" with line lt 1 lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalTheory_5_k4_Var_4.dat" with line lt 1 lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalTheory_5_k4_Var_8.dat" with line lt 1 lw 1.5 lc rgb "red"


#set label 1 'c' @POS
#@TMARGIN; @RMARGIN
@TRMARGIN
@NOYTICS; @NOXTICS
plot "SimulationData/WorkTotal_L5_k16_05.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L5_k16_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L5_k16_2.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L5_k16_4.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L5_k16_8.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "WorkTheory/WorkTotalExact_5_k16_Var_0.5.dat" with line lt "dashed" lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalExact_5_k16_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalExact_5_k16_Var_2.dat" with line lt "dashed" lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalExact_5_k16_Var_4.dat" with line lt "dashed" lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalExact_5_k16_Var_8.dat" with line lt "dashed" lw 1.5 lc rgb "red", \
	 "WorkTheory/WorkTotalTheory_5_k16_Var_0.5.dat" with line lt 1 lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalTheory_5_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalTheory_5_k16_Var_2.dat" with line lt 1 lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalTheory_5_k16_Var_4.dat" with line lt 1 lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalTheory_5_k16_Var_8.dat" with line lt 1 lw 1.5 lc rgb "red"

#set label 1 'd' @POS
#@BMARGIN; @LMARGIN
@MLMARGIN
@NOXTICS; @YTICS
plot "SimulationData/WorkTotal_L20_k1_05.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L20_k1_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L20_k1_2.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L20_k1_4.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L20_k1_8.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder,\
	 "WorkTheory/WorkTotalExact_20_k1_Var_0.5.dat" with line lt "dashed" lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalExact_20_k1_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalExact_20_k1_Var_2.dat" with line lt "dashed" lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalExact_20_k1_Var_4.dat" with line lt "dashed" lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalExact_20_k1_Var_8.dat" with line lt "dashed" lw 1.5 lc rgb "red", \
	 "WorkTheory/WorkTotalTheory_20_k1_Var_0.5.dat" with line lt 1 lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalTheory_20_k1_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalTheory_20_k1_Var_2.dat" with line lt 1 lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalTheory_20_k1_Var_4.dat" with line lt 1 lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalTheory_20_k1_Var_8.dat" with line lt 1 lw 1.5 lc rgb "red"

#set label 1 'e' @POS
#@BMARGIN; @RMARGIN
@MMMARGIN
@NOYTICS; @NOXTICS
plot "SimulationData/WorkTotal_L20_k4_05.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L20_k4_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L20_k4_2.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L20_k4_4.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L20_k4_8.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder,\
	 "WorkTheory/WorkTotalExact_20_k4_Var_0.5.dat" with line lt "dashed" lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalExact_20_k4_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalExact_20_k4_Var_2.dat" with line lt "dashed" lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalExact_20_k4_Var_4.dat" with line lt "dashed" lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalExact_20_k4_Var_8.dat" with line lt "dashed" lw 1.5 lc rgb "red", \
	 "WorkTheory/WorkTotalTheory_20_k4_Var_0.5.dat" with line lt 1 lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalTheory_20_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalTheory_20_k4_Var_2.dat" with line lt 1 lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalTheory_20_k4_Var_4.dat" with line lt 1 lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalTheory_20_k4_Var_8.dat" with line lt 1 lw 1.5 lc rgb "red"


#set label 1 'f' @POS
#@BMARGIN; @RMARGIN
@MRMARGIN
@NOYTICS; @NOXTICS
plot "SimulationData/WorkTotal_L20_k16_05.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L20_k16_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L20_k16_2.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L20_k16_4.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L20_k16_8.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "WorkTheory/WorkTotalExact_20_k16_Var_0.5.dat" with line lt "dashed" lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalExact_20_k16_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalExact_20_k16_Var_2.dat" with line lt "dashed" lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalExact_20_k16_Var_4.dat" with line lt "dashed" lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalExact_20_k16_Var_8.dat" with line lt "dashed" lw 1.5 lc rgb "red", \
	 "WorkTheory/WorkTotalTheory_20_k16_Var_0.5.dat" with line lt 1 lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalTheory_20_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalTheory_20_k16_Var_2.dat" with line lt 1 lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalTheory_20_k16_Var_4.dat" with line lt 1 lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalTheory_20_k16_Var_8.dat" with line lt 1 lw 1.5 lc rgb "red"	 


#set label 1 'g' @POS
#@BMARGIN; @RMARGIN
@BLMARGIN
@YTICS; @XTICS
plot "SimulationData/WorkTotal_L80_k1_05.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L80_k1_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L80_k1_2.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L80_k1_4.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L80_k1_8.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "WorkTheory/WorkTotalExact_80_k1_Var_0.5.dat" with line lt "dashed" lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalExact_80_k1_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalExact_80_k1_Var_2.dat" with line lt "dashed" lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalExact_80_k1_Var_4.dat" with line lt "dashed" lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalExact_80_k1_Var_8.dat" with line lt "dashed" lw 1.5 lc rgb "red",\
	 "WorkTheory/WorkTotalTheory_80_k1_Var_0.5.dat" with line lt 1 lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalTheory_80_k1_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalTheory_80_k1_Var_2.dat" with line lt 1 lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalTheory_80_k1_Var_4.dat" with line lt 1 lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalTheory_80_k1_Var_8.dat" with line lt 1 lw 1.5 lc rgb "red"	 


#set label 1 'h' @POS
#@BMARGIN; @RMARGIN
@BMMARGIN
@NOYTICS; @XTICS
plot "SimulationData/WorkTotal_L80_k4_05.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L80_k4_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L80_k4_2.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L80_k4_4.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L80_k4_8.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "WorkTheory/WorkTotalExact_80_k4_Var_0.5.dat" with line lt "dashed" lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalExact_80_k4_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalExact_80_k4_Var_2.dat" with line lt "dashed" lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalExact_80_k4_Var_4.dat" with line lt "dashed" lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalExact_80_k4_Var_8.dat" with line lt "dashed" lw 1.5 lc rgb "red", \
	 "WorkTheory/WorkTotalTheory_80_k4_Var_0.5.dat" with line lt 1 lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalTheory_80_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalTheory_80_k4_Var_2.dat" with line lt 1 lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalTheory_80_k4_Var_4.dat" with line lt 1 lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalTheory_80_k4_Var_8.dat" with line lt 1 lw 1.5 lc rgb "red"	 	 


#set label 1 'i' @POS
#@BMARGIN; @RMARGIN
@BRMARGIN
@NOYTICS; @XTICS
plot "SimulationData/WorkTotal_L80_k16_05.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L80_k16_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L80_k16_2.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L80_k16_4.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "SimulationData/WorkTotal_L80_k16_8.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "WorkTheory/WorkTotalExact_80_k16_Var_0.5.dat" with line lt "dashed" lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalExact_80_k16_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalExact_80_k16_Var_2.dat" with line lt "dashed" lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalExact_80_k16_Var_4.dat" with line lt "dashed" lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalExact_80_k16_Var_8.dat" with line lt "dashed" lw 1.5 lc rgb "red", \
	 "WorkTheory/WorkTotalTheory_80_k16_Var_0.5.dat" with line lt 1 lw 1.5 lc rgb "purple", \
	 "WorkTheory/WorkTotalTheory_80_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "WorkTheory/WorkTotalTheory_80_k16_Var_2.dat" with line lt 1 lw 1.5 lc rgb "green", \
	 "WorkTheory/WorkTotalTheory_80_k16_Var_4.dat" with line lt 1 lw 1.5 lc rgb "orange", \
	 "WorkTheory/WorkTotalTheory_80_k16_Var_8.dat" with line lt 1 lw 1.5 lc rgb "red"


unset multiplot

#plot "WorkTotal_05.dat" with circles lc rgb "blue" fs transparent solid 0.75 noborder, \
#	 "WorkTotal_1.dat" with circles lc rgb "purple" fs transparent solid 0.75 noborder, \
#     "WorkTotal_2.dat" with circles lc rgb "green" fs transparent solid 0.75 noborder, \
#     "WorkTotal_4.dat" with circles lc rgb "red" fs transparent solid 0.75 noborder, \
#     "WorkTotalExact_50_k1_Var_1.dat" with line lt 1 lw 3 lc rgb "#7029FF", \
#     "WorkTotalExact_50_k1_Var_0.5.dat" with line lt 1 lw 3 lc "#5252FF", \
#     "WorkTotalExact_50_k1_Var_2.dat" with line lt 1 lw 3 lc "#66FF99", \
#     "WorkTotalExact_50_k1_Var_4.dat" with line lt 1 lw 3 lc "#FF6699"

#set title "Constant Velocity Ensemble"
#set xlabel "Protocol Time, (s)"
#set ylabel "Work, (units of k_BT)"

pause -1 "Hit any key to continue..."