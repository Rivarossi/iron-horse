import global_constants
from train import HighSpeedMailConsist, HighSpeedPassengerConsist, Wagon

# for consistency, should be split to high_speed_mail_cars and high_speed_passenger_cars eh?

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = HighSpeedPassengerConsist(title = '[High Speed Passenger Car]',
                               roster = 'pony',
                               base_numeric_id = 980,
                               wagon_generation = 5,
                               intro_date = 1860,
                               vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                           capacity_pax = 25,
                           weight = 30,
                           vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)


    consist = HighSpeedMailConsist(title = '[High Speed Mail Car]',
                               roster = 'pony',
                               base_numeric_id = 970,
                               wagon_generation = 5,
                               intro_date = 1900,
                               vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_mail = 55,
                            weight = 33,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)

    #--------------- llama ----------------------------------------------------------------------


    #--------------- antelope ----------------------------------------------------------------------
