# Chat API app
This is my minimal chatbot application (API based) built with Django REST Framework (DRF). I integrated a very lightweight NLP model, distilgpt2, to generate responses to users' messages.

Project setup & Installing Dependencies.
---
Clone this repo by copying this command:

```git clone https://github.com/rakin54/Raktch_ChatAPI```

After cloning enter the **Raktch_ChatAPI** Directory by `cd Raktch_ChatAPI` command. 


### How to run this application -
**Step1:** Create a virtual environment.

```python -m venv .venv``` 

**Step2:** Activate virtual environment (For windows command prompt).

```.venv\Scripts\activate```

For bash terminal it's ```source .venv/Scripts/activate```

**Step3:** Install dependencies listed in `requirements.txt` file.

```pip install -r requirements.txt```

**Step4:** Login to huggingface by createing huggingface token with *READ* permission. Then use this token to login to huggingface account in command prompt by this command:

```huggingface-cli login```

It may ask for permission to use the token as github authentication. Please grant the permission.

**Step5:** Run server.
```python blog\manage.py runserver```

That's it..

---

API endpoint descriptions:
---

Send text message: ```POST http://127.0.0.1:8000/api/posts/```
---

JSON format input:
```
{
    "message" : "What's my name?"
}
```

**Output & Status code:**
1. For a Successful Request:
```
{
    "reply": "What's my name?\n\nWell my name is James - it's James Kline - I'm the author of the bestselling series ‑A Life is a Lifetime.‌\nHello to the readers!\nI have decided to name my"
}
```
**Status code-** ***200 OK***

2. For a Request without Passing Message or empty field request.
```
{
    "error": "No message provided"
}
```
**Status code-** ***400 Bad Request***




I spent more then 2 hours on this project.

*For any feedback or advice, feel free to reach out through creating issues or email.*


### Reference:
1. Sanh, V., Debut, L., Chaumond, J., & Wolf, T. (2019). DistilBERT, a distilled version of BERT: Smaller, faster, cheaper and lighter. ArXiv. https://arxiv.org/abs/1910.01108