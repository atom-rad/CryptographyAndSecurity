import sys

def prepare_input_ro(text):
    # Convert the text to uppercase and replace 'J' with 'I'
    text = text.upper().replace('J', 'I')
    return text

def remove_whitespace(text):
    return "".join(text.split())

def generate_key_square_ro(key):
    # Generate the Playfair key square for the complete Romanian alphabet
    alphabet_ro = 'AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ'
    key = key.upper()
    key = ''.join(sorted(set(key), key=key.find))
    key_square = key + ''.join(sorted(set(alphabet_ro) - set(key)))
    return [key_square[i:i+5] for i in range(0, 30, 5)]

def find_char_position(matrix, char):
    # Find the position of a character in the key square
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def encrypt_pair_ro(matrix, pair):
    # Encrypt a pair of characters
    (row1, col1), (row2, col2) = find_char_position(matrix, pair[0]), find_char_position(matrix, pair[1])
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 6][col1] + matrix[(row2 + 1) % 6][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair_ro(matrix, pair):
    # Decrypt a pair of characters
    (row1, col1), (row2, col2) = find_char_position(matrix, pair[0]), find_char_position(matrix, pair[1])
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 6][col1] + matrix[(row2 - 1) % 6][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def playfair_cipher(key, text, operation):
    text = prepare_input_ro(text)
    text = remove_whitespace(text)
    key_square = generate_key_square_ro(key)

    # Pad the text with 'X' if its length is odd
    if len(text) % 2 != 0:
        text += 'X'

    result = ""
    i = 0
    while i < len(text):
        pair = text[i:i+2]



        if operation == 'en':
            encrypted_pair = encrypt_pair_ro(key_square, pair)
            result += encrypted_pair
        elif operation == 'de':
            decrypted_pair = decrypt_pair_ro(key_square, pair)
            result += decrypted_pair

        i += 2

    return result

def main():
    print("Playfair Cipher - Romanian Alphabet")
    print("")

    # Get user input
    key_ro = input("Enter the key: ")
    message_ro = input("Enter the message: ")
    operation = input("Enter 'en' to encrypt or 'de' to decrypt: ").lower()

    # Perform the requested operation
    if operation == 'en' or operation == 'de':
        result = playfair_cipher(key_ro, message_ro, operation)
        print(f"{operation.capitalize()}crypted message: {result}")
    else:
        print("Invalid operation. Please enter 'en' or 'de'.")

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    main()















#        if len(pair) == 2 and pair[0] == pair[1]:
#            # Handle consecutive duplicate letters
#            pair = 'Q' + pair[1]
#            i += 1
#
#            print(f"Processing pair: {pair}")  # Add this line to see the pair value
