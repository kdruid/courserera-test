def type(s):
   speciA = "ident"
   speciB = "intLit"
   speciC = "binOp"
   if not isNotKeyword(s):
     return LL(speciC,s)

   elif s == "" or (not("0" <= s[0] <= "9") and ord(s[0]) != 45):
     return LL(speciA, s)

   elif ord(s[0]) == 45:
     return LL(speciB,-strToInt(s))
   else:
     return LL(speciB,strToInt(s))
