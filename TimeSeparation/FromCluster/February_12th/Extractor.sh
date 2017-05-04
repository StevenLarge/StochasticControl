#!/bin/bash
#Extraction script for time separation data

cp TimeSeparation_1/Output/WorkTotal_TS_1.0.dat WorkTotal_1.dat
cp TimeSeparation_1/Output/WorkTotal_TS_2.0.dat WorkTotal_2.dat
cp TimeSeparation_1/Output/WorkTotal_TS_4.0.dat WorkTotal_4.dat
cp TimeSeparation_1/Output/WorkTotal_TS_8.0.dat WorkTotal_8.dat
cp TimeSeparation_1/Output/WorkTotal_TS_16.0.dat WorkTotal_16.dat
cp TimeSeparation_1/Output/WorkTotal_TS_32.0.dat WorkTotal_32.dat


cp TimeSeparation_1/Output/WorkTheoryD_TS_1.0.dat WorkTheoryD_1.dat
cp TimeSeparation_1/Output/WorkTheoryD_TS_2.0.dat WorkTheoryD_2.dat
cp TimeSeparation_1/Output/WorkTheoryD_TS_4.0.dat WorkTheoryD_4.dat
cp TimeSeparation_1/Output/WorkTheoryD_TS_8.0.dat WorkTheoryD_8.dat
cp TimeSeparation_1/Output/WorkTheoryD_TS_16.0.dat WorkTheoryD_16.dat
cp TimeSeparation_1/Output/WorkTheoryD_TS_32.0.dat WorkTheoryD_32.dat


tar -cvf Data.tar *.dat
rm *.dat





