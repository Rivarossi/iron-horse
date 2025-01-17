from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="oribi",
        base_numeric_id=11020,
        name="Oribi",
        power=450,
        power_by_power_source={
            "DIESEL": 450,
        },
        base_track_type_name="NG",
        intro_year=1960,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=65, vehicle_length=8, capacity=30, spriterow_num=0
    )

    return consist
