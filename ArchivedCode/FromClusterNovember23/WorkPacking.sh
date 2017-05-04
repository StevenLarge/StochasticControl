#!bin/bash
#This script packs teh recently obtained work values into a single .tar file

cp kLambda/k1/Tau_1/WorkTotal.dat kLambda/WorkTotal_k1T1.dat
cp kLambda/k1/Tau_2/WorkTotal.dat kLambda/WorkTotal_k1T2.dat
cp kLambda/k1/Tau_4/WorkTotal.dat kLambda/WorkTotal_k1T4.dat
cp kLambda/k1/Tau_8/WorkTotal.dat kLambda/WorkTotal_k1T8.dat
cp kLambda/k1/Tau_16/WorkTotal.dat kLambda/WorkTotal_k1T16.dat

cp kLambda/k2/Tau_1/WorkTotal.dat kLambda/WorkTotal_k2T1.dat
cp kLambda/k2/Tau_2/WorkTotal.dat kLambda/WorkTotal_k2T2.dat
cp kLambda/k2/Tau_4/WorkTotal.dat kLambda/WorkTotal_k2T4.dat
cp kLambda/k2/Tau_8/WorkTotal.dat kLambda/WorkTotal_k2T8.dat
cp kLambda/k2/Tau_16/WorkTotal.dat kLambda/WorkTotal_k2T16.dat

cp kLambda/k4/Tau_1/WorkTotal.dat kLambda/WorkTotal_k4T1.dat
cp kLambda/k4/Tau_2/WorkTotal.dat kLambda/WorkTotal_k4T2.dat
cp kLambda/k4/Tau_4/WorkTotal.dat kLambda/WorkTotal_k4T4.dat
cp kLambda/k4/Tau_8/WorkTotal.dat kLambda/WorkTotal_k4T8.dat
cp kLambda/k4/Tau_16/WorkTotal.dat kLambda/WorkTotal_k4T16.dat

cp kLambda/k8/Tau_1/WorkTotal.dat kLambda/WorkTotal_k8T1.dat
cp kLambda/k8/Tau_2/WorkTotal.dat kLambda/WorkTotal_k8T2.dat
cp kLambda/k8/Tau_4/WorkTotal.dat kLambda/WorkTotal_k8T4.dat
cp kLambda/k8/Tau_8/WorkTotal.dat kLambda/WorkTotal_k8T8.dat
cp kLambda/k8/Tau_16/WorkTotal.dat kLambda/WorkTotal_k8T16.dat

cp kLambda/k16/Tau_1/WorkTotal.dat kLambda/WorkTotal_k16T1.dat
cp kLambda/k16/Tau_2/WorkTotal.dat kLambda/WorkTotal_k16T2.dat
cp kLambda/k16/Tau_4/WorkTotal.dat kLambda/WorkTotal_k16T4.dat
cp kLambda/k16/Tau_8/WorkTotal.dat kLambda/WorkTotal_k16T8.dat
cp kLambda/k16/Tau_16/WorkTotal.dat kLambda/WorkTotal_k16T16.dat

cd kLambda

tar -cvf WorkAll.tar WorkTotal*.dat

