import csv, os, requests
from django.http import JsonResponse
from django.conf import settings
from dotenv import load_dotenv
from fuelroute.utils import calculate_fuel_stops

load_dotenv()

ORS_API_KEY = os.getenv("ORS_API_KEY")

def fuel_route(request):
    start = request.GET.get("start")
    end = request.GET.get("end")

    if not start or not end:
        return JsonResponse({"error": "Missing start or end parameter"}, status=400)

    try:
        # Construct ORS API URL
        url = f"https://api.openrouteservice.org/v2/directions/driving-car"
        headers = {'Authorization': ORS_API_KEY}
        params = {
            "start": f"{start.split(',')[1]},{start.split(',')[0]}",
            "end": f"{end.split(',')[1]},{end.split(',')[0]}"
        }
        res = requests.get(url, headers=headers, params=params)
        data = res.json()

        geometry = data['features'][0]['geometry']['coordinates']
        route = [(coord[1], coord[0]) for coord in geometry]
    except Exception as e:
        print("Routing error:", e)
        return JsonResponse({"error": "Failed to get route"}, status=500)

    try:
        csv_path = os.path.join(settings.BASE_DIR, "fuel-prices-for-be-assessment.csv")
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            fuel_data = [
                {
                    "lat": float(row['latitude']),
                    "lng": float(row['longitude']),
                    "price": float(row['price'])
                }
                for row in reader if row['latitude'] and row['longitude'] and row['price']
            ]
    except Exception as e:
        print("CSV error:", e)
        return JsonResponse({"error": "Failed to read fuel data"}, status=500)

    result = calculate_fuel_stops(route, fuel_data)
    result.update({
        "start": start,
        "end": end,
        "route_map": f"https://maps.openrouteservice.org/directions?n1=0&n2=0&a={start}|{end}&b=0&c=0&k1=en-US&k2=km"
    })

    return JsonResponse(result)
