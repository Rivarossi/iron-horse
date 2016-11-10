import global_constants
from train import EngineConsist, ElectricLoco

consist = EngineConsist(id = 'v8',
              base_numeric_id = 410,
              title = 'V8 2-C+C-2 [Electric]',
              power = 4000,
              speed = 85,
              type_base_buy_cost_points = 35, # dibble buy cost for game balance
              type_base_running_cost_points = -10, # dibble running costs for game balance
              vehicle_life = 50,
              intro_date = 1949)

consist.add_unit(ElectricLoco(consist = consist,
                        weight = 160,
                        vehicle_length = 10,
                        spriterow_num = 0))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
