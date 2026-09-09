from itertools import combinations_with_replacement
from more_itertools import combination_with_replacement_index

# pool = [1, None, 2]
# print(list(combinations_with_replacement(pool, 1)).index((None,)))  # 1
# print(combination_with_replacement_index((None,), pool))          # 2

# print(combination_with_replacement_index((None,), [1, 2]))         # 1
# # Expected: ValueError, because (None,) is not a combination of [1, 2].


# element = (None, None, "b")
# iterable = ('a', None, None, None, "b")

# print(f"{list(combinations_with_replacement(iterable, 3))=}")

# print(f"{combination_with_replacement_index(element, iterable)=}")


from itertools import combinations_with_replacement

combos = list(combinations_with_replacement(('a', None), 1))
# combos == [('a',), (None,)]

print(f"{combos.index(('a',))=}")
# Expected output: 0

print(f"{combination_with_replacement_index(('a',), ('a', None))=}")
