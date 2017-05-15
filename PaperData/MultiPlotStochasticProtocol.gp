#GNUPLOT script to plot Stochastic Protocol ensemble results
#Steven Large
#April 10th 2017
set term postscript landscape color enhanced lw 2 "Times-Roman,30"
set output "StochasticProtocolMulti.ps"
set border lw 0.5
set style data l
set logscale y
set logscale x
set style circle radius graph 0.01

set format y "10^%T"
set format x "10^%T"

set xrange [3:300]
set yrange [50:9000]

set terminal postscript enhanced

unset key
set key off

POS = "at graph 0.15,0.85 font 'Helvetica'"

#TMARGIN = "set tmargin at screen 0.95; set bmargin at screen 0.575"
#BMARGIN = "set tmargin at screen 0.525; set bmargin at screen 0.15"
#LMARGIN = "set lmargin at screen 0.125; set rmargin at screen 0.525"
#RMARGIN = "set lmargin at screen 0.575; set rmargin at screen 0.975"

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
TRMARGIN = "set tmargin at screen 0.97; set bmargin at screen 0.68; set lmargin at screen 0.666; set rmargin at screen 0.95"

MLMARGIN = "set tmargin at screen 0.68; set bmargin at screen 0.39; set lmargin at screen 0.1; set rmargin at screen 0.3833"
MMMARGIN = "set tmargin at screen 0.68; set bmargin at screen 0.39; set lmargin at screen 0.3833; set rmargin at screen 0.666"
MRMARGIN = "set tmargin at screen 0.68; set bmargin at screen 0.39; set lmargin at screen 0.666; set rmargin at screen 0.95"

BLMARGIN = "set tmargin at screen 0.39; set bmargin at screen 0.1; set lmargin at screen 0.1; set rmargin at screen 0.3833"
BMMARGIN = "set tmargin at screen 0.39; set bmargin at screen 0.1; set lmargin at screen 0.3833; set rmargin at screen 0.666"
BRMARGIN = "set tmargin at screen 0.39; set bmargin at screen 0.1; set lmargin at screen 0.666; set rmargin at screen 0.95"

#NOYTICS = "set ytics 10000000; unset ylabel"
#NOXTICS = "set xtics 10000000; unset xlabel"

NOYTICS = "unset ytics; unset ylabel"
NOXTICS = "unset xtics; unset xlabel"

XTICS = "set xtics 10"
YTICS = "set ytics 10"

set label 3 "Protocol Time, {/Symbol t} (s)" at screen 0.35, -0.05
#set label 3 "Protocol Time (s)" at screen 0.35, 0.01
set label 4 "Work (units of k_BT)" at screen -0.025, 0.30 rotate by 90

set label 5 "k = 4" at screen 0.2066, 1.01
set label 6 "k = 16" at screen 0.4899, 1.01
set label 7 "k = 64" at screen 0.7733, 1.01

set label 8 "<{/Symbol D}{/ Symbol l}> = 20" at screen 0.99, 0.9167 rotate by 270 font "Times-Roman, 26"
set label 9 "<{/Symbol D}{/Symbol l}> = 40" at screen 0.99, 0.6501 rotate by 270 font "Times-Roman, 26"
set label 10 "<{/Symbol D}{/Symbol l}> = 80" at screen 0.99, 0.3734 rotate by 270 font "Times-Roman, 26"

#set object circle at screen 0.1425, 0.92 size scr 0.005 fc rgb "black" fs transparent solid 0.5 noborder
#set object circle at screen 0.2062, 0.92 size scr 0.005 fc rgb "grey" fs transparent solid 0.5 noborder
#set object circle at screen 0.2701, 0.92 size scr 0.005 fc rgb "purple" fs transparent solid 0.5 noborder
#set object circle at screen 0.3338, 0.92 size scr 0.005 fc rgb "blue" fs transparent solid 0.5 noborder
#set object circle at screen 0.3976, 0.92 size scr 0.005 fc rgb "green" fs transparent solid 0.5 noborder
#set object circle at screen 0.4614, 0.92 size scr 0.005 fc rgb "orange" fs transparent solid 0.5 noborder
#set object circle at screen 0.5252, 0.92 size scr 0.005 fc rgb "red" fs transparent solid 0.5 noborder

