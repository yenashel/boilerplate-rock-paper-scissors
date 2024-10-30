# The example function below keeps track of the opponent's history 
# #and plays whatever the opponent played two plays ago. 
# It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess


def player2(prev_opponent_play, opponent_history=[], series_dict = {}, play_counter=0):
    #count number of plays
    play_counter += 1
    opponent_history.append(prev_opponent_play)
    last_ten = opponent_history[-5:] #Idea: Increase to say -20 or possibly even more if it seems relevant maybe even completely
    

    #Idea: I can count the most frequent orders of 2 or 3 or 4 and so on
    #reversed_opponent_history = opponent_history.reversed() #no in place!

    if (opponent_history.count >= 1):
        opponents_last_play = opponent_history[play_counter-1] #get the latest entry from the player history, namely the opponents last play. -1 accounts for array index starting with 0
        
        #series_dict.setdefault(opponents_last_play,0) # This here is just academic as I need at least an entry of two previous plays so that I can derive the next play if I am feeding later just one play
        #series_dict[opponents_last_play] += 1         #
    if (opponent_history.count >= 2):
        opponent_last_play_minus_1 = opponent_history[play_counter-2]
        
        #The order I want to use is not appending but having the latest play first
        last_two_plays = "".join(opponent_last_play_minus_1, opponents_last_play) 
        series_dict.setdefault(last_two_plays,0)
        series_dict[last_two_plays] += 1

    #if (opponent_history.count >= 3):
    #    opponent_last_play_minus_2 = opponent_history[play_counter-3]
    #if (opponent_history.count >= 1):
    #    opponent_last_play_minus_3 = opponent_history[play_counter-4]
    #if (opponent_history.count >= 1):
    #    opponent_last_play_minus_4 = opponent_history[play_counter-5]     


    #now look up in the dictionary the last respectiv order of previous plays

    #fit_for_last_play = series_dict[prev_opponent_play]


    #Find all dictionary entries where the second character, meaning the previous play mastches the now provided prev_opponent_play
    filtered_dict_last_play = {key: val for key, val in series_dict.items() if key[1] == prev_opponent_play } #.startswith(prev_opponent_play)}
    filtered_dict_last_play_minus_one = {key: val for key, val in series_dict.items() if key[1:3] == prev_opponent_play }

    #now in order to make it simple, I take the key with the highest count
    
    filtered_dict_last_play_max_key = max(series_dict, key=series_dict.get)

    #From this key I need to extract the first character as it represents the most probable opponents coming play (in terms of his previous behaviour)

    most_probable_opponent_play_based_on_looking_back_only_one_play = filtered_dict_last_play_max_key[0]

    #Go through opponent_history starting at latest until -1 until the array is finished
    #Concatenate the two values in a string
    #Add the string to a dictionary_of_twos and increase the count by one (Upsert)

    #Repeat the same for 3 and 4 and so on

    #Create a consens algorithm which will look into the dictionarys and predict the next opponents move
    #

    
    
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == '':
        most_frequent = "S"

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[most_frequent]


