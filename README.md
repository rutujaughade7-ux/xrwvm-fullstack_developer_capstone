# Dealerships: Car Dealership Review Application

**Project name:** Dealerships, a full-stack car dealership review application
**Author:** Rutuja Ughade (GitHub: [rutujaughade7-ux](https://github.com/rutujaughade7-ux))
**Course:** IBM Full-Stack Developer Capstone Project (Coursera)

## Overview

Dealerships is a national car retailer with branches across the United States. This web application lets visitors:

- browse all dealerships and filter them by state,
- read customer reviews for a dealer, each labelled positive, neutral or negative by a sentiment analysis service,
- sign up, log in and log out,
- post a review for a dealership after buying a car,
- read the About Us and Contact Us pages.

## Architecture

| Part | Technology | Folder |
|------|------------|--------|
| Web app and user management | Django (SQLite) | `server/djangoapp`, `server/djangoproj` |
| Static pages (Home, About, Contact) | HTML, Bootstrap | `server/frontend/static` |
| Dynamic pages (Login, Register, Dealers, Dealer, Post Review) | React | `server/frontend/src` |
| Dealer and review API | Node.js, Express, MongoDB | `server/database` |
| Sentiment analysis microservice | Flask, NLTK VADER | `server/djangoapp/microservices` |
| Deployment | Docker, IBM Cloud Code Engine | `server/Dockerfile` |
| CI | GitHub Actions (flake8 and JSHint) | `.github/workflows` |

## Running locally

1. **Backend API and database**
   ```bash
   cd server/database
   docker build . -t nodeapp
   docker-compose up
   ```
   The API runs on port 3030 (for example `http://localhost:3030/fetchDealers`).

2. **Sentiment analyzer**
   ```bash
   cd server/djangoapp/microservices
   docker build . -t sentiment-analyzer
   docker run -p 5050:5000 sentiment-analyzer
   ```

3. **React frontend**
   ```bash
   cd server/frontend
   npm install
   npm run build
   ```

4. **Django app**
   ```bash
   cd server
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
   Open `http://localhost:8000`. The URLs of the backend and the sentiment analyzer are read from `server/djangoapp/.env`.

## Main endpoints

| Endpoint | Purpose |
|----------|---------|
| `/djangoapp/login`, `/djangoapp/logout`, `/djangoapp/register` | user management |
| `/djangoapp/get_dealers`, `/djangoapp/get_dealers/<state>` | all dealers, dealers of a state |
| `/djangoapp/dealer/<id>` | details of one dealer |
| `/djangoapp/reviews/dealer/<id>` | reviews of one dealer with sentiment |
| `/djangoapp/add_review` | post a review (logged in users only) |
| `/djangoapp/get_cars` | car makes and models |
