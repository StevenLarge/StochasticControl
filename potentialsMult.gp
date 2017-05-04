#! /opt/local/bin/gnuplot
set term postscript landscape color enhanced lw 2 "Times-Roman,22"
set output "potentialsMult.ps"
set border lw 0.2
set border 0
# set pointsize 0.25
set style data l
BIG_NUM = 200000000000.
set samples 10000
# unset key
# set logscale y

set xrange [-2.5:2.5]

X1 = -0.09
X2 = 0.23
X3 = 0.405
X4 = 0.58
X5 = 0.755
Y1 = -0.045
Y2 = 0.17
Y3 = 0.335
Y4 = 0.50
Y5 = 0.665

X_TICS = 20
X_MIN = -23
X_MAX = 23
Y_MIN = -1
Y_MIN_1 = 0
Y_MIN_2 = 0
Y_MIN_3 = 0
Y_MIN_4 = 0
Y_MIN_5 = 0
Y_MAX_1 = 40
Y_MAX_2 = 40
Y_MAX_3 = 40
Y_MAX_4 = 40
Y_MAX_5 = 40
Y_MAX = 14

WIDTH = 0.235
LEFT_WIDTH = WIDTH + 0.155
RIGHT_WIDTH = WIDTH + 0.06
HEIGHT = 0.24
TOP_HEIGHT = HEIGHT + 0.065
BOTTOM_HEIGHT = HEIGHT + 0.05

LW_AN = 2.
LW_NUM = 3.
LW_EX = 3.

kS = 50.
dXEval = 0.00000632
halfDXSample = 0.01
B = 1.
G(kS,kW) = kS*kW/(kS+kW)
nPS = 3165
xShift = 0.
mult = 1.
delXM = 0.02
delXSpring = 1.0666666e-06
# invFiFactor = delXM*delXSpring
trueFiFactor = 1. / delXSpring
fudgeFactor = 2.
fiFactor = fudgeFactor * trueFiFactor
# dt = 0.00000991
vel = 10.
FUDGE = 1.
FUDGE2 = 1.
delT = 0.08701/10.
diffCoef = 500.

# set format y "10^{%L}"

set style line 1 lt 1 lc rgb "purple" lw LW_EX pt 7 dashtype 3
set style line 2 lt 1 lc rgb "#80D200" lw LW_EX pt 7 dashtype 3
set style line 3 lt 1 lc rgb "black" lw LW_EX pt 7
set style line 4 lt 1 lc rgb "#80D200" lw LW_EX pt 7
set style line 5 lt 1 lc rgb "purple" lw LW_EX pt 7

# set origin -0.13,-0.05
set multiplot
set origin -0.06,-0.1
set size 1.15,1.2
set key above title 'Trap minimum  {/Times-Roman-Italic x}_s (nm)'
set key horizontal
unset xtics
unset ytics
set xlabel 'Particle position  {/Times-Roman-Italic x} (nm)'
set ylabel 'Total potential  {/Times-Roman-Italic E}({/Times-Roman-Italic x,x}_s) (units of {/Times-Roman-Italic k}_B{/Times-Roman-Italic T})'
plot [X_MIN:X_MAX] [Y_MIN_1:Y_MAX_1] BIG_NUM ls 1 title '-10', BIG_NUM ls 2 title '-5', BIG_NUM ls 3 title '0', BIG_NUM ls 4 title '5', BIG_NUM ls 5 title '10'

set size LEFT_WIDTH,TOP_HEIGHT
set origin X1,Y5
set ytics 10. nomirror
unset xtics
unset xlabel
unset key
unset ylabel
set title '0.025'
# font "Times-Roman,20"
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW21.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW21.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW21.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW21.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW21.4_o0' using ($1*10):2 ls 5

set size LEFT_WIDTH,HEIGHT
# set ytics 100000. nomirror
unset title
set origin X1,Y4
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW11.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW11.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW11.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW11.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW11.4_o0' using ($1*10):2 ls 5

set origin X1,Y3
# set ytics 1000. nomirror
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW6.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW6.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW6.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW6.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW6.4_o0' using ($1*10):2 ls 5

set origin X1,Y2
# set ytics 100. nomirror
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW3.9_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW3.9_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW3.9_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW3.9_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW3.9_o0' using ($1*10):2 ls 5

set size LEFT_WIDTH, BOTTOM_HEIGHT
set origin X1,Y1
# set ytics 10. nomirror
set xtics X_TICS nomirror font "Times-Roman,20"
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW2.6_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW2.6_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW2.6_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW2.6_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS0.6_kW2.6_o0' using ($1*10):2 ls 5


