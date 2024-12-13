package main

import (
	"adventofcode2024/common"
	"fmt"
)

const DAY = "08"
const TEST = false

func main() {

	var filePath string
	if TEST {
		filePath = "day" + DAY + "/input_test.txt"
	} else {
		filePath = "day" + DAY + "/input.txt"
	}

	grid := common.ReadFileToGrid(filePath)
	antennas := parseData(grid)

	start1 := common.TimeTrackStart()
	result1 := step1(antennas, grid)
	duration1 := common.TimeTrackStop(start1)
	fmt.Printf("Result1 = %d     \t(in %s) \n", result1, &duration1)

	start2 := common.TimeTrackStart()
	result2 := step2(antennas, grid)
	duration2 := common.TimeTrackStop(start2)
	fmt.Printf("Result2 = %d       \t(in %s) \n", result2, &duration2)
}

func parseData(grid [][]rune) map[rune][][2]int {
	antennas := make(map[rune][][2]int)
	for y, row := range grid {
		for x, val := range row {
			if val != '.' {
				if _, ok := antennas[val]; !ok {
					antennas[val] = [][2]int{}
				}
				antennas[val] = append(antennas[val], [2]int{x, y})
			}
		}
	}
	return antennas
}

func getAllCouples(s [][2]int) [][2][2]int {
	var couples [][2][2]int
	for i, k1 := range s {
		for _, k2 := range s[i+1:] {
			couples = append(couples, [2][2]int{k1, k2})
		}
	}
	return couples
}

func getAntinodes(a1, a2 [2]int, harmonic, limX, limY int) [][2]int {
	result := [][2]int{}
	antinode1 := [2]int{a1[0] - (harmonic * (a2[0] - a1[0])), a1[1] - (harmonic * (a2[1] - a1[1]))}
	if antinode1[0] >= 0 && antinode1[0] < limX && antinode1[1] >= 0 && antinode1[1] < limY {
		result = append(result, antinode1)
	}
	antinode2 := [2]int{a2[0] - (harmonic * (a1[0] - a2[0])), a2[1] - (harmonic * (a1[1] - a2[1]))}
	if antinode2[0] >= 0 && antinode2[0] < limX && antinode2[1] >= 0 && antinode2[1] < limY {
		result = append(result, antinode2)
	}
	return result
}

func step1(antennas map[rune][][2]int, grid [][]rune) int {
	antinodes := make(map[[2]int]bool)
	limY := len(grid)
	limX := len(grid[0])
	for _, a := range antennas {
		cs := getAllCouples(a)
		for _, c := range cs {
			for _, an := range getAntinodes(c[0], c[1], 1, limX, limY) {
				antinodes[an] = true
			}
		}
	}
	return len(antinodes)
}

func step2(antennas map[rune][][2]int, grid [][]rune) int {
	antinodes := make(map[[2]int]bool)
	limY := len(grid)
	limX := len(grid[0])
	for _, a := range antennas {
		cs := getAllCouples(a)
		for _, c := range cs {
			n := 0
			for {
				next := getAntinodes(c[0], c[1], n, limX, limY)
				if len(next) == 0 {
					break
				}
				for _, an := range next {
					antinodes[an] = true
				}
				n++
			}
		}
	}
	return len(antinodes)
}
