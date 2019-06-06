import pprint

seq_a='ATGAACGAAAATCTATTTACCTCTTTCATTACCCCTATAATTCTAGGCCTTCCCCTCGTTACCCTAATTGTCTTATTCCCTAGCCTATTATTTCCAACATCAAACCGACTAATAAATAACCGCCTTATCTCTCTTCAACAATGAGTACTTCAACTTGTATCAAAGCAAATAATAAGCATCCACAACCCCAAAGGACAAACATGAGCACTTATACTGATATCCTTAATTCTATTTATTGGATCAACAAACTTACTAGGCCTACTACCTCACTCTTTTACACCAACTACACAACTATCAATAAATCTAGGTATAGCCATCCCCCTATGAGCAGGAGCTGTAATCACGGGCTTCCGCAACAAAACTAAAGCATCACTTGCCCATTTCTTACCACAAGGAACACCCACCCCTCTAATCCCTATACTAGTAATTATCGAAACTATTAGTCTATTTATTCAACCAATAGCCCTCGCAGTACGATTAACAGCCAATATTACAGCAGGACACCTATTAATTCACCTAATTGGAGGAGCTACATTGGCACTAATAAATATTAGCACTACAACAGCTCTTATTACATTTATTATTTTAGTTTTACTAACAATTCTTGAATTCGCAGTAGCCATAATCCAAGCCTACGTATTTACTCTTTTAGTCAGCCTATATCTACACGATAACACATAA'
seq_b='ATGAACGAAAATCTATTTACCTCTTTCATTACCCCTATAATTCTAGGCCTCCCCCTCGTCACTCTCATTGTCTTATTCCCTAGCCTACTGTTTCCAACATCAAACCGACTATTAAATAATCGCCTTATCTCTCTTCAACAATGGGCACTTCAACTTGTATCAAAACAAATAATGAGCATCCACAATCCCAAAGGACAAACATGAGCACTTATACTGATATCTCTAATTCTATTCATTGGGTCAACAAACTTACTAGGCCTATTACCCCACTCTTTTACACCAACCACACAACTATCAATAAATCTAGGCATAGCTATCCCCCTATGAGCAGGAGCTGTAATCACGGGCTTCCGCAACAAGACTAAAGCATCACTTGCCCATTTCTTACCACAAGGAACACCCACCCCTCTAATTCCTATACTAGTAATTATCGAAACTATTAGCCTATTTATTCAACCAGTAGCCCTCGCAGTACGATTAACAGCCAATATTACAGCAGGACACCTATTAATTCACMTAATCGGAGGAGCCACATTGGCACTAATAAATATTAGCACTACAACAGCTCTTATTACATTTATTATTTTAGTTTTACTAACAATTCTTGAATTCGCAGTAGCCATAATCCAGGCCTACGTATTTACTCTTCTAGTTAGCCTATACCTACACGATAACACATAA'

length_a = len(seq_a)
length_b = len(seq_b)

if (length_a == length_b):
    print('Loading... ')
else:
    ('***See a programmer because program is broken***')
'''
print('____________________')
print(list(seq_a))
print(list(seq_b))

print('____________________')
'''

#breaks string into 3 equal parts instead of one long string
seq_a_codon=[seq_a[i:i+3] for i in range(0, len(seq_a), 3)]
seq_b_codon=[seq_b[i:i+3] for i in range(0, len(seq_b), 3)]
'''
print('Codon group for string A is ' +str(seq_a_codon))
print('Codon group for string B is ' +str(seq_b_codon))

print('____________________')
'''

start =0
difference=0
similar=0
n=0
different_codons=[]
#algorithm for script
#assume that all the sequences are equal in length 
while start < (len(seq_a_codon) and len(seq_b_codon)):
    #puts different group into tuples to make sure it is immutible in the program
    if seq_a_codon[n] != seq_b_codon[n]:
        difference +=1
        a=seq_a_codon[n]
        b=seq_b_codon[n]
        differences=(a,b)
        different_codons.append(differences)
        #appends tuples to list
    elif seq_a_codon[n] == seq_b_codon[n]:
        similar +=1
        #delete chunk on similar before moving to excel
    else:
        pass
    start +=1
    n+=1


#print(different_codons)

#part that finds the third base only

i=0
thirdbaseA = []
thirdbaseB = []
while i < len(different_codons):
    A,B = different_codons[i]
    Alist = list(A)
    Blist = list(B)
    Alist[2]
    thirdbaseA.append(Alist)
    thirdbaseB.append(Blist)
    i+=1
#makes pairs mutable by inserting it into a list
#print('____________________')

#print('This is thirdbaseA '+ str(thirdbaseA))
#print('This is thirdbaseB ' +str(thirdbaseB))

counter=0
n=0
pairs =[]
#algorithm that determines if 3rd base are equal and if so are stored into pairs with a tuple
while counter < (len(thirdbaseA)):
    if thirdbaseA[n][2] == thirdbaseB[n][2]:
        n+=1
        counter+=1
    elif thirdbaseA[n][2] != thirdbaseB[n][2]:
        seq_a_base = thirdbaseA[n]
        seq_b_base = thirdbaseB[n]
        compare =(seq_a_base,seq_b_base)
        pairs.append(compare)
        counter+=1
        n+=1
print('____________________')
print('Pairs of codons that are different '+ str(pairs))
print('____________________')

pprint.pprint(pairs)
#Protiens which codons code for.


