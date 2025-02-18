from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="resilient",
        base_numeric_id=13980,
        name="Resilient",
        role="heavy_express",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2750,
        },
        random_reverse=True,
        gen=5,
        intro_year_offset=4,  # let's not have everything turn up in 1990
        fixed_run_cost_points=65,  # give a bonus so this can be a genuine mixed-traffic engine
        # add RfD Euro style triple grey?
        additional_liveries=[
            "INTERCITY_RASPBERRY_RIPPLE",
            "RES",
            "FREIGHTLINER_GBRF",
            "DUTCH",
        ],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
        sprites_additional_liveries_potential=True,  # add RfD Euro style triple grey?, Banger blue, but with black windows
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=103,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        spriterow_num=0,
    )

    consist.description = """I've completely rebuilt some Intrepids."""
    consist.foamer_facts = """BR Class 47, Brush Class 57, original TTD UU '47'"""

    return consist
