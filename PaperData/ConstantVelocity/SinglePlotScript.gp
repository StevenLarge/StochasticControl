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

set xrange [3:300]
set yrange [50:9000]

unset key
set key off

set xlabel "Protocol Time, (s)"
set ylabel "Work, (units of k_BT)"
plot ConstantVelocity/


pause -1 "Hit any key to continue..."
