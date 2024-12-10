#!/usr/bin/env ruby

def step1(data)
    matches = data.scan(/mul\((\d+),(\d+)\)/).map {|x| [x[0].to_i, x[1].to_i]}
    return matches.map{|x| x[0]*x[1]}.sum
end

def step2(data)
    matches = data.scan(/(?:mul\((\d+),(\d+)\)|(do\(\))|(don't\(\)))/)
    result = 0
    disabled = false
    matches.each do |m|
      disabled = false if m[2] == "do()"
      disabled = true if m[3] == "don't()"
      result += m[0].to_i * m[1].to_i if m[0] != nil and ! disabled
    end
    return result
end


if __FILE__ == $0

    INPUT_FILE = "input.txt"
    data = File.read(File.join(__dir__, INPUT_FILE))

    start = Time.now
    result1 = step1(data)
    finish = Time.now
    puts "Result1 = #{result1}   \t(in #{'%.6f' % ((finish - start) * 1000)}ms)"

    start = Time.now
    result2 = step2(data)
    finish = Time.now
    puts "Result2 = #{result2}   \t(in #{'%.6f' % ((finish - start) * 1000)}ms)"

end
