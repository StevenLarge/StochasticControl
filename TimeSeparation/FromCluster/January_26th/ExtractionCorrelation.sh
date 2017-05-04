#!/bin/bash
#Extraction script for autocorrelation files form Time separation data, January 25th 2017

cp TimeSeparation2_1/AutoCorrelation/AutoCorrelation_1.0.dat AutoCorrelation_1.dat
cp TimeSeparation2_2/AutoCorrelation/AutoCorrelation_2.0.dat AutoCorrelation_2.dat
cp TimeSeparation2_4/AutoCorrelation/AutoCorrelation_4.0.dat AutoCorrelation_4.dat
cp TimeSeparation2_8/AutoCorrelation/AutoCorrelation_8.0.dat AutoCorrelation_8.dat
cp TimeSeparation2_16/AutoCorrelation/AutoCorrelation_16.0.dat AutoCorrelation_16.dat
cp TimeSeparation2_32/AutoCorrelation/AutoCorrelation_32.0.dat AutoCorrelation_32.dat
cp TimeSeparation2_64/AutoCorrelation/AutoCorrelation_64.0.dat AutoCorrelation_64.dat
cp TimeSeparation2_128/AutoCorrelation/AutoCorrelation_128.0.dat AutoCorrelation_128.dat

cp TimeSeparation2_1/AutoCorrelation/Friction.dat Friction_1.dat
cp TimeSeparation2_2/AutoCorrelation/Friction.dat Friction_2.dat
cp TimeSeparation2_4/AutoCorrelation/Friction.dat Friction_4.dat
cp TimeSeparation2_8/AutoCorrelation/Friction.dat Friction_8.dat
cp TimeSeparation2_16/AutoCorrelation/Friction.dat Friction_16.dat
cp TimeSeparation2_32/AutoCorrelation/Friction.dat Friction_32.dat
cp TimeSeparation2_64/AutoCorrelation/Friction.dat Friction_64.dat
cp TimeSeparation2_128/AutoCorrelation/Friction.dat Friction_128.dat

tar -xvf Correlations.tar *.dat
rm *.dat
