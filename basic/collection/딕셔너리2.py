place = dict()
place['좋아하는 장소'] = '인천'
place['싫어하는 장소'] = '강릉'

print(place['좋아하는 장소'])
print(place)
place['좋아하는 장소'] = '신촌'
print(place.keys())
print(place.values())

for x in place:
    print(x, place[x])

