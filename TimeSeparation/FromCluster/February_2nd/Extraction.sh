#!/bin/bash
#Extraction script for Feb 2nd time separation data

cp TimeSeparation_200/Output/WorkTotal_TS_200_k1.dat WorkTotal_200.dat
cp TimeSeparation_250/Output/WorkTotal_TS_250_k1.dat WorkTotal_250.dat
cp TimeSeparation_300/Output/WorkTotal_TS_300_k1.dat WorkTotal_300.dat
cp TimeSeparation_350/Output/WorkTotal_TS_350_k1.dat WorkTotal_350.dat
cp TimeSeparation_400/Output/WorkTotal_TS_400_k1.dat WorkTotal_400.dat
cp TimeSeparation_450/Output/WorkTotal_TS_450_k1.dat WorkTotal_450.dat
cp TimeSeparation_500/Output/WorkTotal_TS_500_k1.dat WorkTotal_500.dat

cp TimeSeparation_200/Output/WorkTheoryS_TS_200.dat WorkTheoryS_200.dat
cp TimeSeparation_250/Output/WorkTheoryS_TS_250.dat WorkTheoryS_250.dat
cp TimeSeparation_300/Output/WorkTheoryS_TS_300.dat WorkTheoryS_300.dat
cp TimeSeparation_350/Output/WorkTheoryS_TS_350.dat WorkTheoryS_350.dat
cp TimeSeparation_400/Output/WorkTheoryS_TS_400.dat WorkThoeryS_400.dat
cp TimeSeparation_450/Output/WorkTheoryS_TS_450.dat WorkTheoryS_450.dat
cp TimeSeparation_500/Output/WorkTheoryS_TS_500.dat WorkTheoryS_500.dat

cp TimeSeparation_200/Output/WorkTheoryD_TS_200.dat WorkTheoryD_200.dat
cp TimeSeparation_250/Output/WorkTheoryD_TS_250.dat WorkTheoryD_250.dat
cp TimeSeparation_300/Output/WorkTheoryD_TS_300.dat WorkTheoryD_300.dat
cp TimeSeparation_350/Output/WorkTheoryD_TS_350.dat WorkTheoryD_350.dat
cp TimeSeparation_400/Output/WorkTheoryD_TS_400.dat WorkThoeryD_400.dat
cp TimeSeparation_450/Output/WorkTheoryD_TS_450.dat WorkTheoryD_450.dat
cp TimeSeparation_500/Output/WorkTheoryD_TS_500.dat WorkTheoryD_500.dat

cp TimeSeparation_200/Output/WorkTheorySLag_TS_200.dat WorkTheorySLag_200.dat
cp TimeSeparation_250/Output/WorkTheorySLag_TS_250.dat WorkTheorySLag_250.dat
cp TimeSeparation_300/Output/WorkTheorySLag_TS_300.dat WorkTheorySLag_300.dat
cp TimeSeparation_350/Output/WorkTheorySLag_TS_350.dat WorkTheorySLag_350.dat
cp TimeSeparation_400/Output/WorkTheorySLag_TS_400.dat WorkThoerySLag_400.dat
cp TimeSeparation_450/Output/WorkTheorySLag_TS_450.dat WorkTheorySLag_450.dat
cp TimeSeparation_500/Output/WorkTheorySLag_TS_500.dat WorkTheorySLag_500.dat

tar -cvf Data.tar *.dat
rm *.dat






