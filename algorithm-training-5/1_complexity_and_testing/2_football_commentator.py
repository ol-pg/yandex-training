# Раунд плей-офф между двумя командами состоит из двух матчей. Каждая команда проводит по одному матчу «дома» и «в гостях».
# Выигрывает команда, забившая большее число мячей. Если же число забитых мячей совпадает, выигрывает команда, забившая больше мячей «в гостях».
# Если и это число мячей совпадает, матч переходит в дополнительный тайм или серию пенальти.
#
# Вам дан счёт первого матча, а также счёт текущей игры (которая ещё не завершилась).
# Помогите комментатору сообщить, сколько голов необходимо забить первой команде, чтобы победить, не переводя игру в дополнительное время.

def goals_to_win(first_team_score, current_score, location):
    first_team_goals = int(first_team_score.split(':')[0])
    second_team_goals = int(first_team_score.split(':')[1])
    current_first_team_goals = int(current_score.split(':')[0])
    current_second_team_goals = int(current_score.split(':')[1])

    res = 0
    if first_team_goals + current_first_team_goals > second_team_goals + current_second_team_goals:
        res = 0
    elif location == 1:
        if first_team_goals + current_first_team_goals == second_team_goals + current_second_team_goals:
            if current_first_team_goals > second_team_goals:
                res = 0
            else:
                res = 1
        elif ((second_team_goals + current_second_team_goals) - (
                first_team_goals + current_first_team_goals)) + current_first_team_goals <= second_team_goals:
            res = (second_team_goals + current_second_team_goals) - (first_team_goals + current_first_team_goals) + 1
        else:
            res = (second_team_goals + current_second_team_goals) - (first_team_goals + current_first_team_goals)
    else:
        if first_team_goals + current_first_team_goals == second_team_goals + current_second_team_goals:
            if current_second_team_goals >= first_team_goals:
                res = 1
            else:
                res = 0
        elif first_team_goals > current_second_team_goals:
            res = (second_team_goals + current_second_team_goals) - (first_team_goals + current_first_team_goals)
        else:
            res = (second_team_goals + current_second_team_goals) - (first_team_goals + current_first_team_goals) + 1

    return res


first_match_score = input()
current_game_score = input()
location = int(input())

goals_needed = goals_to_win(first_match_score, current_game_score, location)
print(goals_needed)
