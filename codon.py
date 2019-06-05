seq_a='ATGCAATGCCCTGATTTGGGG'
seq_b='ATGCAATGCCTTGATTAGAAA'

length_a = len(seq_a)
length_b = len(seq_b)

if (length_a == length_b):
    print('will run ')
else:
    ('***See a programmer because program is broken***')
    
print(list(seq_a))
print(list(seq_b))

print('____________________')

#breaks string into 3 equal parts instead of one long string
seq_a_codon=[seq_a[i:i+3] for i in range(0, len(seq_a), 3)]
seq_b_codon=[seq_b[i:i+3] for i in range(0, len(seq_b), 3)]
print('Codon group for string A is ' +str(seq_a_codon))
print('Codon group for string B is ' +str(seq_b_codon))

print('____________________')

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


print(different_codons)

#part that finds the third base only

print('____________________')

i=0
thirdbaseA = []
thirdbaseB = []
while i < len(different_codons):
    A,B = different_codons[i]
    Alist = list(A)
    Blist = list(B)
    print('A list is '+ str(Alist))
    print(Blist)
    Alist[2]
    thirdbaseA.append(Alist)
    thirdbaseB.append(Blist)
    i+=1
print('____________________')
#makes pairs mutable by inserting it into a list
print(thirdbaseA)
print(thirdbaseB)

counter=0
n=0

print(thirdbaseA)
empty =[]
while counter < (len(thirdbaseA)-1):
    if thirdbaseA[n][2] == thirdbaseB[n][2]:
        n+=1
        counter+=1
    else:
        empty.append(thirdbaseA[n])

print(empty)

