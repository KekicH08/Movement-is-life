import sqlite3

from start_end_screen import leaderboard

LEADERBOARD = sqlite3.connect('leaderboard.db')


#  обновление базы данных с результами игроков
def leaderboard_refresh(player, level):
    cur = LEADERBOARD.cursor()
    table = cur.execute(f"SELECT * FROM Leaders").fetchall()
    if (player.name, level, player.pts) in table:
        return table
    else:
        cur.execute(
            f"INSERT INTO Leaders (playername, level, score) VALUES ('{player.name}', {level}, {player.pts})")
        LEADERBOARD.commit()
        return table


#  выбор уровня игры
def level_selection(player, mouse_pos, f, level):
    if 1120 < mouse_pos[0] < 1170 and 15 < mouse_pos[1] < 75:
        level = 1
        player.started = True
        player.hp = 3
        player.pts = 0
        f = 0
    elif 1120 < mouse_pos[0] < 1170 and 75 < mouse_pos[1] < 125:
        level = 2
        player.started = True
        player.hp = 3
        player.pts = 0
        f = 0
    elif 1120 < mouse_pos[0] < 1170 and 135 < mouse_pos[1] < 185:
        level = 3
        player.started = True
        player.hp = 3
        player.pts = 0
        f = 0
    elif 790 < mouse_pos[0] < 1030 and 135 < mouse_pos[1] < 185:
        leaderboard()
    return [level, f]