#show object

#set arrow from screen 0.10,0.90 to screen 0.10,0.97 nohead lw 1 lc rgb "black"
#set arrow from screen 0.950,0.90 to screen 0.95,0.97 nohead lw 1 lc rgb "black"
#set arrow from screen 0.10,0.97 to screen 0.95,0.97 nohead lw 1 lc rgb "black"
#set arrow from screen 0.5677,0.90 to screen 0.5677,0.97 nohead lw 1 lc rgb "black"

#set arrow from screen 0.2701, 0.945 to screen 0.3976, 0.945 heads filled lw 2 lc rgb "black"

#set label 11 "Underdamped" at screen 0.4176, 0.945 font 'Times-Roman, 11'
#set label 12 "Overdamped" at screen 0.1735, 0.945 font 'Times-Roman, 11'

#set arrow from screen 0.5889, 0.92 to screen 0.6672, 0.92 nohead lt 1 lw 2.5 lc rgb "blue"
#set arrow from screen 0.7096, 0.92 to screen 0.8090, 0.92 nohead lt 1 lw 2.5 lc rgb "red"
#set arrow from screen 0.8516, 0.92 to screen 0.9297, 0.92 nohead lt 1 lw 2.5 lc rgb "black"

#set label 13 "Stochastic Work" at screen 0.5799,0.945 font 'Times-Roman, 11'
#set label 14 "Deterministic Work" at screen 0.6996,0.945 font 'Times-Roman, 11'
#set label 15 "Total Work" at screen 0.8566,0.945 font 'Times-Roman, 11'

set label 11 "Total Work" at screen 0.675, 0.330 font "Times-Roman, 14"
set label 12 "Deterministic Work" at screen 0.675, 0.280 font "Times-Roman, 14"
set label 13 "Stochastic Work" at screen 0.675, 0.230 font "Times-Roman, 14"

set arrow from screen 0.675, 0.31 to screen 0.725, 0.31 nohead lt 1 lw 2.5 lc rgb "black"
set arrow from screen 0.675, 0.26 to screen 0.725, 0.26 nohead lt 1 lw 2.5 lc rgb "red"
set arrow from screen 0.675, 0.21 to screen 0.725, 0.21 nohead lt 1 lw 2.5 lc rgb "blue"

set object circle at screen 0.76, 0.15 size scr 0.005 fc rgb "black" fs transparent solid 0.5 noborder
set object circle at screen 0.93, 0.15 size scr 0.005 fc rgb "red" fs transparent solid 0.5 noborder

set arrow from screen 0.775, 0.15 to screen 0.915,0.15 heads filled lw 1.5 lc rgb "black"

set label 14 "Overdamped" at screen 0.735, 0.125 font "Times-Roman, 12"
set label 15 "Underdamped" at screen 0.85, 0.125 font "times-Roman, 12"

#set arrow from screen 0.1366,0.97 to screen 0.3366,0.97 nohead lw 6 lc rgb "purple"
#show arrow

set multiplot layout 3,3 rowsfirst

#set label 1 'a' @POS
#@TMARGIN; @LMARGIN
@TLMARGIN
@NOXTICS; @YTICS
plot "StochasticTheory/WorkStochastic_20_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_20_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticProtocol2/WorkTotal_L20_k4_a30.dat" with circles lc rgb "black" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k4_a50.dat" with circles lc rgb "grey" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k4_a70.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k4_a80.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k4_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k4_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k4_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "StochasticTheory/WorkTotalTheory_20_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black"


#set label 1 'b' @POS
#@TMARGIN; @RMARGIN
@TMMARGIN
@NOYTICS; @NOXTICS
plot "StochasticTheory/WorkStochastic_20_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_20_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticProtocol2/WorkTotal_L20_k16_a30.dat" with circles lc rgb "black" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k16_a50.dat" with circles lc rgb "grey" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k16_a70.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder,\
	 "StochasticProtocol2/WorkTotal_L20_k16_a80.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k16_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k16_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder,\
	 "StochasticProtocol2/WorkTotal_L20_k16_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "StochasticTheory/WorkTotalTheory_20_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black" 


