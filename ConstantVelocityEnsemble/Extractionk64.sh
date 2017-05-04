#!/bin/bash
#Extraction script for k64 Constant velocity ensemble simulations

cp dLambda_5/k64/VelVar_0125/Output/WorkTotal_0.125.dat WorkTotal_L5_k64_0125.dat
cp dLambda_5/k64/VelVar_025/Output/WorkTotal_0.25.dat WorkTotal_L5_k64_025.dat
cp dLambda_5/k64/VelVar_05/Output/WorkTotal_0.5.dat WorkTotal_L5_k64_05.dat
cp dLambda_5/k64/VelVar_1/Output/WorkTotal_1.dat WorkTotal_L5_k64_1.dat
cp dLambda_5/k64/VelVar_2/Output/WorkTotal_2.dat WorkTotal_L5_k64_2.dat
cp dLambda_5/k64/VelVar_4/Output/WorkTotal_4.dat WorkTotal_L5_k64_4.dat
cp dLambda_5/k64/VelVar_8/Output/WorkTotal_8.dat WorkTotal_L5_k64_8.dat

cp dLambda_10/k64/VelVar_0125/Output/WorkTotal_0.125.dat WorkTotal_L10_k64_0125.dat
cp dLambda_10/k64/VelVar_025/Output/WorkTotal_0.25.dat WorkTotal_L10_k64_025.dat
cp dLambda_10/k64/VelVar_05/Output/WorkTotal_0.5.dat WorkTotal_L10_k64_05.dat
cp dLambda_10/k64/VelVar_1/Output/WorkTotal_1.dat WorkTotal_L10_k64_1.dat
cp dLambda_10/k64/VelVar_2/Output/WorkTotal_2.dat WorkTotal_L10_k64_2.dat
cp dLambda_10/k64/VelVar_4/Output/WorkTotal_4.dat WorkTotal_L10_k64_4.dat
cp dLambda_10/k64/VelVar_8/Output/WorkTotal_8.dat WorkTotal_L10_k64_8.dat

cp dLambda_20/k64/VelVar_0125/Output/WorkTotal_0.125.dat WorkTotal_L20_k64_0125.dat
cp dLambda_20/k64/VelVar_025/Output/WorkTotal_0.25.dat WorkTotal_L20_k64_025.dat
cp dLambda_20/k64/VelVar_05/Output/WorkTotal_0.5.dat WorkTotal_L20_k64_05.dat
cp dLambda_20/k64/VelVar_1/Output/WorkTotal_1.dat WorkTotal_L20_k64_1.dat
cp dLambda_20/k64/VelVar_2/Output/WorkTotal_2.dat WorkTotal_L20_k64_2.dat
cp dLambda_20/k64/VelVar_4/Output/WorkTotal_4.dat WorkTotal_L20_k64_4.dat
cp dLambda_20/k64/VelVar_8/Output/WorkTotal_8.dat WorkTotal_L20_k64_8.dat

cp dLambda_40/k64/VelVar_0125/Output/WorkTotal_0.125.dat WorkTotal_L40_k64_0125.dat
cp dLambda_40/k64/VelVar_025/Output/WorkTotal_0.25.dat WorkTotal_L40_k64_025.dat
cp dLambda_40/k64/VelVar_05/Output/WorkTotal_0.5.dat WorkTotal_L40_k64_05.dat
cp dLambda_40/k64/VelVar_1/Output/WorkTotal_1.dat WorkTotal_L40_k64_1.dat
cp dLambda_40/k64/VelVar_2/Output/WorkTotal_2.dat WorkTotal_L40_k64_2.dat
cp dLambda_40/k64/VelVar_4/Output/WorkTotal_4.dat WorkTotal_L40_k64_4.dat
cp dLambda_40/k64/VelVar_8/Output/WorkTotal_8.dat WorkTotal_L40_k64_8.dat

cp dLambda_80/k64/VelVar_0125/Output/WorkTotal_0.125.dat WorkTotal_L80_k64_0125.dat
cp dLambda_80/k64/VelVar_025/Output/WorkTotal_0.25.dat WorkTotal_L80_k64_025.dat
cp dLambda_80/k64/VelVar_05/Output/WorkTotal_0.5.dat WorkTotal_L80_k64_05.dat
cp dLambda_80/k64/VelVar_1/Output/WorkTotal_1.dat WorkTotal_L80_k64_1.dat
cp dLambda_80/k64/VelVar_2/Output/WorkTotal_2.dat WorkTotal_L80_k64_2.dat
cp dLambda_80/k64/VelVar_4/Output/WorkTotal_4.dat WorkTotal_L80_k64_4.dat
cp dLambda_80/k64/VelVar_8/Output/WorkTotal_8.dat WorkTotal_L80_k64_8.dat

tar -cvf Data_k64.tar *.dat
rm *.dat

