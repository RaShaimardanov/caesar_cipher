import argparse
import string


ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" + string.digits + string.punctuation


def translate_message(message: str, mode: str, key: str) -> str:
    translated = []
    key_index = 0
    key = key.upper()

    for symbol in message:
        num = ALPHABET.find(symbol)
        if num != -1:
            if mode == "encode":
                num += ALPHABET.find(key[key_index])
            else:  # mode == "decode"
                num -= ALPHABET.find(key[key_index])

            num %= len(ALPHABET)
            translated.append(ALPHABET[num])
            key_index += 1

            if key_index == len(key):
                key_index = 0
        else:
            translated.append(symbol)
    return "".join(translated)


def calculate_error(decoded_text):
    with open('output.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    total_chars = len(text)
    errors = sum(1 for a, b in zip(text, decoded_text) if a != b)
    error_percentage = (errors / total_chars) * 100
    return error_percentage


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Шифр Вижинера')
    parser.add_argument(
        'mode',
        help='Режим',
        choices=['encode', 'decode'],
    )
    parser.add_argument(
        'key',
        help='Ключ шифрования'
    )
    args = parser.parse_args()

    with open('input.txt', 'r', encoding='utf-8') as input_file:
        plaintext = input_file.read()
        plaintext = plaintext.upper().replace(' ', '')

    translated = translate_message(plaintext, args.mode, args.key)

    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(translated)

    if args.mode == 'decode':
        error_percentage = calculate_error(translated)
        print(f"Процент ошибки: {error_percentage:.2f}%")
