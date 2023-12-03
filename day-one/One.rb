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
    digit_words_to_numbers = {
      'zero' => '0', 'one' => '1', 'two' => '2', 'three' => '3', 'four' => '4',
      'five' => '5', 'six' => '6', 'seven' => '7', 'eight' => '8', 'nine' => '9'
    }
  
    # Sort the digit words by length so that the longest words are tried first
    sorted_digit_words = digit_words_to_numbers.keys.sort_by(&:length).reverse
  
    new_str = ''
    i = 0
  
    while i < str.length
      matched = false
  
      # Try to match the longest word possible at the current position
      sorted_digit_words.each do |word|
        if str[i, word.length].casecmp?(word)
          # If a match is found, append the corresponding digit to the new string
          new_str << digit_words_to_numbers[word]
          # Skip ahead by the length of the matched word
          i += word.length
          matched = true
          break
        end
      end
  
      # If no match was found, just append the current character
      unless matched
        new_str << str[i]
        i += 1
      end
    end
  
    new_str
end
   # Couldn't get this to work. I don't know how to deal with overlap

line = "oneight"
formatted_line = convert_written_digits_to_numerals(line)
puts formatted_line
# puts get_first_last_integers(formatted_line) # doesn't work because it needs to be in order, so two is formatted before one



total = 0;
File.foreach('day-one/Advent2023DayOneInput.txt') do |line|
    formatted_line = convert_written_digits_to_numerals(line)
    total += get_first_last_integers(formatted_line)
end

puts total