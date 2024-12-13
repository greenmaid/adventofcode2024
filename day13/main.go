package main

import (
	"adventofcode2024/common"
	"fmt"
)

const DAY = "13"
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

	start1 := common.TimeTrackStart()
	result1 := step1(parsed)
	duration1 := common.TimeTrackStop(start1)
	fmt.Printf("Result1 = %d     \t(in %s) \n", result1, &duration1)

	start2 := common.TimeTrackStart()
	result2 := step2(parsed)
	duration2 := common.TimeTrackStop(start2)
	fmt.Printf("Result2 = %d       \t(in %s) \n", result2, &duration2)
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
