def distance(strand_a, strand_b):
    hamming = 0
    if len(strand_a) == len(strand_b):
        if strand_a == strand_b:
            return hamming
        for x in range(len(strand_a)):
            if strand_a[x] != strand_b[x]:
                hamming+=1
        return hamming
    else:
        raise ValueError("Strands need to be of the same length")