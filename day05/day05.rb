#!/usr/bin/env ruby

def parse_data(data)
    rules_data, printing_data = data.split("\n\n")
    rules = Hash.new()
    rules_data.split("\n").each do |r|
      a,b = r.split("|").map {|x| x.to_i}
      rules[a] = [] if rules[a] == nil
      rules[a].append(b)
    end
    printings = []
    printing_data.split("\n").each do |pages_data|
      pages = pages_data.split(",").map {|x| x.to_i}
      printings.append(pages)
    end
    return rules, printings
end

def is_valid?(printing, rules)
  previous = []
  printing.each_with_index do |p,i|
    if rules[p]
      rules[p].each do |nb|
        return false if previous.include?(nb)
      end
    end
    previous.append(p)
  end
  return true
end

def step1(rules, printings)
  count = 0
  printings.each do |p|
    count += p[p.size/2] if is_valid?(p, rules)
  end
  return count
end

def sort_printings(p1,p2, rules)
  if rules[p1] != nil and rules[p1].include? p2
    return -1
  end
  if rules[p2] != nil and rules[p2].include? p1
    return 1
  end
  return 0
end

def step2(rules, printings)
  count = 0
  printings.each do |p|
    if ! is_valid?(p, rules)
      sorted = p.sort {|a,b| sort_printings(a,b, rules)}
      count += sorted[p.size/2]
    end
  end
  return count
end


if __FILE__ == $0

    INPUT_FILE = "input.txt"
    data = File.read(File.join(__dir__, INPUT_FILE))
    rules, printings = parse_data(data)

    start = Time.now
    result1 = step1(rules, printings)
    finish = Time.now
    puts "Result1 = #{result1}   \t(in #{'%.6f' % ((finish - start) * 1000)}ms)"

    start = Time.now
    result2 = step2(rules, printings)
    finish = Time.now
    puts "Result2 = #{result2}   \t(in #{'%.6f' % ((finish - start) * 1000)}ms)"

end
