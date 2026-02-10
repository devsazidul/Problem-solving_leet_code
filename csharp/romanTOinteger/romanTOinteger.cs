using System;

public class Solution {
    public int RomanValue(char c) {
        switch (c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }

    public int RomanToInt(string s) {
        int total = 0;
        int previous_value = 0;
        int value = 0;
        int len = s.Length;

        for (int i = 0; i < len; i++) {
            value = RomanValue(s[i]);
            if (value > previous_value) {
                total += value - 2 * previous_value;
            } else {
                total += value;
            }
            previous_value = value;
        }
        return total;
    }

    static void Main(string[] args) {
        Solution sol = new Solution();
        
        string s1 = "III";
        Console.WriteLine($"Input: {s1}, Output: {sol.RomanToInt(s1)}");
        
        string s2 = "IV";
        Console.WriteLine($"Input: {s2}, Output: {sol.RomanToInt(s2)}");
        
        string s3 = "MCMXCIV";
        Console.WriteLine($"Input: {s3}, Output: {sol.RomanToInt(s3)}");
    }
}