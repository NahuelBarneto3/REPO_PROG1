from enemigo import Enemy

def import_ground_enemies():

    enemy_list = []
    enemy_list.append(Enemy(x=700,y=655,speed_walk=10,speed_run=8,gravity=8,frame_rate_ms=40,move_rate_ms=20,e_scale=0.2,dying_time=2))
    enemy_list.append(Enemy(x=1200,y=655,speed_walk=6,speed_run=8,gravity=8,frame_rate_ms=40,move_rate_ms=20,e_scale=0.2,dying_time=2))

    return enemy_list