from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='dragon',
                            base_numeric_id=420,
                            name='Dragon',
                            role='heavy_express',
                            role_child_branch_num=3,
                            power=2750,
                            random_reverse=True,
                            gen=4,
                            intro_date_offset=1,  # introduce later than gen epoch by design
                            fixed_run_cost_points=200, # give a serious malus to this one (balancing eh?)
                            sprites_complete=True)

    consist.add_unit(type=DieselEngineUnit,
                     weight=99,
                     vehicle_length=8,
                     effect_offsets=[(-1, 0), (1, 0)], # double the smoke eh?
                     spriterow_num=0)

    consist.description = """A right big fast diesel hydraulic this one is."""
    consist.cite = """Mr. Train"""

    return consist
