INPUT_FILE = '05-input.txt'

class Entry:
    def __init__(self, origin, destination, range):
        self.origin = int(origin)
        self.destination = int(destination)
        self.range = int(range)

class Maps:
    seeds = None
    seed_soil = []
    soil_fertilizer = []
    fertilizer_water = []
    water_light = []
    light_temperature = []
    temperature_humidity = []
    humidity_location = []

    def _get_correspondance(self, number, map):
        for e in map:
            if number in range(e.origin, e.origin + e.range + 1):
                return e.destination + number - e.origin
        return number

    def get_location(self, seed_number):
        soil = self._get_correspondance(seed_number, self.seed_soil)
        fertilizer = self._get_correspondance(soil, self.soil_fertilizer)
        water = self._get_correspondance(fertilizer, self.fertilizer_water)
        light = self._get_correspondance(water, self.water_light)
        temperature = self._get_correspondance(light, self.light_temperature)
        humidity = self._get_correspondance(temperature, self.temperature_humidity)
        return self._get_correspondance(humidity, self.humidity_location)

    def get_closest_location(self):
        min = 0
        for seed in self.seeds:
            location = self.get_location(int(seed))
            if min == 0 or location < min:
                min = location
        return min

def parse_input():
    maps = Maps()
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        seeds_line = lines[0]
    maps.seeds = seeds_line[:-1].split(" ")[1:]
    iterator = 1
    m = None
    while iterator < len(lines) - 1:
        iterator += 1
        line = lines[iterator][:-1]
        if not line:
            continue
        elif line == 'seed-to-soil map:':
            m = maps.seed_soil
        elif line == 'soil-to-fertilizer map:':
            m = maps.soil_fertilizer
        elif line == 'fertilizer-to-water map:':
            m = maps.fertilizer_water
        elif line == 'water-to-light map:':
            m = maps.water_light
        elif line == 'light-to-temperature map:':
            m = maps.light_temperature
        elif line == 'temperature-to-humidity map:':
            m = maps.temperature_humidity
        elif line == 'humidity-to-location map:':
            m = maps.humidity_location
        else:
            entry_info = line.split(" ")
            m.append(Entry(entry_info[1], entry_info[0], entry_info[2]))
    return maps

def main():
    maps = parse_input()
    return maps.get_closest_location()

print(main())
