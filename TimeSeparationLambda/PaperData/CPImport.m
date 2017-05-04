%This script imports the CP trajectory data
%
%Steven Large
%March 27th 2017

cd Trajectories

TEMP_1 = dlmread('CP_Trajectory_152.5_1.dat');
TEMP_2 = dlmread('CP_Trajectory_152.5_2.dat');
TEMP_3 = dlmread('CP_Trajectory_152.5_3.dat');
TEMP_4 = dlmread('CP_Trajectory_152.5_4.dat');
TEMP_5 = dlmread('CP_Trajectory_152.5_5.dat');
TEMP_6 = dlmread('CP_Trajectory_152.5_6.dat');
TEMP_7 = dlmread('CP_Trajectory_152.5_7.dat');
TEMP_8 = dlmread('CP_Trajectory_152.5_8.dat');
TEMP_9 = dlmread('CP_Trajectory_152.5_9.dat');
TEMP_10 = dlmread('CP_Trajectory_152.5_10.dat');
TEMP_11 = dlmread('CP_Trajectory_152.5_11.dat');
TEMP_12 = dlmread('CP_Trajectory_152.5_12.dat');
TEMP_13 = dlmread('CP_Trajectory_152.5_13.dat');
TEMP_14 = dlmread('CP_Trajectory_152.5_14.dat');
TEMP_15 = dlmread('CP_Trajectory_152.5_15.dat');
TEMP_16 = dlmread('CP_Trajectory_152.5_16.dat');
TEMP_17 = dlmread('CP_Trajectory_152.5_17.dat');
TEMP_18 = dlmread('CP_Trajectory_152.5_18.dat');
TEMP_19 = dlmread('CP_Trajectory_152.5_19.dat');
TEMP_20 = dlmread('CP_Trajectory_152.5_20.dat');
TEMP_21 = dlmread('CP_Trajectory_152.5_21.dat');
TEMP_22 = dlmread('CP_Trajectory_152.5_22.dat');
TEMP_23 = dlmread('CP_Trajectory_152.5_23.dat');
TEMP_24 = dlmread('CP_Trajectory_152.5_24.dat');
TEMP_25 = dlmread('CP_Trajectory_152.5_25.dat');
TEMP_26 = dlmread('CP_Trajectory_152.5_26.dat');
TEMP_27 = dlmread('CP_Trajectory_152.5_27.dat');
TEMP_28 = dlmread('CP_Trajectory_152.5_28.dat');
TEMP_29 = dlmread('CP_Trajectory_152.5_29.dat');
TEMP_30 = dlmread('CP_Trajectory_152.5_30.dat');

Time_1 = TEMP_1(:,1);
Time_2 = TEMP_2(:,1);
Time_3 = TEMP_3(:,1);
Time_4 = TEMP_4(:,1);
Time_5 = TEMP_5(:,1);
Time_6 = TEMP_6(:,1);
Time_7 = TEMP_7(:,1);
Time_8 = TEMP_8(:,1);
Time_9 = TEMP_9(:,1);
Time_10 = TEMP_10(:,1);
Time_11 = TEMP_11(:,1);
Time_12 = TEMP_12(:,1);
Time_13 = TEMP_13(:,1);
Time_14 = TEMP_14(:,1);
Time_15 = TEMP_15(:,1);
Time_16 = TEMP_16(:,1);
Time_17 = TEMP_17(:,1);
Time_18 = TEMP_18(:,1);
Time_19 = TEMP_19(:,1);
Time_20 = TEMP_20(:,1);
Time_21 = TEMP_21(:,1);
Time_22 = TEMP_22(:,1);
Time_23 = TEMP_23(:,1);
Time_24 = TEMP_24(:,1);
Time_25 = TEMP_25(:,1);
Time_26 = TEMP_26(:,1);
Time_27 = TEMP_27(:,1);
Time_28 = TEMP_28(:,1);
Time_29 = TEMP_29(:,1);
Time_30 = TEMP_30(:,1);

CP_1 = TEMP_1(:,2);
CP_2 = TEMP_2(:,2);
CP_3 = TEMP_3(:,2);
CP_4 = TEMP_4(:,2);
CP_5 = TEMP_5(:,2);
CP_6 = TEMP_6(:,2);
CP_7 = TEMP_7(:,2);
CP_8 = TEMP_8(:,2);
CP_9 = TEMP_9(:,2);
CP_10 = TEMP_10(:,2);
CP_11 = TEMP_11(:,2);
CP_12 = TEMP_12(:,2);
CP_13 = TEMP_13(:,2);
CP_14 = TEMP_14(:,2);
CP_15 = TEMP_15(:,2);
CP_16 = TEMP_16(:,2);
CP_17 = TEMP_17(:,2);
CP_18 = TEMP_18(:,2);
CP_19 = TEMP_19(:,2);
CP_20 = TEMP_20(:,2);
CP_21 = TEMP_21(:,2);
CP_22 = TEMP_22(:,2);
CP_23 = TEMP_23(:,2);
CP_24 = TEMP_24(:,2);
CP_25 = TEMP_25(:,2);
CP_26 = TEMP_26(:,2);
CP_27 = TEMP_27(:,2);
CP_28 = TEMP_28(:,2);
CP_29 = TEMP_29(:,2);
CP_30 = TEMP_30(:,2);

Time_1 = Time_1 - Time_1(1);
Time_2 = Time_2 - Time_2(1);
Time_3 = Time_3 - Time_3(1);
Time_4 = Time_4 - Time_4(1);
Time_5 = Time_5 - Time_5(1);
Time_6 = Time_6 - Time_6(1);
Time_7 = Time_7 - Time_7(1);
Time_8 = Time_8 - Time_8(1);
Time_9 = Time_9 - Time_9(1);
Time_10 = Time_10 - Time_10(1);
Time_11 = Time_11 - Time_11(1);
Time_12 = Time_12 - Time_12(1);
Time_13 = Time_13 - Time_13(1);
Time_14 = Time_14 - Time_14(1);
Time_15 = Time_15 - Time_15(1);
Time_16 = Time_16 - Time_16(1);
Time_17 = Time_17 - Time_17(1);
Time_18 = Time_18 - Time_18(1);
Time_19 = Time_19 - Time_19(1);
Time_20 = Time_20 - Time_20(1);
Time_21 = Time_21 - Time_21(1);
Time_22 = Time_22 - Time_22(1);
Time_23 = Time_23 - Time_23(1);
Time_24 = Time_24 - Time_24(1);
Time_25 = Time_25 - Time_25(1);
Time_26 = Time_26 - Time_26(1);
Time_27 = Time_27 - Time_27(1);
Time_28 = Time_28 - Time_28(1);
Time_29 = Time_29 - Time_29(1);
Time_30 = Time_30 - Time_30(1);

cd ..



