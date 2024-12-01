package main

import (
	"adventofcode2015/common"
	"fmt"
	"strings"
)

func main() {
	// filePath := "day01/input_test.txt"
	filePath := "day01/input.txt"
	fileContent := common.ReadFile(filePath)

	in := strings.Count(fileContent, "(")
	out := strings.Count(fileContent, ")")

	result1 := in - out
	fmt.Println("Result1 = ", result1)

	level := 0
	result2 := 0
	for pos, char := range fileContent {
		if string(char) == "(" {
			level += 1
		}
		if string(char) == ")" {
			level -= 1
		}
		if level == -1 {
			result2 = pos + 1
			break
		}
	}
	fmt.Println("Result2 = ", result2)
}
