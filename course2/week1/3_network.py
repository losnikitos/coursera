# python2

import sys


def process(maxBuffer, packets):
    output = []
    buffer = 0
    time = 0
    results = []
    status = 'idle'

    for packet in packets:
        if len(buffer) == maxBuffer:
            # переполнение
            results.append(-1)
            continue

        buffer.append(packet)
        time += packet

        time += packet['size']


# test

def test(bufferSize, packets, expected):
    res = process(bufferSize, packets)
    print 'ok' if res == expected else 'wrong: %s instead of %s' % (res, expected)


test(1, [], [])
test(1, [{"time": 0, "size": 0}], [0])
test(1, [{"time": 0, "size": 1}, {"time": 0, "size": 1}], [0, -1])
test(1, [{"time": 0, "size": 1}, {"time": 1, "size": 1}], [0, 1])

# stdin

bufferSize, packetCount = sys.stdin.readline()
packets = [sys.stdin.readline().split() for _ in range(packetCount)]
packets = [{"time": item[0], "size": item[1]} for item in packets];
print(process(bufferSize, packets))
