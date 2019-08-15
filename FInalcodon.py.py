import pprint

string_a='CGAATGAACGAAAATCTATTTACCTCTTTCATTACCCCTATAATTCTAGGCCTTCCCCTCGTTACCCTAATTGTCTTATTCCCTAGCCTATTATTTCCAACATCAAACCGACTAATAAATAACCGCCTTATCTCTCTTCAACAATGAGTACTTCAACTTGTATCAAAGCAAATAATAAGCATCCACAACCCCAAAGGACAAACATGAGCACTTATACTGATATCCTTAATTCTATTTATTGGATCAACAAACTTACTAGGCCTACTACCTCACTCTTTTACACCAACTACACAACTATCAATAAATCTAGGTATAGCCATCCCCCTATGAGCAGGAGCTGTAATCACGGGCTTCCGCAACAAAACTAAAGCATCACTTGCCCATTTCTTACCACAAGGAACACCCACCCCTCTAATCCCTATACTAGTAATTATCGAAACTATTAGTCTATTTATTCAACCAATAGCCCTCGCAGTACGATTAACAGCCAATATTACAGCAGGACACCTATTAATTCACCTAATTGGAGGAGCTACATTGGCACTAATAAATATTAGCACTACAACAGCTCTTATTACATTTATTATTTTAGTTTTACTAACAATTCTTGAATTCGCAGTAGCCATAATCCAAGCCTACGTATTTACTCTTTTAGTCAGCCTATATCTACACGATAACACATAA'
string_b='CGUATGAACGAAAATCTATTTACCTCTTTCATTACCCCTATAATTCTAGGCCTCCCCCTCGTCACTCTCATTGTCTTATTCCCTAGCCTACTGTTTCCAACATCAAACCGACTATTAAATAATCGCCTTATCTCTCTTCAACAATGGGCACTTCAACTTGTATCAAAACAAATAATGAGCATCCACAATCCCAAAGGACAAACATGAGCACTTATACTGATATCTCTAATTCTATTCATTGGGTCAACAAACTTACTAGGCCTATTACCCCACTCTTTTACACCAACCACACAACTATCAATAAATCTAGGCATAGCTATCCCCCTATGAGCAGGAGCTGTAATCACGGGCTTCCGCAACAAGACTAAAGCATCACTTGCCCATTTCTTACCACAAGGAACACCCACCCCTCTAATTCCTATACTAGTAATTATCGAAACTATTAGCCTATTTATTCAACCAGTAGCCCTCGCAGTACGATTAACAGCCAATATTACAGCAGGACACCTATTAATTCACMTAATCGGAGGAGCCACATTGGCACTAATAAATATTAGCACTACAACAGCTCTTATTACATTTATTATTTTAGTTTTACTAACAATTCTTGAATTCGCAGTAGCCATAATCCAGGCCTACGTATTTACTCTTCTAGTTAGCCTATACCTACACGATAACACATAA'
#if there is no string C to compare to keep empty quotes or program will not work
#Ex: string_c=''
string_c='ATGAACGAAAATCTATTTACCTCTTTCATTACCCCTATAATTCTAGGCCTTCCCCTCGTTACTCTAATTGTCTTATTCCCTAGCCTATTATTTCCAACATCAAATCGACTAATAAATAACCGTCTTATCTCTCTTCAACAGTGAGTACTTCAACTTGTATCAAAACAAATAATAAGCATCCATAACCCCAAAGGACAAACATGAGCACTTATATTGATATCCTTAATTCTATTTATTGGGTCAACAAACTTACTAGGCCTACTACCCCACTCTTTTACACCAACCACACAACTATCAATAAATTTAGGTATAGCTATCCCCCTATGAGCAGGAGCTGTAATCACGGGCTTCCGCAACAAAACTAAAGCATCACTTGCCCACTTCTTACCACAAGGAACACCCACCCCTCTAATCCCTATACTAGTAATTATCGAAACTATTAGCCTATTTATTCAACCAGTAGCCCTCGCAGTACGATTAACAGCCAATATTACAGCAGGACACCTATTAATTCACCTAATCGGAGGAGCCACATTAGCACTAATAAATATTAGCACTACAACAGCTCTTATTACATTTATTATTTTAGTTTTACTAACAATTCTTGAATTCGCAGTAGCTATAATCCAAGCCTACGTATTTACTCTTCTAGTTAGCCTATACCTACACGATAACACATAATAA'

