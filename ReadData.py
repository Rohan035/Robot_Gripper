import requests

url = "http://192.168.1.111/api/v1/nodes/rc_itempick/services/compute_grasps"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

data = {
    "args": {
        "pose_frame": "camera",
        "suction_surface_length": 0.02,
        "suction_surface_width": 0.02
    }
}

response = requests.put(url, headers=headers, json=data)

with open("test.json", "w") as f:
    f.write(response.text)

print("Response saved to test.json")
