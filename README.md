# Blog API app
Project setup & Installing Dependencies.
---
Clone this repo by copying this command:

```git clone https://github.com/rakinplaban/BlogAPI```

After cloning enter the **BlogAPI** Directory by `cd BlogAPI` command. After entering the **BlogAPI** directory, you have to create a ***.env*** file.
In the ***.env*** file you have to fillup the following variables.
```
POSTGRES_PASSWORD = # your_password
NAME = # database_name_you_want_to_connect
USER= # username
HOST= # Where_the_db_located
```

Now you have two ways to run the application- 
### With docker-compose -
**Step1:** Apply migration to create database schema.
1. ```docker-compose run web python blog/manage.py makemigrations```
2. ```docker-compose run web python blog/manage.py migrate```

**Setp2:** Run the container.
```docker-compose up```

Setup complete...

---

### With python virtual environment -
**Step1:** Create a virtual environment.

```python -m venv .venv``` 

**Step2:** Activate virtual environment (For windows platform).

```.venv\Scripts\activate```

**Step3:** Install dependencies listed in `requirements.txt` file.

```pip install -r requirements.txt```

**Setp4:** Make migrations.

1. ```python blog\manage.py makemigrations```
2. ```python blog\manage.py migrate```

The database setup is done, the final step is to run the project.

**Step5:** Run server.
```python blog\manage.py runserver```

That's it..

---

API endpoint descriptions:
---

***Authentication:***

Register a new user: ```POST http://127.0.0.1:8000/api/register/```
---

JSON format input:
```
{
  "username": "user1",
  "email": "user@3s.co",
  "password": "password"
}
```
**Output**
'message': 'User registered successfully!'
**Status code: 201 CREATED**

Login user with JWT: ```POST http://127.0.0.1:8000/api/token/```
---

**JSON format input:**
```
{
  "username": "username",
  "password": "password"
}
```

**Output**
```
  {
    "refresh": "refresh_token",
    "access": "access_token"
}
```
**Status Code: 200 Ok**

*Note: The access token will expire after 5 minutes. Please use refresh token to generate a new token.*

Refresh JWT token: `POST http://127.0.0.1:8000/api/token/refresh/`
---

**JSON format Input**
```
{
  "refresh": "refresh_token"
}
```
**Output**
```
{
    "access": "access_token"
}
```
**Status code: 200 OK**

***Blog Post Operation***

List all posts: `GET http://127.0.0.1:8000/api/posts/`
---

**Output**
```
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "title": "My second post post",
            "content": "this is my second img content",
            "author": 1,
            "image": "/media/post_images/demo_UyXEWSx.jpg",
            "created_at": "2025-05-04T15:50:02.049400Z",
            "updated_at": "2025-05-04T15:50:02.049426Z"
        },
        {
            "id": 1,
            "title": "second post",
            "content": "This is my second img content haha",
            "author": 1,
            "image": "/media/post_images/2025322223525946_ban96F6.png",
            "created_at": "2025-05-04T15:47:46.278205Z",
            "updated_at": "2025-05-04T15:49:02.405442Z"
        }
    ]
}
```

**Status Code: 200 OK**


Create a Post: ```POST http://127.0.0.1:8000/api/posts/```
---

**Form field input**(because of image upload):
| Key     | Type | Value               |
|---------|------|---------------------|
| title   | Text | first title         |
| content | Text | first content       |
| image   | File | (image content upload) |

**Header**
| Key            | Value              |
|----------------|--------------------|
|Authorization   | Bearer <auth_token>|

**Output & Status code:**
```
{
    "id": <id_of_post>,
    "title": "first title",
    "content": "first content",
    "author": "<id_of_author_from_user_table>",
    "image": "<file_location>",
    "created_at": "2025-05-05T08:30:04.884813Z",
    "updated_at": "2025-05-05T08:30:04.884907Z"
}
```
- Status code- **201 CREATED**
- For unauthenticated- **401 Unauthorized**
- For not filling up required data- **400 Bad Request**


Update a Post: ```PUT http://127.0.0.1:8000/api/posts/<post_id>```
---

**Form field input**(because of image upload):
| Key     | Type | Value               |
|---------|------|---------------------|
| title   | Text | first title         |
| content | Text | second content       |
| image   | File | (image content upload) |

**Header**
| Key            | Value              |
|----------------|--------------------|
|Authorization   | Bearer <auth_token>|

**Output & Status code:**
```
{
    "id": <id_of_post>,
    "title": "first title",
    "content": "second content",
    "author": "<id_of_author_from_user_table>",
    "image": "<file_location>",
    "created_at": "2025-05-05T08:30:04.884813Z",
    "updated_at": "2025-05-05T08:30:04.884907Z"
}
```
- Status code- **200 OK** 
- For user who isn't author of the post- **403 Forbidden**
- For unauthenticated- **401 Unauthorized**


Delete a Post: ```DELETE http://127.0.0.1:8000/api/posts/<post_id>```
---

**Output & Status Code:**
```
{
    "message": "Post deleted successfully."
}
```
- Status code- **204 No Content** 
- For user who isn't author of the post- **403 Forbidden**
- For unauthenticated- **401 Unauthorized**


View a Post: ```GET http://127.0.0.1:8000/api/posts/<post_id>```
---

**Output & Status code**
```
{
    "id": <id>,
    "title": "<post_title>",
    "content": "<content>",
    "author": <auth_id>,
    "image": "<location>",
    "created_at": "2025-05-04T15:50:02.049400Z",
    "updated_at": "2025-05-04T15:50:02.049426Z"
}
```

- Status code - **200 OK**
- Invalid post id - **404 Not Found**


*For any feedback or advice, feel free to reach out through creating issues or email ^_^*