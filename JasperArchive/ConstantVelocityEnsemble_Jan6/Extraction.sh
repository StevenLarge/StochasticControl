#!/bin/bash
#This shell script extracts the data files from the constant velocity ensemble simulations from Janusry 6th

cp VelVar_01/Output/WorkTotal_0.1.dat WorkTotal_01.dat
cp VelVar_05/Output/WorkTotal_0.5.dat WorkTotal_05.dat
cp VelVar_1/Output/WorkTotal_1.0.dat WorkTotal_1.dat
cp VelVar_2/Output/WorkTotal_2.0.dat WorkTotal_2.dat
cp VelVar_4/Output/WorkTotal_4.0.dat WorkTotal_4.dat
cp VelVar_8/Output/WorkTotal_8.0.dat WorkTotal_8.dat

tar -cvf Data.tar *.dat
rm *.dat

echo ""
echo ""
echo ""
echo "----- Fihished Extraction -----"
echo ""
echo ""
echo ""




