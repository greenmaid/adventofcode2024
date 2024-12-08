package main

import (
	"adventofcode2024/common"
	"fmt"
)

const DAY = "06"
const TEST = false

func main() {

	var filePath string
	if TEST {
		filePath = "day" + DAY + "/input_test.txt"
	} else {
		filePath = "day" + DAY + "/input.txt"
	}

	board := common.ReadFileToGrid(filePath)
	coord := getGuardCoord(board)

	start1 := common.TimeTrackStart()
	result1, visited := step1(board, coord)
	duration1 := common.TimeTrackStop(start1)
	fmt.Printf("Result1 = %d     \t(in %s) \n", result1, &duration1)

	start2 := common.TimeTrackStart()
	result2 := step2(board, coord, visited)
	duration2 := common.TimeTrackStop(start2)
	fmt.Printf("Result2 = %d       \t(in %s) \n", result2, &duration2)
}

func getGuardCoord(board [][]rune) [3]int {
	for y := range board {
		for x := range board[0] {
			if board[y][x] == '^' {
				return [3]int{x, y, 0}
			}
		}
	}
	return [3]int{}
}

func simu(coord [3]int, board [][]rune, add_obstacle [2]int) map[[3]int]bool {
	visited := map[[3]int]bool{coord: true}
	current := [3]int{coord[0], coord[1], coord[2]}
	for {
		next := move_forward(current, board)
		if next[0] < 0 || next[0] >= len(board[0]) || next[1] < 0 || next[1] >= len(board) {
			break
		}
		if board[next[1]][next[0]] == '#' || (next[0] == add_obstacle[0] && next[1] == add_obstacle[1]) {
			current[2] = (current[2] + 1) % 4
			continue
		}
		current = next
		if _, ok := visited[current]; ok {
			return map[[3]int]bool{} // loop detected return empty
		}
		visited[current] = true
	}
	return visited
}

func move_forward(current [3]int, board [][]rune) [3]int {
	next := current
	switch current[2] {
	case 0:
		next[1] -= 1
	case 1:
		next[0] += 1
	case 2:
		next[1] += 1
	case 3:
		next[0] -= 1
	}
	return next
}

func step1(board [][]rune, coord [3]int) (int, map[[2]int]bool) {
	visited := simu(coord, board, [2]int{-1, -1})
	visited_no_direction := make(map[[2]int]bool)
	for k, _ := range visited {
		visited_no_direction[[2]int{k[0], k[1]}] = true
	}
	return len(visited_no_direction), visited_no_direction
}

func step2(board [][]rune, coord [3]int, visited_step1 map[[2]int]bool) int {
	count := 0
	for k, _ := range visited_step1 {
		test_result := simu(coord, board, k)
		if len(test_result) == 0 {
			count++
		}
	}
	return count
}
