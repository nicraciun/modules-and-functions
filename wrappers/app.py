def wrap_brackets( text ):
  return "(" + text + ")"
def wrap_brackets_1( text ):
  return "[[[" + text + "]]]"
def wrap_brackets_2( text ):
  return "<<<" + text + ">>>"

n = wrap_brackets_2(wrap_brackets_1(wrap_brackets('123456')))
print (n)