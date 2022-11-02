import csv

def users_move():
    first_player =  input("type your chosen move(rock, paper, scissor): ")
    second_player =  input("type your chosen move(rock, paper, scissor): ")
    players_moves = []
    players_moves.append(first_player)
    players_moves.append(second_player)
    return players_moves 

def winner_recognition(players_moves):
    if players_moves[0] == players_moves[1]:
        raise Exception("sorry, players moves can not be the same")     
    elif players_moves[0] == 'rock' and players_moves[1] == 'paper':
        return("second palyer is the winner!")
    elif players_moves[0] == 'rock' and players_moves[1] == 'scissor':
        return("first palyer is the winner!")
    elif players_moves[0] == 'paper' and players_moves[1] == 'scissor':
        return("second palyer is the winner!")
    elif players_moves[0] == 'paper' and players_moves[1] == 'rock':
        return("first palyer is the winner!")
    elif players_moves[0] == 'scissor'  and players_moves[1] == 'paper':
        return("first palyer is the winner!")
    elif players_moves[0] == 'scissor'  and players_moves[1] == 'rock':
        return("second palyer is the winner!")

def cvs_r():
    with open ('scoreboard.csv', 'r') as score_counter:
        score = csv.reader(score_counter)
        for row in score:
            print(row[0],":",row[1])

def csv_r_w (winner):
    with open ('scoreboard.csv', 'r') as score_board:
        points = csv.reader(score_board)
        points_list = []
        for row in points:
           points_list.append(int(row[1]))
    with open ('scoreboard.csv', 'w', newline = '') as score_board:
        board = csv.writer(score_board, delimiter = ',')
        if winner == "first palyer is the winner!":
            board.writerows([['first_player', points_list[0]+1], ['second_player', points_list[1]]])
        else:
            board.writerows([['first_player', points_list[0]], ['second_player', points_list[1]+1]])            

users_opinion = "continue"

while users_opinion == "continue":
    cvs_r()
    actions = users_move()
    try:
         winner = winner_recognition(actions)
    except:
        print("players moves can not be the same, please enter another move")
        continue     
    print(winner)
    csv_r_w(winner)
    users_opinion = input("type continue if you wanna play again: ")