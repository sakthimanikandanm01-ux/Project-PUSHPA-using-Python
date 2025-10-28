# save_detection_to_json.py

import json
import time

def save_detection_to_json(counts, filename="email.json"):
    detected_counts = {k: v for k, v in counts.items() if v > 0}
    if not detected_counts:
        print("🟡 No objects detected — JSON not saved.")
        return None

    detection_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "detected": detected_counts
    }

    with open(filename, "w") as f:
        json.dump(detection_data, f, indent=4)

    print(f"✅ JSON saved to {filename}")
    return filename
