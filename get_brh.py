from Bio import SeqIO
records= list(SeqIO.parse('blast_database_FCG2018.fasta', 'fasta')) #Database of interest

file= open('PENPO_0016_090XX_blastp','r') # Blast file of the sequence (XX) of interest

# Take the 20 best orthologous sequences
c=0
hits=[]
for i in file:
	if c<20:
		x=i.split('\t')		# split by tabs
		hits.append(x[1])	# Take the second column (the one with the orthologous id)
		c+=1
	else:
		break

#Look for the id in the database and print the sequence in fasta format		
for j in hits:
	for i in records:
		if i.id==j:
			print('>'+j)
			print(i.seq)	

