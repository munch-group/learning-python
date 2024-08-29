
codon_map = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
             'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 
             'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*', 
             'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W', 
             'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
             'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 
             'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 
             'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 
             'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 
             'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 
             'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 
             'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 
             'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 
             'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 
             'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 
             'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

# Write your functions below


def split_codons(orf):
    codon_list = []
    for i in range(0, len(orf)-2, 3):
        codon_list.append(orf[i:i+3])
    return codon_list


def count_codons(orf):
    orf = orf.upper()
    codon_list = split_codons(orf)
    counts = {}
    for codon in codon_map:
        counts[codon] = 0
    for codon in codon_list:
        counts[codon] += 1
    return counts


def group_counts_by_amino_acid(codon_counts):
    counts_by_amino_acid = {}
    for codon in codon_counts:
        acid = codon_map[codon]
        if acid not in counts_by_amino_acid:
            counts_by_amino_acid[acid] = {}
        counts_by_amino_acid[acid][codon] = codon_counts[codon]
    return counts_by_amino_acid


# maybe next year make a function that normalizes one innter dict:
def normalize_counts(counts):
    total_count = sum(counts.values())
    if total_count:
        freqs = {}
        for codon in counts:
            freqs[codon] = counts[codon] / total_count
        return freqs

def normalize_grouped_counts(grouped_counts):
    grouped_freqs = {}
    for aa in grouped_counts:
        counts = grouped_counts[aa]
        freqs = normalize_counts(counts)
        if freqs:
            grouped_freqs[aa] = freqs
    return grouped_freqs

# def normalize_grouped_counts(grouped_counts):
#     grouped_freqs = {}
#     for aa in grouped_counts:
#         total_count = sum(grouped_counts[aa].values())
#         if total_count:
#             grouped_freqs[aa] = {}
#             for codon in grouped_counts[aa]:
#                 grouped_freqs[aa][codon] = grouped_counts[aa][codon] / float(total_count)
#     return grouped_freqs


def codon_usage(orf):
    codon_counts = count_codons(orf)
    stats_per_amino_acid = group_counts_by_amino_acid(codon_counts)
    freqs = normalize_grouped_counts(stats_per_amino_acid)
    return freqs
    

"""
if __name__ == "__main__":

    f = open('sample_orfs.txt', 'r')
    orf_list = list()
    for line in f:
        seq = line.strip()
        orf_list.append(seq)
    f.close()

    orf = "ATGTGCGATCCAAAATTACCGCTTTTATTACTCTGA"
#    orf = orf_list[0]
    counts = count_codons(orf)
    print(counts)
    grouped_counts = group_counts_by_amino_acid(counts)
    print(grouped_counts)
    normed = normalize_grouped_counts(grouped_counts)
    print(normed)

    print(normalize_counts({'ATT': 8, 'ATC': 10, 'ATA': 2}))
"""