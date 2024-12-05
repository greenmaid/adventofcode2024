#!/usr/bin/env ruby

def parse_data(lines)
  result = []
  lines.each do |line|
    nums = []
    line.split(" ").each {|num| nums.append(num.to_i)}
    result.append(nums)
  end
  return result
end

def is_safe?(stages)
  direction = stages[0] < stages[1] ? "+" : "-"
  for i in 0..(stages.size - 2) do
    return false if stages[i] == stages[i+1]
    diff = stages[i] - stages[i+1]
    return false if diff.abs > 3
    return false if diff > 0 and direction == "+"
    return false if diff < 0 and direction == "-"
  end 
  return true
end

def is_quite_safe?(stages)
  return true if is_safe?(stages)
  for i in 0..(stages.size - 1) do
    test_stages = stages.slice(0,i) + stages.slice(i+1, stages.size)
    return true if is_safe?(test_stages)
  end
  return false
end

def step1(reports)
    count = 0
    reports.each do |stages|
      if is_safe?(stages) then count += 1 end
    end
    return count
end

def step2(reports)
  count = 0
  reports.each do |stages|
    if is_quite_safe?(stages) then count += 1 end
  end
  return count
end


if __FILE__ == $0

    # INPUT_FILE = "input_test.txt"
    INPUT_FILE = "input.txt"
    data = File.read(File.join(__dir__, INPUT_FILE)).split("\n")
    parsed = parse_data(data)

    start = Time.now
    result1 = step1(parsed)
    finish = Time.now
    puts "Result1 = #{result1}   \t(in #{'%.6f' % ((finish - start) * 1000)}ms)"

    start = Time.now
    result2 = step2(parsed)
    finish = Time.now
    puts "Result2 = #{result2}   \t(in #{'%.6f' % ((finish - start) * 1000)}ms)"

end