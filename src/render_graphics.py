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
        raise Exception('no pipelines')
    else:
        # run pipelines, obvs
        for pipeline in consist.gestalt_graphics.pipelines:
            pipeline.render(consist, global_constants)

def run_intermodal_container_pipelines(intermodal_container_gestalt):
    intermodal_container_gestalt.pipeline.render(intermodal_container_gestalt, global_constants)

def report_sprites_complete(consists):
    # project management eh :P
    complete = len([consist.sprites_complete for consist in consists if consist.sprites_complete])
    print("Sprites complete for", complete, "consists; incomplete for",
          len(consists) - complete, "consists;", str(int(100 * (complete / len(consists)))) + '%')
    incomplete_by_track_type = {}
    for consist in consists:
        if not consist.sprites_complete:
            incomplete_by_track_type.setdefault(consist.base_track_type, []).append(consist)
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
    num_pool_workers = makefile_args.get('num_pool_workers', 0)
    if num_pool_workers == 0:
        use_multiprocessing = False
        # just print, no need for a coloured echo_message
        print('Multiprocessing disabled: (PW=0)')
    else:
        use_multiprocessing = True
        # just print, no need for a coloured echo_message
        print('Multiprocessing enabled: (PW=' + str(num_pool_workers) + ')')

    graphics_input_path = os.path.join(currentdir, 'src', 'graphics')
    graphics_output_path = os.path.join(
        iron_horse.generated_files_path, 'graphics')
    if not os.path.exists(graphics_output_path):
        os.mkdir(graphics_output_path)

    hint_file = codecs.open(os.path.join(
        graphics_output_path, '_graphics_files_here_are_generated.txt'), 'w', 'utf8')
    hint_file.write("Don't edit the graphics files here.  They're generated by the build script. \n Edit sources in src/graphics.")
    hint_file.close()

    consists = iron_horse.get_consists_in_buy_menu_order()
    intermodal_container_gestalts = iron_horse.spritelayer_cargos.intermodal_containers.registered_container_gestalts

    if use_multiprocessing == False:
        for consist in consists:
            run_consist_pipelines(consist)
        for intermodal_container_gestalt in intermodal_container_gestalts:
            run_intermodal_container_pipelines(intermodal_container_gestalt)
    else:
        # Would this go faster if the pipelines from each consist were placed in MP pool, not just the consist?
        # probably potato / potato tbh
        pool = Pool(processes=num_pool_workers)
        pool.map(run_consist_pipelines, consists)
        pool.map(run_intermodal_container_pipelines, intermodal_container_gestalts)
        pool.close()
        pool.join()

    report_sprites_complete(consists)

    for dir_name in ['tail_lights']:
        target_path =  os.path.join(graphics_input_path, dir_name)
        dest_path =  os.path.join(graphics_output_path, dir_name)
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
        shutil.copytree(target_path, dest_path)

    print(format((time() - start), '.2f') + 's')


if __name__ == '__main__':
    main()
