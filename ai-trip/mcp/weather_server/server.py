import sys, json
from datetime import datetime

def get_weather(city: str, date: str):
    # TODO: call real API (e.g., OpenWeather). Demo response:
    return {
        "city": city,
        "date": date,
        "forecast": "Partly Cloudy",
        "high_f": 72,
        "low_f": 58,
        "precip_prob": 0.2
    }

def main():
    for line in sys.stdin:
        req = json.loads(line)
        if req.get("type") == "tool_call" and req.get("tool") == "get_weather":
            city = req["args"]["city"]
            date = req["args"]["date"]
            # validate
            datetime.fromisoformat(date)
            resp = get_weather(city, date)
            sys.stdout.write(json.dumps({"type":"tool_result","id":req["id"],"result": resp}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
