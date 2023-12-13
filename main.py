from Str_Morse import CODES


def spliter(word):
    morse_list = []
    for letter in word:
        if letter == "":
            print("No Valid Input")
        if letter == " ":
            morse_letter = letter
        else:
            morse_letter = CODES[letter]
        morse_list.append(morse_letter)

    convert = ','.join(morse_list)
    print(f"Your Morse:{convert}")


go_on = True
while go_on:
    Str_word = input('Input string to be converted to Morse:\n').upper()
    if Str_word == '':
        print("No Valid Input")
    else:
        spliter(Str_word)
    converting = input("You want to go on?:\n").lower()
    if converting == 'no':
        go_on = False
        break
