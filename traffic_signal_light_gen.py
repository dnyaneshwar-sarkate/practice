## Python programme to generate traffic signal light 

'''
Condition:
    Red light duration - 5 seconds
    Green light duration- 15 seconds
    Yellow - 2 seconds
'''

# import time

# for _ in range(3):
#     print("Go!")
#     time.sleep(15)

#     print('Watch and Go!')
#     time.sleep(2)

#     print('Stop')
#     time.sleep(5)


##################################################################################################################################

import time

signals = [
    ("🟢  ↑↑↑", 15),
    ("🟡  →", 2),
    ("🔴  ✋", 10)
]

for _ in range(2):
    for signal, duration in signals:
        for sec in range(duration, 0, -1):
            print(f"\r{signal} | {sec:02d} sec", end="")
            time.sleep(1)