#!/bin/bash
#This script packs the relavant files into a compressed file for upload to the cluster, January 24th 2017

tar -cvf ToCluster_Jan24.tar TimePrimary.py TimeParameterMasterWrite.py StructureGenerator.sh SubmissionScript.sh TimeDriverLocal.py LangevinPropogator.py Potential.py FrictionCalculation.py FrictionTestPrimary.py GeneratePBS.py GeneratePBSFriction.py Parameters.py WorkTheoryModule.py WriteData.py

mv ToCluster_Jan24.tar ToCluster/ToCluster_Jan24.tar


