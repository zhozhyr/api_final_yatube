# API для Yatube

Yatube — это социальная сеть, предоставляющая возможности публикации постов, комментирования, управления контентом и
подписки на авторов. API для Yatube представляет собой программый интерфейс для взаимодействия с функционалом сервиса.

## Запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

```

https://github.com/zhozhyr/api_final_yatube.git

```

```

cd yatube_api

```

Создать и активировать виртуальное окружение:

```

python3 -m venv venv

```

```

source env/bin/activate

```

```

python3 -m pip install --upgrade pip

```

Установить зависимости из файла requirements.txt:

```

pip install -r requirements.txt

```

Выполнить миграции:

```

python3 manage.py makemigrations

```

```

python3 manage.py migrate

```

Запустить проект:

```

python3 manage.py runserver

```

## Документация:

Документация для API после запуска проекта доступна по адресу http://127.0.0.1:8000/redoc

## Примеры запросов:

### Получение постов с пагинацией

```
GET /api/v1/posts/?limit=5&offset=10
Authorization: Bearer ваш_jwt_токен
```

###### Получает 5 постов начиная с 11-й публикации (offset=10). Параметры limit и offset управляют разбивкой на страницы.

### Создание нового поста

```
POST /api/v1/posts/
Content-Type: application/json
Authorization: Bearer ваш_jwt_токен

{
    "text": "Мой первый пост в Yatube!",
    "group": 3
}
```

###### Создаёт новую публикацию с текстом и привязкой к группе. Обязательно нужен JWT-токен.

### Добавление комментария к посту

```
POST /api/v1/posts/7/comments/
Content-Type: application/json
Authorization: Bearer ваш_jwt_токен

{
    "text": "Отличный пост, спасибо!"
}
```

###### Добавляет комментарий к публикации с id=7. Требуется авторизация.

### Поиск в подписках

```
GET /api/v1/follow/?search=user42
Authorization: Bearer ваш_jwt_токен
```

###### Ищет в подписках пользователя по username "user42". Доступно только авторизованным.

### Обновление JWT-токена

```
POST /api/v1/jwt/refresh/
Content-Type: application/json

{
    "refresh": "ваш_refresh_токен"
}
```

###### Возвращает новую пару access/refresh токенов. Используется для продления сессии.