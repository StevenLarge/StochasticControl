#!/bin/bash
#Extraction routine for 1-64 Time Separation data from Cluster

cp TimeSeparation2_1/Output/WorkTotal_TS_1.0_k1.dat WorkTotal_TS_1.dat
cp TimeSeparation2_2/Output/WorkTotal_TS_2.0_k1.dat WorkTotal_TS_2.dat
cp TimeSeparation2_4/Output/WorkTotal_TS_4.0_k1.dat WorkTotal_TS_4.dat
cp TimeSeparation2_8/Output/WorkTotal_TS_8.0_k1.dat WorkTotal_TS_8.dat
cp TimeSeparation2_16/Output/WorkTotal_TS_16.0_k1.dat WorkTotal_TS_16.dat
cp TimeSeparation2_32/Output/WorkTotal_TS_32.0_k1.dat WorkTotal_TS_32.dat
cp TimeSeparation2_64/Output/WorkTotal_TS_64.0_k1.dat WorkTotal_TS_64.dat

cp TimeSeparation2_1/Output/WorkTheoryD_TS_1.0.dat WorkTheoryD_TS_1.dat
cp TimeSeparation2_2/Output/WorkTheoryD_TS_2.0.dat WorkTheoryD_TS_2.dat
cp TimeSeparation2_4/Output/WorkTheoryD_TS_4.0.dat WorkTheoryD_TS_4.dat
cp TimeSeparation2_8/Output/WorkTheoryD_TS_8.0.dat WorkTheoryD_TS_8.dat
cp TimeSeparation2_16/Output/WorkTheoryD_TS_16.0.dat WorkTheoryD_TS_16.dat
cp TimeSeparation2_32/Output/WorkTheoryD_TS_32.0.dat WorkTheoryD_TS_32.dat
cp TimeSeparation2_64/Output/WorkTheoryD_TS_64.0.dat WorkTheoryD_TS_64.dat

cp TimeSeparation2_1/Output/WorkTheoryS_TS_1.0.dat WorkTheoryS_TS_1.dat
cp TimeSeparation2_2/Output/WorkTheoryS_TS_2.0.dat WorkTheoryS_TS_2.dat
cp TimeSeparation2_4/Output/WorkTheoryS_TS_4.0.dat WorkTheoryS_TS_4.dat
cp TimeSeparation2_8/Output/WorkTheoryS_TS_8.0.dat WorkTheoryS_TS_8.dat
cp TimeSeparation2_16/Output/WorkTheoryS_TS_16.0.dat WorkTheoryS_TS_16.dat
cp TimeSeparation2_32/Output/WorkTheoryS_TS_32.0.dat WorkTheoryS_TS_32.dat
cp TimeSeparation2_64/Output/WorkTheoryS_TS_64.0.dat WorkTheoryS_TS_64.dat

cp TimeSeparation2_1/Output/WorkTheorySLag_TS_1.0.dat WorkTheorySLag_TS_1.dat
cp TimeSeparation2_2/Output/WorkTheorySLag_TS_2.0.dat WorkTheorySLag_TS_2.dat
cp TimeSeparation2_4/Output/WorkTheorySLag_TS_4.0.dat WorkTheorySLag_TS_4.dat
cp TimeSeparation2_8/Output/WorkTheorySLag_TS_8.0.dat WorkTheorySLag_TS_8.dat
cp TimeSeparation2_16/Output/WorkTheorySLag_TS_16.0.dat WorkTheorySLag_TS_16.dat
cp TimeSeparation2_32/Output/WorkTheorySLag_TS_32.0.dat WorkTheorySLag_TS_32.dat
cp TimeSeparation2_64/Output/WorkTheorySLag_TS_64.0.dat WorkTheorySLag_TS_64.dat

tar -cvf Data.tar *.dat
rm *.dat







