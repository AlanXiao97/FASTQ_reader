from csv import writer, DictWriter
the_file=input("Enter the fastq file name with extension ")
with open(the_file,"r") as file:
	fastq_info=file.readlines()
with open("fastq_results.csv","w",newline="") as file:
	headers=["sequence identifier","raw sequence","description","quality values"]
	csv_file=DictWriter(file, fieldnames=headers)
	csv_file.writeheader()
	i0=0
	i1=1
	i2=2
	i3=3
	for n in range(int(len(fastq_info)/4)):
		csv_file.writerow({"sequence identifier":fastq_info[i0],
			"raw sequence":fastq_info[i1],
			"description":fastq_info[i2],
			"quality values":fastq_info[i3]})
		i0+=4
		i1+=4
		i2+=4
		i3+=4
		