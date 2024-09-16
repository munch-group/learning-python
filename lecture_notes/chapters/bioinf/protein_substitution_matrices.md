
# Protein substitution matrices
<!-- ★ -->

## Scoring protein alignments  {.unnumbered}

## PAM matrices  {.unnumbered}

The PAM (Point Accepted Mutation) matrices are a family of substitution matrices used in bioinformatics for comparing protein sequences. PAM matrices are derived from an evolutionary model that assumes a specific rate of amino acid substitution over time. The number in the PAM matrix represents the fraction of accepted mutations (amino acid substitutions) at a specific position over a certain evolutionary distance. Here's how to compute a PAM120 substitution matrix:

Collect a Set of Homologous Sequences:
Gather a set of protein sequences that are believed to be homologous or evolutionarily related. This set of sequences will serve as the input for constructing the substitution matrix.

Calculate Pairwise Alignments:
Align all pairs of sequences in the collected set using a suitable pairwise sequence alignment algorithm, such as Needleman-Wunsch or Smith-Waterman. This generates an alignment for each sequence pair, which helps identify positions where substitutions have occurred.

Calculate Mutation Frequencies:
Count the number of times each pair of amino acids has been substituted for each other across all the alignments. This provides the raw data for calculating the substitution probabilities.

Calculate Fraction of Accepted Mutations (PAM1):
For each amino acid pair, calculate the fraction of accepted mutations, which is the number of observed substitutions divided by the total number of aligned positions. PAM1 is the initial estimate of substitution probabilities.

Estimate PAM Matrix for a Specific Evolutionary Distance:
The PAM120 matrix represents amino acid substitutions over an estimated evolutionary distance of approximately 120 PAM units (PAM120). To compute this matrix, you need to perform a series of calculations using the PAM1 matrix.

Iterative Calculation:
PAM matrices are constructed through iterations. The general idea is to extrapolate from PAM1 to PAM120 through a series of transformations. Each PAM matrix is derived from the previous one using a formula that relates the substitution probability in the current matrix to the substitution probabilities in the previous matrix.

Adjust for Total Probability:
In each iteration, the substitution probabilities are adjusted to ensure that the total probability of amino acid substitution remains constant. This helps maintain the expected properties of a substitution matrix.

Normalization and Scaling:
Normalize the calculated substitution probabilities to ensure they sum up to a certain value (often 1). Scale the probabilities by factors that depend on the number of substitutions and the evolutionary distance.

Rounding and Scaling for Matrix Values:
Round the calculated probabilities to integers, ensuring that they fit into the matrix's integer-based format. Scale the values by a constant factor to control the scoring range.

Matrix Format:
Present the calculated values in a matrix format, where rows and columns correspond to the 20 standard amino acids. The values in the matrix indicate the substitution scores between the respective amino acids.

It's important to note that computing PAM matrices requires a deep understanding of evolutionary models, bioinformatics algorithms, and statistical concepts. PAM matrices are typically provided as precomputed matrices for various evolutionary distances, and their calculation involves complex mathematics. Therefore, most bioinformatics applications use precomputed PAM matrices rather than attempting to compute them from scratch.

## BLOSUM matrices  {.unnumbered}

The BLOSUM (BLOcks SUbstitution Matrix) series of substitution matrices are widely used in bioinformatics for comparing protein sequences. BLOSUM matrices are derived from a set of aligned protein sequences and provide substitution scores that reflect the observed frequencies of substitutions between different amino acids. Here's how to compute a BLOSUM62 substitution matrix:

Collect a Sequence Database:
Gather a diverse and representative set of protein sequences that are homologous or related to each other. This database will be used to calculate the substitution scores.

Create Sequence Pairs:
Generate pairs of sequences from the collected database. These sequence pairs should be aligned to each other to identify the positions where substitutions occur.

Calculate Substitution Frequencies:
Count the number of times each pair of amino acids is observed to be substituted for each other in the aligned sequences. This forms the basis for calculating substitution probabilities.

Calculate Substitution Probabilities:
For each pair of amino acids, calculate the probability of substitution by dividing the observed substitution frequency by the total number of aligned pairs. This gives an idea of how likely one amino acid is to be substituted for another.

Calculate Log-Odds Ratios:
Convert the substitution probabilities into log-odds ratios by taking the logarithm (usually base 2) of the probability of substitution divided by the background frequency of observing those amino acids independently.

