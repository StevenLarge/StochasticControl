#!/bin/bash
#Extraction script for smoothed noise stochastic control simulations

mv Smoothing_Tau_1/Output/WorkTotal_k1.dat WorkTotal_T1_k1.dat
mv Smoothing_Tau_1/Output/WorkTotal_k2.dat WorkTotal_T1_k2.dat
mv Smoothing_Tau_1/Output/WorkTotal_k4.dat WorkTotal_T1_k4.dat
mv Smoothing_Tau_1/Output/WorkTotal_k8.dat WorkTotal_T1_k8.dat
mv Smoothing_Tau_1/Output/WorkTotal_k16.dat WorkTotal_T1_k16.dat
mv Smoothing_Tau_1/Output/WorkTotal_k32.dat WorkTotal_T1_k32.dat
mv Smoothing_Tau_1/Output/WorkTotal_k64.dat WorkTotal_T1_k64.dat
mv Smoothing_Tau_1/Output/WorkTotal_k75.dat WorkTotal_T1_k75.dat

mv Smoothing_Tau_2/Output/WorkTotal_k1.dat WorkTotal_T2_k1.dat
mv Smoothing_Tau_2/Output/WorkTotal_k2.dat WorkTotal_T2_k2.dat
mv Smoothing_Tau_2/Output/WorkTotal_k4.dat WorkTotal_T2_k4.dat
mv Smoothing_Tau_2/Output/WorkTotal_k8.dat WorkTotal_T2_k8.dat
mv Smoothing_Tau_2/Output/WorkTotal_k16.dat WorkTotal_T2_k16.dat
mv Smoothing_Tau_2/Output/WorkTotal_k32.dat WorkTotal_T2_k32.dat
mv Smoothing_Tau_2/Output/WorkTotal_k64.dat WorkTotal_T2_k64.dat
mv Smoothing_Tau_2/Output/WorkTotal_k75.dat WorkTotal_T2_k75.dat

mv Smoothing_Tau_4/Output/WorkTotal_k1.dat WorkTotal_T4_k1.dat
mv Smoothing_Tau_4/Output/WorkTotal_k2.dat WorkTotal_T4_k2.dat
mv Smoothing_Tau_4/Output/WorkTotal_k4.dat WorkTotal_T4_k4.dat
mv Smoothing_Tau_4/Output/WorkTotal_k8.dat WorkTotal_T4_k8.dat
mv Smoothing_Tau_4/Output/WorkTotal_k16.dat WorkTotal_T4_k16.dat
mv Smoothing_Tau_4/Output/WorkTotal_k32.dat WorkTotal_T4_k32.dat
mv Smoothing_Tau_4/Output/WorkTotal_k64.dat WorkTotal_T4_k64.dat
mv Smoothing_Tau_4/Output/WorkTotal_k75.dat WorkTotal_T4_k75.dat

mv Smoothing_Tau_8/Output/WorkTotal_k1.dat WorkTotal_T8_k1.dat
mv Smoothing_Tau_8/Output/WorkTotal_k2.dat WorkTotal_T8_k2.dat
mv Smoothing_Tau_8/Output/WorkTotal_k4.dat WorkTotal_T8_k4.dat
mv Smoothing_Tau_8/Output/WorkTotal_k8.dat WorkTotal_T8_k8.dat
mv Smoothing_Tau_8/Output/WorkTotal_k16.dat WorkTotal_T8_k16.dat
mv Smoothing_Tau_8/Output/WorkTotal_k32.dat WorkTotal_T8_k32.dat
mv Smoothing_Tau_8/Output/WorkTotal_k64.dat WorkTotal_T8_k64.dat
mv Smoothing_Tau_8/Output/WorkTotal_k75.dat WorkTotal_T8_k75.dat

mv Smoothing_Tau_16/Output/WorkTotal_k1.dat WorkTotal_T16_k1.dat
mv Smoothing_Tau_16/Output/WorkTotal_k2.dat WorkTotal_T16_k2.dat
mv Smoothing_Tau_16/Output/WorkTotal_k4.dat WorkTotal_T16_k4.dat
mv Smoothing_Tau_16/Output/WorkTotal_k8.dat WorkTotal_T16_k8.dat
mv Smoothing_Tau_16/Output/WorkTotal_k16.dat WorkTotal_T16_k16.dat
mv Smoothing_Tau_16/Output/WorkTotal_k32.dat WorkTotal_T16_k32.dat
mv Smoothing_Tau_16/Output/WorkTotal_k64.dat WorkTotal_T16_k64.dat
mv Smoothing_Tau_16/Output/WorkTotal_k75.dat WorkTotal_T16_k75.dat

tar -cvf TotalData.tar *.dat
rm *.dat





