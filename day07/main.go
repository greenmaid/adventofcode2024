package main

import (
	"adventofcode2024/common"
	"fmt"
	"iter"
	"regexp"
	"slices"
	"strconv"
	"strings"
)

const DAY = "07"
const TEST = false

func main() {

	var filePath string
	if TEST {
		filePath = "day" + DAY + "/input_test.txt"
	} else {
		filePath = "day" + DAY + "/input.txt"
	}

	lines := common.ReadFileByLine(filePath)
	calibrations := parseData(lines)

	start1 := common.TimeTrackStart()
	result1 := step1(calibrations)
	duration1 := common.TimeTrackStop(start1)
	fmt.Printf("Result1 = %d     \t(in %s) \n", result1, &duration1)

	start2 := common.TimeTrackStart()
	result2 := step2(calibrations)
	duration2 := common.TimeTrackStop(start2)
	fmt.Printf("Result2 = %d       \t(in %s) \n", result2, &duration2)
}

type CalibrationData struct {
	target int
	nums   []int
}

func parseData(lines []string) []CalibrationData {
	calibrations := []CalibrationData{}
	for _, line := range lines {
		firstSplit := strings.Split(line, ": ")
		target, _ := strconv.Atoi(firstSplit[0])
		regex := regexp.MustCompile(`(\d+)`)
		numsStr := regex.FindAllString(firstSplit[1], -1)
		nums := []int{}
		for _, s := range numsStr {
			i, _ := strconv.Atoi(s)
			nums = append(nums, i)
		}
		calibrations = append(calibrations, CalibrationData{target, nums})
	}
	return calibrations
}

func getCombinations(nums []int) iter.Seq[int] {
	return func(yield func(int) bool) {
		if len(nums) == 1 {
			if !yield(nums[0]) {
				return
			}
		} else {
			for v := range getCombinations(nums[:len(nums)-1]) {
				if !yield(v + nums[len(nums)-1]) {
					return
				}
				if !yield(v * nums[len(nums)-1]) {
					return
				}
			}
		}
	}
}

func step1(calibrations []CalibrationData) int {
	result := 0
	for c := range slices.Values(calibrations) {
		for v := range getCombinations(c.nums) {
			if v == c.target {
				result += c.target
				break
			}
		}
	}
	return result
}

func getCombinations2(nums []int) iter.Seq[int] {
	return func(yield func(int) bool) {
		if len(nums) == 1 {
			if !yield(nums[0]) {
				return
			}
		} else {
			for v := range getCombinations2(nums[:len(nums)-1]) {
				if !yield(v + nums[len(nums)-1]) {
					return
				}
				if !yield(v * nums[len(nums)-1]) {
					return
				}
				val, _ := strconv.Atoi(fmt.Sprintf("%d%d", v, nums[len(nums)-1]))
				if !yield(val) {
					return
				}
			}
		}
	}
}

func step2(calibrations []CalibrationData) int {
	result := 0
	for c := range slices.Values(calibrations) {
		for v := range getCombinations2(c.nums) {
			if v == c.target {
				result += c.target
				break
			}
		}
	}
	return result
}
