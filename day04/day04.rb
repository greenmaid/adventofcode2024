#!/usr/bin/env ruby

def step1(grid)
    dimX = grid[0].size
    dimY = grid.size
    count = 0
    grid.each_with_index do |row, y|
        row.each_char.with_index do |k, x|
            if k == "X"
                count += 1 if x < dimX-3 and grid[y][x+1] == "M" and grid[y][x+2] == "A" and grid[y][x+3] == "S"
                count += 1 if x > 2 and grid[y][x-1] == "M" and grid[y][x-2] == "A" and grid[y][x-3] == "S"
                count += 1 if y < dimY-3 and grid[y+1][x] == "M" and grid[y+2][x] == "A" and grid[y+3][x] == "S"
                count += 1 if y > 2 and grid[y-1][x] == "M" and grid[y-2][x] == "A" and grid[y-3][x] == "S"
                count += 1 if x < dimX-3 and y < dimY - 3 and grid[y+1][x+1] == "M" and grid[y+2][x+2] == "A" and grid[y+3][x+3] == "S"
                count += 1 if x < dimX-3 and y > 2 and grid[y-1][x+1] == "M" and grid[y-2][x+2] == "A" and grid[y-3][x+3] == "S"
                count += 1 if x > 2 and y > 2 and grid[y-1][x-1] == "M" and grid[y-2][x-2] == "A" and grid[y-3][x-3] == "S"
                count += 1 if x > 2 and y < dimY-3 and grid[y+1][x-1] == "M" and grid[y+2][x-2] == "A" and grid[y+3][x-3] == "S"
            end
        end
    end
    return count
end

def step2(grid)
    dimX = grid[0].size
    dimY = grid.size
    count = 0
    grid.each_with_index do |row, y|
        row.each_char.with_index do |k, x|
            if k == "A" and x > 0 and y > 0 and x < dimX-1 and y < dimY-1
                corners = [grid[y+1][x+1], grid[y-1][x-1], grid[y+1][x-1], grid[y-1][x+1]]
                count += 1 if corners.count("M") == 2 and corners.count("S") == 2 and corners[0] != corners[1]
            end
        end
    end
    return count
end

if __FILE__ == $0

    INPUT_FILE = "input.txt"
    data = File.read(File.join(__dir__, INPUT_FILE)).split("\n")

    start = Time.now
    result1 = step1(data)
    finish = Time.now
    puts "Result1 = #{result1}   \t(in #{'%.6f' % ((finish - start) * 1000)}ms)"

    start = Time.now
    result2 = step2(data)
    finish = Time.now
    puts "Result2 = #{result2}   \t(in #{'%.6f' % ((finish - start) * 1000)}ms)"

end
