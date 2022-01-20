from L5XeTree import L5XeTree as L5X
from widgets.custom_QStandardItems.myQt_rung_generation import mQtItem_rung
import re


class PerformedModification:

    def __init__(self):
        self.original_tag_name = None
        self.current_tag_name = None
        # dictionary where key is original_subelement_name of original_tag_name (if subelement or one of it's
        #  subelements changes) and value is tuple of: current_subelement_name and similar dictionary of it's
        #  subelements
        self.tag_elements_dict = dict()


class PerfAlphabeticModification(PerformedModification):

    def __init__(self):
        super().__init__()
        pass


class PerfRungModification(PerformedModification):

    def __init__(self, rung_number, rung_element_index):
        super().__init__()
        self.rung_number = rung_number
        self.rung_element_index = rung_element_index


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

    def apply_change_in_root(self, root: L5X.L5XRoot, scope: str):
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
        # if none of elements are of the same original_tag_name, current_tag_name stays None
        for element in change_list:
            element: ModifierFunction
            if self.original_tag_name == element.original_tag_name:
                self.current_tag_name = element.current_tag_name

    def get_original_tag(self, root: L5X.L5XRoot, scope: str):
        original_tag = root.tag(self.current_tag_name, scope=scope)
        if original_tag is None and scope != "Controller":
            original_tag = root.tag(self.current_tag_name, scope="Controller")
        return original_tag


class ModifierNewTag(ModifierFunction):
    # TODO: modifying constant value or changing to constant value should be done as ModifierNewTag

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
        # check if new value is a constant instead of a tag
        pattern = r'(\A\".+"\Z)|(\A[0-9\-][0-9\-.]*\Z)'
        self.is_constant = bool(re.match(pattern, value))

    def is_tag_changed(self):
        # Returns information if beggining of the tag was selected. If so, whole tag changes, return True
        return self._beginning_selected

    def apply_change_in_root(self, root: L5X.L5XRoot, scope: str):
        # Changing element of L5X file (checking if necessary to create new tag and doing that)
        # Check if modification changes tag to another tag
        if self.is_tag_changed and not self.is_constant:
            # Check if tag (beginning of the name) exist in tag list of the file (root)
            tag = self.get_original_tag(root, scope)
            # create new tag if necessary. Template of the tag is in header (data type, scope etc)
            if tag is None:
                # find original_tag to get to know the data_type and scope
                original_tag = root.tag(self.original_tag_name, scope=scope)
                if original_tag is None and scope != "Controller":
                    original_tag = root.tag(self.original_tag_name, scope="Controller")
                # If original_tag is found, then get from it data_type and scope, else get default values
                # Create new tag
                if original_tag is not None:
                    root.copy_tag(self.current_tag_name, original_tag)
                else:
                    root.new_tag(self.current_tag_name, "BOOL")

    def apply_change_in_rung_template(self, rungs_copy: list):
        # TODO: function for changing rungs to create new one based on CSV modification, replacing name of tags
        # rungs_copy - list of mQtItem_rung
        # check if all rungs must be checked or just single one (alphabetical order or appear order was selected)
        # if
        if True:
            self.change_in_single_place(rungs_copy)
        else:
            self.change_in_all_rung(rungs_copy)
        # handle also constants

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

    def apply_change_in_root(self, root: L5X.L5XRoot, scope: str):
        # Function for changing element of L5X file. Changing data_type is data loss action. Changing data_type is done
        #  by creating copy of the tag, the deleting original tag
        original_tag = self.get_original_tag(root, scope)
        if original_tag is not None:
            if self.value != original_tag.data_type:
                if self.value.upper() in L5X.L5XTag.SIMPLE_DATA_TYPE or \
                        self.value in root.get_data_types_all_names():
                    root.copy_tag(self.current_tag_name, original_tag, data_type=self.value)
                    root.delete_tag(original_tag)
                else:
                    raise ValueError("There is no data_type: " + self.value + " in L5X file")
        else:
            raise ValueError("There is no tag " + self.current_tag_name + " for changing data_type")


class ModifierDescription(ModifierFunction):

    def __init__(self, value, header, single_selection):
        super().__init__(value, header, single_selection)
        # store new description
        # check if it rung description modification - if group(2) is not empty, then it is rung desc modification:
        pattern = r"(Rung [0-9]+\:)?(DSC)?"
        self._is_rung_modification = bool(re.search(pattern, header).group(2))
        self._is_subelement_modification = bool(re.match(r"[\.\[\]]", header))
        self._current_whole_tag_name = None  # not only first part of the tag, but also subelement names included

    @property
    def is_rung_modification(self):
        return self._is_rung_modification

    @property
    def current_whole_tag_name(self):
        if self._current_whole_tag_name is not None:
            return self._current_whole_tag_name
        elif self._is_rung_modification is None:
            return None
        else:
            pattern = r"(Rung [0-9]+\:[0-9]+\:)?([^\:]+)"
            match = re.match(pattern, self.header)
            if match:
                whole_tag_name = match.group(2)
                whole_tag_name = whole_tag_name.replace("{", "").replace("}", "")
                return whole_tag_name
            else:
                return None

    @current_whole_tag_name.setter
    def current_whole_tag_name(self, value):
        self._current_whole_tag_name = value

    def apply_change_in_root(self, root: L5X.L5XRoot, scope: str):
        # TODO: function for changing element of L5X file
        # do only if not self.is_rung_modification
        if not self.is_rung_modification:
            tag = self.get_original_tag(root, scope)
            if tag is not None:
                pass
            else:
                raise ValueError("There is no tag " + self.current_tag_name + " for changing description")

    def apply_change_in_rung_template(self, rungs_copy: list):
        # TODO: function for changing rungs to create new one based on CSV modification
        # rungs_copy - list of mQtItem_rung
        # do only if self.is_rung_modification
        if self.is_rung_modification:
            pass

    def check_name_change(self, change_list: list):
        # TODO: override check_name_changes to find not only tag name changes, but also whole name including nested
        #  element if that is the case
        super().check_name_change(change_list)
        # do override function only if description modification is of subelement of the tag
        if self._is_subelement_modification:
            for element in change_list:
                # TODO: change this if sentence - if it is alphabetical order compare firstly original_tag_name then all
                #  subelement of the tag. If it is appear order, then Rung and index in rung should match
                if self.original_tag_name == element.original_tag_name:
                    # if element changes name, check what part of the name, and change it in here
                    # changes stored in self.current_whole_tag_name
                    pass


class ModifierValue(ModifierFunction):
    # Modifying only tag values, constant values should be inserted by changing tag name, not value

    def apply_change_in_root(self, root: L5X.L5XRoot, scope: str):
        # TODO: function for changing element of L5X file
        # it is not constant, so change is in root. Constant values should be inserted by changing tag name, not value
        pass


class ModifierScope(ModifierFunction):

    def apply_change_in_root(self, root: L5X.L5XRoot, scope: str):
        # TODO: function for changing element of L5X file
        pass
