package main

import (
	"adventofcode2024/common"
	"fmt"
	"strconv"
	"strings"
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
	printing_orders, rules := parseData(data)

	start1 := common.TimeTrackStart()
	result1 := step1(printing_orders, rules)
	duration1 := common.TimeTrackStop(start1)
	fmt.Printf("Result1 = %d     \t(in %s) \n", result1, &duration1)

	start2 := common.TimeTrackStart()
	result2 := step2(printing_orders, rules)
	duration2 := common.TimeTrackStop(start2)
	fmt.Printf("Result1 = %d       \t(in %s) \n", result2, &duration2)
}

func parseData(data string) ([][]int, map[int][]int) {
	rule_print_split := strings.Split(data, "\n\n")

	rule_data := rule_print_split[0]
	rules := make(map[int][]int)
	for _, rule := range strings.Split(rule_data, "\n") {
		rule_split := strings.Split(rule, "|")
		val1, _ := strconv.Atoi(rule_split[0])
		val2, _ := strconv.Atoi(rule_split[1])
		if _, ok := rules[val1]; !ok {
			rules[val1] = []int{}
		}
		rules[val1] = append(rules[val1], val2)
	}

	printing_data := rule_print_split[1]
	printing_orders := [][]int{}
	for _, order := range strings.Split(printing_data, "\n") {
		print_split := strings.Split(order, ",")
		pages := []int{}
		for _, p := range print_split {
			val, _ := strconv.Atoi(p)
			pages = append(pages, val)
		}
		if len(pages) > 1 {
			printing_orders = append(printing_orders, pages)
		}
	}
	return printing_orders, rules

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
	fmt.Println("")
	result := 0
	return result
}
