with open("./input.txt", encoding = 'utf-8') as f:
    data = [d for d in f.read().split('\n')]

call_numbers = [int(i) for i in data[0].split(',')]

raw_boards = data[1:]

def create_boards(raw_boards):
    boards = {}
    i = 0
    for c,item in enumerate(raw_boards):
        if item != '':
            if str(i) in boards.keys():
                boards[str(i)].append(item)
            else:
                boards[str(i)] = [item]
        if item == '' and c > 0:
            i += 1
    return boards

boards_rows = create_boards(raw_boards)

for board_id in boards_rows.keys():
        board = boards_rows[board_id]
        for c,row in enumerate(board):
            board[c] = row.split(' ')
            for cc in board[c]:
                if cc == '':
                    board[c].remove(cc)
            board[c] = [int(x) for x in board[c]]
        boards_rows[board_id] = board

def get_boards_cols_from_boards_rows(boards_rows):
    boards_cols = {board_id:[] for board_id in boards_rows.keys()}
    for board_id in boards_rows.keys():
        board = boards_rows[board_id]
        for cc,row in enumerate(board):
            boards_cols[board_id].append([row[cc] for row in board])
    return boards_cols

boards_cols = get_boards_cols_from_boards_rows(boards_rows)

def find_first_win_for_boards(boards):
    results = {}
    for call_num_index,call_num in enumerate(call_numbers):
        for board_id in boards.keys():
            board = boards[board_id]
            for dim in board:
                if set(dim).issubset(set(call_numbers[0:call_num_index+1])) and board_id not in results.keys():
                    results[board_id] = {'call_num_index':call_num_index,'call_num':call_num}
    return results

boards_rows_wins = find_first_win_for_boards(boards_rows)
boards_cols_wins = find_first_win_for_boards(boards_cols)

def get_win_info(boards_rows_wins,boards_cols_wins):
    results = {}
    for i in range(0,len(boards_rows_wins)):
        i = str(i)
        if boards_rows_wins[i]['call_num_index'] < boards_cols_wins[i]['call_num_index']:
            results[i]  = boards_rows_wins[i]
            results[i]['board_type'] = 'row'
        else:
            results[i]  = boards_cols_wins[i]
            results[i]['board_type'] = 'col'

    return results

win_info = get_win_info(boards_rows_wins,boards_cols_wins)

smallest_index_win = min(win_info, key=lambda k: win_info[k]['call_num_index'])
smallest_call_num_index = win_info[smallest_index_win]['call_num_index']
smallest_call_num = win_info[smallest_index_win]['call_num']
flat_list_small = [item for sublist in boards_rows[smallest_index_win] for item in sublist]
smallest_win_set = set(flat_list_small)-set(call_numbers[0:smallest_call_num_index+1])
print(sum(smallest_win_set)*smallest_call_num)

largest_index_win = max(win_info, key=lambda k: win_info[k]['call_num_index'])
largest_call_num_index = win_info[largest_index_win]['call_num_index']
largest_call_num = win_info[largest_index_win]['call_num']
flat_list_large = [item for sublist in boards_rows[largest_index_win] for item in sublist]
largest_win_set = set(flat_list_large)-set(call_numbers[0:largest_call_num_index+1])
print(sum(largest_win_set)*largest_call_num)

