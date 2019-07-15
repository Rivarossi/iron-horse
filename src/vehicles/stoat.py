from train import EngineConsist, ElectricEngineUnit


def main(roster):
    consist = EngineConsist(roster=roster,
                            id='stoat',
                            base_numeric_id=3340,
                            name='Stoat',
                            role='branch_express',
                            power=800,
                            random_reverse=True,
                            pantograph_type='diamond-single',
                            gen=2,
                            intro_date_offset=6, # introduce later than gen epoch by design
                            sprites_complete=False)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=59,
                     vehicle_length=6,
                     spriterow_num=0)

    return consist