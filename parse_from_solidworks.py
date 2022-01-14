import json
import helpers as hp


target_name = "wig_target"
target_id = "1"
points = []
with open("points_wig.txt", "r") as f:
    [points.append([float(x) for x in line.replace(",", ".").split("\t")]) for line in f]

model_definition = {
    "ModelData": {
        "name": target_name,
        "id": target_id,
        "status": 0,
        "points": hp.convert_points_to_json_array(points),
    }
}

jsonFile = open(f"{target_name}.json", "w")
jsonFile.write(json.dumps(model_definition))
jsonFile.close()
print(model_definition)
print(len(points))






