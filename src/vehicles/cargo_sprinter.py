from train import MailEngineCargoSprinterEngineConsist, DieselRailcarMailUnit

# implemented as dual headed, it really is just the nicer way to build these units (esp. when adding container wagons)

# NOTE that cargo sprinter will NOT randomise containers on load as of Dec 2020 - there is a bug with rear unit running unwanted triggers and re-randomising in depots etc


def main(roster_id):
    consist = MailEngineCargoSprinterEngineConsist(
        roster_id=roster_id,
        id="cargo_sprinter",
        base_numeric_id=12040,
        name="Cargo Sprinter",
        role="mail_railcar",  # abuse of existing railcar role for convenience
        role_child_branch_num=-1,
        dual_headed=True,
        power_by_power_source={
            "NULL": 1650,  # matched to Griffon, Ultra Shoebox
        },
        gen=6,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselRailcarMailUnit,
        weight=32,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_4",
    )

    consist.description = """Runs like the wind."""
    consist.foamer_facts = """Windhoff MPV"""

    return consist
