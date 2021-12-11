from typing import List


def signed_decomposition(x: int, base_log: int, total_num_bits=32) -> List[int]:
    result = []
    base = 1 << base_log
    digit_mask = (1 << base_log) - 1
    base_over_2_threshold = 1 << (base_log - 1)
    carry = 0

    for i in range(total_num_bits // base_log):
        unsigned_digit = (x >> (i * base_log)) & digit_mask
        if carry:
            unsigned_digit += carry
            carry = 0

        signed_digit = unsigned_digit
        if signed_digit >= base_over_2_threshold:
            signed_digit -= base
            carry = 1
        result.append(signed_digit)

    return result
