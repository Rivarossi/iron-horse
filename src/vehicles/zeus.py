from train import PassengerEngineRailcarConsist, ElectricRailcarPaxUnit


def main(roster):
    consist = PassengerEngineRailcarConsist(roster=roster,
                                            id='zeus',
                                            base_numeric_id=3210,
                                            name='Zeus',
                                            role='pax_railcar_2',
                                            power=800,  # RL EMU HP is much lower, but eh
                                            pantograph_type='z-shaped-single-with-base',
                                            easter_egg_haulage_speed_bonus=True,
                                            gen=6,
                                            sprites_complete=False,
                                            intro_date_offset=-3)  # introduce early by design

    consist.add_unit(type=ElectricRailcarPaxUnit,
                     weight=40,
                     vehicle_length=8,
                     chassis='railcar')

    return consist
