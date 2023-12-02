def get_first_last_integers(str)
    digitOne = -1
    digitTwo = -1
    str.each_char do |char|
        if char.match?(/\d/) && digitOne == -1
            digitOne = char.to_i
            digitTwo = char.to_i
        elsif char.match?(/\d/)
            digitTwo = char.to_i
        end
    end
    (digitOne * 10) + digitTwo
end

def convert_written_digits_to_numerals(str)
    str.sub!("one", "1")
    str.sub!("two", "2")
    str.sub!("three", "3")
    str.sub!("four", "4")
    str.sub!("five", "5")
    str.sub!("six", "6")
    str.sub!("seven", "7")
    str.sub!("eight", "8")
    str.sub!("nine", "9")
    str
end

line = "xtwone3four"
formatted_line = convert_written_digits_to_numerals(line)
puts get_first_last_integers(formatted_line) # doesn't work because it needs to be in order, so two is formatted before one



total = 0;
File.foreach('day-one/Advent2023DayOneInput.txt') do |line|
    formatted_line = convert_written_digits_to_numerals(line)
    total += get_first_last_integers(formatted_line)
end

puts total