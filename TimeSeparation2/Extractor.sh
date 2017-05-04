#!/bin/bash
#Extraction script for February 19th stochastic control simulations

cp a25/Output/WorkTotal_k1.dat WorkTotal_25_k1.dat
cp a25/Output/WorkTotal_k2.dat WorkTotal_25_k2.dat
cp a25/Output/WorkTotal_k4.dat WorkTotal_25_k4.dat
cp a25/Output/WorkTotal_k8.dat WorkTotal_25_k8.dat
cp a25/Output/WorkTotal_k16.dat WorkTotal_25_k16.dat
cp a25/Output/WorkTotal_k32.dat WorkTotal_25_k32.dat
cp a25/Output/WorkTotal_k64.dat WorkTotal_25_k64.dat


cp a50/Output/WorkTotal_k1.dat WorkTotal_50_k1.dat
cp a50/Output/WorkTotal_k2.dat WorkTotal_50_k2.dat
cp a50/Output/WorkTotal_k4.dat WorkTotal_50_k4.dat
cp a50/Output/WorkTotal_k8.dat WorkTotal_50_k8.dat
cp a50/Output/WorkTotal_k16.dat WorkTotal_50_k16.dat
cp a50/Output/WorkTotal_k32.dat WorkTotal_50_k32.dat
cp a50/Output/WorkTotal_k64.dat WorkTotal_50_k64.dat


cp a75/Output/WorkTotal_k1.dat WorkTotal_75_k1.dat
cp a75/Output/WorkTotal_k2.dat WorkTotal_75_k2.dat
cp a75/Output/WorkTotal_k4.dat WorkTotal_75_k4.dat
cp a75/Output/WorkTotal_k8.dat WorkTotal_75_k8.dat
cp a75/Output/WorkTotal_k16.dat WorkTotal_75_k16.dat
cp a75/Output/WorkTotal_k32.dat WorkTotal_75_k32.dat
cp a75/Output/WorkTotal_k64.dat WorkTotal_75_k64.dat


cp a90/Output/WorkTotal_k1.dat WorkTotal_90_k1.dat
cp a90/Output/WorkTotal_k2.dat WorkTotal_90_k2.dat
cp a90/Output/WorkTotal_k4.dat WorkTotal_90_k4.dat
cp a90/Output/WorkTotal_k8.dat WorkTotal_90_k8.dat
cp a90/Output/WorkTotal_k16.dat WorkTotal_90_k16.dat
cp a90/Output/WorkTotal_k32.dat WorkTotal_90_k32.dat
cp a90/Output/WorkTotal_k64.dat WorkTotal_90_k64.dat


cp a95/Output/WorkTotal_k1.dat WorkTotal_95_k1.dat
cp a95/Output/WorkTotal_k2.dat WorkTotal_95_k2.dat
cp a95/Output/WorkTotal_k4.dat WorkTotal_95_k4.dat
cp a95/Output/WorkTotal_k8.dat WorkTotal_95_k8.dat
cp a95/Output/WorkTotal_k16.dat WorkTotal_95_k16.dat
cp a95/Output/WorkTotal_k32.dat WorkTotal_95_k32.dat
cp a95/Output/WorkTotal_k64.dat WorkTotal_95_k64.dat


cp a99/Output/WorkTotal_k1.dat WorkTotal_99_k1.dat
cp a99/Output/WorkTotal_k2.dat WorkTotal_99_k2.dat
cp a99/Output/WorkTotal_k4.dat WorkTotal_99_k4.dat
cp a99/Output/WorkTotal_k8.dat WorkTotal_99_k8.dat
cp a99/Output/WorkTotal_k16.dat WorkTotal_99_k16.dat
cp a99/Output/WorkTotal_k32.dat WorkTotal_99_k32.dat
cp a99/Output/WorkTotal_k64.dat WorkTotal_99_k64.dat

tar -cvf TotalData.tar *.dat
rm *.dat


