# News Fetcher (Python)

A lightweight command-line tool that fetches the latest news articles based on a user-provided topic. It uses the NewsAPI service to retrieve results and displays each article’s title and link in a readable format. 

---

## Features

* Accepts any topic or keyword from the user.
* Sends a GET request to NewsAPI’s `/v2/everything` endpoint.
* Retrieves fresh news sorted by publish time.
* Prints titles and URLs for all returned articles.
* Simple, minimal, and easy to modify.

---

## How It Works

1. User enters a news topic:

   ```python
   query = input("What type of news are you interested in today? ")
   ```
2. Script builds a NewsAPI URL with the query, date filter, and API key.

3. Sends request using:

   ```python
   r = requests.get(url)
   ```
4. Extracts article list:

   ```python
   articles = data["articles"]
   ```
5. Prints each article’s title and URL in a numbered format.

---

## Installation

### Install dependencies:

```bash
pip install requests
```

---

## Setup

### Get a NewsAPI key

Sign up at: [https://newsapi.org/](https://newsapi.org/)
Replace the placeholder key in the script:

```python
api = "your_api_key_here"
```

---

## Usage

Run the script:

```bash
python main.py
```

Example interaction:

```
What type of news are you interested in today? AI
```

Example output:

```
1 OpenAI releases new model https://example.com/ai-news
****************************************
2 AI transforms industry... https://example.com/ai-update
****************************************
```

---

## Requirements

* Python 3.x
* NewsAPI key
* Internet connection

---

## Notes

* The included key in the file must be **replaced**; never hard-code real API keys in public code.
* `from=2025-02-08` is fixed; adjust to dynamically fetch current news.
* NewsAPI has free-tier request limits.

---
