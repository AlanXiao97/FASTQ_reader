the_file=input("Enter the fastq file name with extension ")
with open(the_file,"r") as file:
	fastq_info=file.readlines()
with open("fastq_raw_sequence.fastq","w",newline="") as file:
	i=1
	for n in range(int(len(fastq_info)/4)):
		file.write(fastq_info[i])
		i += 4


