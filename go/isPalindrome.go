package main

import "fmt"

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	var original = x
	var reverse = 0
	for x > 0 {
		var digit = x % 10
		reverse = reverse*10 + digit
		x = x / 10
	}
	return original == reverse
}

func main() {
	var x = 121
	fmt.Println(isPalindrome(x))
}
