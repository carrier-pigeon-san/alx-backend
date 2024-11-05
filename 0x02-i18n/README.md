# ALX Backend - 0x02 i18n

## Description

This project focuses on internationalization (i18n) and localization (l10n) in web applications: learning how to make your applications accessible to users from different linguistic and cultural backgrounds.

## Learning Objectives

- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings or request headers
- Learn how to localize timestamps

## Project Structure

```
.
├── templates
│   ├── 0-index.html
│   ├── 1-index.html
│   ├── 2-index.html
│   ├── 3-index.html
│   ├── 4-index.html
│   ├── 5-index.html
│   ├── 6-index.html
│   └── 7-index.html
├── translations
│   ├── en
│   │   └── LC_MESSAGES
│   │       ├── messages.mo
│   │       └── messages.po
│   │    
│   └── fr
│       └── LC_MESSAGES
│           ├── messages.mo
│           └── messages.po
├── 0-app.py
├── 1-app.py
├── 2-app.py
├── 3-app.py
├── 4-app.py
├── 5-app.py
├── 6-app.py
├── 7-app.py
├── babel.cfg
└── README.md
```

## Requirements

- Python 3.x
- Flask
- Babel
