# Even or Odd
def even_or_odd(number):
    if (number % 2) == 0:
        return ("Even")
    else:
        return ("Odd")
        
        
        
# Convert a Number to a String 
def number_to_string(num):
    number_to_string = str("")
    return str(num)


# Vowel  Count 
def get_count(sentence):
    count_vowels = 0
    for vowels in ['a', 'e', 'i', 'o', 'u']:
        count_vowels += sentence.count(vowels)
    return count_vowels