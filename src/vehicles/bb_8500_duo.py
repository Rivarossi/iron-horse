from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="bb_8500_duo",
        base_numeric_id=200,
        name="BB 8500 / 16000 (duo)",
        role="ultra_heavy_freight",
        role_child_branch_num=-3,
        power_by_power_source={"DC": 10700},
        gen=5,
        pantograph_type="diamond-double",
        intro_year_offset=8,  # introduce later than gen epoch by design
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=105, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist.description = """ """
    consist.foamer_facts = """SNCF BB 8500 / 16000 (duo)"""

    return consist
