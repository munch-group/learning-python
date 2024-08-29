
from math import log

# Write your code below:


def sequence_difference(seq1, seq2):
    differences = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            differences += 1
    return differences / len(seq1)


def jukes_cantor(dist):
    return -(3/4) * log(1 - (4/3)*dist)


def lower_trian_matrix(seq_list):
    lower_trian = []
    for i in range(len(seq_list)):
        row = []
        for j in range(i):
            diff = sequence_difference(seq_list[i], seq_list[j])
            row.append(jukes_cantor(diff))
        lower_trian.append(row)
    return lower_trian


def find_lowest_cell(table):
    x = 1
    y = 0
    min_val = table[x][y]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] < min_val:
                min_val = table[i][j]
                x = i
                y = j
    return [x, y]


def link(x, y):
    # mean, makes this WPGMA (centroid-like linking - not UPGMA)
    return (x + y) / 2
    # return min(x, y)
    # return max(x, y)


def update_labels(labels, i, j):

    # turn the label at first index into a combination of both labels
    labels[j] = "({},{})".format(labels[j], labels[i])
    # labels[j] = (labels[j], labels[i])

    # Remove the (now redundant) label in the first index
    del labels[i]


def update_table(table, a, b):

    # For the lower index, reconstruct the entire row (ORANGE)
    for i in range(0, b):
        table[b][i] = link(table[b][i], table[a][i])

    # Link cells to update the column above the min cell (BLUE)
    for j in range(b+1, a):
        table[j][b] = link(table[j][b], table[a][j])
        
    # Link cells to update the column below the min cell (RED)
    for i in range(a+1, len(table)):
        table[i][b] = link(table[i][b], table[i][a])

    # Delete cells we no longr need (GREY)
    for i in range(a+1, len(table)):
        # Remove the (now redundant) first index column entry
        del table[i][a]
    # Remove the (now redundant) first index row
    del table[a] 


def cluster(sequences, names):

    table = lower_trian_matrix(sequences)
    labels = names[:]

    # Until all labels have been joined...
    while len(labels) > 1:
        # Locate lowest cell in the table
        i, j = find_lowest_cell(table)

        # Join the table on the cell co-ordinates
        update_table(table, i, j)

        # Update the labels accordingly
        update_labels(labels, i, j)

    # Return the final label
    return labels[0]



def read_fasta(filename):

    f = open(filename, 'r')

    record_list = []
    header = ""
    sequence = ""
    for line in f:
        line = line.strip() ## get rid of whitespace and newline
        if line.startswith(">"):
            if header != "": ## if it is the first header
                record_list.append([header, sequence])
                sequence = ""
            header = line[1:]
        else:
            sequence += line
    record_list.append([header, sequence])

    return record_list


if __name__ == "__main__":

#    names = ['A', 'B', 'C','D']
    names = ['Henning', 'Preben', 'Mogens', 'Kurt']
    sequences = ['TAAAAAAAAAAA', 
                 'TTAAAAAAAAAA', 
                 'AAAAAAAAAAGG', 
                 'AAAAAAAAGGGG']

    print(cluster(sequences, names))

    print(lower_trian_matrix(sequences))

    if False:
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns

        diffs = np.linspace(0, 0.7499, 750)
        lens = [jukes_cantor(p) for p in diffs]
        with sns.plotting_context('poster', font_scale=1.5):
            with sns.axes_style('whitegrid'):
                with sns.color_palette("Set2", 2):
                    d = np.linspace(0, 1, 10)

                    plt.plot(d, d, '--')
                    plt.plot(lens, diffs, 'r')
                    plt.ylabel('Obervable substutitions')
                    plt.xlabel('Actual substutitions')

                    # plt.xlabel('Obervable substutitions')
                    # plt.ylabel('Actual substutitions')
                    # plt.plot(diffs, lens, 'r')

                    plt.savefig('tmp.pdf')

