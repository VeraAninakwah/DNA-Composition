"""the very first genome to be sequenced fully (by Sanger in 1977 and later the first genome to be created synthetically (by Venter in 
2003).

This genome is a common case study in biology since it is only about 
5300 nucleotides long and belongs to the humble bacteriophage φX174
a virus which infects and hijacks the cellular machinery of bacterial cells."""

from Bio import SeqIO

with open('data/human-PrR1jPIaAG.fasta', 'r') as phage_file:
    phage_records = SeqIO.parse(phage_file, 'fasta')
    for record in phage_records:
        # Access sequence ID
        phage_id = record.id
        # Access sequence
        phage_sequence = str(record.seq)
        #print("phage_id:", phage_id)
        print("phage_Sequence:", phage_sequence)



def phage(string):
    count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

    for char in string:
        if char == 'A':
            count[char] += 1
        if char == 'T':
            count[char] += 1
        if char == 'C':
            count[char] += 1
        if char == 'G':
            count[char] += 1

    return count


phagee = phage(phage_sequence)
print('bacteriophage:', phagee)