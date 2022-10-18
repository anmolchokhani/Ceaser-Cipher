"""  
I have written the main logic. Rest can be modified like we can create diff
functions for inputs, etc


"""


import string

all_char=list(string.ascii_lowercase)


def main():
    possible_input= [ 'encode', 'decode']
    encoded_word=""
    decoded_word=""
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
 
        if direction in possible_input:
            text= input("Typer your message: ").lower()
            text.strip()
            shift = int(input("Type the shift number: "))
            total_char= len(all_char)
            shift = shift % total_char
            

            if direction == "encode":
                for _ , letter in enumerate(text):
                    after_shift_index = shift + all_char.index(letter) 
                    after_shift_index = after_shift_index % total_char
                    encoded_word += all_char[after_shift_index]
                print(encoded_word)
           
            else:
                for _ , letter in enumerate(text):
                    after_shift_index = (total_char + (all_char.index(letter) - shift))% total_char
                    after_shift_index = after_shift_index % total_char
                    decoded_word += all_char[after_shift_index]
                print(decoded_word)
             
            break
        else:
            print("The direction inputed is wrong try again")



main()
