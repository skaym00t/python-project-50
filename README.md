# Python Project 50

[![CI Status](https://github.com/skaym00t/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/skaym00t/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/d50f2fac7a7c884e161a/maintainability)](https://codeclimate.com/github/skaym00t/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d50f2fac7a7c884e161a/test_coverage)](https://codeclimate.com/github/skaym00t/python-project-50/test_coverage)


### Hexlet tests and linter status:
[![Actions Status](https://github.com/skaym00t/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/skaym00t/python-project-50/actions)

[![Gendiff presentation](https://asciinema.org/a/JBQpATNVxKYJNJkcFxoQKW7zu.svg)](https://asciinema.org/a/JBQpATNVxKYJNJkcFxoQKW7zu)
# Проект Gendiff

Проект предоставляет функциональность для генерации различий между двумя конфигурационными файлами форматов JSON и YAML.

## Установка

Для настройки проекта с использованием UV выполните следующие шаги:

1. **Установка UV**:
   Если вы ещё не установили UV, сделайте это, выполнив следующую команду:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh

2. Синхронизация зависимостей :
После установки UV перейдите в директорию проекта и синхронизируйте зависимости:

make install

## ASCII-схема работы пакета

+-------------------------+
|       Gendiff           |
|-------------------------|
| Input: file1, file2     |
| Optional: format        |
|-------------------------|
| Step 1: Parse files     |
| Step 2: Build diff      |
| Step 3: Format diff     |
|-------------------------|
| Output: formatted diff   |
+-------------------------+
         |   |
         v   v
+-------------------------+       +-------------------------+
|  JSON/YAML Parser       |       |  Formatter (Stylish/Plain)|
|-------------------------|       |-------------------------|
| Convert JSON/YAML to    |       | Convert internal diff    |
| Python dict             |       | to desired output format |
+-------------------------+       +-------------------------+
         |   |
         v   v
+-------------------------+
|  Diff Builder           |
|-------------------------|
| Compare two dicts and   |
| create internal diff    |
+-------------------------+
         |
         v
+-------------------------+
|  Generate Diff          |
|-------------------------|
| Choose formatter based  |
| on user input or default|
+-------------------------+
         |
         v
+-------------------------+
|  Output                 |
|-------------------------|
| Print formatted diff    |
+-------------------------+

#### Тестирование

Для запуска тестов используйте следующую команду:

make test

Для запуска тестов с покрытием используйте:

make test-coverage

#### Линтер

Для проверки кода на соответствие стандартам PEP8 используйте следующую команду:

make lint