Normalization:
Normalize the log-odds ratios to ensure that the values are centered around zero and suitable for scoring alignments. This normalization step helps in preventing very high or very low scores.

Adjustment for Diagonal Elements:
The diagonal elements of the matrix (representing substitution of an amino acid with itself) are usually set to a fixed value, typically a negative value, to discourage mismatches.

Rounding and Scaling:
Round the log-odds ratios to integers and scale them by a constant factor to ensure that the substitution scores are suitable for the scoring range desired.

Matrix Format:
Present the computed values in a matrix format, where rows and columns correspond to the 20 standard amino acids. The values in the matrix indicate the substitution scores between the respective amino acids.

BLOSUM62 is specifically derived from a sequence identity of around 62% and is suited for comparing protein sequences that share this level of identity. It is widely used for aligning moderately divergent protein sequences. Different BLOSUM matrices with different sequence identity cutoffs (e.g., BLOSUM45, BLOSUM80) are available to accommodate sequences with varying degrees of similarity.

It's important to note that BLOSUM matrices are typically precomputed and provided as standard matrices for various sequence comparison tools. If you're looking to generate a BLOSUM matrix from scratch, it involves significant computational and statistical analysis, and specialized software tools are often used for this purpose.


## PAM vs BLOSUM

BLOSUM (BLOcks SUbstitution Matrix) and PAM (Point Accepted Mutation) are both families of substitution matrices used in bioinformatics for comparing protein sequences. They are designed to quantify the likelihood of amino acid substitutions between sequences and are fundamental components in sequence alignment algorithms. Each family has its own advantages and limitations. Here's a comparison of the pros and cons of BLOSUM and PAM matrices:

BLOSUM (BLOcks SUbstitution Matrix):

Pros:

Empirical Nature: BLOSUM matrices are derived from a specific set of aligned protein sequences, often representing more recent evolutionary events. As a result, they capture more recent divergence and are suited for comparing moderately similar sequences.
Variability: Different BLOSUM matrices are available (e.g., BLOSUM30, BLOSUM62, BLOSUM80), catering to varying degrees of sequence identity. This allows users to choose the matrix that best fits the similarity level of their sequences.
Specificity: BLOSUM matrices can be used for aligning sequences with a wide range of similarity levels, making them versatile for various types of sequence comparisons.
Scoring Range: BLOSUM matrices often result in a wider scoring range, providing more detailed information about sequence similarities and differences.
Cons:

Limited Evolutionary Distance: BLOSUM matrices are less suitable for highly divergent sequences or sequences separated by long evolutionary distances.
Pre-computed Nature: BLOSUM matrices are precomputed and can't be easily recalculated with custom data. This limits their adaptability to specific datasets.
Homologous Sequences Required: The quality of BLOSUM matrices depends on the quality and diversity of the input sequences used to derive them.
Alignment Quality Sensitivity: BLOSUM matrices are sensitive to the quality of the initial sequence alignment used to derive them.
PAM (Point Accepted Mutation):

Pros:

Evolutionary Model: PAM matrices are derived from an evolutionary model, which attempts to capture long-term evolutionary processes. They can be used for comparing sequences with a broader range of evolutionary distances.
Flexibility: PAM matrices can be theoretically recalculated for custom datasets, although it requires significant computational effort and expertise.
Range of Matrices: Like BLOSUM, different PAM matrices (e.g., PAM30, PAM120, PAM250) are available for varying degrees of sequence divergence.
Long-Distance Comparisons: PAM matrices are more suitable for comparing highly divergent sequences due to their focus on longer-term evolutionary events.
Cons:

Dependence on Model Assumptions: PAM matrices rely on the assumption of a specific evolutionary model, which may not perfectly represent all evolutionary processes.
Complexity: Constructing and recalculating PAM matrices require significant computational resources and expertise.
Sensitivity to Input Sequences: Like BLOSUM matrices, the quality of PAM matrices depends on the quality and diversity of the input sequences.
Non-Contemporary Alignments: PAM matrices are designed to capture historical substitutions, which can be a limitation when comparing sequences with recent divergence.
In summary, both BLOSUM and PAM matrices offer valuable tools for comparing protein sequences. The choice between them depends on the specific characteristics of the sequences being aligned, the desired degree of sensitivity, and the computational resources available. BLOSUM matrices are preferred for more recent evolutionary events and moderately similar sequences, while PAM matrices are better suited for longer-term evolutionary processes and highly divergent sequences.