package main

import (
	"adventofcode2024/common"
	"fmt"
	"strconv"
	"strings"
)

const DAY = "02"
const TEST = false

func main() {

	var filePath string
	if TEST {
		filePath = "day" + DAY + "/input_test.txt"
	} else {
		filePath = "day" + DAY + "/input.txt"
	}

	data := common.ReadFileByLine(filePath)
	reports := parseData(data)

	result1 := step1(reports)
	fmt.Println("Result1 = ", result1)

	result2 := step2(reports)
	fmt.Println("Result2 = ", result2)
}

func parseData(lines []string) [][]int {
	result := [][]int{}
	for _, line := range lines {
		stages := []int{}
		for _, char := range strings.Split(line, " ") {
			val, _ := strconv.Atoi(string(char))
			stages = append(stages, val)
		}
		result = append(result, stages)
	}
	return result
}

func isSafe(report []int) int {
	direction := ""
	if report[1]-report[0] > 0 {
		direction = "+"
	} else {
		direction = "-"
	}
	for idx := 0; idx < len(report)-1; idx++ {
		diff := report[idx+1] - report[idx]
		if diff == 0 || common.Abs(diff) > 3 {
			return idx
		}
		if report[idx+1] < report[idx] && direction == "+" {
			return idx
		}
		if report[idx+1] > report[idx] && direction == "-" {
			return idx
		}
	}
	return -1
}

func step1(reports [][]int) int {
	count := 0
	for _, report := range reports {
		// fmt.Println(report, isSafe(report))
		if isSafe(report) == -1 {
			count++
		}
	}
	return count
}

func step2(reports [][]int) int {
	count := 0
	for _, report := range reports {
		isSafeOrError := isSafe(report)
		if isSafeOrError == -1 {
			count++
		} else {
			partial := report[:isSafeOrError]
			partial = append(partial, report[isSafeOrError+1:]...)
			if isSafe(partial) == -1 {
				count++
			} else {
				partial := report[:isSafeOrError+1]
				partial = append(partial, report[isSafeOrError+2:]...)
				if isSafe(partial) == -1 {
					count++
				}
			}
		}
	}
	return count
}
