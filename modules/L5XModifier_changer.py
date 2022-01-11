from L5XeTree import L5XeTree as L5X


class Modifier_function:

    def make_change(self, root: L5X.L5XRoot):
        # TODO: virtual function for changing element of L5X file
        pass


class Modifier_new_tag(Modifier_function):

    def __init__(self, name, tag_template):
        # TODO: instantiating new modifier, having new name and template (data_type, scope etc)
        pass

    def make_change(self, root: L5X.L5XRoot):
        # TODO: changing element of L5X file (checking if necessary to create new tag and doing that
        pass

# TODO: subclasses for all cases
