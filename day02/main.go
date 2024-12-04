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

	start1 := common.TimeTrackStart()
	result1 := step1(reports)
	duration1 := common.TimeTrackStop(start1)
	fmt.Printf("Result1 = %d     \t(in %s) \n", result1, &duration1)

	start2 := common.TimeTrackStart()
	result2 := step2(reports)
	duration2 := common.TimeTrackStop(start2)
	fmt.Printf("Result1 = %d       \t(in %s) \n", result2, &duration2)
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

func isSafe2(report []int) bool {
	isSafeOrError := isSafe(report)
	if isSafeOrError == -1 {
		return true
	}
	for i := isSafeOrError - 1; i <= isSafeOrError+1; i++ {
		if i >= 0 {
			partial := []int{}
			for idx, s := range report {
				if idx != i {
					partial = append(partial, s)
				}
			}
			if isSafe(partial) == -1 {
				return true
			}
		}
	}
	return false
}

func step2(reports [][]int) int {
	count := 0
	for _, report := range reports {
		if isSafe2(report) {
			count++
		}
	}
	return count
}
