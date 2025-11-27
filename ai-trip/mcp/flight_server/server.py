import sys, json

def search_flights(origin, destination, depart_date, return_date, cabin="economy", max_price=None):
    # TODO: integrate Amadeus/Sabre/Skyscanner API
    return {
        "itineraries": [
            {"carrier":"AA","num":"AA123","depart":"2026-03-10T08:05","arrive":"2026-03-10T11:15","duration_min":190,"price_usd":350,"cabin":cabin},
            {"carrier":"DL","num":"DL456","depart":"2026-03-10T09:30","arrive":"2026-03-10T12:45","duration_min":195,"price_usd":370,"cabin":cabin}
        ],
        "constraints": {"max_price": max_price}
    }

def main():
    for line in sys.stdin:
        req = json.loads(line)
        if req.get("type") == "tool_call" and req.get("tool") == "search_flights":
            args = req["args"]
            result = search_flights(**args)
            sys.stdout.write(json.dumps({"type":"tool_result","id":req["id"],"result": result}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
