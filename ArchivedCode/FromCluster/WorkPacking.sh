#!/bin/bash
#This shell script packs all of the stochastic work functions into a single .tar file

cp kLambda/k1/WorkStochastic.dat kLambda/WorkStochastic_k1L.dat
cp kLambda/k2/WorkStochastic.dat kLambda/WorkStochastic_k2L.dat
cp kLambda/k4/WorkStochastic.dat kLambda/WorkStochastic_k4L.dat
cp kLambda/k8/WorkStochastic.dat kLambda/WorkStochastic_k8L.dat
cp kLambda/k16/WorkStochastic.dat kLambda/WorkStochastic_k16L.dat
cp kLambda/k32/WorkStochastic.dat kLambda/WorkStochastic_k32L.dat
cp kLambda/k63/WorkStochastic.dat kLambda/WorkStochastic_k64L.dat

cp kSystem/k1/WorkStochastic.dat kSystem/WorkStochastic_k1S.dat
cp kSystem/k2/WorkStochastic.dat kSystem/WorkStochastic_k2S.dat
cp kSystem/k4/WorkStochastic.dat kSystem/WorkStochastic_k4S.dat
cp kSystem/k8/WorkStochastic.dat kSystem/WorkStochastic_k8S.dat
cp kSystem/k16/WorkStochastic.dat kSystem/WorkStochastic_k16S.dat
cp kSystem/k32/WorkStochastic.dat kSystem/WorkStochastic_k32S.dat
cp kSystem/k64/WorkStochastic.dat kSystem/WorkStochastic_k64S.dat

cp kLambda/Work* ..
cp kSystem/Work* ..

tar -cvf WorkStochastic.tar Work*.dat

echo "..."
echo "Finished Packing Work Data"
echo "..."
