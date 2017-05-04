#!/bin/bash
#Extraction script for altering mass data, February 11th

cp MassTest/MASS_1/Output/WorkTotal_TS_1_M1.dat WorkTotal_1_M1.dat
cp MassTest/MASS_2/Output/WorkTotal_TS_1_M2.dat WorkTotal_1_M2.dat
cp MassTest/MASS_4/Output/WorkTotal_TS_1_M4.dat WorkTotal_1_M4.dat
cp MassTest/MASS_8/Output/WorkTotal_TS_1_M8.dat WorkTotal_1_M8.dat
cp MassTest/MASS_16/Output/WorkTotal_TS_11_M16.dat WorkTotal_1_M16.dat
cp MassTest/MASS_32/Output/WorkTotal_TS_1_M32.dat WorkTotal_1_M32.dat

cp MassTest/MASS_1/Output/WorkTheoryD_TS_1_M1.dat WorkTheoryD_1_M1.dat
cp MassTest/MASS_2/Output/WorkTheoryD_TS_1_M2.dat WorkTheoryD_1_M2.dat
cp MassTest/MASS_4/Output/WorkTheoryD_TS_1_M4.dat WorkTheoryD_1_M4.dat
cp MassTest/MASS_8/Output/WorkTheoryD_TS_1_M8.dat WorkTheoryD_1_M8.dat
cp MassTest/MASS_16/Output/WorkTheoryD_TS_1_M16.dat WorkTheoryD_1_M16.dat
cp MassTest/MASS_32/Output/WorkTheoryD_TS_1_M32.dat WorkTheoryD_1_M32.dat

cp MassTest/MASS_1/Output/WorkTheoryS_TS_1_M1.dat WorkTheoryS_1_M1.dat
cp MassTest/MASS_2/Output/WorkTheoryS_TS_1_M2.dat WorkTheoryS_1_M2.dat
cp MassTest/MASS_4/Output/WorkTheoryS_TS_1_M4.dat WorkTheoryS_1_M4.dat
cp MassTest/MASS_8/Output/WorkTheoryS_TS_1_M8.dat WorkTheoryS_1_M8.dat
cp MassTest/MASS_16/Output/WorkTheoryS_TS_1_M16.dat WorkTheoryS_1_M16.dat
cp MassTest/MASS_32/Output/WorkTheoryS_TS_1_M32.dat WorkTheoryS_1_M32.dat

cp MassTest/MASS_1/Output/WorkTheorySLag_TS_1_M1.dat WorkTheorySLag_1_M1.dat
cp MassTest/MASS_2/Output/WorkTheorySLag_TS_1_M2.dat WorkTheorySLag_1_M2.dat
cp MassTest/MASS_4/Output/WorkTheorySLag_TS_1_M4.dat WorkTheorySLag_1_M4.dat
cp MassTest/MASS_8/Output/WorkTheorySLag_TS_1_M8.dat WorkTheorySLag_1_M8.dat
cp MassTest/MASS_16/Output/WorkTheorySLag_TS_1_M16.dat WorkTheorySLag_1_M16.dat
cp MassTest/MASS_32/Output/WorkTheorySLag_TS_1_M32.dat WorkTheorySLag_1_M32.dat

tar -cvf Data.tar *.dat
rm *.dat




