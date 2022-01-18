from L5XeTree import L5XeTree as L5X
from widgets.custom_QStandardItems.myQt_rung_generation import mQtItem_rung
import re


class ModifierFunction:

    def __init__(self, value, header, single_selection):
        self.value = value  # new value
        self.header = header  # header of modification
        self.single_selection = single_selection  # selected in appear order instead of alphabetical order
        self._current_tag_name = None
        self.original_tag_name = self.get_tag_name(header)

    @property
    def current_tag_name(self):
        if self._current_tag_name:
            return self._current_tag_name
        else:
            return self.original_tag_name

    @current_tag_name.setter
    def current_tag_name(self, current_tag_name):
        self._current_tag_name = current_tag_name

    @staticmethod
    def get_tag_name(header):
        # extract tag name of modification (first part of tag name in header, make sure to handle case when
        # it is rung modification)
        # pattern matches begginig of the tag, omiting optional "Rung 1:2:" at the beggining of header
        pattern = r"(Rung [0-9]+\:)?(([0-9]+\:)|(DSC))?{?(\w+)?}?"
        match = re.seatch(pattern, header)
        # return name from header
        if match.group(5):
            return match.group(5)
        else:
            return None

    def apply_change_in_root(self, root: L5X.L5XRoot):
        # virtual function for changing element of L5X file
        pass

    def apply_change_in_rung_template(self, rungs_copy: list):
        # virutal function for changing rungs to create new one based on CSV modification
        # rungs_copy - list of mQtItem_rung
        pass

    def check_name_change(self, change_list: list):
        # function for checking for current tag name in already prepared change_list, to know, which
        # tag is needed to be modified (DT, DSC etc.)
        # change_list - list of ModifierFunction (already done)
        # if none of elements are of the same original_tag_name, current_tag_name stayes None
        for element in change_list:
            element: ModifierFunction
            if self.original_tag_name == element.original_tag_name:
                self.current_tag_name = element.current_tag_name


class ModifierNewTag(ModifierFunction):

    def __init__(self, value, header, single_selection):
        super().__init__(value, header, single_selection)
        # Instantiating new modifier. If will be necessary to create new tag, here will be new name
        #  and template (data_type, scope etc) will be in L5X file under self.original_tag_name tag
        # seperate part of name which changes
        pattern = r"(Rung [0-9]+\:[0-9]+\:)?([\w\.\[\]]+)?\{([\w\.]+)\}"
        match = re.match(pattern, header)
        self.changing_part = match.group(3)
        # check if change is in the beginning of the name - if group(2) is empty, then beginning_selected is True
        # (later needs to be check if this tag exist or need to create new one)
        self._beginning_selected = not bool(match.group(2))
        # modify self._current_tag_name if whole tag is modified (extract tag name from 'value')
        if self.is_tag_changed():
            self.current_tag_name = re.search(r"\w+", value)
        # maybe not? - create name of tag which must be modified (remove { } from header and put into:
        # self.tag_name = ""

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

    def apply_change_in_rung_template(self, rungs_copy: list):
        # TODO: function for changing rungs to create new one based on CSV modification, replacing name of tags
        # rungs_copy - list of mQtItem_rung
        # check if all rungs must be checked or just single one (alphabetical order or appear order was selected)
        # if
        if True:
            self.change_in_single_place(rungs_copy)
        else:
            self.change_in_all_rung(rungs_copy)

    def change_in_single_place(self, rungs_copy):
        # TODO: select single rung and place and do modification
        # find single rung
        # find single tag for modification
        # modify tag in selected rung and tag in rung.used_tags and in rung.used_tags_parted
        # find all self.tag_name in rung.original_tag - tag_name might be only the part of element of original_tags
        # (get index of found tags)
        self.change_tag()
        pass

    def change_in_all_rung(self, rungs_copy):
        # TODO: search in all rungs and all places for needed modification
        for rung in rungs_copy:
            # search in each rung of rungs_copy for self.tag_name in rung.used_tags, then change whole tag
            # (change_whole_tag) or just the part of it (change_part_of_tag). Change tag in rung.used_tags and
            # in rung.used_tags_parted
            pass
        pass

    def change_tag(self, rung: mQtItem_rung, index_of_tag_to_change, ):
        # TODO: somehow import mQtItem_rung? to write rung:mQtItem_rung?
        # TODO: change whole tag (whole tag was selected)
        # TODO: change_whole_tag and change_part_of_tag should be one function
        #  (can't tell if it is whole o part tag - in code could be specified more nested element of structure than
        #  selected to CSV)
        # in rung change tag in index index_of... Check in rung.original_tags what part must be changed
        # make changes in rung.used_tags and rung.used_tags_parted
        pass


class ModifierDataType(ModifierFunction):

    def __init__(self, value, header, single_selection):
        super().__init__(value, header, single_selection)
        # store new data_type
        pass

    def apply_change_in_root(self, root: L5X.L5XRoot):
        # TODO: function for changing element of L5X file
        pass


class ModifierDescription(ModifierFunction):

    def __init__(self, value, header, single_selection):
        super().__init__(value, header, single_selection)
        # store new description
        # check if it rung description modification:
        self._is_rung_modification = True or False
        pass

    @property
    def is_rung_modification(self):
        return self._is_rung_modification

    def apply_change_in_root(self, root: L5X.L5XRoot):
        # TODO: function for changing element of L5X file
        # do only if not self.is_rung_modification
        pass

    def apply_change_in_rung_template(self, rungs_copy: list):
        # TODO: function for changing rungs to create new one based on CSV modification
        # rungs_copy - list of mQtItem_rung
        # do only if self.is_rung_modification
        pass


class ModifierValue(ModifierFunction):
    # TODO: some way for changing constant values

    def __init__(self, value, header, single_selection):
        super().__init__(value, header, single_selection)

    def apply_change_in_root(self, root: L5X.L5XRoot):
        # TODO: function for changing element of L5X file
        # if it is not constant, then change is in root
        pass

    def apply_change_in_rung_template(self, rungs_copy: list):
        # TODO: function for changing rungs to create new one based on CSV modification
        # rungs_copy - list of mQtItem_rung
        # if it is constant, then change is in rung
        pass


class ModifierScope(ModifierFunction):

    def __init__(self, value, header, single_selection):
        super().__init__(value, header, single_selection)

    def apply_change_in_root(self, root: L5X.L5XRoot):
        # TODO: function for changing element of L5X file
        pass
