package main

import (
	"adventofcode2024/common"
	"fmt"
	"regexp"
	"strconv"
)

const DAY = "03"
const TEST = false

func main() {

	var filePath string
	if TEST {
		filePath = "day" + DAY + "/input_test.txt"
	} else {
		filePath = "day" + DAY + "/input.txt"
	}

	data := common.ReadFile(filePath)

	start1 := common.TimeTrackStart()
	result1 := step1(data)
	duration1 := common.TimeTrackStop(start1)
	fmt.Printf("Result1 = %d     \t(in %s) \n", result1, &duration1)

	start2 := common.TimeTrackStart()
	result2 := step2(data)
	duration2 := common.TimeTrackStop(start2)
	fmt.Printf("Result1 = %d       \t(in %s) \n", result2, &duration2)
}

func step1(data string) int {
	regex := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	matches := regex.FindAllStringSubmatch(data, -1)
	result := 0
	for _, m := range matches {
		val1, _ := strconv.Atoi(m[1])
		val2, _ := strconv.Atoi(m[2])
		result += val1 * val2
	}
	return result
}

func step2(data string) int {
	regex := regexp.MustCompile(`(?:mul\((\d+),(\d+)\)|do\(\)|don't\(\))`)
	matches := regex.FindAllStringSubmatch(data, -1)
	result := 0
	enabled := true
	for _, m := range matches {
		if m[0] == "do()" {
			enabled = true
		} else if m[0] == "don't()" {
			enabled = false
		} else {
			if enabled {
				val1, _ := strconv.Atoi(m[1])
				val2, _ := strconv.Atoi(m[2])
				result += val1 * val2
			}
		}
	}
	return result
}
