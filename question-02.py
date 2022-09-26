# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

""" Sample Output : {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 
'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 
's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122} """


keys = int(input('please enter the number of alphabets = '))
key = []
for i in range(1,keys+1):
  keys1 = input('alphabets = ')
  key.append(keys1)
print('alphabets = ',key)


values = int(input('please enter the number of ASCII values = '))
value = []
for j in range(1,values+1):
  values1 = int(input("ASCII numbers = "))
  value.append(values1)
print('ASCII values = ',value)

dict1 = dict(zip(key,value))
print(dict1)