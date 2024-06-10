import numpy as np

# Koordinater af skæringspunkterne
A = np.array([10, 150])
B = np.array([8.33, 150])
C = np.array([16.67, 250])

# Beregning af sidelængder
AB = np.linalg.norm(A - B)
BC = np.linalg.norm(B - C)
CA = np.linalg.norm(C - A)

# Beregning af vinkler ved hjælp af cosinusrelationen
angle_A = np.degrees(np.arccos((BC**2 + CA**2 - AB**2) / (2 * BC * CA)))
angle_B = np.degrees(np.arccos((CA**2 + AB**2 - BC**2) / (2 * CA * AB)))
angle_C = np.degrees(np.arccos((AB**2 + BC**2 - CA**2) / (2 * AB * BC)))

# Beregning af trekantens areal ved hjælp af Herons formel
s = (AB + BC + CA) / 2
area = np.sqrt(s * (s - AB) * (s - BC) * (s - CA))

AB, BC, CA, angle_A, angle_B, angle_C, area
