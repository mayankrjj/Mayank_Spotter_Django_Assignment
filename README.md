# Spotter Django Fuel Route API

Instructions to run the project...
# README.md

## 🚀 Django Fuel Route Optimizer API (Spotter Assignment)

This Django API calculates the optimal route between two US locations and determines the most cost-effective fuel stops based on fuel prices and vehicle range.

---

### ✅ Features
- Accepts `start` and `end` coordinates via query params
- Uses OpenRouteService API to generate a driving route
- Calculates fuel stops assuming:
  - Max range: 500 miles
  - Fuel efficiency: 10 MPG
- Loads fuel price data from CSV (provided)
- Returns:
  - Route map link
  - Fuel stops (location, price, cost per segment)
  - Total fuel cost

---

### 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/spotter_fuel_api.git
   cd spotter_fuel_api
   ```

2. Create virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # for Mac/Linux
   env\Scripts\activate    # for Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add `.env` file in root:
   ```env
   ORS_API_KEY=your_openrouteservice_api_key
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Run server:
   ```bash
   python manage.py runserver
   ```

---

### 🧪 Testing via Postman

#### GET `/api/fuel-route/`
**Example:**
```http
http://localhost:8000/api/fuel-route/?start=34.0522,-118.2437&end=36.1699,-115.1398
```

**Query Params:**
- `start`: `lat,lng` (e.g., Los Angeles)
- `end`: `lat,lng` (e.g., Las Vegas)

**Sample Response:**
```json
{
  "start": "34.0522,-118.2437",
  "end": "36.1699,-115.1398",
  "route_map": "https://maps.openrouteservice.org/...",
  "fuel_stops": [
    {
      "location": "35.0,-117.0",
      "price_per_gallon": 3.59,
      "cost_for_this_segment": 179.5
    }
  ],
  "total_fuel_cost": 179.5
}
```

---

### 📹 Loom Video Instructions
- Walk through `views.py`, `utils.py`, `.env`, and fuel CSV
- Show API call in Postman with query string parameters
- Keep video under 5 minutes
- Upload it as part of your Spotter application

---

### 📁 Folder Structure
```
spotter_fuel_api/
├── fuelroute/
│   ├── views.py
│   ├── urls.py
│   ├── utils.py
├── spotter_fuel_api/
│   ├── settings.py
│   ├── urls.py
├── .env
├── manage.py
├── requirements.txt
├── README.md
└── fuel-prices-for-be-assessment.csv
```

---

### 📧 Contact
Mayank Rajput – [mayankrajput1304@gmail.com](mailto:mayankrajput1304@gmail.com)

---

**🎉 Good luck and thank you for the opportunity, Spotter!**
