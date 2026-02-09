class Solution(object):
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        total = 0
        previous_value = 0

        for char in s:
            value = roman_to_int[char]
            
            if value > previous_value:
                total += value - 2 * previous_value
            else:
                total += value
            previous_value = value
            
        return total

if __name__ == "__main__":
    sol = Solution()
    roman_input = input("Type roman number (e.g., III, IV, MCMXCIV): ").upper().strip()
    
    try:
        result = sol.romanToInt(roman_input)
        print(f"The integer value of {roman_input} is: {result}")
    except KeyError:
        print("Invalid character detected. Please use characters: I, V, X, L, C, D, M.")
    except Exception as e:
        print(f"An error occurred: {e}")