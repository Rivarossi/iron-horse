from railtype import Railtype


def main(disabled=False):
    railtype = Railtype(
        id="metro",
        label="MTRO",
        construction_cost=10,
        maintenance_cost=10,
        railtype_flags=["RAILTYPE_FLAG_NO_LEVEL_CROSSING"],
        map_colour=0x25,
        compatible_railtype_list=[
            "SAA3",
            "SAAN",
            "SABN",
            "SACN",
            "SADN",
            "SAEN",
            "SAAE",
            "SABE",
            "SACE",
            "SADE",
            "SAEE",
            "SAAD",
            "SABD",
            "SACD",
            "SADD",
            "SAED",
            "SAAd",
            "SABd",
            "SACd",
            "SADd",
            "SAEd",
            "SAAA",
            "SABA",
            "SACA",
            "SADA",
            "SAEA",
            "SAAa",
            "SABa",
            "SACa",
            "SADa",
            "SAEa",
            "SAAZ",
            "SSAZ",
            "SUAZ",
        ],
        powered_railtype_list=["SAA3", "SAAZ", "SSAZ", "SUAZ"],
        alternative_railtype_list=[
            "3RDR",
            "SAA3",
            "SAB3",
            "SAC3",
            "SAD3",
            "SAE3",
        ],
        use_custom_sprites=True,
        use_custom_signals=True,
    )
    railtype.register(disabled=disabled)