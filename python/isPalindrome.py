# This code for leetcode problem ----------------

# class Solution:
#     def isPalindrome(self, x):
#         if x <0:
#             return False

#         original = x
#         reverse =0

#         while x >0:
#             digit = x % 10
#             reverse = reverse * 10 + digit
#             x = x // 10

#         return original == reverse 


# this Code for Vs code run ---------------------

class Solution:
    def isPalindrome(self, x):
        if x <0:
            return False

        original = x
        reverse =0

        while x >0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10

        return original == reverse

if __name__ == "__main__":
    x = 12 # same or pichone same number hole is palindrome hobe (Ture) // jodi same na hoi tahole (False) hobe
    print(Solution().isPalindrome(x))