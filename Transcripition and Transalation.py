# TRANSCRIPTION AND TRANSLATION USING BIOPYTHON
from Bio.Seq import Seq

dna_input = input("THE SEQUENCE OF DNA: ")
dna = Seq(dna_input.upper())

# Check type of sequence
if set(dna).issubset(set("AUGC")):
    print("RNA")
elif set(dna).issubset(set("ATGC")):
    print("DNA")
else:
    print("NOT ANY GENOMIC SEQ")

# Complement and reverse complement
print("Complement:", dna.complement())
print("Reverse Complement:", dna.reverse_complement())
print(len(dna))

# Transcription to RNA
rna = dna.transcribe()
print("RNA:", rna)
print(len(rna))
# Translation to protein
protein = dna.translate()
print("Protein:", protein)
print(len(protein))
