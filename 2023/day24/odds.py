from dataclasses import dataclass


# with open("./odds_input.txt", "r") as f:
with open("./test.txt", "r") as f:
    lines = f.readlines()


@dataclass
class Hailstone:
    x: int
    y: int
    z: int
    vx: int
    vy: int
    vz: int


hailstones = []
for line in lines:
    line = line.strip()
    p, v = line.split(" @ ")
    px, py, pz = p.split(", ")
    vx, vy, vz = v.split(", ")
    hailstones.append(Hailstone(int(px), int(py), int(pz), int(vx), int(vy), int(vz)))

print(hailstones)


def extract_line(hailstone):
    p0 = (hailstone.x, hailstone.y)
    p1 = (hailstone.x + hailstone.vx, hailstone.y + hailstone.vy)
    a = (p0[1] - p1[1]) / (p0[0] - p1[0])
    b = p0[1] - a * p0[0]

    return (a, b)


def extract_intersection(line1, line2):
    a1, b1 = line1
    a2, b2 = line2
    if a1 == a2:
        return None, None
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return (x, y)


# Part one
# lines = [extract_line(hailstone) for hailstone in hailstones]
# total = 0
# for i in range(len(lines)):
#     for j in range(i + 1, len(lines)):
#         x, y = extract_intersection(lines[i], lines[j])
#         if x is None or y is None:
#             continue
#         m = hailstones[i]
#         n = hailstones[j]
#         if m.vx < 0:
#             if x > m.x:
#                 continue
#         else:
#             if x < m.x:
#                 continue
#         if n.vx < 0:
#             if x > n.x:
#                 continue
#         else:
#             if x < n.x:
#                 continue
#         print((x, y))
#         print("---------")
#         if 2e14 < x < 4e14 and 2e14 < y < 4e14:
#         # if 7 < x < 27 and 7 < y < 27:
#             total += 1
# print(total)

# Part two
