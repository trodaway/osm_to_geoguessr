import geojson
import csv

def osm_geojson_to_geoguessr_csv(input_geojson, output_csv):
    with open(input_geojson) as input_file:
        gf = geojson.load(input_file)
    coord_list = []
    for i in gf["features"]:
        coords = i["geometry"]["coordinates"]
        coord_list.append(coords[1])
        coord_list.append(coords[0])
    with open(output_csv, 'w') as output_file:
        wr = csv.writer(output_file)
        wr.writerow(coord_list)
