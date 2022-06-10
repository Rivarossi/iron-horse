import codecs  # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os

currentdir = os.curdir
from multiprocessing import Pool
import multiprocessing

logger = multiprocessing.log_to_stderr()
logger.setLevel(25)
from time import time

import iron_horse
import utils
import global_constants


def run_consist_pipelines(consist):
    if len(consist.gestalt_graphics.pipelines) == 0:
        raise Exception("no pipelines")
    else:
        # run pipelines, obvs
        for pipeline in consist.gestalt_graphics.pipelines:
            pipeline.render(consist, global_constants)


def run_spritelayer_cargo_set_pipelines(spritelayer_cargo_set_pair):
    for pipeline in spritelayer_cargo_set_pair[
        0
    ].gestalt_graphics.spritelayer_cargo_pipelines:
        pipeline.render(spritelayer_cargo_set_pair, global_constants)


def report_sprites_complete(consists):
    # project management eh :P
    complete = len(
        [consist.sprites_complete for consist in consists if consist.sprites_complete]
    )
    print(
        "Sprites complete for",
        complete,
        "consists; incomplete for",
        len(consists) - complete,
        "consists;",
        str(int(100 * (complete / len(consists)))) + "%",
    )
    incomplete_by_track_type = {}
    for consist in consists:
        if not consist.sprites_complete:
            incomplete_by_track_type.setdefault(consist.base_track_type, []).append(
                consist
            )
    for track_type, incomplete_consists in incomplete_by_track_type.items():
        print("  *", track_type, len(incomplete_consists))


# wrapped in a main() function so this can be called explicitly, because unexpected multiprocessing fork bombs are bad
def main():
    print("[RENDER GRAPHICS] render_graphics.py")
    start = time()
    iron_horse.main()
    # get args passed by makefile
    makefile_args = utils.get_makefile_args(sys)
    # default to no mp, makes debugging easier (mp fails to pickle errors correctly)
    num_pool_workers = makefile_args.get("num_pool_workers", 0)
    if num_pool_workers == 0:
        use_multiprocessing = False
        # just print, no need for a coloured echo_message
        print("Multiprocessing disabled: (PW=0)")
    else:
        use_multiprocessing = True
        # just print, no need for a coloured echo_message
        print("Multiprocessing enabled: (PW=" + str(num_pool_workers) + ")")

    graphics_input_path = os.path.join(currentdir, "src", "graphics")
    graphics_output_path = os.path.join(iron_horse.generated_files_path, "graphics")
    if not os.path.exists(graphics_output_path):
        os.mkdir(graphics_output_path)

    hint_file = codecs.open(
        os.path.join(graphics_output_path, "_graphics_files_here_are_generated.txt"),
        "w",
        "utf8",
    )
    hint_file.write(
        "Don't edit the graphics files here.  They're generated by the build script. \n Edit sources in src/graphics."
    )
    hint_file.close()

    consists = iron_horse.ActiveRosters().consists_in_buy_menu_order

    for consist in consists:
        # rosters won't pickle reliably, and blow up multiprocessing, never figured out why
        # work around that by freezing anything for graphics processing that depends on roster lookups
        consist.freeze_cross_roster_lookups()

    # get a list of 2-tuple pairs for spritelayer cargos + cargo sets
    # a list format is wanted for convenience with graphics multiprocessing pool
    # the parent spritelayer_cargo object must be passed with the cargo set as cargo sets have render-time properties which change according to context
    # but cargo_sets are global and reused across spritelayer_cargos, so they can't just store a single reference to their spritelayer_cargo parent
    spritelayer_cargo_set_pairs = []
    for spritelayer_cargo in iron_horse.registered_spritelayer_cargos:
        for cargo_set in spritelayer_cargo.cargo_sets:
            spritelayer_cargo_set_pairs.append((spritelayer_cargo, cargo_set))

    # sort the consists in priority processing order, priority 1 is first
    # this enables some consists to depend on generated sprites from other consists
    consists_in_priority_groups = {1:[], 2:[]}
    for consist in consists:
        consists_in_priority_groups[consist.gestalt_graphics.processing_priority].append(consist)

    if use_multiprocessing == False:
        for spritelayer_cargo_set_pair in spritelayer_cargo_set_pairs:
            run_spritelayer_cargo_set_pipelines(spritelayer_cargo_set_pair)
        for processing_priority in [1, 2]:
            for consist in consists_in_priority_groups[processing_priority]:
                run_consist_pipelines(consist)
    else:
        # Would this go faster if the pipelines from each consist were placed in MP pool, not just the consist?
        # probably potato / potato tbh
        pool = Pool(processes=num_pool_workers)
        pool.map(run_spritelayer_cargo_set_pipelines, spritelayer_cargo_set_pairs)
        pool.close()
        pool.join()
        # wait for first pool job to finish before starting further pool jobs
        # vehicle pool jobs are repeated so that some vehicles can depend on generated sprites from others
        for processing_priority in [1, 2]:
            pool = Pool(processes=num_pool_workers)
            pool.map(run_consist_pipelines, consists_in_priority_groups[processing_priority])
            pool.close()
            pool.join()

    report_sprites_complete(consists)

    for dir_name in ["railtypes", "signals", "tail_lights"]:
        target_path = os.path.join(graphics_input_path, dir_name)
        dest_path = os.path.join(graphics_output_path, dir_name)
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
        shutil.copytree(target_path, dest_path)

    print("[RENDER GRAPHICS] complete", format((time() - start), ".2f") + "s")


if __name__ == "__main__":
    main()
