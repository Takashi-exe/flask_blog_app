# Flask Blog App

A simple blog application built using Flask.


## Features in this project

- User registration, login and authentication
- Blog post creation, updating/editing, and deletion
- Password reset via email (using Gmail SMTP)
- Error handling pages



## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask_blog_app.git
cd flask_blog_app
```

### 2. Install Python 3 and pip

Ensure you have Python 3 and pip installed on your system. You can check by running:

```bash
python3 --version
pip --version
```
If not installed, you can download Python from [python.org](https://www.python.org/downloads/).
or install it using your package manager.
For windows;

```bash
choco install python
```
or for macOS:

```bashbrew install python
```
or for Linux:
```bashsudo apt-get install python3 python3-pip
```

### 3. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Edit the `.env` file in the project root with the following content:

```
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
EMAIL_USER=your_gmail_address@gmail.com
EMAIL_PASS=your_app_password
```

#### How to Set Up a Python App Password for Gmail

1. Go to [Google Account Security](https://myaccount.google.com/security).
2. Enable 2-Step Verification if not already enabled.
3. Under "Signing in to Google", select **App Passwords**.
4. Select **Mail** as the app and **Other (Custom name)** as the device (e.g., "Flask Blog App").
5. Click **Generate**. Copy the 16-character app password.
6. Use this password as `EMAIL_PASS` in your `.env` file.

#### How to Set Up a `SECRET_KEY`

This is used by Flask to secure sessions and cookies. You should generate a strong, random value for it.

**To generate a secure key:**

```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and set it in your `.env` file:

```
SECRET_KEY=your_generated_secret_key
```

Never share your `SECRET_KEY` publicly.

### 5. Initialize the Database

```bash
flask shell
>>> from flask_blog import db
>>> db.create_all()
>>> exit()
```

### 6. Run the Application

```bash
python3 run.py
```

Visit `http://127.0.0.1:5000` in your browser.

## License

MIT
```
This guide covers setup, environment variables, and Gmail app password configuration.