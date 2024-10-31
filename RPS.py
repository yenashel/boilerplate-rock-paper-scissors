# The example function below keeps track of the opponent's history 
# #and plays whatever the opponent played two plays ago. 
# It is not a very good player so you will need to change the code to pass the challenge.

#from collections import defaultdict
#from operator import itemgetter

def player(prev_opponent_play, opponent_history=[], series_dict = {}, play_counter_list=[0]):
    #count number of plays
    play_counter_list[0] += 1 #This hack is for preserving state between plays
    play_counter = play_counter_list[0]
    opponent_history.append(prev_opponent_play)
    opponents_last_play = ''
    last_two_plays = ''
    last_three_plays = ''
    last_four_plays = ''
    last_five_plays = ''

    #Idea: I can count the most frequent orders of 2 or 3 or 4 and so on

    if (len(opponent_history) >= 1):
        opponents_last_play = opponent_history[play_counter-1] #get the latest entry from the player history, namely the opponents last play. -1 accounts for array index starting with 0

    if (len(opponent_history) >= 2):
        opponent_last_play_minus_1 = opponent_history[play_counter-2]
        
        #The order I want to use is not appending but having the latest play first, I am achieving this by concat in the opposite order
        last_two_plays = opponents_last_play + opponent_last_play_minus_1
        series_dict.setdefault(last_two_plays,0)
        series_dict[last_two_plays] += 1

    if (len(opponent_history) >= 3):
        opponent_last_play_minus_2 = opponent_history[play_counter-3]

        #The order I want to use is not appending but having the latest play first
        last_three_plays = last_two_plays + opponent_last_play_minus_2
        series_dict.setdefault(last_three_plays,0)
        series_dict[last_three_plays] += 1

    if (len(opponent_history) >= 4):
        opponent_last_play_minus_3 = opponent_history[play_counter-4]

        #The order I want to use is not appending but having the latest play first
        last_four_plays = last_three_plays + opponent_last_play_minus_3
        series_dict.setdefault(last_four_plays,0)
        series_dict[last_four_plays] += 1

    if (len(opponent_history) >= 5):
        opponent_last_play_minus_4 = opponent_history[play_counter-5]

        #The order I want to use is not appending but having the latest play first
        last_five_plays = last_four_plays + opponent_last_play_minus_4
        series_dict.setdefault(last_five_plays,0)
        series_dict[last_five_plays] += 1



    #Find all dictionary entries where the second character, meaning the previous play mastches the now provided prev_opponent_play
    filtered_dict_last_play = {key: val for key, val in series_dict.items() if (len(key) == 2 and key[1] == prev_opponent_play) } 
    #...and with the same method look for larger pattern matches
    filtered_dict_last_play_minus_one = {key: val for key, val in series_dict.items() if ( len(key) == 3 and key[1:3] == last_two_plays) }
    filtered_dict_last_play_minus_two = {key: val for key, val in series_dict.items() if ( len(key) == 4 and key[1:4] == last_three_plays) }
    filtered_dict_last_play_minus_three = {key: val for key, val in series_dict.items() if ( len(key) == 5 and key[1:5] == last_four_plays) }
    filtered_dict_last_play_minus_four = {key: val for key, val in series_dict.items() if ( len(key) == 6 and key[1:6] == last_five_plays) }


    prediction_from_last_play = ''
    prediction_from_last_play_minus_one = ''
    prediction_from_last_play_minus_two = ''
    prediction_from_last_play_minus_three = ''
    prediction_from_last_play_minus_four = ''

    #now I am extracting the matches which had the highest number of occurences
    if len(filtered_dict_last_play) >= 1:

        prediction_from_last_play = max(filtered_dict_last_play, key=filtered_dict_last_play.get)[0] #get the most left character from the string, which represents the opponents next likely move

    if len(filtered_dict_last_play_minus_one) >= 1:

        prediction_from_last_play_minus_one = max(filtered_dict_last_play_minus_one, key=filtered_dict_last_play_minus_one.get)[0] #get the most left character from the string, which represents the opponents next likely move

    if len(filtered_dict_last_play_minus_two) >= 1:

        prediction_from_last_play_minus_two = max(filtered_dict_last_play_minus_two, key=filtered_dict_last_play_minus_two.get)[0] #get the most left character from the string, which represents the opponents next likely move

    if len(filtered_dict_last_play_minus_three) >= 1:

        prediction_from_last_play_minus_three = max(filtered_dict_last_play_minus_three, key=filtered_dict_last_play_minus_three.get)[0] #get the most left character from the string, which represents the opponents next likely move

    if len(filtered_dict_last_play_minus_four) >= 1:

        prediction_from_last_play_minus_four = max(filtered_dict_last_play_minus_four, key=filtered_dict_last_play_minus_four.get)[0] #get the most left character from the string, which represents the opponents next likely move

    unweighted_prediction_list = [prediction_from_last_play, prediction_from_last_play_minus_one, prediction_from_last_play_minus_two, prediction_from_last_play_minus_three, prediction_from_last_play_minus_four]

    predicted_next_move = ''

    if len(unweighted_prediction_list) >=1:

        #I could create a more complicate quorum algorithm here which e.g. would prefer larger matches over smaller matches, but I do not want to overcomplicate it 
        predicted_next_move = max(unweighted_prediction_list,key=unweighted_prediction_list.count)

    #This is for the situation of the first move in case there is no opponent history yet
    if predicted_next_move == '':
        predicted_next_move = "S"

    ideal_response_dict = {'P': 'S', 'R': 'P', 'S': 'R'}

    ideal_response = ideal_response_dict[predicted_next_move]
    return ideal_response


