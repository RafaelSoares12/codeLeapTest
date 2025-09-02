# CodeLeap API

A simple Django REST Framework (DRF) project providing a CRUD API for posts.  
The API is live and deployed on AWS EC2, available at:  
http://18.230.116.6/api/

---
## Repository

GitHub: [https://github.com/RafaelSoares12/codeLeapTest](https://github.com/RafaelSoares12/codeLeapTest)

---
## Features

- Django 5 + Django REST Framework
- CRUD for **Posts**:
  - Create
  - List
  - Update (PATCH only: `title` and `content`)
  - Delete
- Automatic schema generation with **drf-spectacular**
- Interactive documentation via **Swagger UI** and **ReDoc**
- CORS enabled
- Deployment tested on AWS EC2

---
## Data Model

Each **Post** has the following structure:

```json
{
  "id": "number",
  "username": "string",
  "created_datetime": "datetime",
  "title": "string",
  "content": "string"
}
```

---
## API Endpoints

### Create Post  
`POST /api/posts/`

**Request:**

```json
{
  "username": "string",
  "title": "string",
  "content": "string"
}
```

---

### List Posts  
`GET /api/posts/`

**Response example:**

```json
[
  {
    "id": 1,
    "username": "alice",
    "created_datetime": "2025-09-02T18:10:00Z",
    "title": "Hello",
    "content": "World"
  }
]
```

---

### Update Post (PATCH only)  
`PATCH /api/posts/{id}/`

**Request:**

```json
{
  "title": "new title",
  "content": "new content"
}
```

---

### Delete Post  
`DELETE /api/posts/{id}/`

No content is returned.

---
## Example cURL Commands (Production: 18.230.116.6)

Always include the trailing slash `/`.

**Create:**

```bash
curl -X POST http://18.230.116.6/api/posts/   -H "Content-Type: application/json"   -d '{"username": "alice", "title": "Hello", "content": "World"}'
```

**List:**

```bash
curl http://18.230.116.6/api/posts/
```

**Update:**

```bash
curl -X PATCH http://18.230.116.6/api/posts/1/   -H "Content-Type: application/json"   -d '{"title": "Updated title", "content": "Updated content"}'
```

**Delete:**

```bash
curl -X DELETE http://18.230.116.6/api/posts/1/
```

---
## API Documentation

- Swagger UI: http://18.230.116.6/api/docs/
- ReDoc: http://18.230.116.6/api/redoc/
- OpenAPI Schema: http://18.230.116.6/api/schema/

---
## Local Development

### Requirements
- Python 3.12+
- Virtualenv recommended

### Setup

```bash
git clone https://github.com/RafaelSoares12/codeLeapTest
cd codeLeapTest
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### .env Configuration

Create a `.env` file in the project root with the following variables:

```ini
SECRET_KEY=9pu3b2_ccl-8r(^o(fh9-z81^&q@o^!pzw1b&*&tt7ps+92t1a
DEBUG=True
ALLOWED_HOSTS=localhost
```

---
### Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run

```bash
python manage.py runserver 0.0.0.0:8000
```

Local base URL:  
http://localhost:8000/api/

---
## Local cURL Examples

**Create:**

```bash
curl -X POST http://localhost:8000/api/posts/   -H "Content-Type: application/json"   -d '{"username": "alice", "title": "Hello", "content": "World"}'
```

**List:**

```bash
curl http://localhost:8000/api/posts/
```

**Update:**

```bash
curl -X PATCH http://localhost:8000/api/posts/1/   -H "Content-Type: application/json"   -d '{"title": "Updated title", "content": "Updated content"}'
```

**Delete:**

```bash
curl -X DELETE http://localhost:8000/api/posts/1/
```

**Docs:**

```bash
curl http://localhost:8000/api/docs/
curl http://localhost:8000/api/redoc/
curl http://localhost:8000/api/schema/
```

---

## Deployment

- Deployed on AWS EC2 (Ubuntu).  
- Served with Gunicorn + Nginx.  
- Public base URL: http://18.230.116.6/api/
