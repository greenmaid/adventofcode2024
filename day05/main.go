package main

import (
	"adventofcode2024/common"
	"fmt"
	"regexp"
	"strconv"
	"strings"

	"golang.org/x/exp/slices"
)

const DAY = "05"
const TEST = false

func main() {

	var filePath string
	if TEST {
		filePath = "day" + DAY + "/input_test.txt"
	} else {
		filePath = "day" + DAY + "/input.txt"
	}

	data := common.ReadFile(filePath)
	printingOrders, rules := parseData(data)

	start1 := common.TimeTrackStart()
	result1 := step1(printingOrders, rules)
	duration1 := common.TimeTrackStop(start1)
	fmt.Printf("Result1 = %d     \t(in %s) \n", result1, &duration1)

	start2 := common.TimeTrackStart()
	result2 := step2(printingOrders, rules)
	duration2 := common.TimeTrackStop(start2)
	fmt.Printf("Result2 = %d       \t(in %s) \n", result2, &duration2)
}

func parseData(data string) ([][]int, map[int][]int) {
	rulePrintSplit := strings.Split(data, "\n\n")

	rule_data := rulePrintSplit[0]
	rules := make(map[int][]int)
	regex1 := regexp.MustCompile(`^(\d+)\|(\d+)$`)
	for _, rule := range strings.Split(rule_data, "\n") {
		match := regex1.FindStringSubmatch(rule)
		val1, _ := strconv.Atoi(match[1])
		val2, _ := strconv.Atoi(match[2])
		if _, ok := rules[val1]; !ok {
			rules[val1] = []int{}
		}
		rules[val1] = append(rules[val1], val2)
	}

	printingData := rulePrintSplit[1]
	printingOrders := [][]int{}
	regex2 := regexp.MustCompile(`(\d+)`)
	for _, order := range strings.Split(printingData, "\n") {
		matches := regex2.FindAllStringSubmatch(order, -1)
		pages := []int{}
		for _, m := range matches {
			if val, err := strconv.Atoi(m[1]); err == nil {
				pages = append(pages, val)
			}
		}
		if len(pages) > 0 {
			printingOrders = append(printingOrders, pages)
		}
	}
	return printingOrders, rules
}

func isValid(order []int, rules map[int][]int) bool {
	for i, page := range order {
		if snbbList, ok := rules[page]; ok {
			for _, val := range order[:i] {
				for _, snbb := range snbbList {
					if val == snbb {
						return false
					}
				}
			}
		}
	}
	return true
}

func sortOrder(order []int, rules map[int][]int) []int {
	compOrder := func(a int, b int) int {
		if lst, ok := rules[a]; ok {
			for _, k := range lst {
				if b == k {
					return -1
				}
			}
		}
		return 0
	}
	slices.SortFunc(order, compOrder)
	return order
}

func step1(orders [][]int, rules map[int][]int) int {
	result := 0
	for _, o := range orders {
		if isValid(o, rules) {
			result += o[len(o)/2]
		}
	}
	return result
}

func step2(orders [][]int, rules map[int][]int) int {
	result := 0
	for _, o := range orders {
		if !isValid(o, rules) {
			sorted := sortOrder(o, rules)
			result += sorted[len(o)/2]
		}
	}
	return result
}
