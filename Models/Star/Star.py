"""
Star class implementation
"""


class Star:

    _instance: bool = False
    _name: str
    _type: str
    _cycles_to_supernova = 100

    def __new__(cls):
        raise Exception('Cannot create more stars, sorry :(\nUse Star.instance instead!')

    @classmethod
    def instance(cls):
        if not cls._instance:
            ''' 
            todo decide how (or if we care at all) to pick simulation length, 
            for now lets go with hardcoded Single named Red Sun,
            leaving some more ideas for future
            '''
            star_selection = (
                ('Single', 100),
                ('Binary System', 150),
                ('Red Giant', 50)
            )
            choice = star_selection[0]
            cls._name, cls._type, cls._cycles_to_supernova = 'Red Sun', choice[0], choice[1]
        return cls