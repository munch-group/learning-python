
def read_data(fileName):
    f = open(fileName)
    data = {}
    for l in f:
        name, seq = l.split()
        data[name] = seq
    f.close()
    return data


def mean_length(reads):
    s = 0
    tot = 0
    for name, seq in reads.items():
        s += len(seq)
        tot += 1
    return s/float(tot)


def get_overlap(left, right):
    max_overlap = min(len(left), len(right))
    for i in range(max_overlap, 0, -1):
        if left[-i:] == right[:i]:
            return left[-i:]
    return ''


def get_all_overlaps(reads):
    d = {}
    for name1 in reads:
        seq1 = reads[name1]
        for name2 in reads:
            seq2 = reads[name2]
            if name1 != name2:
                if name1 not in d:
                    d[name1] = {}
                d[name1][name2] = len(get_overlap(seq1, seq2))
    return d
# OR:
# def get_all_overlaps(reads):
#     all_overlaps = {}
#     for name1 in reads:
#         seq1 = reads[name1]
#         overlaps_to_read = {}
#         for name2 in reads:
#             seq2 = reads[name2]
#             if name1 != name2:
#                 overlaps_to_read[name2] = len(get_overlap(seq1, seq2))
#         all_overlaps[name1] = overlaps_to_read
#     return overlaps    

def pretty_print(d):
    print('      ', end='')
    for j in sorted(d):
        print("{: >6}".format(j), end='')
    print()

    for i in sorted(d):
        print("{: >6}".format(i), end='')
        for j in sorted(d):
            if i == j:
                s = '     -'
            else:
                s = "{: >6}".format(d[str(i)][str(j)])
            print(s, end='')
        print()


def get_left_overlaps(overlaps, right):
    left_overlaps = []
    for left in overlaps:
        if right in overlaps[left]:
            left_overlaps.append(overlaps[left][right])
    return sorted(left_overlaps)


def find_first_read(overlaps):
    for read in overlaps:
        if not max(get_left_overlaps(overlaps, read)) > 2:
            return read


# def find_first_read(overlaps):
#     for i in overlaps:
#         signifOverlaps = False
#         for j in overlaps[i]:
#             if overlaps[j][i] >= 3:
#                 signifOverlaps = True
#         if not signifOverlaps:
#             return i


def find_key_for_largest_value(d):
    m = max(d.values())
    for k in d:
        if d[k] == m:
            return k


# def find_order_of_reads(left_read, d):
#     order = [left_read]
#     right_read = find_key_for_largest_value(d[left_read])
#     for i in range(len(d)):
#         if d[left_read][right_read] > 2:
#             order.append(right_read)
#             left_read = right_read
#             right_read = find_key_for_largest_value(d[left_read])
#     return order

def find_order_of_reads(left_read, d):
    order = [left_read]
    for i in range(len(d)):
        right_read = find_key_for_largest_value(d[left_read])
        if d[left_read][right_read] > 2:
            order.append(right_read)
            left_read = right_read
        else:
            # no significant right overlap, so this must be the end read
            return order

def reconstruct_sequence(readOrder, reads, overlaps):
    genome = ''
    for readName in readOrder[:-1]:
        rightOverlap = max(x for x in overlaps[readName].values() if x >= 3)
        genome += reads[readName][:-rightOverlap]
    genome += reads[readOrder[-1]]
    return genome


def assemble_genome(input_file_name):
    reads = read_data(input_file_name)
    overlaps = get_all_overlaps(reads)
    first = find_first_read(overlaps)
    order = find_order_of_reads(first, overlaps)
    return reconstruct_sequence(order, reads, overlaps)



if __name__ == '__main__':
    fileName = 'sequencing_reads.txt'
    reads = read_data(fileName)
    print(reads)

    print(mean_length(reads))

    overlaps = get_all_overlaps(reads)
    print(overlaps)

    pretty_print(overlaps)

    name = find_first_read(overlaps)
    print(name)
    order = find_order_of_reads(name, overlaps)
    print(order)
    genome = reconstruct_sequence(order, reads, overlaps)
    print(genome)

    genome = assemble_genome("sequencing_reads.txt")
    print(genome)




