# Check if two words are anagrams 

def find_anagram(word, anagram):
    # [assignment] Add your code here
    
  word = word.replace(" ", "")
  anagram = anagram.replace(" ", "")
    
  if sorted(word) == sorted(anagram):
    return True

  else:  
    return False

word= "silence"
anagram= "listen"

print("Checking for anagrams with 'silence' and 'listen' ", find_anagram(word,anagram))
