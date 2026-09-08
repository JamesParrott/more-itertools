from itertools import combinations_with_replacement
from more_itertools import combination_with_replacement_index

pool = [1, None, 2]
print(list(combinations_with_replacement(pool, 1)).index((None,)))  # 1
print(combination_with_replacement_index((None,), pool))          # 2

print(combination_with_replacement_index((None,), [1, 2]))         # 1
# Expected: ValueError, because (None,) is not a combination of [1, 2].