#!/bin/bash
#Extraction script for time separation data

cp TimeSeparation_2/Output/WorkTotal_TS_2_k2.dat WorkTotal_2_2.dat
cp TimeSeparation_4/Output/WorkTotal_TS_4_k2.dat WorkTotal_4_2.dat
cp TimeSeparation_8/Output/WorkTotal_TS_8_k2.dat WorkTotal_8_2.dat
cp TimeSeparation_16/Output/WorkTotal_TS_16_k2.dat WorkTotal_16_2.dat
cp TimeSeparation_32/Output/WorkTotal_TS_32_k2.dat WorkTotal_32_2.dat
cp TimeSeparation_64/Output/WorkTotal_TS_64_k2.dat WorkTotal_64_2.dat
cp TimeSeparation_128/Output/WorkTotal_TS_128_k2.dat WorkTotal_128_2.dat
cp TimeSeparation_128/Output/WorkTotal_SHORT_TS_64_k2.dat WorkTotal_64S_2.datr
cp TimeSeparation_128/Output/WorkTotal_SHORT_TS_128_k2.dat WorkTotal_128S_2.dat
cp TimeSeparation_256/Output/WorkTotal_SHORT_TS_256_k2.dat WorkTotal_256_2.dat

cp TimeSeparation_2/Output/WorkTheoryD_TS_2_k2.dat WorkTheoryD_2_2.dat
cp TimeSeparation_4/Output/WorkTheoryD_TS_4_k2.dat WorkTheoryD_4_2.dat
cp TimeSeparation_8/Output/WorkTheoryD_TS_8_k2.dat WorkTheoryD_8_2.dat
cp TimeSeparation_16/Output/WorkTheoryD_TS_16_k2.dat WorkTheoryD_16_2.dat
cp TimeSeparation_32/Output/WorkTheoryD_TS_32_k2.dat WorkTheoryD_32_2.dat
cp TimeSeparation_64/Output/WorkTheoryD_TS_64_k2.dat WorkTheoryD_64_2.dat
cp TimeSeparation_128/Output/WorkTheoryD_TS_128_k2.dat WorkTheoryD_128_2.dat
cp TimeSeparation_128/Output/WorkTheoryD_SHORT_TS_64_k2.dat WorkTheoryD_64S_2.dat
cp TimeSeparation_128/Output/WorkTheoryD_SHORT_TS_128_k2.dat WorkTheoryD_128S_2.dat
cp TimeSeparation_256/Output/WorkTheoryD_SHORT_TS_256_k2.dat WorkTheoryD_256_2.dat

cp TimeSeparation_2/Output/WorkTheoryS_TS_2_k2.dat WorkTheoryS_2_2.dat
cp TimeSeparation_4/Output/WorkTheoryS_TS_4_k2.dat WorkTheoryS_4_2.dat
cp TimeSeparation_8/Output/WorkTheoryS_TS_8_k2.dat WorkTheoryS_8_2.dat
cp TimeSeparation_16/Output/WorkTheoryS_TS_16_k2.dat WorkTheoryS_16_2.dat
cp TimeSeparation_32/Output/WorkTheoryS_TS_32_k2.dat WorkTheoryS_32_2.dat
cp TimeSeparation_64/Output/WorkTheoryS_TS_64_k2.dat WorkTheoryS_64_2.dat
cp TimeSeparation_128/Output/WorkTheoryS_TS_128_k2.dat WorkTheoryS_128_2.dat
cp TimeSeparation_128/Output/WorkTheoryS_SHORT_TS_64_k2.dat WorkTheoryS_64S_2.dat
cp TimeSeparation_128/Output/WorkTheoryS_SHORT_TS_128_k2.dat WorkTheoryS_128S_2.dat
cp TimeSeparation_256/Output/WorkTheoryS_SHORT_TS_256_k2.dat WorkTheoryS_256_2.dat

tar -cvf Data.tar *.dat
rm *.dat





