
# Pairwise alignment
<!-- ★ -->

## An optimal alignment  {.unnumbered}

- What is an alignment?
- What do we want it to represent?
- Scoring an alignment

## A recursive solution  {.unnumbered}

## Global pairwise alignment  {.unnumbered}

If i give you the following three optimal alignments: n-1, m-1; n, m-1; n-1, m can you the. Give me the optimal alignment of n,m?


The Needleman-Wunsch algorithm is a dynamic programming algorithm commonly used for global sequence alignment in bioinformatics and computational biology. Developed by Saul B. Needleman and Christian D. Wunsch in 1970, this algorithm is fundamental for comparing two sequences, such as DNA, RNA, or protein sequences, to identify similarities, differences, and evolutionary relationships between them.

**Problem Statement:**
The primary objective of sequence alignment is to identify the optimal alignment between two sequences by inserting gaps (representing insertions or deletions) to maximize the similarity score while adhering to predefined scoring rules.

**Algorithm Overview:**
The Needleman-Wunsch algorithm builds a dynamic programming matrix to efficiently calculate the optimal alignment score and traceback through the matrix to retrieve the optimal alignment itself. It employs a recurrence relation to calculate the score of aligning prefixes of the two sequences and incrementally fills the matrix based on these calculations.

**Scoring Scheme:**
The algorithm uses a scoring scheme to assign scores to matches, mismatches, and gaps. Typically, a positive score is assigned to matches, a negative score to mismatches, and negative penalties for gap openings and gap extensions. The scoring scheme reflects the biological context and influences the alignment results.

**Dynamic Programming Matrix:**
The dynamic programming matrix is constructed with dimensions M x N, where M is the length of the first sequence and N is the length of the second sequence. Each cell in the matrix represents the score of aligning the prefixes of the two sequences up to that point.

**Initialization:**
The first row and the first column of the matrix are initialized based on the gap penalties. The first row corresponds to aligning the first sequence with gaps in the second sequence, and the first column corresponds to aligning the second sequence with gaps in the first sequence.

**Recurrence Relation:**
Starting from the second row and the second column, each cell (i, j) in the matrix is calculated as the maximum of three values:

The cell above (i-1, j) plus the gap penalty (gap extension).
The cell to the left (i, j-1) plus the gap penalty (gap extension).
The diagonal cell (i-1, j-1) plus the match/mismatch score based on the characters in the sequences at positions i and j.
Traceback:
After the matrix is filled, the optimal alignment can be reconstructed by backtracking from the bottom-right corner (i.e., the end of both sequences) to the top-left corner (i.e., the beginning of both sequences). At each step, the decision to move diagonally, up, or left is based on the values in the neighboring cells and the scoring rules.

**Alignment Output:**
The traceback results in the aligned sequences with gaps, showcasing the optimal alignment between the input sequences. The alignment score is the value in the bottom-right corner of the matrix and represents the degree of similarity between the two sequences.

**Complexity:**
The Needleman-Wunsch algorithm has a time and space complexity of O(M * N), where M and N are the lengths of the input sequences. This complexity makes it suitable for relatively short sequences but can become impractical for very long sequences.

In summary, the Needleman-Wunsch algorithm is a foundational tool for performing global sequence alignment, allowing researchers to compare and analyze biological sequences to uncover evolutionary relationships, genetic variations, and functional similarities between genes, proteins, and other biological molecules.

## Local pairwise alignment  {.unnumbered}

## Alignment significance  {.unnumbered}

## Do it yourself:   {.unnumbered}

