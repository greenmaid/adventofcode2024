package common

import (
	"encoding/json"
	"log"
	"reflect"
	"slices"
	"strings"
	"time"
)

// handy error checker
func Check(e error) {
	if e != nil {
		panic(e)
	}
}

func TimeTrack(start time.Time, name string) {
	elapsed := time.Since(start)
	log.Printf("%s took %s", name, elapsed)
}

// get each line as a list of integer
func ParseLineAsBits(line string) []int {
	var bits []int
	for _, bitStr := range line {
		bits = append(bits, ConvertRuneToInt(bitStr))
	}
	return bits
}

// https://stackoverflow.com/questions/21322173/convert-rune-to-int
func ConvertRuneToInt(rune rune) int {
	return int(rune - '0')
}

// classical map function
func Map[T, V any](ts []T, fn func(T) V) []V {
	result := make([]V, len(ts))
	for i, t := range ts {
		result[i] = fn(t)
	}
	return result
}

// easily deepcopy struct (only exported Fields !)
// https://stackoverflow.com/questions/50269322/how-to-copy-struct-and-dereference-all-pointers
func DeepCopy(v interface{}) (interface{}, error) {
	data, err := json.Marshal(v)
	if err != nil {
		return nil, err
	}

	vptr := reflect.New(reflect.TypeOf(v))
	err = json.Unmarshal(data, vptr.Interface())
	if err != nil {
		return nil, err
	}
	return vptr.Elem().Interface(), err
}

// get all permutations of an array
func Permutations(array []interface{}) [][]interface{} {
	var result [][]interface{}
	if len(array) <= 1 {
		result = append(result, array)
		return result
	}
	for _, perm := range Permutations(array[1:]) {
		for i := 0; i < len(array); i++ {
			elem := slices.Concat(perm[:i], array[0:1], perm[i:])
			result = append(result, elem)
		}
	}
	return result
}

func FindAllSubstringIndexes(s string, sub string) []int {
	indexes := []int{}
	idx := 0
	for {
		next := strings.Index(s[idx:], sub)
		if next >= 0 {
			indexes = append(indexes, idx+next)
			idx += next + 1
			continue
		}
		break

	}
	return indexes
}
