sequence = "CUGGUGUCGCCGACGGCGCGGGGGCUCGUCUCCCCCACCGCCCGCGGCCUAGUAUCACCAACAGCACGAGGACUTGUTUCTCCTACTGCTCGTGGT"
####LEUCINE####
Leu_list = ["CUG", "CUC", "CUA", "CUT"]

# store the starting positions of the codons
found_Leu_positions = []

n = len(sequence)
k = 0
while k < n-2:
    # extract a three-nucleotide subsequence
    possible_Leu = sequence[k:k+3]
    if possible_Leu in Leu_list:
        found_Leu_positions.append(k)
    k += 3

print('found Leucine at indices {}'.format(found_Leu_positions))
####VALINE####
Val_list = ["GUG", "GUC", "GUA", "GUT"]
found_Val_positions = []
n = len(sequence)
k = 0
while k < n-2:
    possible_Val = sequence[k:k+3]
    if possible_Val in Val_list:
        found_Val_positions.append(k)
    k += 3
print('found Valine at indices {}'.format(found_Val_positions))
####SERINE####
Ser_list = ["UCG", "UCC", "UCA", "UCT"]
found_Ser_positions = []
n = len(sequence)
k = 0
while k < n-2:
    possible_Ser = sequence[k:k+3]
    if possible_Ser in Ser_list:
        found_Ser_positions.append(k)
    k += 3
print('found Serine at indices {}'.format(found_Ser_positions))
####PROLINE####
Pro_list = ["CCG", "CCC", "CCA", "CCT"]
found_Pro_positions = []
n = len(sequence)
k = 0
while k < n-2:
    possible_Pro = sequence[k:k+3]
    if possible_Pro in Pro_list:
        found_Pro_positions.append(k)
    k += 3
print('found Proline at indices {}'.format(found_Pro_positions))
####THREONINE####
Thr_list = ["ACG", "ACC", "ACA", "ACT"]
found_Thr_positions = []
n = len(sequence)
k = 0
while k < n-2:
    possible_Thr = sequence[k:k+3]
    if possible_Thr in Thr_list:
        found_Thr_positions.append(k)
    k += 3
print('found Threonine at indices {}'.format(found_Thr_positions))
####ALANINE####
Ala_list = ["GCG", "GCC", "GCA", "GCT"]
found_Ala_positions = []
n = len(sequence)
k = 0
while k < n-2:
    possible_Ala = sequence[k:k+3]
    if possible_Ala in Ala_list:
        found_Ala_positions.append(k)
    k += 3
print('found Alanine at indices {}'.format(found_Ala_positions))
####ARGININE####
Arg_list = ["CGG", "CGC", "CGA", "CGT"]
found_Arg_positions = []
n = len(sequence)
k = 0
while k < n-2:
    possible_Arg = sequence[k:k+3]
    if possible_Arg in Arg_list:
        found_Arg_positions.append(k)
    k += 3
print('found Arginine at indices {}'.format(found_Arg_positions))
####GLYCINE####
Gly_list = ["GGG", "GGC", "GGA", "GGT"]
found_Gly_positions = []
n = len(sequence)
k = 0
while k < n-2:
    possible_Gly = sequence[k:k+3]
    if possible_Gly in Gly_list:
        found_Gly_positions.append(k)
    k += 3
print('found Glycine at indices {}'.format(found_Gly_positions))




