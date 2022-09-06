

def mod_cycle_massive(a, Q):
    for q in range(2, Q + 1):
        M, p = [], 1
        while (a ** p) % q not in M:
            M.append((a ** p) % q)
            p += 1
        print('Множество для [' + str(a) + ', ' + str(q) + ']: ' + str(M))
#       M.sort()
#       print(st + '. Его отсортированная версия: ', M)
    return 0

mod_cycle_massive(int(input()), int(input()))