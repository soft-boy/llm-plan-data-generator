import random

options = {
  'jungle': {
    'agent': 'E',
    'goal': 'T',
    'wall': '*',
    'empty': " ",
    'actions': [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)],
    'reward': 5
  },
  'space_rover': {
    'agent': 'R',
    'goal': 'P',
    'wall': 'O',
    'empty': ".",
    'actions': [(0,1), (1,0), (0,-1), (-1,0)],
    'reward': 3
  },
  'underwater_diver': {
    'agent': 'D',
    'goal': 'C',
    'wall': '~',
    'empty': "-",
    'actions': [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)],
    'reward': 2
  },
  'knight_castle': {
    'agent': 'E',
    'goal': 'T',
    'wall': '*',
    'empty': " ",
    'actions': [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)],
    'reward': 5
  },
  'worm_in_garden': {
    'agent': 'R',
    'goal': 'P',
    'wall': 'O',
    'empty': ".",
    'actions': [(0,1), (1,0), (0,-1), (-1,0)],
    'reward': 3
  },
  'snow_adventure': {
    'agent': 'S',
    'goal': 'H',
    'wall': '^',
    'empty': "*",
    'actions': [(0,1), (1,0), (0,-1), (-1,0), (0,2), (2,0), (0,-2), (-2,0)] ,
    'reward': 3
  },
  'desert_trek': {
    'agent': 'T',
    'goal': 'O',
    'wall': '@',
    'empty': ".",
    'actions': [(0,1), (1,0), (0,-1), (-1,0)],
    'reward': 2
  },
  'pirate_quest': {
    'agent': 'P',
    'goal': 'X',
    'wall': '~',
    'empty': " ",
    'actions': [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)],
    'reward': 5
  },
  'lunar_landing': {
    'agent': 'L',
    'goal': 'B',
    'wall': 'O',
    'empty': ".",
    'actions': [(0,1), (1,0), (0,-1), (-1,0)],
    'reward': 3
  },
  'ninja_mission': {
    'agent': 'N',
    'goal': 'S',
    'wall': '|',
    'empty': "_",
    'actions': [(0,1), (1,0), (0,-1), (-1,0), (0,2), (2,0), (0,-2), (-2,0)],
    'reward': 2
  }
}

def get_random_option():
    # Convert dictionary items to a list of tuples (key-value pairs) and select one randomly
    key, value = random.choice(list(options.items()))
    return value