set size WIDTH,TOP_HEIGHT
set origin X2,Y5
unset xtics
unset ytics
set title '0.05'
# font "Times-Roman,20"
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW21.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW21.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW21.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW21.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW21.4_o0' using ($1*10):2 ls 5

set size WIDTH,HEIGHT
unset title
set origin X2,Y4
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW11.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW11.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW11.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW11.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW11.4_o0' using ($1*10):2 ls 5

set origin X2,Y3
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW6.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW6.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW6.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW6.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW6.4_o0' using ($1*10):2 ls 5

set origin X2,Y2
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW3.9_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW3.9_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW3.9_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW3.9_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW3.9_o0' using ($1*10):2 ls 5

set size WIDTH, BOTTOM_HEIGHT
set origin X2,Y1
set xtics X_TICS nomirror font "Times-Roman,20"
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW2.6_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW2.6_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW2.6_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW2.6_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS1.2_kW2.6_o0' using ($1*10):2 ls 5


set size WIDTH,TOP_HEIGHT
set origin X3,Y5
unset xtics
unset ytics
set title '{/Times-Roman-Italic k}_s = 0.1 pN/nm'
# font "Times-Roman,20"
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW21.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW21.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW21.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW21.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW21.4_o0' using ($1*10):2 ls 5

set size WIDTH,HEIGHT
unset title
set origin X3,Y4
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW11.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW11.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW11.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW11.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW11.4_o0' using ($1*10):2 ls 5

set origin X3,Y3
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW6.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW6.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW6.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW6.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW6.4_o0' using ($1*10):2 ls 5

set origin X3,Y2
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW3.9_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW3.9_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW3.9_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW3.9_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW3.9_o0' using ($1*10):2 ls 5

set size WIDTH, BOTTOM_HEIGHT
set origin X3,Y1
set xtics X_TICS nomirror font "Times-Roman,20"
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW2.6_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW2.6_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW2.6_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW2.6_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS2.4_kW2.6_o0' using ($1*10):2 ls 5


set size WIDTH,TOP_HEIGHT
set origin X4,Y5
unset xtics
unset ytics
set title '0.2'
# font "Times-Roman,20"
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW21.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW21.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW21.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW21.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW21.4_o0' using ($1*10):2 ls 5

set size WIDTH,HEIGHT
unset title
set origin X4,Y4
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW11.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW11.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW11.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW11.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW11.4_o0' using ($1*10):2 ls 5

set origin X4,Y3
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW6.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW6.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW6.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW6.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW6.4_o0' using ($1*10):2 ls 5

set origin X4,Y2
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW3.9_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW3.9_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW3.9_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW3.9_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW3.9_o0' using ($1*10):2 ls 5

set size WIDTH, BOTTOM_HEIGHT
set origin X4,Y1
set xtics X_TICS nomirror font "Times-Roman,20"
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW2.6_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW2.6_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW2.6_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW2.6_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS4.8_kW2.6_o0' using ($1*10):2 ls 5


set size RIGHT_WIDTH,TOP_HEIGHT
set origin X5,Y5
unset xtics
set y2label '10'
set title '0.4'
# font "Times-Roman,20"
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW21.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW21.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW21.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW21.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW21.4_o0' using ($1*10):2 ls 5

set size RIGHT_WIDTH,HEIGHT
unset title
set origin X5,Y4
set y2label '5'
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW11.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW11.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW11.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW11.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW11.4_o0' using ($1*10):2 ls 5

set origin X5,Y3
set y2label '{/Symbol-Italic b}{/Symbol D}{/Times-Roman-Italic E}_m^{\263} = 2.5'
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW6.4_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW6.4_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW6.4_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW6.4_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW6.4_o0' using ($1*10):2 ls 5

set origin X5,Y2
set y2label '1.25'
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW3.9_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW3.9_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW3.9_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW3.9_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW3.9_o0' using ($1*10):2 ls 5

set size RIGHT_WIDTH, BOTTOM_HEIGHT
set origin X5,Y1
set xtics X_TICS nomirror font "Times-Roman,20"
set y2label '0.625'
plot [X_MIN:X_MAX] [Y_MIN:Y_MAX] 'array/pot0_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW2.6_o0' using ($1*10):2 ls 1, 'array/pot5_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW2.6_o0' using ($1*10):2 ls 2, 'array/pot10_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW2.6_o0' using ($1*10):2 ls 3, 'array/pot15_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW2.6_o0' using ($1*10):2 ls 4, 'array/pot20_xM-2.5_2.5_nX81_tS2_dT2.887e-07_v10_b1_D4399.49_kS9.6_kW2.6_o0' using ($1*10):2 ls 5


