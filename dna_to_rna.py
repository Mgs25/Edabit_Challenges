def dna_to_rna(strands):
    DNA = {"A":"U", "T":"A", "G":"C", "C":"G"}
    RNA = []
    for strand in strands:
        RNA.append(DNA[strand])
    return "".join(RNA)

print(dna_to_rna("ATTAGCGCGATATACGCGTAC"))