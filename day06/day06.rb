#!/usr/bin/env ruby

def get_position(grid)
  grid.each_with_index do |row, y|
    row.each_char.with_index do |k, x|
      return x, y if k == "^"
    end
  end
end

DIRECTIONS = {
  "<" => [-1, 0],
  ">" => [1, 0],
  "^" => [0, -1],
  "v" => [0, 1]
}

def scan_forward(x, y, direction, grid, additional_obstacle)
  dx, dy = DIRECTIONS[direction]
  nx, ny = x + dx, y + dy
  return nx, ny, "" if nx < 0 || ny < 0 || nx >= grid[0].size || ny >= grid.size
  return nx, ny, "#" if nx == additional_obstacle[0] && ny == additional_obstacle[1]
  return nx, ny, grid[ny][nx]
end

TURN = {
  "<" => "^",
  ">" => "v",
  "^" => ">",
  "v" => "<"
}

def move(x, y, direction, grid, additional_obstacle)
  nx, ny, forward = scan_forward(x,y, direction, grid, additional_obstacle)
  while forward == "#"
    direction = TURN[direction]
    nx, ny, forward = scan_forward(x,y, direction, grid, additional_obstacle)
  end
  return nx, ny, direction, forward
end

def simulation(x, y, direction, grid, additional_obstacle=[-1,-1])
  visited = {[x,y] => true}
  oriented_visited = {[x,y,direction] => true}
  oriented_visited_list = [[x,y,direction]]
  while true
    x, y, direction, val = move(x, y, direction, grid, additional_obstacle)
    return visited, oriented_visited_list if val == ""
    return nil, nil if oriented_visited.has_key?([x,y,direction])
    visited[[x,y]] = true
    oriented_visited[[x,y,direction]] = true
    oriented_visited_list.append([x,y,direction])
  end
end

def step1(grid)
  x, y = get_position(grid)
  direction = "^"
  visited, _ = simulation(x, y, direction, grid)
  return visited.size
end

def step2(grid)
  x, y = get_position(grid)
  direction = "^"
  _, visited = simulation(x, y, direction, grid)

  count = 0
  tested = Hash.new
  visited.each_with_index do |step, i|
    if i > 0
      ox, oy, _ = step
      next if tested.has_key? [ox,oy]
      tested[[ox,oy]] = true
      px, py, p_dir = visited[i-1]
      v, _ = simulation(px, py, p_dir, grid, additional_obstacle=[ox,oy])
      count += 1 if v == nil
    end
  end
  return count
end

if __FILE__ == $0
#  INPUT_FILE = "input_test.txt"
  INPUT_FILE = "input.txt"
  grid = File.read(File.join(__dir__, INPUT_FILE)).split("\n")

  start = Time.now
  result1 = step1(grid)
  finish = Time.now
  puts "Result1 = #{result1}   \t(in #{'%.6f' % ((finish - start) * 1000)}ms)"

  start = Time.now
  result2 = step2(grid)
  finish = Time.now
  puts "Result2 = #{result2}   \t(in #{'%.6f' % ((finish - start) * 1000)}ms)"
end
