package main

import (
	"adventofcode2024/common"
	"fmt"
	"regexp"
	"sort"
	"strconv"
)

const DAY = "01"
const TEST = false

func main() {

	var filePath string
	if TEST {
		filePath = "day" + DAY + "/input_test.txt"
	} else {
		filePath = "day" + DAY + "/input.txt"
	}

	data := common.ReadFileByLine(filePath)
	list1, list2 := parseData(data)

	start1 := common.TimeTrackStart()
	result1 := step1(list1, list2)
	duration1 := common.TimeTrackStop(start1)
	fmt.Printf("Result1 = %d     \t(in %s) \n", result1, &duration1)

	start2 := common.TimeTrackStart()
	result2 := step2(list1, list2)
	duration2 := common.TimeTrackStop(start2)
	fmt.Printf("Result1 = %d       \t(in %s) \n", result2, &duration2)
}

func parseData(data []string) ([]int, []int) {
	var list1 []int
	var list2 []int
	regex := regexp.MustCompile(`^(\d+)\s+(\d+)$`)
	for _, line := range data {
		match := regex.FindStringSubmatch(line)
		val1, _ := strconv.Atoi(match[1])
		list1 = append(list1, val1)
		val2, _ := strconv.Atoi(match[2])
		list2 = append(list2, val2)
	}
	sort.Ints(list1)
	sort.Ints(list2)
	return list1, list2
}

func step1(list1 []int, list2 []int) int {
	count := 0
	for i, k := range list1 {
		diff := k - list2[i]
		if diff < 0 {
			diff *= -1
		}
		count += diff
	}
	return count
}

func step2(list1 []int, list2 []int) int {
	similarity := 0
	for _, k1 := range list1 {
		count := 0
		for _, k2 := range list2 {
			if k2 == k1 {
				count++
			}
		}
		similarity += k1 * count

	}
	return similarity
}
