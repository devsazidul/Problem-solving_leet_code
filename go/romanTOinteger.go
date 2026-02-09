package main

import (
	"fmt"
	"strings"
)

func romanToInt(s string) int {
	roman_to_int := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
	total := 0
	previous_value := 0
	s = strings.ToUpper(strings.TrimSpace(s))

	for _, char := range s {
		value := roman_to_int[string(char)]

		if value > previous_value {
			total += value - 2*previous_value
		} else {
			total += value
		}
		previous_value = value
	}
	return total
}

func main() {
	var input string
	fmt.Print("Type roman number (e.g., III, IV, MCMXCIV): ")
	fmt.Scanln(&input)

	result := romanToInt(input)
	fmt.Printf("The integer value of %s is: %d\n", strings.ToUpper(input), result)
}
