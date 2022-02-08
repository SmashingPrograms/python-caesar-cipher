uppercase_letters_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters_string = uppercase_letters_string.lower()

uppercase_letters = list(uppercase_letters_string)
lowercase_letters = list(lowercase_letters_string)

# test_string = "In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example,"

test_string = input("String to test: ")
shift_amount = input("Pick a shift value: ")

try:
  shift_amount = int(shift_amount)
except ValueError:
  print("Please enter an actual number!")
  exit()

if shift_amount > 26:
  shift_amount = shift_amount % 26
if shift_amount < 0:
  if shift_amount < -26:
    shift_amount = shift_amount % -26
  shift_amount = 26 + shift_amount

def caesar_cipher(string):
  new_list = []
  for letter in string:
    if letter in uppercase_letters:
      new_list.append(uppercase_letters[uppercase_letters.index(letter)-shift_amount])
    elif letter in lowercase_letters:
      new_list.append(lowercase_letters[lowercase_letters.index(letter)-shift_amount])
    else:
      new_list.append(letter)
  return ''.join(new_list)

print(caesar_cipher(test_string))