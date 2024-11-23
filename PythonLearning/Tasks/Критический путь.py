road = input()
road = road.split(',')
road.reverse()

road_dict = {}

for i in road:
    update_item = i.split(':')
    road_dict[update_item[0]] = update_item[1]

result_road = ['1', road_dict['1']]
while result_road[-1] != '0':
    for i, j in road_dict.items():
        if result_road[-1] == '0':
            break
        if i == result_road[-1]:
            result_road.append(j)

result_road.reverse()
print(', '.join(result_road))