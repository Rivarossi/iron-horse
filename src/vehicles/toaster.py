from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='toaster',
                            base_numeric_id=4800,
                            name='Toaster',
                            role='heavy_freight',
                            role_child_branch_num=2,
                            power=4650,
                            # dibble for game balance, assume super-slip control
                            tractive_effort_coefficient=0.4,
                            random_reverse=True,
                            gen=6,
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=128, # weight reduced from 140 to nerf run cost down :P
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """I've heard these might catch fire, but we're getting them cheap."""
    consist.cite = """Mr. Train"""
    consist.foamer_facts = """GE Class 70 <i>Powerhaul</i>, uprated GE prime mover."""

    return consist
