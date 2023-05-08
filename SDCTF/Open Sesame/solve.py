
MOD = 131
FLAG_LEN = 36
DOOR_SHAPE = [94,68,98,110,45,81,6,76,119,53,16,19,122,91,51,44,13,35,2,124,83,101,75,122,75,124,37,8,127,0,22,130,11,42,114,19]

def gencave(flaglen):
    cave = []
    ps = []
    i = 1
    while len(cave) <= flaglen:
        i += 1
        skip = False
        for p in ps:
            if i % p == 0:
                skip = True
        if not skip:
            ps.append(i)
            if not cave or len(cave[(-1)]) >= flaglen:
                cave.append([])
            cave[(-1)].append(i % MOD)
    cave = cave[:-1]
    return cave

def solveModule(arr, sols, MOD):
    solution = []
    while len(solution) != len(sols):
        oldArr = [x[:] for x in arr]
        oldSols = sols[:]
        while len(oldArr) != 1:
            newArr = []
            newSols = []
            lastEq = oldArr[-1][:]
            lastSol = oldSols[-1]
            for i in range(len(oldSols)-1):
                thisEq = oldArr[i][:]
                thisSol = oldSols[i]
                newEq = []
                for n in range(len(lastEq) - 1):
                    newEq.append((lastEq[n] * thisEq[-1] - thisEq[n] * lastEq[-1]) % MOD)
                newSol = (lastSol * thisEq[-1] - thisSol * lastEq[-1]) % MOD
                newArr.append(newEq[:])
                newSols.append(newSol)
            # get last line
            # for all other lines build compare, then subtract, then add it as new line
            # forget last line at end
            oldArr = [x[:] for x in newArr]
            oldSols = newSols[:]
        print(oldArr)
        for n in range(MOD):
            if (oldArr[0][0] * n) % MOD == oldSols[0]:
                solution.append(n)
                break
        for eq in arr:
            eq.append(eq[0])
            eq.pop(0)
    return solution

cave = [[4, 3, 2], [-2, 2, 3], [3, -5, 2]]
sol = [4, 4, -4]

count = 0
for n in solveModule(gencave(36), DOOR_SHAPE, MOD):
    if n == 0:
        count += 1
        print("$", end="")
    else:
        print(chr(n), end="")
print()
print(count)
# sdctf{0p$n$s$sA$3_bUt$$n$l3$7Sp3aK!}


# sdctf{0p3n_s3sAm3_bUt_1n_l337Sp3aK!}