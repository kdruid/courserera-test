def type(s):
   speciA = "ident"
   speciB = "intLit"
   speciC = "binOp"
   if not isNotKeyword(s):
     return LL(speciC,s)

   elif s == "" or (not("0" <= s[0] <= "9") and s[0] != "-"):
     return LL(speciA, s)

   elif s[0] == "-":
     return LL(speciB,-strToInt(s[1:]))

   else:
     return LL(speciB,strToInt(s))

def strToInt(s):
   currentVal = 0
   if s != "" and "0" <= s[0] <= "9":
     for ch in s:
        currentVal = currentVal*10 + (ord(ch) - ord("0"))
   return currentVal
