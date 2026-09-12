# Business Listening Dashboard

A web-based dashboard for monitoring and analyzing business listings by city, category, and source.

## Project Overview

The Business Listening Dashboard connects a React frontend with a FastAPI backend and MySQL database.

It displays business listing information in an easy-to-understand dashboard format.

## Features

- Total business listings count
- Total cities count
- Total business categories count
- Total listing sources count
- City-wise listing analysis
- Category-wise listing analysis
- Source-wise listing analysis
- Data fetched dynamically from MySQL database
- REST API using FastAPI
- Responsive dashboard interface

## Technologies Used

### Frontend
- React.js
- Vite
- JavaScript
- CSS

### Backend
- Python
- FastAPI
- Uvicorn

### Database
- MySQL

## Database Table

The project uses a `listing_master` table containing:

- Business Name
- Category
- City
- Address
- Phone
- Source

## API Endpoints

- `GET /` - Check whether the API is running
- `GET /api/dashboard/city` - Get city-wise listing counts
- `GET /api/dashboard/category` - Get category-wise listing counts
- `GET /api/dashboard/source` - Get source-wise listing counts
- `POST /api/listings/bulk` - Insert multiple business listings

## Project Structure

```text
business-listening-dashboard/
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── App.css
    │   └── main.jsx
    ├── package.json
    └── README.md