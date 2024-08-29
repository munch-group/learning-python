def sequence_similarity(seq1, seq2):
    num_similar = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            num_similar = num_similar + 1
    return num_similar / len(seq1)


def alignment_similarity(seq1, seq2):
    num_similar = 0
    num_gap_cols = 0
    for i in range(len(seq1)):
        if seq1[i] == '-' and seq2[i] == '-':
            num_gap_cols = num_gap_cols + 1
        elif seq1[i] == seq2[i]:
            num_similar = num_similar + 1
    return num_similar / (len(seq1) - num_gap_cols)


def read_data(file_name):
    f = open(file_name, 'r')
    sequences = list()
    for line in f:
        seq = line.strip()
        sequences.append(seq)
    f.close()
    return sequences


def load_typed_sequences():
    return {'A': read_data('subtypeA.txt'),
            'B': read_data('subtypeB.txt'),
            'C': read_data('subtypeC.txt'),
            'D': read_data('subtypeD.txt') }


def get_similarities(unknown, typed_sequences):
    list_of_similarities = []
    for target_seq in typed_sequences:
        list_of_similarities.append(alignment_similarity(unknown, target_seq))
    return list_of_similarities


# def get_all_similarities(unknown):
#     return {'A': max(get_similarities(unknown, subtypeA_list)),
#             'B': max(get_similarities(unknown, subtypeB_list)),
#             'C': max(get_similarities(unknown, subtypeC_list)),
#             'D': max(get_similarities(unknown, subtypeD_list))}
def get_max_similarities(unknown, typed_data):
    return {'A': max(get_similarities(unknown, typed_data['A'])),
            'B': max(get_similarities(unknown, typed_data['B'])),
            'C': max(get_similarities(unknown, typed_data['C'])),
            'D': max(get_similarities(unknown, typed_data['D']))}


def predict_subtype(unknown, typed_data):
    d = get_max_similarities(unknown, typed_data)
    max_val = max(d.values())
    for subtype in d:
    	if d[subtype] == max_val:
    		return subtype


# unknown_list = read_data('unknown_type.txt')
# typed_data = load_typed_sequences()
# subtype = predict_subtype(unknown_list[0], typed_data)
# print("Patient HIV is subtype {}".format(subtype))





