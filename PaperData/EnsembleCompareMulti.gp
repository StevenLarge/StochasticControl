#GNUPLOT script to compare Stochastic Protocols and Constant Velocity Ensemble results
#3x1 multi-panel plot
#Steven Large
#April 10th 2017
set term postscript landscape color enhanced lw 2 "Times-Roman,30"
set output "EnsembleCompareMulti.ps"
set border lw 0.5
set style data l
set logscale y
set logscale x
set style circle radius graph 0.01

set format y "10^%T"
set format x "10^%T"

set xrange [3:200]
set yrange [150:10000]

set terminal postscript enhanced

unset key
set key off

POS = "at graph 0.15,0.85 font 'Helvetica'"

#TLMARGIN = "set tmargin at screen 0.95; set bmargin at screen 0.6834; set lmargin at screen 0.100; set rmargin at screen 0.3833"
#TMMARGIN = "set tmargin at screen 0.95; set bmargin at screen 0.6834; set lmargin at screen 0.3833; set rmargin at screen 0.6666"
#TRMARGIN = "set tmargin at screen 0.95; set bmargin at screen 0.6834; set lmargin at screen 0.6666; set rmargin at screen 0.950"

#MLMARGIN = "set tmargin at screen 0.6834; set bmargin at screen 0.4167; set lmargin at screen 0.100; set rmargin at screen 0.3833"
#MMMARGIN = "set tmargin at screen 0.6834; set bmargin at screen 0.4167; set lmargin at screen 0.3833; set rmargin at screen 0.6666"
#MRMARGIN = "set tmargin at screen 0.6834; set bmargin at screen 0.4167; set lmargin at screen 0.6666; set rmargin at screen 0.950"

#BLMARGIN = "set tmargin at screen 0.4167; set bmargin at screen 0.15; set lmargin at screen 0.100; set rmargin at screen 0.3833"
#BMMARGIN = "set tmargin at screen 0.4167; set bmargin at screen 0.15; set lmargin at screen 0.3833; set rmargin at screen 0.6666"
#BRMARGIN = "set tmargin at screen 0.4167; set bmargin at screen 0.15; set lmargin at screen 0.6666; set rmargin at screen 0.950"

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

NOYTICS = "unset ytics; unset ylabel"
NOXTICS = "unset xtics; unset xlabel"

XTICS = "set xtics 10"
YTICS = "set ytics 10"

set label 3 "ProtocolTime, {/Symbol t} (s)" at screen 0.35, -0.05
set label 4 "Work (units of k_BT)" at screen -0.025, 0.3 rotate by 90

set label 5 "k = 4" at screen 0.2066, 1.01
set label 6 "k = 16" at screen 0.4899, 1.01
set label 7 "k = 64" at screen 0.7733, 1.01

set label 8 "<{/Symbol D}{/ Symbol l}> = 20" at screen 0.99, 0.9167 rotate by 270 font "Times-Roman, 26"
set label 9 "<{/Symbol D}{/Symbol l}> = 40" at screen 0.99, 0.6501 rotate by 270 font "Times-Roman, 26"
set label 10 "<{/Symbol D}{/Symbol l}> = 80" at screen 0.99, 0.3734 rotate by 270 font "Times-Roman, 26"

#set arrow from screen 0.10,0.90 to screen 0.10,0.97 nohead lw 1 lc rgb "black"
#set arrow from screen 0.10,0.97 to screen 0.95,0.97 nohead lw 1 lc rgb "black"
#set arrow from screen 0.95,0.90 to screen 0.95,0.97 nohead lw 1 lc rgb "black"

#set object circle at screen 0.15,0.935 size scr 0.01 fc rgb "red" fs transparent solid 0.5 noborder
#set label 11 "Stochastic Ensemble" at screen 0.17,0.945 font "Times-Roman, 14"
#set label 12 "(Underdamped)" at screen 0.18,0.925 font "Times-Roman, 14"

#set object circle at screen 0.35,0.935 size scr 0.01 fc rgb "blue" fs transparent solid 0.5 noborder
#set label 13 "Constant Velocity Ensemble" at screen 0.37,0.935 font "Times-Roman, 14"

#set arrow from screen 0.6,0.92 to screen 0.725,0.92 nohead lw 3 lc rgb "black"
#set label 14 "Theoretical Prediction" at screen 0.595,0.94 font "Times-Roman, 14"

#set arrow from screen 0.8,0.92 to screen 0.925,0.92 nohead ls 'dashed' lw 6 lc rgb "purple"
#set label 15 "Lower Bound" at screen 0.81,0.94 font "Times-Roman, 11"

set arrow from screen 0.680, 0.17 to screen 0.775, 0.17 nohead lt 1 lw 2.5 lc rgb "black"
set arrow from screen 0.680, 0.12 to screen 0.775, 0.12 nohead ls 'dashed' lw 6 lc rgb "purple"

