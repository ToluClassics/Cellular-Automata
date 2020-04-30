def ca(rule_list):
    # initial generation grid
    init_grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0]
    # subsequent generations grid
    new_gen_grid = init_grid[:]

    # dictionary to map cell values to a symbol
    symbol_dic = {0: '#', 1: '@'}

    print(''.join([symbol_dic[x] for x in new_gen_grid]))
    x = {'a':[1,1,1],
         'b':[1,1,0],
         'c':[1,0,1],
         'd':[1,0,0],
         'e':[0,1,1],
         'f':[0,1,0],
         'g':[0,0,1],
         'h':[0,0,0]}
    # 32 new generations
    steps = 1
    while steps < 32:
        new_gen_grid = []
        for i in range(len(init_grid)):
            if i > 0 and i < 63:
                neighborhood_list = [init_grid[i - 1],init_grid[i],init_grid[i+1]]
                #print(neighborhood_list)
                for k,(key,lis) in enumerate(x.items()):
                    if lis == neighborhood_list:
                        new_gen_grid.append(rule_list[k])
                '''if init_grid[i - 1] == init_grid[i + 1]:
                    #new_gen_grid.append(0)
                else:
                    new_gen_grid.append(1)'''

            # left-most cell : check the second cell
            elif(i == 0):
                if init_grid[1] == 1:
                    new_gen_grid.append(1)
                else:
                    new_gen_grid.append(0)

            # right-most cell : check the second to the last cell
            elif(i == 63):
                if init_grid[62] == 1:
                    new_gen_grid.append(1)
                else:
                    new_gen_grid.append(0)

        print(''.join([symbol_dic[x] for x in new_gen_grid]))

        # update cell list
        init_grid = new_gen_grid[:]

        steps+=1


if __name__ == '__main__':
    ca([0,0,0,1,1,1,1,0])
