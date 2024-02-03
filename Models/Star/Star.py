"""
Implementation of Star class
"""


class Star:

    _instance: bool = False
    _name: str
    _type: str
    _cycles_to_supernova = 100

    def __new__(cls):
        raise TypeError('Cannot create more stars, sorry :(\nUse Star.instance instead!')

    @classmethod
    def instance(cls):
        if not cls._instance:
            # todo decide how (or if we care at all) to pick simulation length,
            #  for now lets go with hardcoded Single named Red Sun,
            #  leaving some more ideas for future
            star_selection = (
                ('Single', 100),
                ('Binary System', 150),
                ('Red Giant', 50)
            )
            choice = star_selection[0]
            cls._name, cls._type, cls._cycles_to_supernova = 'Red Sun', choice[0], choice[1]
            cls._instance = True
        return cls

    @classmethod
    def do_cycle(cls):
        # this will most likely be replaced with event/observer system
        cls._cycles_to_supernova -= 1
        if cls._cycles_to_supernova > 0:
            return
        # todo connect this with rest of simulation, calculate score, display statistics,
        #  maybe call event instead of just print and exit
        print(f'{cls._name} goes supernova!')
        exit()
