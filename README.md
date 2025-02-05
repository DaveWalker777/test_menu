# Тестовое приложение для управления древовидным меню

## Описание

Это тестовое Django-приложение демонстрирует реализацию древовидного меню с помощью пользовательских шаблонных тегов. Функции приложения:

- Создание и управление меню через админку Django.
- Отображение меню на страницах сайта с учётом активного пункта меню и вложенности.
- Рендер нескольких меню на одной странице.
- База данных SQLite

## Выполненные задачи

- Реализован кастомный templatetag для отображения меню (draw_menu)
- Добавлена возможность редактирования меню и его пунктов в стандартной админке Django.
- Реализовано отображение активного пункта меню с учётом его вложенности.
- Создан Dockerfile для запуска проекта в контейнере.

## Доступ к админке

Существует заранее созданный суперпользователь. Чтобы зайти в админку Django, используйте следующие учетные данные:

- **Имя пользователя**: `test`
- **Пароль**: `test`

## Сборка и запуск проекта с помощью Docker

1. Сборка и запуск контейнера с помощью команды:
    ```
    docker-compose up --build
    ```

2. Приложение запустится по адресу [http://localhost:8000](http://localhost:8000)

## Сборка и запуск проекта без Docker


1. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

2. Выполните миграции:
    ```bash
    python manage.py migrate
    ```

3. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

4. Приложение запустится по адресу [http://localhost:8000](http://localhost:8000)

## Дополнительная информация

В проекте добавлено несколько меню и подменю для демонстрации работы древовидного меню на одной странице - main_menu и 
sub_menu.

Текущий пункт меню выделяется красным цветом
