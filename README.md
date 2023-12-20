# ШИФР ЦЕЗАРЯ
## Возможности проекта:
- Шифровать текст.
- Дешифровать текст.
- Читать данные с файла.
- Записывать данные в файл.
- Выводить процент ошибки дешифровки.
## Технологии
![Python](https://img.shields.io/badge/Python-3.9.8-%23254F72?style=flat-square&logo=python&logoColor=yellow&labelColor=254f72)

## Как запустить проект:

Клонировать репозиторий и перейти в него в терминале:

```
git clone https://github.com/RaShaimardanov/caesar_cipher.git
```

Перейдите в директорию:
```
cd caesar_cipher
```
Сохраните в файле 'input.txt' текст для шифрования/дешифрования.
Для запуска программы необходимо запустить файл с аргументами
```
имя файла -> режим -> ключ
```
Пример:
```
python caesar.py encode 3
python caesar.py decode 3
```
Вызов справки:
```
python caesar.py -h
```
Все данные будут сохранены в файл output.txt.
