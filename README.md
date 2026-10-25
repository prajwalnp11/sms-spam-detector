# SMS Spam Detector

A machine learning web application that classifies SMS messages as Spam or Not Spam.

## Technologies Used
- Python
- Flask
- Machine Learning
- HTML and CSS
- Docker
- Kubernetes
- Git and GitHub

## Run Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Run with Docker

```bash
docker build -t sms-spam-detector:local .
docker run --rm -p 8080:8080 sms-spam-detector:local
```

Open http://localhost:8080 in your browser.

## Author
Prajwal N P

GitHub: https://github.com/prajwalnp11/sms-spam-detector
