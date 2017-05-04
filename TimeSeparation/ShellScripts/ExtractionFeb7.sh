#!/bin/bash
#Extraction script for February 7th data

mv TimeSeparation_1/Output/WorkTotal_TS_1.0_k1.dat WorkTotal_1.dat
mv TimeSeparation_2/Output/WorkTotal_TS_2.0_k1.dat WorkTotal_2.dat
mv TimeSeparation_4/Output/WorkTotal_TS_4.0_k1.dat WorkTotal_4.dat
mv TimeSeparation_8/Output/WorkTotal_TS_8.0_k1.dat WorkTotal_8.dat
mv TimeSeparation_16/Output/WorkTotal_TS_16.0_k1.dat WorkTotal_16.dat
mv TimeSeparation_32/Output/WorkTotal_TS_32.0_k1.dat WorkTotal_32.dat
mv TimeSeparation_64/Output/WorkTotal_TS_64.0_k1.dat WorkTotal_64.dat
mv TimeSeparation_128/Output/WorkTotal_TS_128.0_k1.dat WorkTotal_128.dat

mv TimeSeparation_1/Output/WorkTheoryD_TS_1.0.dat WorkTheoryD_1.dat
mv TimeSeparation_2/Output/WorkTheoryD_TS_2.0.dat WorkTheoryD_2.dat
mv TimeSeparation_4/Output/WorkTheoryD_TS_4.0.dat WorkTheoryD_4.dat
mv TimeSeparation_8/Output/WorkTheoryD_TS_8.0.dat WorkTheoryD_8.dat
mv TimeSeparation_16/Output/WorkTheoryD_TS_16.0.dat WorkTheoryD_16.dat
mv TimeSeparation_32/Output/WorkTheoryD_TS_32.0.dat WorkTheoryD_32.dat
mv TimeSeparation_64/Output/WorkTheoryD_TS_64.0.dat WorkTheoryD_64.dat
mv TimeSeparation_128/Output/WorkTheoryD_TS_128.0.dat WorkTheoryD_128.dat

mv TimeSeparation_1/Output/WorkTheoryS_TS_1.0.dat WorkTheoryS_1.dat
mv TimeSeparation_2/Output/WorkTheoryS_TS_2.0.dat WorkTheoryS_2.dat
mv TimeSeparation_4/Output/WorkTheoryS_TS_4.0.dat WorkTheoryS_4.dat
mv TimeSeparation_8/Output/WorkTheoryS_TS_8.0.dat WorkTheoryS_8.dat
mv TimeSeparation_16/Output/WorkTheoryS_TS_16.0.dat WorkTheoryS_16.dat
mv TimeSeparation_32/Output/WorkTheoryS_TS_32.0.dat WorkTheoryS_32.dat
mv TimeSeparation_64/Output/WorkTheoryS_TS_64.0.dat WorkTheoryS_64.dat
mv TimeSeparation_128/Output/WorkTheoryS_TS_128.0.dat WorkTheoryS_128.dat

mv TimeSeparation_1/Output/WorkTheorySLag_TS_1.0.dat WorkTheorySLag_1.dat
mv TimeSeparation_2/Output/WorkTheorySLag_TS_2.0.dat WorkTheorySLag_2.dat
mv TimeSeparation_4/Output/WorkTheorySLag_TS_4.0.dat WorkTheorySLag_4.dat
mv TimeSeparation_8/Output/WorkTheorySLag_TS_8.0.dat WorkTheorySLag_8.dat
mv TimeSeparation_16/Output/WorkTheorySLag_TS_16.0.dat WorkTheorySLag_16.dat
mv TimeSeparation_32/Output/WorkTheorySLag_TS_32.0.dat WorkTheorySLag_32.dat
mv TimeSeparation_64/Output/WorkTheorySLag_TS_64.0.dat WorkTheorySLag_64.dat
mv TimeSeparation_128/Output/WorkTheorySLag_TS_128.0.dat WorkTheorySLag_128.dat

tar -cvf Data.tar *.dat
rm *.dat


