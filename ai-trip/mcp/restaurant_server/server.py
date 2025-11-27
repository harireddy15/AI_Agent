import sys, json

def search_restaurants(city, date, time, party_size=2, cuisine=None):
    # TODO: integrate Yelp/OpenTable API
    return {
        "options": [
            {"name":"Basil & Birch","cuisine":"New American","price_level":"$$","reserve_url":"https://...","walk_time_min":8},
            {"name":"Piccolo Forno","cuisine":"Italian","price_level":"$$$","reserve_url":"https://...","walk_time_min":12}
        ],
        "query":{"city":city,"date":date,"time":time,"party_size":party_size,"cuisine":cuisine}
    }

def main():
    for line in sys.stdin:
        req = json.loads(line)
        if req.get("type") == "tool_call" and req.get("tool") == "search_restaurants":
            result = search_restaurants(**req["args"])
            sys.stdout.write(json.dumps({"type":"tool_result","id":req["id"],"result": result}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
