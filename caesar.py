import string
import argparse


ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' + string.digits + string.punctuation


def caesar_cipher(text, key, mode):
    result = ''

    for char in text:
        if char in ALPHABET:
            index = ALPHABET.index(char)
            if mode == 'encode':
                new_index = (index + key) % len(ALPHABET)
            else:  # mode == 'decode'
                new_index = (index - key) % len(ALPHABET)
            result += ALPHABET[new_index]
        else:
            result += char

    return result


def calculate_error(decoded_text):
    with open('output.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    total_chars = len(text)
    errors = sum(1 for a, b in zip(text, decoded_text) if a != b)
    error_percentage = (errors / total_chars) * 100
    return error_percentage


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Шифр Цезаря')
    parser.add_argument(
        'mode',
        help='Режим',
        choices=['encode', 'decode'],
    )
    parser.add_argument(
        'key',
        help='Ключ шифрования',
        type=int
    )
    args = parser.parse_args()

    with open('input.txt', 'r', encoding='utf-8') as input_file:
        plaintext = input_file.read()

    plaintext = plaintext.upper().replace(' ', '')
    ciphertext = caesar_cipher(plaintext, args.key, args.mode)

    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(ciphertext)

    if args.mode == 'decode':
        error_percentage = calculate_error(ciphertext)
        print(f"Процент ошибки: {error_percentage:.2f}%")
