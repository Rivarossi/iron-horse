from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="kwa_falls",
        base_numeric_id=11010,
        name="2-8-2 Kwa Falls",
        power=1800,
        tractive_effort_coefficient=0.19,
        base_track_type_name="NG",
        intro_year=1945,
    )

    consist.add_unit(
        type=SteamEngineUnit, weight=100, vehicle_length=7, spriterow_num=0
    )

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=40, vehicle_length=5, spriterow_num=1
    )

    return consist
