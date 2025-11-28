def strToTokenList(s):
  '''
  strToTokenList takes a string that represents a valid fimpl program
                 and returns the sequential LList of tokens that
                 appear in that program.
  s       - str
  returns - LList of str

  Examples:
    strToTokenList("mul add -3 5 sub 1 -4 ")
        -> LL("mul", "add", "-3", "5", "sub", "1", "-4")
    strToTokenList("add      -2\n\n   \t4")
        -> LL("add", "-2", "4")
  '''
  def is_whitespace(s):
      return s == " " or s == "\t" or s =="\n"

  def split_into_words(text):
        '''
    This function separates the text into a llist of words
    text    - str
    returns - LList of str
        '''

        chars = foldr(text, lambda char, acc: cons(char, acc), empty())

        def process_char(char, acc):
            '''
        This function uses each character to make words
        char - str (single character)
        acc  - tuple of (current_word: str, words_list: LList of str)
        returns - tuple of (updated_current_word, updated_words_list)
            '''
            current_word, words_list = acc

            if is_whitespace(char):

                if current_word == "":
                    return ("", words_list)
                else:
                    return ("", cons(current_word, words_list))
            else:
                return (current_word + char, words_list)


        final_word, words_reversed = foldl(chars, process_char, ("", empty()))


        if final_word == "":
            result = words_reversed
        else:
            result = cons(final_word, words_reversed)


        return foldl(result, lambda word, acc: cons(word, acc), empty())
  words = split_into_words(s)
  return words
