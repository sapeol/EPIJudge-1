from test_framework import generic_test

# NOTE: First initialize the bits to zero then while x is not 0, use the formula
# x &= x - 1 to flip the 1 bit to 0 and increase the bits variable by 1, return the bits
# time complexity O(k) where is the number of 1 bits in a number


def count_bits(x: int) -> int:
    bits = 0
    while x:
        x &= x - 1
        bits += 1
    return bits


if __name__ == "__main__":
    exit(generic_test.generic_test_main("count_bits.py", "count_bits.tsv", count_bits))
