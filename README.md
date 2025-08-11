# URL Shortener

A simple url shortener service

## 

## Run

### docker compose
```shell
docker compose up
```

### manual
```shell
git clone https://github.com/ArshiaYousefnia/url_shortener.git
cd url_shortener

virtualenv .venv
source .venv/bin/activate

pip install --upgrade pip && pip install -r requirements.txt

fastapi dev main.py
```

## Endpoints Overview

| Method | Endpoint                      | Description              |
|--------|-------------------------------|--------------------------|
| GET    | `/{short_code}`               | Redirect to original URL |
| POST   | `/shorten/`                   | Create a new short URL   |
| GET    | `/shorten/{short_code}`       | Get the original URL     |
| PUT    | `/shorten/{short_code}`       | Update a short URL       |
| DELETE | `/shorten/{short_code}`       | Delete a short URL       |
| GET    | `/shorten/{short_code}/stats` | Get statistics           |

---

## 1. Create a new short URL

**Request**
```http
POST /shorten/ HTTP/1.1
Host: host
Content-Type: application/json

{
  "url": "https://example.com",
}
```

**Response**
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 0,
  "url": "string",
  "short_code": "string",
  "created_at": "2025-08-11T13:27:45.178Z",
  "updated_at": "2025-08-11T13:27:45.178Z"
}
```

## 2. Get an existing short URL

**Request**
```http
GET /shorten/{short_code} HTTP/1.1
Host: host
Accept: application/json
```

**Response**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 0,
  "url": "string",
  "short_code": "string",
  "created_at": "2025-08-11T13:36:46.225Z",
  "updated_at": "2025-08-11T13:36:46.225Z"
}
```

---

## 3. Update an existing short URL

**Request**
```http
PUT /shorten/{short_code} HTTP/1.1
Host: host
Content-Type: application/json

{
  "url": "https://newexample.com"
}
```

**Response**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 0,
  "url": "string",
  "short_code": "string",
  "created_at": "2025-08-11T13:37:00.602Z",
  "updated_at": "2025-08-11T13:37:00.602Z"
}
```

---

## 4. Delete a short URL

**Request**
```http
DELETE /shorten/{short_code} HTTP/1.1
Host: host
```

**Response**
```http
HTTP/1.1 204 No Content
```

---

## 5. Get short URL statistics

**Request**
```http
GET /shorten/{short_code}/stats HTTP/1.1
Host: host
Accept: application/json
```

**Response**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 0,
  "url": "string",
  "short_code": "string",
  "created_at": "2025-08-11T13:38:13.464Z",
  "updated_at": "2025-08-11T13:38:13.464Z",
  "access_count": 0
}
```

Access count is number of times a certain short url is accessed via ```GET```