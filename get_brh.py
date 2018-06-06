from Bio import SeqIO
records= list(SeqIO.parse('blast_database_FCG2018.fasta', 'fasta'))
file= open('20first52.txt','r')

file= open('PENPO_0016_09048_blastp','r')
c=0
hits=[]
for i in file:
	if c<20:
		x=i.split('\t')
		hits.append(x[1])
		c+=1
	else:
		break
		
for j in hits:
	for i in records:
		if i.id==j:
			print('>'+j)
			print(i.seq)	

