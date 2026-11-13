# # -- exercise_1--
#
# def is_odd(n):
#     return n % 2 == 1
#
# x = int(input("Please give me a number:"))
# print(is_odd(x))
#
#
# # -- exercise_2 --
#
# def is_leapyear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
#
# print(is_leapyear(2000))

# # -- exercise_3 --
#
# def triangular_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total = total + i
#         print(i, total)
#
# triangular_numbers(5)

# # -- exercise_4 --
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
#
# print(is_prime(17))

# # -- exercise_5 --
#
# def reverse(s):
#     result = ""
#     for char in s:
#         result = char + result
#     return result
# print(reverse("hello world"))
#
# def reverse_2(s):
#     return s[::-1]
#
# print(reverse_2("hello world"))

# # -- exercise_6 --
#
# def remove_all_occurrences(sub, s):
#     return s.replace(sub,"")
#
#
# print (remove_all_occurrences("ll", "hello world"))

# # --exercise_7--
# def substitute(message, key):
#     alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "qwertyuıopğüasdfghjklşizxcvbn"
# print(substitute("Hello, World!", key))


# # -- exercise_8 --
# def remove_dups(s):
#     result = ""
#     for ch in s:
#         if ch.lower() not in result.lower():
#             result = result + ch
#     return result
#
# print(remove_dups("HeLlo World!"))