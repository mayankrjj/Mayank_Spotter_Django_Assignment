from geopy.distance import geodesic

def calculate_fuel_stops(route, fuel_data, mpg=10, tank_miles=500):
    stops = []
    total_cost = 0
    distance = 0
    last_point = route[0]

    for point in route[1:]:
        segment = geodesic(last_point, point).miles
        distance += segment
        if distance >= tank_miles:
            nearest = min(fuel_data, key=lambda x: geodesic((x['lat'], x['lng']), point).miles)
            gallons = tank_miles / mpg
            cost = gallons * nearest['price']
            stops.append({
                "location": f"{nearest['lat']},{nearest['lng']}",
                "price_per_gallon": nearest['price'],
                "cost_for_this_segment": round(cost, 2)
            })
            total_cost += cost
            distance = 0
        last_point = point

    return {"fuel_stops": stops, "total_fuel_cost": round(total_cost, 2)}