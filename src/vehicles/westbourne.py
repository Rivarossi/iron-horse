from train import PassengerEngineMetroConsist, MetroUnit


def main(roster):
    consist = PassengerEngineMetroConsist(roster=roster,
                                          id='westbourne',
                                          base_numeric_id=360,
                                          name='Westbourne',
                                          role='pax_metro',
                                          power=900,
                                          gen=2,
                                          sprites_complete=True)

    consist.add_unit(type=MetroUnit,
                     weight=36,
                     vehicle_length=8,
                     capacity=160,
                     chassis='railcar_32px',
                     repeat=2)

    return consist
