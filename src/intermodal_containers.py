# intermodal containers are sandboxed into their own module to avoid them spawning tentacles into gestalt graphics, global constants, train.py etc

from gestalt_graphics.pipelines import GenerateCompositedIntermodalContainers

class IntermodalContainerGestalt(object):
    """ Sparse class to hold container gestalts """
    # a gestalt is a set of containers of specific length and appearance
    # each set corresponds to a spritesheet which will be generated by the graphics processor
    # each set is used for a specific group of cargo labels or classes
    # - multiple container types exist, e.g. box, tank, flat, bulk etc
    # - unknown and generic cargos default to box containers)
    # ====== #
    # each container set may have one or more spriterows
    # spriterows are chosen randomly when vehicles load new cargo
    # rows are composed by the graphics processor, and may include variations for
    # - combinations of container lengths
    # - combinations of container types
    # - container colours
    def __init__(self):
        self.pipeline = GenerateCompositedIntermodalContainers()

    @property
    def id(self):
        return "intermodal_" + self.type + "_" + str(self.length) + "px"

    @property
    def variants(self):
        return [1, 2, 3]


class IntermodalBox16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'box'


class IntermodalBox24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'box'


class IntermodalBox32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'box'


class IntermodalBulk16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'bulk'


class IntermodalBulk24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'bulk'


class IntermodalBulk32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'bulk'


class IntermodalEdiblesTank16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'edibles_tank'


class IntermodalEdiblesTank24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'edibles_tank'


class IntermodalEdiblesTank32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'edibles_tank'


class IntermodalFlat16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'flat'


class IntermodalFlat24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'flat'


class IntermodalFlat32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'flat'


class IntermodalLivestock16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'livestock'


class IntermodalLivestock24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'livestock'


class IntermodalLivestock32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'livestock'


class IntermodalReefer16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'reefer'


class IntermodalReefer24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'reefer'


class IntermodalReefer32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'reefer'


class IntermodalTank16px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 16
        self.type = 'tank'


class IntermodalTank24px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 24
        self.type = 'tank'


class IntermodalTank32px(IntermodalContainerGestalt):
    def __init__(self):
        super().__init__()
        self.length = 32
        self.type = 'tank'


def get_container_types():
    for container_gestalt in registered_container_gestalts:
        print(container_gestalt.id)
    return {'bulk': [1, 2, 3], 'reefer': [1, 2, 3], 'box': [1, 2, 3], 'tank': [1, 2, 3],
            'livestock': [1, 2, 3], 'flat': [1, 2, 3], 'edibles_tank': [1, 2, 3]}

def get_container_gestalts_by_length(vehicle_length):
    result = []
    for container_gestalt in registered_container_gestalts:
        if container_gestalt.length == 4 * vehicle_length:
            result.append(container_gestalt)
    return result

registered_container_gestalts = [IntermodalBox16px(),
                                 IntermodalBox24px(),
                                 IntermodalBox32px(),
                                 IntermodalBulk16px(),
                                 IntermodalBulk24px(),
                                 IntermodalBulk32px(),
                                 IntermodalEdiblesTank16px(),
                                 IntermodalEdiblesTank24px(),
                                 IntermodalEdiblesTank32px(),
                                 IntermodalFlat16px(),
                                 IntermodalFlat24px(),
                                 IntermodalFlat32px(),
                                 IntermodalLivestock16px(),
                                 IntermodalLivestock24px(),
                                 IntermodalLivestock32px(),
                                 IntermodalReefer16px(),
                                 IntermodalReefer24px(),
                                 IntermodalReefer32px(),
                                 IntermodalTank16px(),
                                 IntermodalTank24px(),
                                 IntermodalTank32px()]
