x_template ='''
This is a maze problem that I want you to solve.

```
maze={maze}
```

Information about the problem:
1. "{agent}": agent
2. "{goal}": goal
3. "{wall}": wall
4. "{empty}": empty space


These are the set of actions that an agent can perform:
```
actions={actions}
```

The rewards are:
1. "{goal}": 1
'''

def genXDatum(maze, agent, goal, wall, empty, actions, reward):
  return x_template.format(
    maze=maze,
    agent=agent,
    goal=goal,
    wall=wall,
    empty=empty,
    actions=actions,
    reward=reward,
  )

def writeXDatum(name, maze, agent, goal, wall, empty, actions, reward):
  text_file = open("x_data/"+name+".txt", "w")
  text_file.write(genXDatum(maze, agent, goal, wall, empty, actions, reward))
  text_file.close()