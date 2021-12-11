from hypothesis import example
from hypothesis import given
from hypothesis.strategies import integers

from signed_decomposition import signed_decomposition

num_bits = 32
base_log = 8
base = 1 << base_log

max_digit = base // 2 - 1
max_representable = (max_digit 
    * (base ** (num_bits // base_log) - 1) // (base - 1)
)

@given(integers(min_value=0, max_value=max_representable))
@example(2047)
@example(max_representable)
def test_signed_decomposition(number):
    base = 2**base_log
    decomp = signed_decomposition(number, base_log, total_num_bits=32)
    reconstructed = sum(digit * base**i for (i, digit) in enumerate(decomp))
    assert max(decomp) < base // 2
    assert -base // 2 <= min(decomp)
    assert reconstructed == number

@given(integers(min_value=max_representable+1))
@example(max_representable+1)
def test_larger_than_max_representable_fails(number):
    base = 2**base_log
    decomp = signed_decomposition(number, base_log, total_num_bits=32)
    reconstructed = sum(digit * base**i for (i, digit) in enumerate(decomp))
    assert reconstructed != number

