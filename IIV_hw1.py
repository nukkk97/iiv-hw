import math

def read_input_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        tau = float(file.readline().strip())
        messages = []
        for _ in range(n):
            line = file.readline().strip().split()
            priority, transmission_time, period = map(float, line)
            messages.append({'priority': priority, 'transmission_time': transmission_time, 'period': period})
    return n, tau, messages

def calculate_bi(messages):
    n = len(messages)
    bi_values = []
    for i in range(n):
        max_transmission_time = 0
        for j in range(n):
            if messages[j]['priority'] >= messages[i]['priority']:
                max_transmission_time = max(max_transmission_time, messages[j]['transmission_time'])
        bi_values.append(max_transmission_time)
    return bi_values

filename = 'input.dat' # you must change this to your target input file!
n, tau, messages = read_input_file(filename)

B = calculate_bi(messages)
for i in range(n):
    Qi = B[i]
    while (1):
        RHS = B[i]
        for j in range(n):
            if messages[j]['priority']  < messages[i]['priority']:
                RHS += math.ceil((Qi+tau)/messages[j]['period'])*messages[j]['transmission_time']
        if RHS + messages[i]['transmission_time'] > messages[i]['period']:
            print("constraint violation: not schedulable!")
            break
        elif Qi == RHS:
            Ri = Qi + messages[i]['transmission_time']
            print(f"{round(Ri, 2)}")
            break
        else:
            Qi = RHS