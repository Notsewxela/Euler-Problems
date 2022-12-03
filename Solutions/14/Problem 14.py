'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int(3*n+1)
    
def collatz_seq(n, dic):
    count = 1
    original_number = n
    while True:
        if n < original_number:
            dic[original_number] = dic[n] + count - 1 #-1 because when n < original_number, n is counted twice otherwise
            break
        if n == 1:
            dic[original_number] = count
            break
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        count += 1
    return dic


limit = int(1e6)
seq_lens = {x:0 for x in range(1, limit+1)}

for j in range(2, limit+1):
    seq_lens = collatz_seq(j, seq_lens)

max_len = max(seq_lens.values())
max_val = max(seq_lens, key=seq_lens.get)

print(f"The longest Collatz sequence with starting term under {limit} is {max_val} with a length of {max_len}!")