def add_lvl(lvl_list, added_list):
    new_lvl_list = []
    for item in added_list:
        for lvl in lvl_list:
            new_lvl_list.append({"sum": lvl['sum'] + item[0],
                                 "ryad": lvl['ryad'] + ' ' + str(item[0]),
                                 "ver": lvl['ver'] * item[1]})
    return new_lvl_list


if __name__ == '__main__':
    NN = 10
    arr = [(1, 1 / 2), (2, 1 / 4), (4, 1 / 8), (8, 1 / 16), (16, 1 / 32)]
    lvl_arr = []
    for i in arr:
        lvl_arr.append({"sum": i[0],
                        "ryad": str(i[0]),
                        "ver": i[1]})

    for _ in range(NN - 1):
        lvl_arr = add_lvl(lvl_arr, arr)

    lvl_arr.sort(key=lambda val: val['sum'])

    sum_ver=0
    for i in range(len(lvl_arr)):
        sum_ver += lvl_arr[i]['ver']
        lvl_arr[i]['sum_ver'] = sum_ver
        print(lvl_arr[i])
        if sum_ver > 0.5:
            break
