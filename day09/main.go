package main

import (
	"adventofcode2024/common"
	"fmt"
	"slices"
	"strconv"
)

const DAY = "09"
const TEST = false

func main() {

	var filePath string
	if TEST {
		filePath = "day" + DAY + "/input_test.txt"
	} else {
		filePath = "day" + DAY + "/input.txt"
	}

	data := common.ReadFile(filePath)

	sectors := parseData(data)
	start1 := common.TimeTrackStart()
	result1 := step1(sectors)
	duration1 := common.TimeTrackStop(start1)
	fmt.Printf("Result1 = %d     \t(in %s) \n", result1, &duration1)

	sectors = parseData(data)
	start2 := common.TimeTrackStart()
	result2 := step2(sectors)
	duration2 := common.TimeTrackStop(start2)
	fmt.Printf("Result2 = %d       \t(in %s) \n", result2, &duration2)
}

type Sector struct {
	id, size int
}

func parseData(data string) []Sector {
	sectors := []Sector{}
	id := 0
	for i, c := range data {
		v, _ := strconv.Atoi(string(c))
		if v > 0 {
			if i%2 == 0 {
				sectors = append(sectors, Sector{id: id, size: v})
				id++
			} else {
				sectors = append(sectors, Sector{id: -1, size: v})
			}
		}
	}
	return sectors
}

func calculateChecksum(sectors []Sector) int {
	result := 0
	idx := 0
	for _, s := range sectors {
		if s.id > 0 {
			for i := 0; i < s.size; i++ {
				result += s.id * (idx + i)
			}
		}
		idx += s.size
	}
	return result
}

func step1(sectors []Sector) int {
	for {
		firstAvailableSectorIdx := -1
		for i, s := range sectors {
			if s.id == -1 {
				firstAvailableSectorIdx = i
				break
			}
		}
		sectorToMoveIdx := -1
		for i := len(sectors) - 1; i >= 0; i-- {
			if sectors[i].id != -1 {
				sectorToMoveIdx = i
				break
			}
		}
		if sectorToMoveIdx < firstAvailableSectorIdx {
			break
		}
		movingSector := Sector{id: sectors[sectorToMoveIdx].id, size: 1}
		sectors[sectorToMoveIdx].size--
		if sectors[sectorToMoveIdx].size == 0 {
			sectors = slices.Delete(sectors, sectorToMoveIdx, sectorToMoveIdx+1)
		}
		sectors[firstAvailableSectorIdx].size--
		if sectors[firstAvailableSectorIdx].size == 0 {
			sectors = slices.Delete(sectors, firstAvailableSectorIdx, firstAvailableSectorIdx+1)
		}
		sectors = slices.Insert(sectors, firstAvailableSectorIdx, movingSector)
	}
	return calculateChecksum(sectors)
}

func step2(sectors []Sector) int {
	targetId := 0
	for _, s := range sectors {
		if s.id > targetId {
			targetId = s.id
		}
	}
	for targetId > 0 {
		targetSectorIdx := -1
		for i := len(sectors) - 1; i >= 0; i-- {
			if sectors[i].id == targetId {
				targetSectorIdx = i
				break
			}
		}
		targetSector := Sector{id: sectors[targetSectorIdx].id, size: sectors[targetSectorIdx].size}
		firstAvailableSectorIdx := -1
		for i, s := range sectors {
			if s.id == -1 && s.size >= targetSector.size {
				firstAvailableSectorIdx = i
				break
			}
		}
		targetId--
		if firstAvailableSectorIdx == -1 || firstAvailableSectorIdx > targetSectorIdx {
			continue
		}
		sectors[targetSectorIdx].id = -1
		sectors[firstAvailableSectorIdx].size -= targetSector.size
		if sectors[firstAvailableSectorIdx].size == 0 {
			sectors = slices.Delete(sectors, firstAvailableSectorIdx, firstAvailableSectorIdx+1)
		}
		sectors = slices.Insert(sectors, firstAvailableSectorIdx, targetSector)
	}
	return calculateChecksum(sectors)
}
