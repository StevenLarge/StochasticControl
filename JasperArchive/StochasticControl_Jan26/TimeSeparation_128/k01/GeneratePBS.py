#This Python script generates the a basic PBS runscript for submitting westgrid jobs to the cluster
#
#Steven Large
#June 29th 2016

filename = 'SubmissionScript.pbs'

file1 = open(filename, 'w')

file1.write('#!/bin/bash\n')
file1.write('# PBS -S /bin/bash\n\n')
file1.write('#PBS run script for Westgrid Jobs\n\n')

file1.write('cd $PBS_O_WORKDIR\n\n')
file1.write('echo \'Current Working Directory is `pwd`\'\n')
file1.write('echo \'Running job on Hostname `hostname`\'\n\n')

file1.write('echo \'Starting run at: `date`\'\n\n')

file1.write('python TimePrimary.py\n\n')

file1.write('echo \'Finsihed Execution\'')

file1.close()



