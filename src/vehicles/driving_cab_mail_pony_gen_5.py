from train import MailEngineCabbageDVTConsist, CabbageDVTUnit


def main(roster_id):
    consist = MailEngineCabbageDVTConsist(
        roster_id=roster_id,
        id="driving_cab_mail_pony_gen_5",
        base_numeric_id=13020,
        name="Driving Van Trailer",
        gen=5,
        sprites_complete=True,
    )

    consist.add_unit(type=CabbageDVTUnit, weight=32, chassis="railcar_32px")

    consist.description = """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Clever idea we had eh?"""
    consist.foamer_facts = """BR MK3 Driving Van Trailer (DVT) with added generator"""

    return consist
