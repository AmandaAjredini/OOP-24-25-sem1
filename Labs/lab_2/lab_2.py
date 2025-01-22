
vowels = 'aeiou'


while True:
    user_input = input("Enter an English word to translate to Pig Latin (or '.' to quit): ")
    
    if user_input == '.':
        break 

    

    if user_input[0] in vowels:  # Rule (a): user_input starts with a vowel
        translated_word = user_input + 'yay'
    else:  # Rule (b): Word starts with a consonant
        # Find the first vowel index
        index = next((i for i, char in enumerate(word) if char in vowels), None)

        if index is not None: 
            translated_word = user_input[index:] + user_input[:index] + 'ay'
        else:
            translated_word = user_input 

   
    print("Pig Latin:", translated_word)

