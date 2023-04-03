# distinct values
def target_difference_pairs(values, target):
  candidates = {}
  for index, value in enumerate(values):
    candidates[value] = index
  pairs = 0
  for _, value in enumerate(values):
    if (value - target) in candidates:
      pairs += 1
  return pairs

print(target_difference_pairs([1, 7, 5, 9, 2, 12, 3], 2))
