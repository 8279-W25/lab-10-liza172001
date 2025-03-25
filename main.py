import time
from adafruit_circuitplayground import cp

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
    exit()

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



def play_tone(frequency, duration):
    cp.play_tone(frequency, duration)

for word in morse_output:
    for letter in word.split():
        for symbol in letter:
            if symbol == '.':
                print('.')
                cp.pixels.fill((255, 255, 255))
                play_tone(1000, time_unit)  
                time.sleep(time_unit)
                cp.pixels.fill((0, 0, 0))
            elif symbol == '-':
                print('-')
                cp.pixels.fill((255, 255, 255))
                play_tone(500, 3 * time_unit)  
                time.sleep(3 * time_unit)
                cp.pixels.fill((0, 0, 0))
            time.sleep(time_unit)
        print('_')
        time.sleep(3 * time_unit)
    print('//')
    time.sleep(7 * time_unit)