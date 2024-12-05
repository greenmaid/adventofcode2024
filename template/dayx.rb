#!/usr/bin/env ruby

def parse_data(data)
    return data
end

def step1(parsed_data)
    result = 0
    return result
end

def step2(parsed_data)
    result = 0
    return result
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