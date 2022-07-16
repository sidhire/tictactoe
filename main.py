import random
from typing import Dict, List, Tuple
import numpy as np

from check_submission import check_submission
from game_mechanics import (
    Cell,
    WildTictactoeEnv,
    choose_move_randomly,
    load_dictionary,
    play_wild_ttt_game,
    render,
    save_dictionary,
)

TEAM_NAME = "Memes"  # <---- Enter your team name here!
assert TEAM_NAME != "Team Name", \
    "Please change your TEAM_NAME!"

# def is_state_valid(state):


class TTTEnv:

    ALL_ACTIONS = [
        (0, 'X'),
        (0, 'O'),
        (1, 'X'),
        (1, 'O'),
        (2, 'X'),
        (2, 'O'),
        (3, 'X'),
        (3, 'O'),
        (4, 'X'),
        (4, 'O'),
        (5, 'X'),
        (5, 'O'),
        (6, 'X'),
        (6, 'O'),
        (7, 'X'),
        (7, 'O'),
        (8, 'X'),
        (8, 'O'),
    ]

    CONVERSION_str_to_array = {'': 0, 'O': 1, 'X': 2}

    CONVERSION_array_to_str = {
        v: k for k, v in CONVERSION_str_to_array.items()
    }

    def __init__(self):
        self._board = np.zeros((3, 3))
        self.reset()

        self.array  # Current state of the board in array

    def strlist_to_array(self, sl):
        converted = [self.CONVERSION_str_to_array[i] for i in sl]
        return np.array(converted).reshape(3, 3)

    def array_to_strlist(self, array):
        return [self.CONVERSION_array_to_str[i] for i in array.reshape(9)]

    def get_possible_actions(self, state):
        return [list(i) for i in np.transpose(np.where(self.array==0))]
        # return [a for a in self.ALL_ACTIONS if is_state_valid(transition_function(state, a))]

    def step(self, action: Tuple[int, int]):
        assert action in self.get_possible_actions(self.state)
        reward = 10 if self.state == (0, 9) else 0
        self.done = self.state == (0, 9)
        if not self.done:
            # Don't update the state when you're in the terminal state (self.done == True)
            self.state = transition_function(self.state, action)
        self.total_return += reward
        return self.state, reward, self.done, {}

    def reset(self):
        self.state = np.zeros((3, 3))
        self.total_return = 0
        self.done = False
        return self.state, self.total_return, self.done, {}


def train() -> Dict:
    """Write this function to train your algorithm.

    Returns:
         Value function dictionary used by your agent. You can
         structure this how you like, however your choose_move must
         be able to use it.
    """
    raise NotImplementedError("You need to implement this function!")


def choose_move(board: List[str], value_function: Dict) -> Tuple[int, str]:
    """
    TODO: WRITE THIS FUNCTION

    This is what will be called during competitive play.
    It takes the current state of the board as input.
    It returns a single move to play.

    Args:
        board: list representing the board.
                (see README Technical Details for more info)

        value_function: The dictionary output by train().

    Returns:
        position (int): The position to place your piece 
                        (an integer 0 -> 8), where 0 is 
                        top left and 8 is bottom right.
        counter (str): The counter to place. "X" or "O".

    It's important that you think about exactly what this 
     function does when you submit, as it will be called 
     in order to take your turn!
    """

    # We provide an example here that chooses a random position on the board and
    # and places a random counter there.
    # position = random.choice([count for count, item in enumerate(board) if item == Cell.EMPTY])
    # counter = random.choice([Cell.O, Cell.X])
    # return position, counter
    raise NotImplementedError("You need to implement this function!")


if __name__ == "__main__":

    ## Example workflow, feel free to edit this! ###
    my_value_fn = train()
    save_dictionary(my_value_fn, TEAM_NAME)
    my_value_fn = load_dictionary(TEAM_NAME)

    def choose_move_no_value_fn(board: List[str]) -> Tuple[int, str]:
        """
        The arguments in play_wild_ttt_game() require functions 
         that only take the state as input.

        This converts choose_move() to that format.
        """
        return choose_move(board, my_value_fn)

    # Code below plays a single game of Wild Tic-Tac-Toe vs a random
    # opponent, think about how you might want to adapt this to
    # test the performance of your algorithm.

    # total_return = play_wild_ttt_game(
    #     your_choose_move=choose_move_no_value_fn,
    #     opponent_choose_move=choose_move_randomly,
    #     game_speed_multiplier=1,
    #     verbose=True,
    # )

    # Below renders a game graphically. You must click to take turns
    render(choose_move_no_value_fn)

    check_submission()
