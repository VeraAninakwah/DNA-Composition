from Bio import SeqIO

# Open the FASTA file and parse it

with open('data/human-PrR1jPIaAG.fasta', 'r') as human_file:
    human_records = SeqIO.parse(human_file, 'fasta')
    for record in human_records:
        # Access sequence ID
        humans_id = record.id
        # Access sequence
        humans_sequence = str(record.seq)
        #print("humans_id:", humans_id)
        #print("humans_Sequence:", humans_sequence)
        
        
with open('data/mosquito-AK2jNK0ahq.fasta', 'r') as mosquito_file:
    mosquito_records = SeqIO.parse(mosquito_file, 'fasta')
    for record in mosquito_records:
        mosquito_id = record.id
        mosquito_sequence = str(record.seq)
        #print("mosquito_id:", mosquito_id)
        #print("mosquito_sequence:", mosquito_sequence)


with open('data/plasmodium-RkREaPiyih.fasta', 'r') as plasmodium_file:
    plasmodium_records = SeqIO.parse(plasmodium_file, 'fasta')
    for record in plasmodium_records:
        plasmodium_id = record.id
        plasmodium_sequence = str(record.seq)
        #print("plasmodium_id:", plasmodium_id)
        #print("plasmodium_sequence:", plasmodium_sequence)

def nucleotides(sequence): 
    count = {'A': 0, 'T':0, 'G': 0, 'C':0}

    for char in sequence:
            if char == 'A':
                count[char] += 1
            if char == 'T':
                count[char] += 1
            if char == 'C':
                count[char] += 1
            if char == 'G':
                count[char] += 1 

    return count

#print the number of each nucleotides in each specimen

humans = nucleotides(humans_sequence)
mosquito = nucleotides(mosquito_sequence)
plasmodium = nucleotides(plasmodium_sequence)


print('humans_sequence:', humans, '\nmosquito_sequence:', mosquito, '\nplasmodium:',plasmodium)








