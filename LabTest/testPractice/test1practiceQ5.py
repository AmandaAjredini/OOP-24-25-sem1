def reverseSecondWord(sentence):
    lines = sentence.splitlines()

    result_lines = ""

    for line in lines:
        words = line.split()

        for i in range(1, len(words), 2):
            words[i] = words[i][::-1]

        result_lines += " ".join(words) + "\n"

    print(result_lines)



sentence = input("Please enter any sentence: ")
reverseSecondWord(sentence)
