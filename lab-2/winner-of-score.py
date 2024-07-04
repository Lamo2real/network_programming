point_saver = {}

with open('score2.txt', 'r') as file:
    for line in file: 
        parts = line.strip().split()
        first_name = parts[2]
        last_name = parts[3]
        points = int(parts[4])
        name = parts[2] + ' ' + parts[3]

        if name in point_saver:
            point_saver[name] += points
        else:
            point_saver[name] = points


max_points = max(point_saver.values())
for name, total_points in point_saver.items():
    if total_points == max_points:
        print(f"{name}: {total_points}")


