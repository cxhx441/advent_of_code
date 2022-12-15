from collections import defaultdict

def get_sensors_and_beacons(infile):
    sensors_to_nearest_beacon = dict()
    beacons = defaultdict(set)
    sensors = defaultdict(set)
    with open(infile, 'r') as f:
        for line in f:
            line = line[:-1]
            line = line.split(",")
            line = [int(x) for x in line]
            sensor = (line[0], line[1])
            closest_beacon = (line[2], line[3])
            sensors_to_nearest_beacon[sensor] = closest_beacon
            beacons[closest_beacon[1]].add(closest_beacon[0])
            sensors[sensor[1]].add(sensor[0])
    return sensors_to_nearest_beacon, beacons, sensors

def get_unvisited_neighbors(prev_edge_set, visited):
    new_edge = set()
    for point in prev_edge_set:
        up = (point[0], point[1]-1)
        down = (point[0], point[1]+1)
        left = (point[0]-1, point[1])
        right = (point[0]+1, point[1])
        if up not in visited: new_edge.add(up)
        if down not in visited: new_edge.add(down)
        if left not in visited: new_edge.add(left)
        if right not in visited: new_edge.add(right)
    return new_edge

def get_distances(sensors_to_nearest_beacon):
    dist = dict()
    for sensor, beacon in sensors_to_nearest_beacon.items():
        x_dist = abs(sensor[0] - beacon[0])
        y_dist = abs(sensor[1] - beacon[1])
        dist[sensor] = x_dist + y_dist
    return dist

infile, ROW_OF_INTEREST = "sample_input.txt", 10
infile, ROW_OF_INTEREST = "real_input.txt", 2_000_000

sensors_to_nearest_beacon, beacons, sensors = get_sensors_and_beacons(infile) # (x, y) : (x, y)
dist_from_sens_to_beacon = get_distances(sensors_to_nearest_beacon)
# print(sensors_to_nearest_beacon)
target_row_coverage = set()

# add beacons/sensors to coverage
sensors_in_target_row = set()
beacons_in_target_row = set()
for sensor, beacon in sensors_to_nearest_beacon.items():
    if sensor[1] == ROW_OF_INTEREST:
        sensors_in_target_row.add(sensor[0])
    if beacon[1] == ROW_OF_INTEREST:
        beacons_in_target_row.add(beacon[0])

# add sensed areas to coverage
for sensor in sensors_to_nearest_beacon:
    sensor_to_beacon_dist = dist_from_sens_to_beacon[sensor]
    sensor_to_target_row_dist = abs(ROW_OF_INTEREST - sensor[1])
    if sensor_to_beacon_dist >= sensor_to_target_row_dist:
        # add the target row points visited
        num_points_add_to_each_side = sensor_to_beacon_dist - sensor_to_target_row_dist
        x = sensor[0]
        for i in range(num_points_add_to_each_side + 1):
            target_row_coverage.add(x+i)
            target_row_coverage.add(x-i)





print(len(target_row_coverage) \
    - len(sensors_in_target_row)\
    - len(beacons_in_target_row))
