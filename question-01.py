#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)

given_list= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
final_result = []
len_check = len(given_list)
print("length of given list = ",len_check)
print("sample list = ",given_list)
for i in range(0,len_check):
  for j in range(i+1):
    if (given_list[i][1] < given_list[j][1]):
      given_list[i],given_list[j] = given_list[j],given_list[i]

# final_result.append(given_list)
print("expected output = ",given_list)