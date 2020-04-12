def allsubsets(s):
  """Funkcja generująca wszyskie podzbiory zadanego zbioru"""
  if (len(s) == 0):
    return [[]]
  a,t = s[0], s[1:]
  res = allsubsets(t)
  return list(map(lambda subset: [a] + subset, res)) + res