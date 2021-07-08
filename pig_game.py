import random
import time

TOTAL_SCORE_TO_WIN = 20
SIDE_DICE_COUNT = 6

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def addScore(self, amt):
        self.score += amt
        
    def is_winner(self):
        return self.score >= TOTAL_SCORE_TO_WIN
        
    def __str__(self):
        return f'{self.name}'


def showBoard(players):
    """Returns a string representing the current game"""
    return (player.name for player in players)


def stop_at(m, n):
    accum_scores = 0
    while True:
        num = random.randint(1, m)
        yield num, accum_scores
        accum_scores += num
        if accum_scores >= n:
            return


def roll():
    for curr_val, all_prev_scores in stop_at(SIDE_DICE_COUNT, TOTAL_SCORE_TO_WIN):
        if curr_val == 1 or random.choice([False*10, True]):
            break
    if curr_val == 1:
        all_prev_scores = 0
    return all_prev_scores


if __name__=='__main__':
    players = [Player('Olga'), Player('Anhelica'), Player('George')]
    print('')
    print('-'*15)
    print("Today's players are:", ', '.join(showBoard(players)))
    print('')
   
    player_index = 0
    while True:
        player = players[player_index]
        print(f'{player} spins:')
        time.sleep(3)
        accum_sum = roll()
        print(f'    got for this round {accum_sum}')
        time.sleep(2)
        if accum_sum > 0:
            player.addScore(accum_sum)
        print(f'    total score for now is {player.score}')
        if player.is_winner():
            print('')
            print('-'*15)
            print(f'The winner is {player.name} with total score {player.score}')
            break
        player_index = (player_index + 1) % len(players)
