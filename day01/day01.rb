#!/usr/bin/env ruby

def parse_data(data)
    list1 = []
    list2 = []
    data.each do |line|
        numbers = line.split
        list1.append(numbers[0].to_i)
        list2.append(numbers[1].to_i)
    end
    return list1.sort, list2.sort
end

def step1(list1, list2)
    result = 0
    for i in 0..(list1.size - 1) do
        result += (list1[i] - list2[i]).abs
    end
    return result
end

def step2(list1, list2)
   similarity = 0
   list1.each do |num|
      similarity += num * list2.count(num)
   end
   return similarity
end


if __FILE__ == $0

    # INPUT_FILE = "input_test.txt"
    INPUT_FILE = "input.txt"
    data = File.read(File.join(__dir__, INPUT_FILE)).split("\n")
    list1, list2 = parse_data(data)

    start = Time.now
    result1 = step1(list1, list2)
    finish = Time.now
    puts "Result1 = #{result1}   \t(in #{'%.6f' % ((finish - start) * 1000)}ms)"

    start = Time.now
    result2 = step2(list1, list2)
    finish = Time.now
    puts "Result2 = #{result2}   \t(in #{'%.6f' % ((finish - start) * 1000)}ms)"

end