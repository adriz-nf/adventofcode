with open('/Users/andrewemmett/Projects/adventofcode/2020/day13input.txt') as file:
    data = [line.strip() for line in file.readlines()]
time = int(data[0])
freqs = data[1].split(',')
#print(freqs)

def find_bus(time, freqs):
    bus_list = map(int, freqs)
    bus_list = []
    for i in freqs:
        try:
            bus_list.append(int(i))
        except:
            continue
    best_wait_time = min(bus_list)
    # extract ints from freqs
    for bus_id in bus_list:
        waiting_time = (((time // bus_id) +1) * bus_id) - time
        if waiting_time < best_wait_time:
            best_wait_time = waiting_time
            best_bus = bus_id 
        else:
            continue
    return best_bus * best_wait_time

print(find_bus(time, freqs))


def check_offset(t, t_offset, bus_id):
    return (t+t_offset) % bus_id == 0

def find_t(freqs):
    bus_list = []
    for i in freqs:
        try:
            bus_list.append(int(i))
        except:
            1

    t=1
    step_size = bus_list[0]
    matching_buses = []
    while len(matching_buses) != len(freqs):
        matching_buses.clear()
        for t_offset, bus_id in enumerate(bus_list[1:],1):
            matching_buses.append(bus_id)
            while check_offset(t, t_offset, (bus_id)):
                    continue
                else:
                    break
            
        t += step_size 
    return t

def find_time(freqs):
    bus_list = []
    for i in freqs:
        try:
            bus_list.append(int(i))
        except:
            bus_list.append(1)
    
    t=0
    step_size = bus_list[0]

    for t_offset , bus_id in enumerate(bus_list[1:], 1):
        while (t+t_offset) % bus_id != 0:
            t += step_size
        step_size *= bus_id    
        
    return t

print(find_time(freqs))


#print(find_t(freqs))
#find_t(freqs)
print('done')
