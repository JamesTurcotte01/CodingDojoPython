# //write formula that reads whole string//
# //add new string//
# //push string letter by letter starting with the the last place in the string working towards the first//
# //console log new string//

# string = "Monday"[::-1]
# print(string)
# string = 'today is monday'
# string= sentence.replace(" ", "")
# print(string)


# # function getDigits(str) {}
# # console.log(getDigits('z4d2g5s2'));
# # // should log 4252
# # function isPalindrome(str) {}
# # console.log(isPalindrome('Tuesday'));
# # // false
# # console.log(isPalindrome('tacocat'));
# # // true
# def isPalindrome(str):
#     for i in range(0, int(len(str)/2)): 
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True
# s = "racecar"
# ans = isPalindrome(s)
# if (ans):
#     print("Yes")
# else:
#     print("No")


#     def acronyms(str):
#     pass

# """
# Given a string of words, return an acronym of the words in the original string
# Input => "Thank goodness it's Friday"
# Output => "TGIF"
# """
# def makeacronym():

#     acro = input("Enter")
#     phrase_split = acro.split()
#     acronym = ""
#     for i in phrase_split:
#         acronym = acronym + i[0].upper()
#     print(acronym)

# makeacronym()








# def parensValid(str):
#     pass

# """
# Create a function that given a string input, returns a boolean whether parenthesis in the string are valid.
# Input => "ad(dad)(asdf)"
# Output => True
# Input => "add)asdf(sdaf)("
# Output => False
# """

# """
# Book Index
# Write a function that given a sorted array of page numbers, return a string representing a book index. Combine consecutive pages to create ranges.

# Given [1, 3, 4, 5, 7, 8, 10],
# return the string "1, 3-5, 7-8, 10".
# """""
def book_index(arr):
    for i in range(0,10,1):
        if arr[i] > 0:
            return(arr)
    
print(book_index([1, 3, 4, 5, 7, 8, 10]))


"""
Common Suffix
When given an array of words, returns the largest suffix (word-end) that is common between all words. 

Given ["ovation", "notation", "action"], return "tion".

Given ["nice", "ice", "sic"], return "".
"""



def longestCommonPrefix(self, strs):
    longest_pre = ""
    if not strs: return longest_pre
    shortest_str = min(strs, key=len)
    for i in range(len(shortest_str)):
        if all([x.startswith(shortest_str[:i+1]) for x in strs]):
            longest_pre = shortest_str[:i+1]
        else:
            break
    return longest_pre







# print(common_suffix(["ovation", "notation", "action"]))
# "tion"

# print(common_suffix(["nice", "ice", "sic"]))
# ""


"""
Braces Valid
Given a string, returns whether the sequence of various parentheses, braces and brackets within it are valid.

Given "w(a{t}s[o(n{c}o)m]e)h[e{r}e]!", return True.

Given "d(i{a}l[t]o)n{e", return False.

Given "a(1)s[O(n]0{t)0}k", return False.
"""

def braces_valid(string):
    pass

print(braces_valid("w(a{t}s[o(n{c}o)m]e)h[e{r}e]!"))
# True

print(braces_valid("d(i{a}l[t]o)n{e"))
# False

print(braces_valid("a(1)s[O(n]0{t)0}k"))
# False