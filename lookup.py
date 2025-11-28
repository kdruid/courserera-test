def lookup(key, pairs):
  '''
  lookup returns the value associated with the given key in the
         LList of pairs. May assume the key exists in the LList
         of pairs

  key     - X
  pairs   - LList of LL(X, Y)
  returns - Y

  Examples:
    lookup("x", LL(LL("x", 5), LL("y", 10))) -> 5
    lookup("y", LL(LL("x", 5), LL("y", 10))) -> 10
  '''
  if key == first(first(pairs)):
     return rest(first(pairs))
  return lookup(key, rest(pairs))
