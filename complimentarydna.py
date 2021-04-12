  # Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

  # If you want to know more http://en.wikipedia.org/wiki/DNA

  # In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

  # More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

# valid input only contains ["A", "T", "C", "G"]

# def DNA_strand(dna):
#   new_strand = ""
#   for char in dna:
#     if char == "A":
#       new_strand += "T"
#     elif char == "T":
#       new_strand += "A"
#     elif char == "C":
#       new_strand += "G"
#     elif char == "G":
#       new_strand += "C"
#   return new_strand


dna_dict = {
  "A": "T",
  "T": "A",
  "C": "G",
  "G": "C"
}


def DNA_strand(dna):
  new_strand = ""

  for i in dna:
      new_strand += dna_dict[i]
  return new_strand


def DNA_strand(dna):
  new_strand = "".join([dna_dict[char] for char in dna])
  return new_strand


# my_list = [1,2,3,4]

# my_list_squared = []
# for el in my_list:
#   my_list_squared.append(el * el)


# list comprehension
# my_list_squared = [el * el for el in my_list]




print(DNA_strand("AAAA"))  # == "TTTT"
print(DNA_strand("ATTGC")) # == "TAACG"
print(DNA_strand("GTAT")) # == "CATA"

# A -> T
# T -> A
# C -> G
# G -> C

