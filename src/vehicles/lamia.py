from train import EngineConsist, SteamEngineUnit

def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='lamia',
                            base_numeric_id=4880,
                            name='0-6-0 Lamia',
                            role='gronk!',
                            role_child_branch_num=-2,
                            replacement_consist_id='gronk', # this Joker ends with Gronk
                            power=350,
                            speed=35,
                            # dibble TE up for game balance, assume low gearing or something
                            tractive_effort_coefficient=0.375,
                            fixed_run_cost_points=109, # substantial cost bonus so it can make money
                            random_reverse=True,
                            gen=2,
                            sprites_complete=False)

    consist.add_unit(type=SteamEngineUnit,
                     weight=35,
                     vehicle_length=4,
                     spriterow_num=0)

    return consist
