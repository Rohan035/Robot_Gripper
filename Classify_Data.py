import requests
import json
import math

def length_width_ratio(x, y, z, angle):
    # Calculate length and width based on the orientation angle
    length = max(x, y)  # Assuming the object's length is along the maximum dimension
    width = min(x, y)   # Assuming the object's width is along the minimum dimension

    # If the angle is not 0
    if angle != 0:
        cos_angle = abs(math.cos(angle))
        sin_angle = abs(math.sin(angle))
        # Calculate rotated length and width
        length = length * cos_angle + width * sin_angle
        width = width * cos_angle + length * sin_angle

    return length / width

def classify_objects(data):
    objects = data["response"]["grasps"]
    for obj in objects:
        x = obj["pose"]["position"]["x"]
        y = obj["pose"]["position"]["y"]
        z = obj["pose"]["position"]["z"]
        angle = obj["pose"]["orientation"]["z"]

        # Calculate the length-to-width ratio
        ratio = length_width_ratio(x, y, z, angle)

        if ratio < 1.2:
            obj["classification"] = "Circular"
        else:
            obj["classification"] = "Elongated"

    return objects


file_path = "test.json"
with open(file_path, "r") as file:
    data = json.load(file)


classified_objects = classify_objects(data)


for obj in classified_objects:
    print("Object UUID:", obj["uuid"])
    print("Classification:", obj["classification"])
    print()
