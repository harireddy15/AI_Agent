import sys, json

def search_hotels(city, check_in, check_out, guests=1, min_rating=3, max_price=None):
    # TODO: integrate Booking/Expedia API
    return {
        "hotels": [
            {"name":"The Parkside","rating":4.3,"price_usd":145,"neighborhood":"Downtown","amenities":["wifi","gym"]},
            {"name":"Riverlight Suites","rating":4.6,"price_usd":185,"neighborhood":"Riverfront","amenities":["wifi","pool","spa"]}
        ],
        "filters":{"min_rating":min_rating,"max_price":max_price}
    }

def main():
    for line in sys.stdin:
        req = json.loads(line)
        if req.get("type") == "tool_call" and req.get("tool") == "search_hotels":
            result = search_hotels(**req["args"])
            sys.stdout.write(json.dumps({"type":"tool_result","id":req["id"],"result": result}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
