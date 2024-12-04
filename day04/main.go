package main

import (
	"adventofcode2024/common"
	"fmt"
	"strings"
)

const DAY = "04"
const TEST = false

func main() {

	var filePath string
	if TEST {
		filePath = "day" + DAY + "/input_test.txt"
	} else {
		filePath = "day" + DAY + "/input.txt"
	}

	table := common.ReadFileToGrid(filePath)

	start1 := common.TimeTrackStart()
	result1 := step1(table)
	duration1 := common.TimeTrackStop(start1)
	fmt.Printf("Result1 = %d     \t(in %s) \n", result1, &duration1)

	start2 := common.TimeTrackStart()
	result2 := step2(table)
	duration2 := common.TimeTrackStop(start2)
	fmt.Printf("Result1 = %d       \t(in %s) \n", result2, &duration2)
}

func step1(table [][]rune) int {
	result := 0
	for y, row := range table {
		for x, _ := range row {
			result += findXMAS(x, y, table)
		}
	}
	return result
}

func step2(table [][]rune) int {
	result := 0
	for y, row := range table {
		for x, _ := range row {
			if findCrossMAS(x, y, table) {
				result++
			}
		}
	}
	return result
}

func findXMAS(x int, y int, table [][]rune) int {
	if table[y][x] != rune('X') {
		return 0
	}
	count := 0
	dimX := len(table[0])
	dimY := len(table)
	if x < dimX-3 {
		if table[y][x+1] == 'M' && table[y][x+2] == 'A' && table[y][x+3] == 'S' {
			count += 1
		}
	}
	if x > 2 {
		if table[y][x-1] == 'M' && table[y][x-2] == 'A' && table[y][x-3] == 'S' {
			count += 1
		}
	}
	if y < dimY-3 {
		if table[y+1][x] == 'M' && table[y+2][x] == 'A' && table[y+3][x] == 'S' {
			count += 1
		}
	}
	if y > 2 {
		if table[y-1][x] == 'M' && table[y-2][x] == 'A' && table[y-3][x] == 'S' {
			count += 1
		}
	}
	if x < dimX-3 && y < dimY-3 {
		if table[y+1][x+1] == 'M' && table[y+2][x+2] == 'A' && table[y+3][x+3] == 'S' {
			count += 1
		}
	}
	if x < dimX-3 && y > 2 {
		if table[y-1][x+1] == 'M' && table[y-2][x+2] == 'A' && table[y-3][x+3] == 'S' {
			count += 1
		}
	}
	if x > 2 && y > 2 {
		if table[y-1][x-1] == 'M' && table[y-2][x-2] == 'A' && table[y-3][x-3] == 'S' {
			count += 1
		}
	}
	if x > 2 && y < dimY-3 {
		if table[y+1][x-1] == 'M' && table[y+2][x-2] == 'A' && table[y+3][x-3] == 'S' {
			count += 1
		}
	}
	return count
}

func findCrossMAS(x int, y int, table [][]rune) bool {
	if table[y][x] != 'A' {
		return false
	}
	dimX := len(table[0])
	dimY := len(table)
	if x > 0 && x < dimX-1 && y > 0 && y < dimY-1 {
		elems := string([]rune{
			table[y+1][x-1],
			table[y-1][x-1],
			table[y+1][x+1],
			table[y-1][x+1],
		})
		if elems[0] != elems[3] {
			return false
		}
		if strings.Count(elems, "M") == 2 && strings.Count(elems, "S") == 2 {
			return true
		}
	}
	return false
}
