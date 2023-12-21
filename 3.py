import argparse
import string
from enum import Enum
from typing import Tuple

ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" + string.digits + string.punctuation


class Mode(Enum):
    ENCODE = 'encode'
    DECODE = 'decode'


def translate_message(message: str, mode: Mode, key: str) -> str:
    translated = []
    key = key.upper()
    key_length = len(key)

    for index, symbol in enumerate(message):
        alphabet_index = ALPHABET.find(symbol.upper())
        if alphabet_index != -1:
            key_index = ALPHABET.find(key[index % key_length])
            if mode == Mode.ENCODE:
                num = (alphabet_index + key_index) % len(ALPHABET)
            else:  # mode == Mode.DECODE
                num = (alphabet_index - key_index) % len(ALPHABET)

            translated.append(ALPHABET[num])
        else:
            translated.append(symbol)

    return "".join(translated)


def calculate_error(decoded_text: str) -> float:
    with open('output.txt', 'r', encoding='utf-8') as input_file:
        correct_text = input_file.read()
    total_chars = len(correct_text)
    errors = sum(a != b for a, b in zip(correct_text, decoded_text))
    error_percentage = (errors / total_chars) * 100
    return error_percentage


def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def write_file(file_path: str, content: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def process_input(arguments: argparse.Namespace) -> Tuple[str, Mode, str]:
    mode = Mode(arguments.mode)
    key = arguments.key.upper().replace(' ', '')
    text = read_file('input.txt').upper().replace(' ', '')
    return text, mode, key


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Шифр Вижинера')
    parser.add_argument('mode', help='Режим', choices=[mode.value for mode in Mode])
    parser.add_argument('key', help='Ключ шифрования')
    args = parser.parse_args()

    plaintext, mode, key = process_input(args)

    translated_text = translate_message(plaintext, mode, key)

    write_file('output.txt', translated_text)

    if mode == Mode.DECODE:
        error_percentage = calculate_error(translated_text)
        print(f"Процент ошибки: {error_percentage:.2f}%")
