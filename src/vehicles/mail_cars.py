from train import MailCarConsist, Wagon


def main():
    #--------------- pony NG ----------------------------------------------------------------------
    consist = MailCarConsist(roster='pony',
                          base_numeric_id=950,
                          gen=1,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=Wagon,
                     capacity=12,
                     vehicle_length=5)

    #--------------- pony ----------------------------------------------------------------------
    consist.add_model_variant(spritesheet_suffix=0)

    consist = MailCarConsist(roster='pony',
                          base_numeric_id=2280,
                          gen=1,
                          subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=10,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = MailCarConsist(roster='pony',
                          base_numeric_id=2220,
                          gen=1,
                          subtype='B')

    consist.add_unit(type=Wagon,
                     capacity=12,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = MailCarConsist(roster='pony',
                          base_numeric_id=2290,
                          gen=2,
                          subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=10,
                     vehicle_length=4)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = MailCarConsist(roster='pony',
                          base_numeric_id=920,
                          gen=2,
                          subtype='B')

    consist.add_unit(type=Wagon,
                     capacity=12,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = MailCarConsist(roster='pony',
                          base_numeric_id=2300,
                          gen=3,
                          subtype='B')

    consist.add_unit(type=Wagon,
                     capacity=12,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = MailCarConsist(roster='pony',
                          base_numeric_id=940,
                          gen=3,
                          subtype='C')

    consist.add_unit(type=Wagon,
                     capacity=15,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = MailCarConsist(roster='pony',
                          base_numeric_id=3160,
                          gen=4,
                          subtype='B')

    consist.add_unit(type=Wagon,
                     capacity=12,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = MailCarConsist(roster='pony',
                          base_numeric_id=3170,
                          gen=4,
                          subtype='C')

    consist.add_unit(type=Wagon,
                     capacity=15,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = MailCarConsist(roster='pony',
                          base_numeric_id=970,
                          gen=5,
                          subtype='B')

    consist.add_unit(type=Wagon,
                     capacity=12,
                     vehicle_length=6)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = MailCarConsist(roster='pony',
                          base_numeric_id=3140,
                          gen=5,
                          subtype='C')

    consist.add_unit(type=Wagon,
                     capacity=15,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    # no gen 6 for brit roster, max speed reached for engines

    """
    #--------------- llama ----------------------------------------------------------------------
    consist = MailCarConsist(roster = 'llama',
                          base_numeric_id = 960,
                          gen = 1,
                                    subtype='A')

    consist.add_unit(type = Wagon,
                            capacity = 30,
                            vehicle_length = 7)

    consist.add_model_variant()


    consist = MailCarConsist(roster = 'llama',
                          base_numeric_id = 970,
                          gen = 2,
                                    subtype='A')

    consist.add_unit(type = Wagon,
                            capacity = 45,
                            vehicle_length = 7)

    consist.add_model_variant()


    consist = MailCarConsist(roster = 'llama',
                          base_numeric_id = 980,
                          gen = 3,
                                    subtype='A')

    consist.add_unit(type = Wagon,
                            capacity = 60,
                            vehicle_length = 8)

    consist.add_model_variant()


    consist = MailCarConsist(roster = 'llama',
                          base_numeric_id = 990,
                          gen = 1,
                                    subtype='A',
                          track_type = 'NG')

    consist.add_unit(type = Wagon,
                            capacity = 30,
                            vehicle_length = 6)

    consist.add_model_variant()


    consist = MailCarConsist(roster = 'llama',
                          base_numeric_id = 1380,
                          gen = 2,
                                    subtype='A',
                          track_type = 'NG')

    consist.add_unit(type = Wagon,
                            capacity = 40,
                            vehicle_length = 6)

    consist.add_model_variant()


    consist = MailCarConsist(roster = 'llama',
                          base_numeric_id = 1450,
                          gen = 3,
                                    subtype='A',
                                                              track_type = 'NG')

    consist.add_unit(type = Wagon,
                            capacity = 50,
                            vehicle_length = 6)

    consist.add_model_variant()

    """
    #--------------- antelope ----------------------------------------------------------------------
    consist = MailCarConsist(roster='antelope',
                          base_numeric_id=1730,
                          gen=1,
                          subtype='A')

    consist.add_unit(type=Wagon,
                     capacity=10,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = MailCarConsist(roster='antelope',
                          base_numeric_id=2120,
                          gen=1,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=Wagon,
                     capacity=20,
                     vehicle_length=5)

    consist.add_model_variant(spritesheet_suffix=0)

    consist = MailCarConsist(roster='antelope',
                          base_numeric_id=1950,
                          gen=2,
                          subtype='A',
                          track_type='NG')

    consist.add_unit(type=Wagon,
                     capacity=30,
                     vehicle_length=8)

    consist.add_model_variant(spritesheet_suffix=0)
