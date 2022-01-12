from L5XeTree import L5XeTree as L5X


class ModifierFunction:

    def __init__(self, value, header, single_selection):
        self.value = value  # new value
        self.header = header  # header of modification
        self.single_selection = single_selection  # selected in appear order instead of alphabetical order

    def apply_change_in_root(self, root: L5X.L5XRoot):
        # TODO: virtual function for changing element of L5X file
        pass


class ModifierNewTag(ModifierFunction):

    def __init__(self, value, header, single_selection):
        super().__init__(value, header, single_selection)
        # TODO: instantiating new modifier, having new name and template (data_type, scope etc)
        # seperate part of name which changes
        # check if change is in the beginning of the name
        # (then needs to be check if this tag exist or need to create new one)
        self._beginning_selected = True or False
        pass

    def is_tag_changed(self):
        # Returns information if beggining of the tag was selected. If so, whole tag changes, return True
        return self._beginning_selected

    def apply_change_in_root(self, root: L5X.L5XRoot):
        # TODO: changing element of L5X file (checking if necessary to create new tag and doing that)
        if self.is_tag_changed:
            # Check if tag (beggining of the name) exist in tag list of the file (root)
            # create new tag if necessary. Template of the tag is in header (data type, scope etc)
            pass
        pass

# TODO: subclasses for all cases
