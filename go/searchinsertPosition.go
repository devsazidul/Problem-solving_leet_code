package main

import "fmt"

func searchInsert(nums []int, target int) int {
	leftindex := 0
	rightindex := len(nums) - 1

	for leftindex <= rightindex {
		mid := (leftindex + rightindex) / 2

		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			leftindex = mid + 1

		} else {
			rightindex = mid - 1
		}
	}
	return leftindex
}

func main() {
	nums := []int{1, 3, 5, 6}
	target := 5
	fmt.Println(searchInsert(nums, target))
}
