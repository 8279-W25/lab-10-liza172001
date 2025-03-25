import time


morse_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '//' 
    }


user_text = input("Enter the text to convert into Morse code: ").lower()
try:
   time_unit = float(input("Specify the time unit (milliseconds or seconds): "))
except ValueError:
    print("Enter a Valid input please!Invalid input! Please enter a number")

morse_output = []

 
for word in user_text.split():
    converted_word = []
    for char in word:
        if char in morse_dict:
            converted_word.append(morse_dict[char])
        else:
            print(f"Unsupported character found: {char}")
            exit()
    morse_output.append(' '.join(converted_word))
        


print(morse_output)


for word in morse_output:
    for letter in word.split():
        for symbol in letter:
            if symbol == '.':
                print('.')
                time.sleep(time_unit)
            elif symbol == '-':
                print('-')
                time.sleep(3 * time_unit)
        print('_')
        time.sleep(3 *time_unit)
    print('//')
    time.sleep(7 * time_unit)