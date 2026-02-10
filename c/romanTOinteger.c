#include <stdio.h>
#include <string.h>

int romanValue(char c) {
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

int romanToInt(char* s) {
    int total = 0;
    int previous_value = 0;
    int value = 0;
    int len = strlen(s);
    
    for (int i = 0; i < len; i++) {
        value = romanValue(s[i]);
        if (value > previous_value) {
            total += value - 2 * previous_value;
        } else {
            total += value;
        }
        previous_value = value;
    }
    return total;
}

int main() {
    char s[] = "III";
    printf("Input: %s, Integer: %d\n", s, romanToInt(s));
    
    char s2[] = "IV";
    printf("Input: %s, Integer: %d\n", s2, romanToInt(s2));
    
    char s3[] = "MCMXCIV";
    printf("Input: %s, Integer: %d\n", s3, romanToInt(s3));
    
    return 0;
}