#set label 1 'c' @POS
#@TMARGIN; @RMARGIN
@TRMARGIN
@NOYTICS; @NOXTICS
plot "StochasticTheory/WorkStochastic_20_k64_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_20_k64_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticProtocol2/WorkTotal_L20_k64_a30.dat" with circles lc rgb "black" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k64_a50.dat" with circles lc rgb "grey" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k64_a70.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder,\
	 "StochasticProtocol2/WorkTotal_L20_k64_a80.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k64_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k64_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L20_k64_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "StochasticTheory/WorkTotalTheory_20_k64_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black"	 


#set label 1 'd' @POS
#@BMARGIN; @LMARGIN
@MLMARGIN
@NOXTICS; @YTICS
plot "StochasticTheory/WorkStochastic_40_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_40_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticProtocol2/WorkTotal_L40_k4_a30.dat" with circles lc rgb "black" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k4_a50.dat" with circles lc rgb "grey" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k4_a70.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k4_a80.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k4_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k4_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k4_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "StochasticTheory/WorkTotalTheory_40_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black"	 


#set label 1 'e' @POS
#@BMARGIN; @RMARGIN
@MMMARGIN
@NOYTICS; @NOXTICS
plot "StochasticTheory/WorkStochastic_40_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_40_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticProtocol2/WorkTotal_L40_k16_a30.dat" with circles lc rgb "black" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k16_a50.dat" with circles lc rgb "grey" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k16_a70.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k16_a80.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k16_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k16_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k16_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "StochasticTheory/WorkTotalTheory_40_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black"	 


#set label 1 'f' @POS
#@BMARGIN; @RMARGIN
@MRMARGIN
@NOYTICS; @NOXTICS
plot "StochasticTheory/WorkStochastic_40_k64_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_40_k64_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticProtocol2/WorkTotal_L40_k64_a30.dat" with circles lc rgb "black" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k64_a50.dat" with circles lc rgb "grey" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k64_a70.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k64_a80.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k64_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k64_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L40_k64_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "StochasticTheory/WorkTotalTheory_40_k64_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black"


#set label 1 'g' @POS
#@BMARGIN; @RMARGIN
@BLMARGIN
@YTICS; @XTICS
plot "StochasticTheory/WorkStochastic_80_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_80_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticProtocol2/WorkTotal_L80_k4_a30.dat" with circles lc rgb "black" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k4_a50.dat" with circles lc rgb "grey" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k4_a70.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k4_a80.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k4_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k4_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k4_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "StochasticTheory/WorkTotalTheory_80_k4_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black" 


#set label 1 'h' @POS
#@BMARGIN; @RMARGIN
@BMMARGIN
@NOYTICS; @XTICS
plot "StochasticTheory/WorkStochastic_80_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_80_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticProtocol2/WorkTotal_L80_k16_a30.dat" with circles lc rgb "black" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k16_a50.dat" with circles lc rgb "grey" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k16_a70.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k16_a80.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k16_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k16_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k16_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "StochasticTheory/WorkTotalTheory_80_k16_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black"


#set label 1 'i' @POS
#@BMARGIN; @RMARGIN
@BRMARGIN
@NOYTICS; @XTICS
plot "StochasticTheory/WorkStochastic_80_k64_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_80_k64_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticProtocol2/WorkTotal_L80_k64_a30.dat" with circles lc rgb "black" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k64_a50.dat" with circles lc rgb "grey" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k64_a70.dat" with circles lc rgb "purple" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k64_a80.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k64_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k64_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol2/WorkTotal_L80_k64_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder, \
	 "StochasticTheory/WorkTotalTheory_80_k64_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black"


unset multiplot

#set title "Constant Velocity Ensemble"
#set xlabel "Protocol Time, (s)"
#set ylabel "Work, (units of k_BT)"

pause -1 "Hit any key to continue..."