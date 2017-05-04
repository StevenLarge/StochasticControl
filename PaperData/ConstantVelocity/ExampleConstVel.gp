#GNUPLOT script to plot constant velocity ensemble results
#Steven Large
#April 10th 2017
set term postscript landscape color enhanced lw 2 "Times-Roman,22"
set output "constVelocityMulti.ps"
set border lw 0.5
set style data l
set logscale y
set logscale x
set style circle radius graph 0.01

set format y "10^%T"
set format x "10^%T"

set xrange [1:500]
set yrange [300:20000]

unset key
set key off

set title "Constant Velocity Ensemble"
set xlabel "Protocol Time, (s)"
set ylabel "Work, (units of k_BT)"
plot "WorkTotal_05.dat" with circles lc rgb "blue" fs transparent solid 0.75 noborder, \
	 "WorkTotal_1.dat" with circles lc rgb "purple" fs transparent solid 0.75 noborder, \
     "WorkTotal_2.dat" with circles lc rgb "green" fs transparent solid 0.75 noborder, \
     "WorkTotal_4.dat" with circles lc rgb "red" fs transparent solid 0.75 noborder, \
     "WorkTotalExact_50_k1_Var_1.dat" with line lt 1 lw 3 lc rgb "#7029FF", \
     "WorkTotalExact_50_k1_Var_0.5.dat" with line lt 1 lw 3 lc "#5252FF", \
     "WorkTotalExact_50_k1_Var_2.dat" with line lt 1 lw 3 lc "#66FF99", \
     "WorkTotalExact_50_k1_Var_4.dat" with line lt 1 lw 3 lc "#FF6699"

pause -1 "Hit any key to continue..."
