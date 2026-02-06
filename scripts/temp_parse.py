# Heating home log analyzer.
# You are analyzing heating sytem logs (one line per event). Each raw line looks like:
# "2026-01-15 07:10;zone=living;temp=22.5;mode=auto"
# Create raw_lines list of strings with at least 5 lines: at least 2 zones,
# 2 invlaid lines, one line with unknown mode (not auto/manual)

raw_lines: list[str] = [
    "2026-01-15 07:10;zone=living;temp=22.5;mode=auto",
    "2026-01-15 08:10;zone=bedroom;temp=23.5;mode=manual",
    "2026-01-15 09:10;zone=kitchen;temp=22.5;mode=auto",
    "broken line",
    "2026-01-15 10:10;zone=bathroom;temp=23.0;mode=eco",
    "2026-01-15 07:15;zone=living;temp=25.5;mode=auto",
    "2026-01-15 07:20;zone=living;temp=22.0;mode=auto",
    "2026-01-15 08:15;zone=bedroom;temp=22.5;mode=manual",
    "2026-01-15 08:20;zone=bedroom;temp=20.0;mode=manual"
]

# 1) Line parsing with robust errors.
# def parse_line(line: str) -> dict[str,object]
# retuns: "timestamp" - original timesatp string
# "zone" as string, "temp" as float
# "mode" as string - must be auto or manual or raise value error
# if a line is malformed, raise value error with a message that includes the line

def audit_calls(func):
    call_count = 0
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        print(f"Calling function name: {func.__name__} (call #{call_count})")
        result = func(*args, **kwargs)
        print(f"Finished calling function name: {func.__name__} (call #{call_count})")

        return result 
    
    return wrapper

@audit_calls
def parse_line(line: str) -> dict[str,object]:
    try:
        parts = line.split(";")
        if len(parts) < 4:
            raise ValueError("Not enough fields")
        timestamp = parts[0].strip()
        kv_parts = parts[1:]
        kv: dict[str,str] = {}
        for part in kv_parts:
            k,v = part.split("=")
            kv[k.strip()] = v.strip()
        if "zone" not in kv or "temp" not in kv or "mode" not in kv:
            raise ValueError("Missing field")
        
        zone = kv["zone"]
        temp = float(kv["temp"])
        mode = kv["mode"]

        if mode not in ("auto", "manual"):
            raise ValueError(f"Unknown mode: {mode}.")
        
        return {"timestamp": timestamp,
                "zone": zone,
                "temp": temp,
                "mode": mode}
    except ValueError as e:
        raise ValueError (f"Malforemd line {line} {e}") from e


def make_treshold_checker(*, low: float, high: float) -> object:
    def checker(temperature: float) -> str:
        if temperature < low:
            return "LOW"
        if temperature > high:
            return "HIGH"
        return "OK"

valid_lines: list[dict[str,object]] = []

for line in raw_lines:
    valid_lines.append(parse_line(line))

checker = make_treshold_checker(low = 20.0, high = 23)

for valid_line in valid_lines:
    temp = valid_line["temp"]
    zone = str(valid_line["zone"])
    lable = checker(temp)


# 2) Stats per zone.
# def summarize(readings: list[dict[str,object]]) -> dict[str,dict[str,float]]
# for each zone compute count, mintmep, maxtemp and avarage time
# rerun nested dict like: {"living": {"count": 2, "mintmep": 22.0...}}

def summarize(readings: list[dict[str, object]]) -> dict[str, dict[str, float]]:
    stats = {}
    for reading in readings:
        zone = str(reading["zone"])
        temp = float(reading["temp"])
        
        if zone not in stats:
            stats[zone] = {"count": 0, "min_temp": temp, "max_temp": temp, "total_temp": 0.0}
        
        s = stats[zone]
        s["count"] += 1
        s["min_temp"] = min(s["min_temp"], temp)
        s["max_temp"] = max(s["max_temp"], temp)
        s["total_temp"] += temp

    for zone in stats:
        stats[zone]["avg_temp"] = round(stats[zone].pop("total_temp") / stats[zone]["count"], 2)
        
    return stats

#todo:
#count how many low/high events happen per zone

event_counts = {}

for valid_line in valid_lines:
    temp = float(valid_line["temp"])
    zone = str(valid_line["zone"])
    label = checker(temp)
    
    if zone not in event_counts:
        event_counts[zone] = {"LOW": 0, "HIGH": 0}
    
    if label == "LOW":
        event_counts[zone]["LOW"] += 1
    elif label == "HIGH":
        event_counts[zone]["HIGH"] += 1