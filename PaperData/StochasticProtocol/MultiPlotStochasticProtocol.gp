#GNUPLOT script to plot Stochastic Protocol ensemble results
#Steven Large
#April 10th 2017
set term postscript landscape color enhanced lw 2 "Times-Roman,22"
set output "StochasticProtocolMulti.ps"
set border lw 0.5
set style data l
set logscale y
set logscale x
set style circle radius graph 0.01

set format y "10^%T"
set format x "10^%T"

set xrange [1:100]
set yrange [100:40000]

unset key
set key off

POS = "at graph 0.15,0.85 font 'Helvetica'"

#TMARGIN = "set tmargin at screen 0.95; set bmargin at screen 0.575"
#BMARGIN = "set tmargin at screen 0.525; set bmargin at screen 0.15"
#LMARGIN = "set lmargin at screen 0.125; set rmargin at screen 0.525"
#RMARGIN = "set lmargin at screen 0.575; set rmargin at screen 0.975"

TLMARGIN = "set tmargin at screen 0.95; set bmargin at screen 0.6834; set lmargin at screen 0.125; set rmargin at screen 0.4083"
TMMARGIN = "set tmargin at screen 0.95; set bmargin at screen 0.6834; set lmargin at screen 0.4083; set rmargin at screen 0.6916"
TRMARGIN = "set tmargin at screen 0.95; set bmargin at screen 0.6834; set lmargin at screen 0.6916; set rmargin at screen 0.975"

MLMARGIN = "set tmargin at screen 0.6834; set bmargin at screen 0.4167; set lmargin at screen 0.125; set rmargin at screen 0.4083"
MMMARGIN = "set tmargin at screen 0.6834; set bmargin at screen 0.4167; set lmargin at screen 0.4083; set rmargin at screen 0.6916"
MRMARGIN = "set tmargin at screen 0.6834; set bmargin at screen 0.4167; set lmargin at screen 0.6916; set rmargin at screen 0.975"

BLMARGIN = "set tmargin at screen 0.4167; set bmargin at screen 0.15; set lmargin at screen 0.125; set rmargin at screen 0.4083"
BMMARGIN = "set tmargin at screen 0.4167; set bmargin at screen 0.15; set lmargin at screen 0.4083; set rmargin at screen 0.6916"
BRMARGIN = "set tmargin at screen 0.4167; set bmargin at screen 0.15; set lmargin at screen 0.6916; set rmargin at screen 0.975"

#NOYTICS = "set ytics 10000000; unset ylabel"
#NOXTICS = "set xtics 10000000; unset xlabel"

NOYTICS = "unset ytics; unset ylabel"
NOXTICS = "unset xtics; unset xlabel"

XTICS = "set xtics 10"
YTICS = "set ytics 10"

set label 3 "ProtocolTime (s)" at screen 0.45, 0.02
set label 4 "Work (units of k_BT)" at screen 0.01, 0.4 rotate by 90

set multiplot layout 3,3 rowsfirst

#set label 1 'a' @POS
#@TMARGIN; @LMARGIN
@TLMARGIN
@NOXTICS; @YTICS
plot "StochasticTheory/WorkStochastic_5_k1_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_5_k1_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticTheory/WorkTotalTheory_5_k1_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black", \
	 "StochasticProtocol/WorkTotal_L5_k1_a30.dat" with circles lc rgb "darkslateblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k1_a50.dat" with circles lc rgb "darkviolet" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k1_a70.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k1_a80.dat" with circles lc rgb "deepskyblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k1_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k1_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k1_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder	 


#set label 1 'b' @POS
#@TMARGIN; @RMARGIN
@TMMARGIN
@NOYTICS; @NOXTICS
plot "StochasticTheory/WorkStochastic_5_k8_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_5_k8_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticTheory/WorkTotalTheory_5_k8_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black", \
	 "StochasticProtocol/WorkTotal_L5_k8_a30.dat" with circles lc rgb "darkslateblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k8_a50.dat" with circles lc rgb "darkviolet" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k8_a70.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k8_a80.dat" with circles lc rgb "deepskyblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k8_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k8_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k8_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder	 


#set label 1 'c' @POS
#@TMARGIN; @RMARGIN
@TRMARGIN
@NOYTICS; @NOXTICS
plot "StochasticTheory/WorkStochastic_5_k128_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_5_k128_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticTheory/WorkTotalTheory_5_k128_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black", \
	 "StochasticProtocol/WorkTotal_L5_k128_a30.dat" with circles lc rgb "darkslateblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k128_a50.dat" with circles lc rgb "darkviolet" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k128_a70.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k128_a80.dat" with circles lc rgb "deepskyblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k128_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k128_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L5_k128_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder	 


