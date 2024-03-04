"""Following in Chargaff’s footsteps, we’ll analyze a real chromosome, 
represented as a string, and measure the different nucleotide populations in much the same way.
Following in Chargaff’s footsteps, we’ll analyze a real chromosome, represented as a string, 
and measure the different nucleotide populations in much the same way.

Write a function in Python that takes a string of DNA and counts the number of thymine(T) nucleotides within it."""



# Input sequence
test_sequence = "ACAACATACAAAGGGCCACAGATACATCAAAAAATGCTCAACATCACTATTTGTCAGGGAAGTACTAATTAAAACCAAAATGAGATGTCCCCTCAAACCTGTTAGAATGGCTATTATCAAAAAGATGAAAGATAGCAACTATCAGAGAGGATGATAGAAAAGGGAACCCTTGCATCATGTACAAATTAAAAATAGAACTATCACATGATCCAAGAATCCTACTTCTGGGTATATAGCCAAAGGAATTGAAATCAATATGTCAAAGGGATATCTGCACTCCTATGTTATTGCAGCATGTTCACAATGGCCAAGATATAGAATCAACCTAACTGTTCATAGACAGATGAATGGATAAATGAAATGTGATATGGAAAATTATTCAGCCTTAAAAACAGTAGGAAATTCTGTCATTTGAGACAACGTGGATGAACCTAGAGGACATTAAGCTAAGTGAAATAAGCTAGACACAGAAAGACAAATATTGCATGATCTCACTTAGAATCTAAAAAATCTGAACTCATAGAAGCAGAGAATAGTATGATGGTTACTAGGGTTATCTGGCAGGGAGAGGATGAGGAAATGGGACATTGTTAATAAAAGGAAAAAAATTCAATTAGTAGG"

def length(string):
    length = 0;
    # Make a function here that counts the number of nucleotides in the input 
    # sequence, return as variable "length".
    for i in string:
        if i is 'T':
            length += 1
    return {'Thyamine': length }

# Print your result.
print(length(test_sequence))