from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="rapid",
        base_numeric_id=12130,
        name="Rapid",
        role="heavy_express",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 2800,  # significant jump from previous gen
        },
        # dibble, assume super-slip control, intent is to give higher TE as a non-significant variation from Resilient
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        gen=5,
        intro_year_offset=2,  # let's not have everything turn up in 1990
        speed=125,  # Rapid not replaced, but has gen 6 speeds
        fixed_run_cost_points=45,  # give a bonus so this can be a genuine mixed-traffic engine
        additional_liveries=["RES"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=105, vehicle_length=8, spriterow_num=0
    )

    consist.description = """They said they wanted these for a freight engine.  No I said.  We need a general purpose engine I said.  We talked about it for twenty minutes then we decided I was right."""
    consist.foamer_facts = """proposed BR Class 41/48, NIR 201 Class"""

    return consist
