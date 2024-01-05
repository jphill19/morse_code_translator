from logo import logo_art
from translator import decode_morse, encode_to_morse
from audio_encoding import play_morse_sound

options = ['Encode to Morse Code', 'Decode from Morse Code', 'Play Morse Sound', 'Morse Sound Settings', 'Quit']

PITCH = 1
SPEED = 1



def menu():
    print("\nWhat would you like to do?")
    # i is my index and option is the value, and start is so we can begin counting at 1 instead of 0
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")




def main():
    global SPEED
    global PITCH
    print(logo_art)
    
    input_options = None
    while input_options != '5':
        menu()
        user_input = input("\n-> ")
        
        if user_input == '1': 
            # This is the input for the user to encode to Morse Code
            text_to_encode = input("\nWhat would you like to encode to Morse Code: ")
            encoded_text = encode_to_morse(text_to_encode)
            print(f"Morse Code Output:\n{encoded_text}")
            
        elif user_input == '2':
            # This is the input for the user to decode from Morse Code
            text_to_decode = input("\nWhat would you like to decode from Morse Code: ")
            decoded_text = decode_morse(text_to_decode)
            print(f"Morse Code Decoded Output:\n{encoded_text}")

        elif user_input == '3':
            # This is the input for the user to play the Morse Code sound
            if encoded_text:
                print("\nWould you like to play your previous Encoded Message or a new one?")
                print("1. Previous Message")
                print("2. New Message")
                user_input = input("Enter 1 or 2: ")
                if user_input == '1':
                    play_morse_sound(encoded_text, Speed=SPEED, Pitch=PITCH)
                elif user_input == '2':
                    text_to_encode = input("What would you like to encode to Morse Code: ")
                    encoded_text = encode_to_morse(text_to_encode)
                    print(f"Morse Code Output:\n{encoded_text}")
                    play_morse_sound(encoded_text, Speed=SPEED, Pitch=PITCH)
                else: 
                    print("Invalid input, returning to main menu")
                    continue
            else:
                text_to_encode = input("What would you like to encode to Morse Code: ")
                encoded_text = encode_to_morse(text_to_encode)
                print(f"Morse Code Output:\n{encoded_text}")
                play_morse_sound(encoded_text, Speed=SPEED, Pitch=PITCH)

        elif user_input == '4':
            # This is the input for the user to change the Morse Code sound settings ( global variables at the top of the file)
            print("\nMorse Sound Settings:")
            print(f"Current Speed: {SPEED}")
            print(f"Current Pitch: {PITCH}")
            print("\nWould you like to change the Speed or Pitch?")
            print("1. Speed")
            print("2. Pitch")
            print("3. Both")
            print("4. Return to main menu")
            
            sound_input = input("\nEnter 1, 2, 3, or 4: ")
            if sound_input == '1':
                speed_setting= (input("Enter a new Speed number (1-10): "))
                if speed_setting.isdigit() == False:
                    print("Invalid input, please try again")
                    continue
                elif int(speed_setting) < 1 or int(speed_setting) > 10:
                    print("Invalid input, please try again")
                    continue
                SPEED = int(sound_input)
                print(f"New Speed: {SPEED}")
            
            elif sound_input == '2':
                pitch_setting= (input("Enter a new Pitch number (1-10): "))
                if pitch_setting.isdigit() == False:
                    print("Invalid input, please try again")
                    continue
                elif int(pitch_setting) < 1 or int(pitch_setting) > 10:
                    print("Invalid input, please try again")
                    continue
                PITCH = int(sound_input)
                print(f"New Pitch: {PITCH}")
            
            elif sound_input == '3':
                speed_setting= (input("Enter a new Speed number (1-10): "))
                if speed_setting.isdigit() == False:
                    print("Invalid input, please try again")
                    continue
                elif int(speed_setting) < 1 or int(speed_setting) > 10:
                    print("Invalid input, please try again")
                    continue
                SPEED = int(sound_input)
                print(f"New Speed: {SPEED}")
                
                pitch_setting= (input("Enter a new Pitch number (1-10): "))
                if pitch_setting.isdigit() == False:
                    print("Invalid input, please try again")
                    continue
                elif int(pitch_setting) < 1 or int(pitch_setting) > 10:
                    print("Invalid input, please try again")
                    continue
                PITCH = int(sound_input)
                print(f"New Pitch: {PITCH}")

            elif sound_input == '4':
                print("Returning to main menu")
                continue
            else:
                print("Invalid input, please try again")
                continue

        elif user_input == '5':
            input_options = '5'
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid input, please try again")
            continue



if __name__ == "__main__":
    main()