#set label 1 'd' @POS
#@BMARGIN; @LMARGIN
@MLMARGIN
@NOXTICS; @YTICS
plot "StochasticTheory/WorkStochastic_20_k1_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_20_k1_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticTheory/WorkTotalTheory_20_k1_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black", \
	 "StochasticProtocol/WorkTotal_L20_k1_a30.dat" with circles lc rgb "darkslateblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k1_a50.dat" with circles lc rgb "darkviolet" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k1_a70.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k1_a80.dat" with circles lc rgb "deepskyblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k1_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k1_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k1_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder	 


#set label 1 'e' @POS
#@BMARGIN; @RMARGIN
@MMMARGIN
@NOYTICS; @NOXTICS
plot "StochasticTheory/WorkStochastic_20_k8_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_20_k8_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticTheory/WorkTotalTheory_20_k8_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black", \
	 "StochasticProtocol/WorkTotal_L20_k8_a30.dat" with circles lc rgb "darkslateblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k8_a50.dat" with circles lc rgb "darkviolet" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k8_a70.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k8_a80.dat" with circles lc rgb "deepskyblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k8_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k8_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k8_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder	 


#set label 1 'f' @POS
#@BMARGIN; @RMARGIN
@MRMARGIN
@NOYTICS; @NOXTICS
plot "StochasticTheory/WorkStochastic_20_k128_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_20_k128_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticTheory/WorkTotalTheory_20_k128_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black", \
	 "StochasticProtocol/WorkTotal_L20_k128_a30.dat" with circles lc rgb "darkslateblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k128_a50.dat" with circles lc rgb "darkviolet" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k128_a70.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k128_a80.dat" with circles lc rgb "deepskyblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k128_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k128_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L20_k128_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder	 	 


#set label 1 'g' @POS
#@BMARGIN; @RMARGIN
@BLMARGIN
@YTICS; @XTICS
plot "StochasticTheory/WorkStochastic_80_k1_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_80_k1_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticTheory/WorkTotalTheory_80_k1_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black", \
	 "StochasticProtocol/WorkTotal_L80_k1_a30.dat" with circles lc rgb "darkslateblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k1_a50.dat" with circles lc rgb "darkviolet" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k1_a70.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k1_a80.dat" with circles lc rgb "deepskyblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k1_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k1_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k1_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder	 


#set label 1 'h' @POS
#@BMARGIN; @RMARGIN
@BMMARGIN
@NOYTICS; @XTICS
plot "StochasticTheory/WorkStochastic_80_k8_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_80_k8_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticTheory/WorkTotalTheory_80_k8_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black", \
	 "StochasticProtocol/WorkTotal_L80_k8_a30.dat" with circles lc rgb "darkslateblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k8_a50.dat" with circles lc rgb "darkviolet" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k8_a70.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k8_a80.dat" with circles lc rgb "deepskyblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k8_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k8_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k8_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder


#set label 1 'i' @POS
#@BMARGIN; @RMARGIN
@BRMARGIN
@NOYTICS; @XTICS
plot "StochasticTheory/WorkStochastic_80_k128_Var_1.dat" with line lt 1 lw 1.5 lc rgb "blue", \
	 "StochasticTheory/WorkDeterministic_80_k128_Var_1.dat" with line lt 1 lw 1.5 lc rgb "red", \
	 "StochasticTheory/WorkTotalTheory_80_k128_Var_1.dat" with line lt 1 lw 1.5 lc rgb "black", \
	 "StochasticProtocol/WorkTotal_L80_k128_a30.dat" with circles lc rgb "darkslateblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k128_a50.dat" with circles lc rgb "darkviolet" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k128_a70.dat" with circles lc rgb "blue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k128_a80.dat" with circles lc rgb "deepskyblue" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k128_a90.dat" with circles lc rgb "green" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k128_a95.dat" with circles lc rgb "orange" fs transparent solid 0.5 noborder, \
	 "StochasticProtocol/WorkTotal_L80_k128_a99.dat" with circles lc rgb "red" fs transparent solid 0.5 noborder


unset multiplot

#set title "Constant Velocity Ensemble"
#set xlabel "Protocol Time, (s)"
#set ylabel "Work, (units of k_BT)"

pause -1 "Hit any key to continue..."