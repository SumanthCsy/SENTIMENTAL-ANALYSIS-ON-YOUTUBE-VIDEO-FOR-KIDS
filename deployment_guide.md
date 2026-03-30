# 🚀 Deployment Guide: YouTube Sentiment Analysis For Kids

This guide explains how to move your application from your local development environment to a live server.

## 1. Security Checklist (Mandatory)
Before you go live, you **MUST** update your `ytksa/settings.py` file for security:

1.  **Disable Debug Mode:** Set `DEBUG = False`.
2.  **Allowed Hosts:** Add your live domain (e.g., `['yourdomain.com', 'localhost']`).
3.  **Secret Key:** Use an environment variable instead of a hardcoded string.
4.  **Static Files:** Configure a directory for static files:
    ```python
    import os
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    ```

## 2. Recommended Hosting Platforms

### 🌍 Option A: PythonAnywhere (Recommended for Students)
This is the easiest platform for Django.
1.  Create an account at [PythonAnywhere](https://www.pythonanywhere.com/).
2.  Upload your code using Git or their web interface.
3.  Open their **Consoles** and run:
    ```bash
    pip install -r requirements.txt
    python manage.py collectstatic
    ```
4.  Follow their "Web" tab wizard to set up a new Django app.

### 🌍 Option B: Render or Heroku
1.  Create a `Procfile` in your root folder:
    ```
    web: gunicorn ytksa.wsgi
    ```
2.  Install `gunicorn` and `whitenoise` (for static files):
    ```bash
    pip install gunicorn whitenoise
    ```
3.  Add `whitenoise.middleware.WhiteNoiseMiddleware` to your `MIDDLEWARE` in `settings.py`.
4.  Connect your GitHub repository to [Render.com](https://render.com).

## 3. Environment Variables
To keep your **YouTube API Key** secure, don't hardcode it in `settings.py`. Set it as an environment variable on your server:
- **Key:** `GOOGLE_API_KEY`
- **Value:** `YOUR_API_KEY_HERE`

In `settings.py`, use it like this:
```python
import os
GOOGLE_API = os.getenv('GOOGLE_API_KEY', 'your-fallback-if-local')
```

## 4. Final Deployment Steps
Once your code is on the server, you need to:
1.  **Run Migrations:** `python manage.py migrate`
2.  **Collect Static:** `python manage.py collectstatic`
3.  **Create Admin:** `python manage.py createsuperuser`

---
**Note:** Since you are using **SQLite** (`db.sqlite3`), remember that your data might be lost every time the server restarts on ephemeral platforms like Heroku/Render. 
For a truly persistent site, upgrade to a **PostgreSQL** database (most hosting providers offer a free tier).
