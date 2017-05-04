#!/bin/bash
#Extraction s cript for Long-Time simulations of Time Separation from february 2nd

cp TimeSeparation_550/Output/WorkTotal_TS_550_k1.dat WorkTotal_550.dat
cp TimeSeparation_600/Output/WorkTotal_TS_600_k1.dat WorkTotal_600.dat
cp TimeSeparation_650/Output/WorkTotal_TS_650_k1.dat WorkTotal_650.dat
cp TimeSeparation_700/Output/WorkTotal_TS_700_k1.dat WorkTotal_700.dat
cp TimeSeparation_750/Output/WorkTotal_TS_750_k1.dat WorkTotal_750.dat
cp TimeSeparation_800/Output/WorkTotal_TS_800_k1.dat WorkTotal_800.dat
cp TimeSeparation_850/Output/WorkTotal_TS_850_k1.dat WorkTotal_850.dat
cp TimeSeparation_900/Output/WorkTotal_TS_900_k1.dat WorkTotal_900.dat
cp TimeSeparation_950/Output/WorkTotal_TS_950_k1.dat WorkTotal_950.dat
cp TimeSeparation_1000/Output/WorkTotal_TS_1000_k1.dat WorkTotal_1000.dat


cp TimeSeparation_550/Output/WorkTheoryD_TS_550.dat WorkTheoryD_550.dat
cp TimeSeparation_600/Output/WorkTheoryD_TS_600.dat WorkTheoryD_600.dat
cp TimeSeparation_650/Output/WorkTheoryD_TS_650.dat WorkTheoryD_650.dat
cp TimeSeparation_700/Output/WorkTheoryD_TS_700.dat WorkTheoryD_700.dat
cp TimeSeparation_750/Output/WorkTheoryD_TS_750.dat WorkTheoryD_750.dat
cp TimeSeparation_800/Output/WorkTheoryD_TS_800.dat WorkTheoryD_800.dat
cp TimeSeparation_850/Output/WorkTheoryD_TS_850.dat WorkTheoryD_850.dat
cp TimeSeparation_900/Output/WorkTheoryD_TS_900.dat WorkTheoryD_900.dat
cp TimeSeparation_950/Output/WorkTheoryD_TS_950.dat WorkTheoryD_950.dat
cp TimeSeparation_1000/Output/WorkTheoryD_TS_1000.dat WorkTheoryD_1000.dat

cp TimeSeparation_550/Output/WorkTheoryS_TS_550.dat WorkTheoryS_550.dat
cp TimeSeparation_600/Output/WorkTheoryS_TS_600.dat WorkTheoryS_600.dat
cp TimeSeparation_650/Output/WorkTheoryS_TS_650.dat WorkTheoryS_650.dat
cp TimeSeparation_700/Output/WorkTheoryS_TS_700.dat WorkTheoryS_700.dat
cp TimeSeparation_750/Output/WorkTheoryS_TS_750.dat WorkTheoryS_750.dat
cp TimeSeparation_800/Output/WorkTheoryS_TS_800.dat WorkTheoryS_800.dat
cp TimeSeparation_850/Output/WorkTheoryS_TS_850.dat WorkTheoryS_850.dat
cp TimeSeparation_900/Output/WorkTheoryS_TS_900.dat WorkTheoryS_900.dat
cp TimeSeparation_950/Output/WorkTheoryS_TS_950.dat WorkTheoryS_950.dat
cp TimeSeparation_1000/Output/WorkTheoryS_TS_1000.dat WorkTheoryS_1000.dat

cp TimeSeparation_550/Output/WorkTheorySLag_TS_550.dat WorkTheorySLag_550.dat
cp TimeSeparation_600/Output/WorkTheorySLag_TS_600.dat WorkTheorySLag_600.dat
cp TimeSeparation_650/Output/WorkTheorySLag_TS_650.dat WorkTheorySLag_650.dat
cp TimeSeparation_700/Output/WorkTheorySLag_TS_700.dat WorkTheorySLag_700.dat
cp TimeSeparation_750/Output/WorkTheorySLag_TS_750.dat WorkTheorySLag_750.dat
cp TimeSeparation_800/Output/WorkTheorySLag_TS_800.dat WorkTheorySLag_800.dat
cp TimeSeparation_850/Output/WorkTheorySLag_TS_850.dat WorkTheorySLag_850.dat
cp TimeSeparation_900/Output/WorkTheorySLag_TS_900.dat WorkTheorySLag_900.dat
cp TimeSeparation_950/Output/WorkTheorySLag_TS_950.dat WorkTheorySLag_950.dat
cp TimeSeparation_1000/Output/WorkTheorySLag_TS_1000.dat WorkTheorySLag_1000.dat

tar -cvf DataLong.tar *.dat
rm *.dat



