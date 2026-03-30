# 📂 YouTube Sentiment Analysis - Source Code

This directory contains the full Django implementation of the **# SENTIMENTAL-ANALYSIS-ON-YOUTUBE-VIDEO-FOR-KIDS** project.

---

## 🛠 Project Components
- `ytksa/`: Core settings and URL configurations.
- `userapp/`: Handles YouTube API calls, VADER analysis, and user dashboard.
- `adminapp/`: Administrative controls and visualization graphs.
- `mainapp/`: Public-facing pages (Home, About, Contact, Registration).
- `assets/`: Static files (CSS, JS, Images).

---

## 🔗 Main URL Entry Points
| URL Path | Name | Description |
| :--- | :--- | :--- |
| `/` | `main_index` | Public Landing Page |
| `/main-user-login` | `main_user_login` | User Login Portal |
| `/main-admin-login`| `main_admin_login`| Admin Login Portal |
| `/user-index` | `user_index` | **Core Tool:** YouTube Search & Analysis |
| `/admin-index` | `admin_index` | Admin Analytics Dashboard |

---

## 🚀 Quick Run
1.  **Ensure Requirements are Installed:** `pip install -r requirements.txt`
2.  **Initialize Database:** `python manage.py migrate`
3.  **Start Development Server:** `python manage.py runserver`
4.  **Open in Browser:** `http://127.0.0.1:8000/`

> [!NOTE]
> For more detailed explanations and feature lists, see the `README.md` in the root extraction directory.
