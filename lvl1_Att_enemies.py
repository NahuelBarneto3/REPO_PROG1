from Attacking_Enemy import Attacking_Enemy
from collitions import Collition


def import_attacking_enemies():

    enemy_list = []
    enemy_list.append(Attacking_Enemy(x=850,y=85,speed_walk=1,speed_run=8,gravity=8,frame_rate_ms=60,move_rate_ms=5,e_scale=0.2,dying_time=2))
    #enemy_list.append(Attacking_Enemy(x=1200,y=655,speed_walk=6,speed_run=8,gravity=8,frame_rate_ms=10,move_rate_ms=20,e_scale=0.2,dying_time=2))

    return enemy_list