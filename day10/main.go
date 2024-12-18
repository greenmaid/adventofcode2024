package main

import (
	"adventofcode2024/common"
	"fmt"
)

const DAY = "10"
const TEST = false

func main() {

	var filePath string
	if TEST {
		filePath = "day" + DAY + "/input_test.txt"
	} else {
		filePath = "day" + DAY + "/input.txt"
	}

	grid := common.ReadFileToIntGrid(filePath)

	start1 := common.TimeTrackStart()
	result1, result2 := run(grid)
	duration1 := common.TimeTrackStop(start1)
	fmt.Printf("Result1 = %d     \t(in %s) \n", result1, &duration1)
	fmt.Printf("Result2 = %d \n", result2)
}

func run(grid [][]int) (int, int) {
	result1 := 0
	result2 := 0
	for y, row := range grid {
		for x, val := range row {
			if val == 0 {
				summits, trailCount := climb([2]int{x, y}, grid, make(map[[2]int]bool), 0)
				result1 += len(summits)
				result2 += trailCount
			}
		}
	}
	return result1, result2
}

func climb(pos [2]int, grid [][]int, currentSummits map[[2]int]bool, currentCount int) (map[[2]int]bool, int) {
	x := pos[0]
	y := pos[1]
	val := grid[y][x]
	if val == 9 {
		currentSummits[[2]int{x, y}] = true
		currentCount += 1
		return currentSummits, currentCount
	}
	directions := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for _, d := range directions {
		nx := x + d[0]
		ny := y + d[1]
		limX := len(grid[0])
		limY := len(grid)
		if nx >= 0 && nx < limX && ny >= 0 && ny < limY && grid[ny][nx] == val+1 {
			currentSummits, currentCount = climb([2]int{nx, ny}, grid, currentSummits, currentCount)
		}
	}
	return currentSummits, currentCount
}
