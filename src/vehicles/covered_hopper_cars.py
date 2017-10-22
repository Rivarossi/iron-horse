from train import CoveredHopperConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = CoveredHopperConsist(roster='pony',
                                   base_numeric_id=1270,
                                   gen=2,
                                   subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = CoveredHopperConsist(roster='pony',
                                   base_numeric_id=1260,
                                   gen=3,
                                   subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = CoveredHopperConsist(roster='pony',
                                   base_numeric_id=2940,
                                   gen=4,
                                   subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = CoveredHopperConsist(roster='pony',
                                   base_numeric_id=1230,
                                   gen=4,
                                   subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = CoveredHopperConsist(roster='pony',
                                   base_numeric_id=1240,
                                   gen=5,
                                   subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = CoveredHopperConsist(roster='pony',
                                   base_numeric_id=2700,
                                   gen=5,
                                   subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = CoveredHopperConsist(roster='pony',
                                   base_numeric_id=3040,
                                   gen=6,
                                   subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist = CoveredHopperConsist(roster='pony',
                                   base_numeric_id=2910,
                                   gen=6,
                                   subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    # no gen 6 covered hopper cars, cap to gen 5 in Pony

    #--------------- llama ----------------------------------------------------------------------