set label 11 "Theoretical Prediction" at screen 0.675, 0.19 font "Times-Roman,14"
set label 12 "Lower Bound" at screen 0.675, 0.14 font "Times-Roman,14"

set object circle at screen 0.406, 0.18 size scr 0.01 fc rgb "red" fs transparent solid 0.5 noborder
set object circle at screen 0.406, 0.13 size scr 0.01 fc rgb "blue" fs transparent solid 0.5 noborder

set label 13 "Stochastic Ensemble" at screen 0.421,0.18 font "Times-Roman,14"
set label 14 "Constant Velocity Ensemble" at screen 0.421, 0.13 font "Times-Roman,14"

set multiplot layout 3,3 rowsfirst

@TLMARGIN
@YTICS; @NOXTICS
plot "ConstantVelocity/WorkTheory/WorkTotalExact_20_k4_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue" ,\
	 "StochasticTheory/WorkTotalTheory_20_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black",\
	 "StochasticProtocol2/WorkTotal_L20_k4_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "ConstantVelocity/SimulationData/WorkTotal_L20_k4_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder

@TMMARGIN
@NOYTICS; @NOXTICS
plot "ConstantVelocity/WorkTheory/WorkTotalExact_20_k16_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue" ,\
	 "StochasticTheory/WorkTotalTheory_20_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black", \
	 "StochasticProtocol2/WorkTotal_L20_k16_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "ConstantVelocity/SimulationData/WorkTotal_L20_k16_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder

@TRMARGIN
@NOYTICS; @NOXTICS
plot "ConstantVelocity/WorkTheory/WorkLowerBound_20_Var_1.dat" with line lt "dashed" lw 6.0 lc rgb "purple", \
	 "ConstantVelocity/WorkTheory/WorkTotalExact_20_k64_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue" ,\
	 "StochasticTheory/WorkTotalTheory_20_k64_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black", \
	 "StochasticProtocol2/WorkTotal_L20_k64_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "ConstantVelocityK64/WorkTotal_L20_k64_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder

@MLMARGIN
@YTICS; @NOXTICS
plot "ConstantVelocity/WorkTheory/WorkTotalExact_40_k4_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue" ,\
	 "StochasticTheory/WorkTotalTheory_40_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black" , \
	 "StochasticProtocol2/WorkTotal_L40_k4_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "ConstantVelocity/SimulationData/WorkTotal_L40_k4_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder

@MMMARGIN
@NOYTICS; @NOXTICS
plot "ConstantVelocity/WorkTheory/WorkTotalExact_40_k16_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue" ,\
	 "StochasticTheory/WorkTotalTheory_40_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black" , \
	 "StochasticProtocol2/WorkTotal_L40_k16_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "ConstantVelocity/SimulationData/WorkTotal_L40_k16_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder

@MRMARGIN
@NOYTICS; @NOXTICS
plot "ConstantVelocity/WorkTheory/WorkLowerBound_40_Var_1.dat" with line lt "dashed" lw 6.0 lc rgb "purple", \
	 "ConstantVelocity/WorkTheory/WorkTotalExact_40_k64_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue" ,\
	 "StochasticTheory/WorkTotalTheory_40_k64_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black", \
	 "StochasticProtocol2/WorkTotal_L40_k64_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "ConstantVelocityK64/WorkTotal_L40_k64_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder 

@BLMARGIN
@YTICS; @XTICS
plot "ConstantVelocity/WorkTheory/WorkTotalExact_80_k4_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue" ,\
	 "StochasticTheory/WorkTotalTheory_80_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black", \
	 "StochasticProtocol2/WorkTotal_L80_k4_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "ConstantVelocity/SimulationData/WorkTotal_L80_k4_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder

@BMMARGIN
@NOYTICS; @XTICS
plot "ConstantVelocity/WorkTheory/WorkTotalExact_80_k16_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue" ,\
	 "StochasticTheory/WorkTotalTheory_80_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black" ,\
	 "StochasticProtocol2/WorkTotal_L80_k16_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "ConstantVelocity/SimulationData/WorkTotal_L80_k16_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder

@BRMARGIN
@NOYTICS; @XTICS
plot "ConstantVelocity/WorkTheory/WorkLowerBound_80_Var_1.dat" with line lt "dashed" lw 6.0 lc rgb "purple", \
	 "ConstantVelocity/WorkTheory/WorkTotalExact_80_k64_Var_1.dat" with line lt "dashed" lw 1.5 lc rgb "blue" ,\
	 "StochasticTheory/WorkTotalTheory_80_k64_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black" ,\
	 "StochasticProtocol2/WorkTotal_L80_k64_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "ConstantVelocityK64/WorkTotal_L80_k64_1.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder	 

unset multiplot

pause -1 "Hit any key to continue..."
