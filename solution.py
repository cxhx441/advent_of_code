from collections import defaultdict

def get_sensors_and_beacons(infile):
    sensors_to_nearest_beacon = dict()
    beacons = set()
    sensors = set()
    with open(infile, 'r') as f:
        for line in f:
            line = line[:-1]
            line = line.split(",")
            line = [int(x) for x in line]
            sensor = (line[0], line[1])
            closest_beacon = (line[2], line[3])
            sensors_to_nearest_beacon[sensor] = closest_beacon
            beacons.add(closest_beacon)
            sensors.add(sensor)
    return sensors_to_nearest_beacon, beacons, sensors

def get_distances(sensors_to_nearest_beacon):
    dist = dict()
    for sensor, beacon in sensors_to_nearest_beacon.items():
        x_dist = abs(sensor[0] - beacon[0])
        y_dist = abs(sensor[1] - beacon[1])
        dist[sensor] = x_dist + y_dist
    return dist

infile, ROW_OF_INTEREST, COORD_MAX = "sample_input.txt", 10, 20
infile, ROW_OF_INTEREST, COORD_MAX = "real_input.txt", 2_000_000, 4_000_000

def tuning_freq(coords):
    return coords[0]*4_000_000 + coords[1]

sensors_to_nearest_beacon, beacons, sensors = get_sensors_and_beacons(infile) # (x, y) : (x, y)
dist_from_sens_to_beacon = get_distances(sensors_to_nearest_beacon)
# print(sensors_to_nearest_beacon)
no_beacon_coverage = defaultdict(set)


def sensor_covers_point(sensors, point):
    covered = False
    for sensor in sensors:
        dist = abs(sensor[0] - point[0]) + abs(sensor[1] - point[1])
        if dist <= dist_from_sens_to_beacon[sensor]:
            covered = True
    return covered


covered = True
for row in range(COORD_MAX+1):
    print(row)
    for col in range(COORD_MAX+1):
        if not sensor_covers_point(sensors, (row, col)):
            print(tuning_freq((row, col)))

print('hi')
# # add beacons/sensors to coverage
# sensors_coverage = defaultdict(set)
# beacons_coverage = defaultdict(set)
# for sensor, beacon in sensors_to_nearest_beacon.items():
#     sensors_coverage[sensor[1]].add(sensor[0])
#     beacons_coverage[beacon[1]].add(beacon[0])

# # add sensed areas to coverage
# for sensor in sensors_to_nearest_beacon:
#     sensor_to_beacon_dist = dist_from_sens_to_beacon[sensor]
#     # sensor_to_target_row_dist = abs(ROW_OF_INTEREST - sensor[1])
#     # if sensor_to_beacon_dist >= sensor_to_target_row_dist:
#     for dist in range(sensor_to_beacon_dist):
#         print(dist, sensor_to_beacon_dist)
#         print('hi')
#         # add the target row points visited
#         num_points_add_to_each_side = sensor_to_beacon_dist - dist
#         row_up = sensor[1] - dist
#         row_down = sensor[1] + dist
#         col = sensor[0]
#         for i in range(num_points_add_to_each_side + 1):
#             no_beacon_coverage[row_up].add(col+i)
#             no_beacon_coverage[row_down].add(col+i)
#             no_beacon_coverage[row_up].add(col-i)
#             no_beacon_coverage[row_down].add(col-i)

# print(len(no_beacon_coverage[ROW_OF_INTEREST]) \
#     - len(beacons_coverage[ROW_OF_INTEREST])\
#     - len(sensors_coverage[ROW_OF_INTEREST]))
