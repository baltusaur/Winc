# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Defining players that scored
player_that_scored = "Ruud Gullit "
player_2_that_scored = "Marco van Basten "

# Defining what minute the goal was scored
goal_0 = 32
goal_1 = 54

scorers = f'{player_that_scored}{goal_0}, {player_2_that_scored}{goal_1}'

report = f'{player_that_scored}scored in the {goal_0}nd minute\n{player_2_that_scored}scored in the {goal_1}th minute'

player = "Ruud Gullit"
first_name_find_space = player.find(" ")
first_name = player[:first_name_find_space]
first_name_len = len(first_name)
last_name_find_space = player.find(" ")
last_name_slice = player[(last_name_find_space+1):]
last_name_len = len(last_name_slice)
name_short = f'{player[0]}. {last_name_slice}'
chant = (first_name+"! ")*(first_name_len-1)+(first_name+"!")
good_chant = (chant[-1] != " ")
print(good_chant)