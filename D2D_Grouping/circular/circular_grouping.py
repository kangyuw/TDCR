import pandas as pd
import numpy as np
import sys
import time

start_time = time.time()

nMTCD = int(sys.argv[1])
d2d_r = 100
MTCD_Position = pd.read_csv(f'/home/kangyu/TDCR/MTCD_Position/MTCD_position_{nMTCD}.csv', index_col=False)
MTCDx = MTCD_Position.x
MTCDy = MTCD_Position.y
cluster = np.full(nMTCD, -1)
shortest = np.full(nMTCD, np.inf)

for a in range(nMTCD):
    if cluster[a] == -1:
        cluster[a] = a
        for b in range(nMTCD):
            if a != b:
                dist = (MTCDx[a] - MTCDx[b])**2 + (MTCDy[a] - MTCDy[b])**2
                if dist <= d2d_r**2 and dist <= shortest[b]:
                    shortest[b] = dist
                    cluster[b] = a
    print(f'current point {a}, time spent: {time.time() - start_time:.3f}')

MTCD_group = MTCD_Position.assign(clusters=cluster)
MTCD_group.x = round(MTCD_group.x, 3)
MTCD_group.y = round(MTCD_group.y, 3)
MTCD_group.to_csv(f'MTCD_grouping_{nMTCD}.csv', index=False)
