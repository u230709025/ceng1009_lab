# myList = [76, 92.3, "hello", True, 4, 76]

# myList.append("apple")
# myList.append(76)
# myList.insert(3, "cat")
# myList.insert(0, 99)
# print(myList)

# print(myList.index("hello"))

# print(myList.count(76))

# myList.remove(76)
# print(myList)

# def sum_of_squares(number_list):
#     total = 0
#     for number in number_list:
#         total = total + number**2
#     return total

# my_list = [3, 4, 5, 6, 8, 10]
# print(sum_of_squares(my_list))

# def total_even(number_list):
#     total = 0
#     for number in number_list:
#         if number % 2 == 0:
#             total = total + number
#         else:
#             continue
#     return total

# print(total_even(my_list))

# def count_five_letter(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter

# my_list = ["apple", "cat", "lemon", "python", "tiger"]
# print(count_five_letter(my_list))

# def sum_until_even(number_list):
#     sum = 0
#     for number in number_list:
#         if  number % 2 == 0:
#             break
#         sum += number
#     return sum

# my_list = [1, 3, 3, 7, 5, 6]
# print(sum_until_even(my_list))

# def count_until_sam(words):
#     count = 0
#     for word in words:
#         count += 1
#         if word == "sam":
#             break
#     return count

# my_list = ["joe", "ali", "veli", "sam", "nigar"]
# print(count_until_sam(my_list))

# def replace(s, old, new):
#     pieces = s.split(old)
#     return new.join(pieces)

# def test(actual, expected):
#     if actual == expected:
#         print("PASSED!")
#     else:
#         print("FAILED!")

# test(replace("Mississippi", "i", "I"), "MIssIssIppI")

# def max(list_of_integers):
#     max = 0
#     for number in list_of_integers:
#         if number >= max:
#             max = number
#     return max

# my_list = [0, 2, 24, 97, 54, 62, 32]
# print(max(my_list))