def codon(seq_a,seq_b):
    length_a = len(seq_a)
    length_b = len(seq_b)

    #made to check if seq a and b are the same length
    if (length_a == length_b):
        print('Loading... ')
    elif (len(seq_a) != len(seq_b)):
        print('***Go cry in a corner cause program will not work, The sequences are not the same Length***')
        quit()

    #breaks string into 3 equal parts instead of one long string
    seq_a_codon=[seq_a[i:i+3] for i in range(0, len(seq_a), 3)]
    seq_b_codon=[seq_b[i:i+3] for i in range(0, len(seq_b), 3)]


    #made to check if it is possible to break the sequences into 3 seperate pieces equally
    for stuff in seq_a_codon:
        if len(stuff) != 3:
            print('***Exit the program and throw your computer at the wall because of the disappointment you\'ve brought to your parents: Error A there are missing base pair(s) ***')
            quit()
    for stuff in seq_b_codon:
        if len(stuff) != 3:
            print('***Exit the program and throw your computer at the wall because of the disappointment you\'ve brought to your parents: Error B there are missing base pair(s) ***')
            quit()

    start =0
    difference=0
    similar=0
    n=0
    different_codons=[]
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


    i=0
    thirdbaseA = []
    thirdbaseB = []
    while i < len(different_codons):
        A,B = different_codons[i]
        #hereistheproblem
        Alist = list(A)
        Blist = list(B)
        thirdbaseA.append(Alist)
        thirdbaseB.append(Blist)
        i+=1


    #makes pairs mutable by inserting it into a list

    if not thirdbaseA:
        print('There is no similarities seq A')
        quit()
    if not thirdbaseB:
        print('There is no similaarities seq B')
        quit()
        
    counter=0
    n=0
    pairs =[]
    #algorithm that determines if 3rd base are not equal and if so are stored into pairs with a tuple
    while counter < (len(thirdbaseA)):
        if thirdbaseA[n][2] == thirdbaseB[n][2]:
            n+=1
            counter+=1
        elif thirdbaseA[n][2] != thirdbaseB[n][2]:
            if (thirdbaseA[n][0] == thirdbaseB[n][0]) and (thirdbaseA[n][1] == thirdbaseB[n][1]):
                seq_a_base = thirdbaseA[n]
                seq_b_base = thirdbaseB[n]
                compare =(seq_a_base,seq_b_base)
                pairs.append(compare)
                counter+=1
                n+=1
            else:
                counter+=1
                n+=1
            
    if not pairs:
        print('**The first two bases for codons are the same**')
        quit()
    print('____________________')


    bothGlycine=[]
    bothAlanine=[]
    bothValine=[]
    bothTheronine =[]
    bothArginine =[]
    bothProline=[]
    bothLeucine=[]
    bothSerine=[]


    def tuplereader(pair):
        Glycine = 0
        Alanine = 0
        Valine = 0
        Threonine = 0
        Arginine = 0
        Proline = 0
        Leucine = 0
        Serine = 0
        for i in pair:
            if (i[0][0] == 'A') and (i[0][1] == 'C'):
                Threonine +=1
                bothTheronine.append(i)
            elif (i[0][0] == 'G') and (i[0][1] == 'T'):
                Valine +=1
                bothValine.append(i)
            elif (i[0][0] == 'G') and (i[0][1] == 'C'):
                Alanine +=1
                bothAlanine.append(i)
            elif (i[0][0] == 'G') and (i[0][1] == 'G'):
                Glycine +=1
                bothGlycine.append(i)
            elif (i[0][0] == 'T') and (i[0][1] == 'C'):
                Serine +=1
                bothSerine.append(i)
            elif (i[0][0] == 'C') and (i[0][1] == 'T'):
                Leucine +=1
                bothLeucine.append(i)
            elif (i[0][0] == 'C') and (i[0][1] == 'C'):
                Proline +=1
                bothProline.append(i)
            elif (i[0][0] == 'C') and (i[0][1] == 'G'):
                Arginine +=1
                bothArginine.append(i)
            else:
                continue
        for i in pair:
            if (i[1][0] == 'A') and (i[1][1] == 'C'):
                Threonine +=1
                bothTheronine.append(i)
            elif (i[1][0] == 'G') and (i[1][1] == 'T'):
                Valine +=1
                bothValine.append(i)
            elif (i[1][0] == 'G') and (i[1][1] == 'C'):
                Alanine +=1
                bothAlanine.append(i)
            elif (i[1][0] == 'G') and (i[1][1] == 'G'):
                Glycine +=1
                bothGlycine.append(i)
            elif (i[1][0] == 'T') and (i[1][1] == 'C'):
                Serine +=1
                bothSerine.append(i)
            elif (i[1][0] == 'C') and (i[1][1] == 'T'):
                Leucine +=1
                bothLeucine.append(i)
            elif (i[1][0] == 'C') and (i[1][1] == 'C'):
                Proline +=1
                bothProline.append(i)
            elif (i[1][0] == 'C') and (i[1][1] == 'G'):
                Arginine +=1
                bothArginine.append(i)
            else:
                continue
        print('How many amino acids are present:')
        print('Glycine : %s, \nAlanine: %s, \nValine: %s, \nThreonine: %s, \nArginine: %s, \nProline: %s, \nLeucine: %s, \nSerine: %s' %(Glycine, Alanine, Valine, Threonine, Arginine, Proline, Leucine, Serine))
        print('________________')
    tuplereader(pairs)
    pprint.pprint(pairs)
    print('________________')
    pprint.pprint('Theronine changes are '+ str(bothTheronine))
    pprint.pprint('Valine changes are '+ str(bothValine))
    pprint.pprint('Alanine changes are '+ str(bothAlanine))
    pprint.pprint('Glycine changes are '+ str(bothGlycine))
    pprint.pprint('Serine changes are '+ str(bothSerine))
    pprint.pprint('Leucine changes are '+ str(bothLeucine))
    pprint.pprint('Proline changes are '+ str(bothProline))
    pprint.pprint('Arginine changes are '+ str(bothArginine))

    print('________________')
    def changecounter(L):
        AtoT_or_TtoA = 0
        AtoC_or_TtoG = 0
        TtoC_or_AtoG = 0
        CtoG_or_GtoC = 0
        CtoA_or_GtoT = 0
        GtoA_or_CtoT = 0
        for k,v in L:
            if (k[2] == 'A' and v[2] == 'T') or (k[2] == 'T' and v[2] == 'A'):
                 AtoT_or_TtoA +=1
            elif (k[2] == 'A' and v[2] == 'C') or (k[2] == 'T' and v[2] == 'G'):
                AtoC_or_TtoG +=1
            elif (k[2] == 'T' and v[2] == 'C') or (k[2] == 'A' and v[2] == 'G'):
                TtoC_or_AtoG +=1
            elif (k[2] == 'C' and v[2] == 'G') or (k[2] == 'G' and v[2] == 'C'):
                CtoG_or_GtoC +=1
            elif (k[2] == 'C' and v[2] == 'A') or (k[2] == 'G' and v[2] == 'T'):
                CtoA_or_GtoT +=1
            elif (k[2] == 'G' and v[2] == 'A') or (k[2] == 'C' and v[2] == 'T'):
                GtoA_or_CtoT +=1

        print('A to T or T to A: ' + str(AtoT_or_TtoA))
        print('A to C or T to G: ' + str(AtoC_or_TtoG))
        print('T to C or A to G: ' + str(TtoC_or_AtoG))
        print('C to G or G to C: ' + str(CtoG_or_GtoC))
        print('C to A or G to T: ' + str(CtoA_or_GtoT))
        print('G to A or C to T: ' + str(GtoA_or_CtoT))
    print('Theronine:')
    changecounter(bothTheronine)
    print('________________')
    print('Valine: ')
    changecounter(bothValine)
    print('________________')
    print('Alanine: ')
    changecounter(bothAlanine)
    print('________________')
    print('Glycine: ')
    changecounter(bothGlycine)
    print('________________')
    print('Serine: ')
    changecounter(bothSerine)
    print('________________')
    print('Leucine: ')
    changecounter(bothLeucine)
    print('________________')
    print('Proline: ')
    changecounter(bothProline)
    print('________________')
    print('Arginine: ')
    changecounter(bothArginine)

print('Seq A vs Seq B')
codon(string_a,string_b)
print('''

______________________________________________________________________

Seq A vs Seq C

''')
if not string_c:
    print('String C is empty; Program will end' )
    quit()
else:
    pass
codon(string_a,string_c)
