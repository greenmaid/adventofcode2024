package main

import (
	"adventofcode2015/common"
	"fmt"
)

const DAY = "xx"
const TEST = true

func main() {

	var filePath string
	if TEST {
		filePath = "day" + DAY + "/input_test.txt"
	} else {
		filePath = "day" + DAY + "/input.txt"
	}

	data := common.ReadFileByLine(filePath)
	parsed := parseData(data)

	result1 := step1(parsed)
	fmt.Println("Result1 = ", result1)

	result2 := step2(parsed)
	fmt.Println("Result2 = ", result2)
}

func parseData(data []string) []string {
	return data
}

func step1(data []string) int {
	fmt.Println(data)
	result := 0
	return result
}

func step2(data []string) int {
	fmt.Println(data)
	result := 0
	return result
}
