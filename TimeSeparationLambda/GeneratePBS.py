#This Python script generates the a basic PBS runscript for submitting westgrid jobs to the cluster
#
#Steven Large
#June 29th 2016

Spring = [1,2,4,8,16,32,64,75]

for index in range(len(Spring)):

	filename = 'SubmissionScript_k' + str(Spring[index]) + '.pbs'

	WriteCommand = 'python WorkCalculation_k' + str(Spring[index]) + '.py\n\n'

	file1 = open(filename, 'w')

	file1.write('#!/bin/bash\n')
	file1.write('# PBS -S /bin/bash\n\n')
	file1.write('#PBS run script for Westgrid Jobs\n\n')	
	file1.write('cd $PBS_O_WORKDIR\n\n')
	file1.write('echo \'Current Working Directory is `pwd`\'\n')
	file1.write('echo \'Running job on Hostname `hostname`\'\n\n')
	file1.write('echo \'Starting run at: `date`\'\n\n')
	file1.write(WriteCommand)
	file1.write('echo \'Finished Execution\'')

	file1.close()
