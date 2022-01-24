from L5XeTree import L5XeTree as L5X
from L5XeTree.modules.RSLogixEncoding import RSLogixEncoding
from modules.myQt import *
from modules.L5XModifier_changer import *
from modules import common_functions as CF
from widgets.custom_QStandardItems.myQt_rung_generation import *
from PySide6.QtGui import QStandardItemModel

from encodings.aliases import aliases
import csv
import re
import warnings


class L5XModifier:

    def __init__(self):
        self.L5XeTree: L5X.L5XeTree = None
        self.root: L5X.L5XRoot = None
        self.tag_list_all = None

    def open_file(self, xml_open):
        self.L5XeTree = L5X.L5XeTree(xml_open, remove_blank_text=True)
        self.L5XeTree.parse_tree()
        self.root = self.L5XeTree.tree.getroot()

    def save_file(self, xml_save):
        self.L5XeTree.save_file(xml_save)

    def get_scope(self):
        list1 = self.root.programs_name
        list1.insert(0, "Controller")
        return list1

    def scope_changed(self, scope_name):
        self.tag_list_all = self.root.get_tag_all_names(scope_name)

    def get_tag_list_filtered(self, filter_text):
        filter_text = filter_text.lower()
        if len(filter_text):
            return list(filter(lambda x: filter_text in x.lower(), self.tag_list_all))
        else:
            return self.tag_list_all

    def get_tag_info_tuple(self, tag_name, scope, encoder=None):
        return self.root.tag(tag_name, scope).get_tag_structure(encoder=encoder)

    def insert_into_tree(self, parent_item, element_tuple, print_headers, concatenate, encoder=None):
        name, data_type, value, children = element_tuple
        if value is None:
            value = ""
            has_value = False
        else:
            has_value = True
        if has_value or print_headers:
            tree_element = MyQTreeItemName(name)
            data_type_element = MyQTreeItemDataType(data_type)
            if data_type_element == "STRING" or data_type_element in self.root.get_data_types_string_names():
                value_element = MyQTreeItemString(str(value))
            else:
                value_element = MyQTreeItemValue(str(value), True) #editable=has_value)         !!!!! DO ZMIANY
            parent_item.appendRow([tree_element, data_type_element, value_element])
        else:
            tree_element = parent_item
        if children is not None:
            for child in children:
                child_tuple = child.build_child_structure(name, data_type, encoder=encoder,
                                                          concatenate_path=concatenate)
                self.insert_into_tree(tree_element, child_tuple, print_headers, concatenate, encoder=encoder)

    def check_custom_ecnoder(self, encoder):
        encoder = encoder.lower()
        return [(k, v) for k, v in aliases.items() if encoder in k or encoder in v]

    def iterItems(self, root):
        def recurse_item_tree(parent):
            for row in range(parent.rowCount()):
                child = parent.child(row, 0)
                yield [parent.child(row, 0).text(), parent.child(row, 1).text(), parent.child(row, 2).text()]
                if child.hasChildren():
                    yield from recurse_item_tree(child)
        return recurse_item_tree(root)

    def export_tag_to_csv(self, tree_view, save_file, output_encoder):
        with open(save_file, 'w', encoding=output_encoder, newline='') as f_w:
            writer = csv.writer(f_w, dialect='excel')
            writer.writerow(["Name", "Data type", "Value"])
            for item in self.iterItems(tree_view.model().invisibleRootItem()):
                writer.writerow(item)

    def import_tag_from_csv(self, load_file, scope="Controller", file_encoding=None, encoding=None):
        with open(load_file, 'r', encoding=file_encoding, newline='') as f_r:
            dialect = csv.Sniffer().sniff(f_r.read(1000))
            f_r.seek(0)
            reader = csv.DictReader(f_r, dialect=dialect)
            if "Name" in reader.fieldnames and "Value" in reader.fieldnames:
                pattern = r"(\w+)((\.)|(\[[0-9]+\]).*)?"
                while True:
                    try:
                        new_row = next(reader)
                    except StopIteration:
                        break
                    match = re.search(pattern, new_row["Name"])
                    tag_name = match.group(1)
                    tag_specified_address = match.group(2)
                    if match:
                        tag = self.root.tag(tag_name, scope)
                        if tag_specified_address is not None:
                            template = tag.get_value_element(tag_specified_address, encoding)
                        else:
                            template = tag.get_value(encoding)
                    else:
                        raise ValueError("Cannot extract tag name from '{}' in column 'Name'".format(new_row["Name"]))
                    try:
                        reordered_data = self.reorder_data_of_csv(reader, template, first_row_value=new_row["Value"])
                    except StopIteration:
                        raise StopIteration("Number of values in CSV is incorrect - cannot import tag")
                    if tag_specified_address is not None:
                        tag.set_value_element(reordered_data, tag_specified_address, encoding)
                    else:
                        tag.set_value(reordered_data, encoding)
            else:
                raise ImportError("CSV file does not contain 'Name' or 'Value' headers")

    @staticmethod
    def reorder_data_of_csv(csv_reader: csv.DictReader, template_list: list, first_row_value=None):
        if isinstance(template_list, list):
            reordered_data = list()
            for template_element in template_list:
                if isinstance(template_element, list):
                    next(csv_reader)
                    single_data = L5XModifier.reorder_data_of_csv(csv_reader, template_element)
                else:
                    single_data = next(csv_reader)["Value"]
                reordered_data.append(single_data)
        else:
            reordered_data = first_row_value
        return reordered_data

    @staticmethod
    def encode_string(string: str, encoder):
        return RSLogixEncoding.encode_string(string, encoder)

    @staticmethod
    def decode_string(string: str, encoder):
        return RSLogixEncoding.decode_string(string, encoder)

    def change_file_element(self, change_element: ModifierFunction, scope: str):
        # change file element - make change in file (self.root) with change_element object
        change_element.apply_change_in_root(self.root, scope)

    def insert_new_rungs(self, rung_list, scope, routine, rung_index):
        # TODO: insert new rungs into main file in place described by inputs
        pass


class L5XModifier_r_generator(L5XModifier):

    def __init__(self):
        self.rung_template = list()
        super().__init__()

    def generate_tree_appear_order(self, tree_model):
        routine = self.root.any_program().any_routine()
        i = 0
        self.rung_template = list()
        for rung in routine.rungs:
            rung_name = "Rung " + str(i)
            rung_item = mQtItem_rung(self.root, rung_name, rung.comment, rung.code)
            tree_model.appendRow(rung_item.get_row())
            self.rung_template.append(rung_item)
            i += 1

    def generate_tree_alphabetical_order(self, tree_alphabetical_model: QStandardItemModel,
                                         tree_appear_mode: QStandardItemModel):
        appeared_elements = set()
        for i in range(tree_appear_mode.rowCount()):
            rung_item: mQtItem_rung = tree_appear_mode.item(i, 0)
            [appeared_elements.add(element) for element in rung_item.used_tags]
        elems_dict = dict()
        for element in appeared_elements:
            elem_splited = CF.split_tag_to_parts(element, join_index=True)
            self.build_elements_dict(elems_dict, elem_splited)
        for tag in sorted(elems_dict):
            tag_item = mQtItem_alphabetical_tag(self.root, tag, elems_dict[tag])
            tree_alphabetical_model.appendRow(tag_item.get_row())

    def build_elements_dict(self, elems_dict, elem_splited):
        if not elem_splited[0] in elems_dict:
            elems_dict[elem_splited[0]] = dict()
        if len(elem_splited) > 1:
            self.build_elements_dict(elems_dict[elem_splited[0]], elem_splited[1:])

    def generate_list_of_changes(self, headers, rows) -> list:
        # generate list of changes
        # prepare list of changes of main files (list of new tags, changes in description etc, changes to rungs)
        # parse all headers, depending on what is in header prepare list of subclasses of ModifierFunction
        # TODO: Changing this function to parse every possible information from header. Use class storing changes of
        #  each header (eg. to know which tag description should be changed after changing selected name)
        # patterns for selecting correct type of change
        # TODO: Correct patterns to retrive more information (tag name, rung number, rung element index)
        pattern_rung_change = r"Rung (\d+)\:((\d+)\:)?"  # group(1)- rung number, group(3)- rung element index
        pattern_tag_name = r"\{\w+\}"
        pattern_property_change = r":([a-zA-Z]{1,3})\Z"
        # dictionary of property modification key names to subclasses of ModifierFunction
        property_change_dictionary = {"DT": ModifierDataType, "DSC": ModifierDescription, "VAL": ModifierValue,
                                      "SCP": ModifierScope}
        modification_class_list = list()  # subclasses of class ModifierFunction
        rung_modification = list()  # list of bool values: rung modification - True, global modification - False
        # TODO: Use these lists
        performed_modification_obj_dict = dict()  # dict of PerfAlphabeticModification obj as values, tag_name as keys
        performed_modification_rung_obj_dict = dict()  # dict of PerfRungModification obj as values, tag_name as keys
        for header in headers:
            # check if rung modification of global modification
            # TODO: if this is rung modification, get also rung number and run element index (if exist last one)
            rung_modification.append(bool(re.search(pattern_rung_change, header)))
            # check what is need to be changed
            # check if name is selected {...}
            match = re.search(pattern_tag_name, header)
            if match:
                # TODO: Tag name should be matched, find it in performed_modification_obj_dict or
                #  performed_modification_rung_obj_dictkeys, if there is no one
                #  then create PerformedModification object (one of the subclass) and append to appropriate dict
                # append class name changing tag name (and creating new one if necessary)
                modification_class_list.append(ModifierNewTag)
                continue
            # check other :DT, :DSC, :VAL, :SCP
            match = re.search(pattern_property_change, header)
            if match:
                # append class name changing property
                # match.group(1) should be one of the key of property_change_dictionary
                if match.group(1).upper() in property_change_dictionary:
                    modification_class_list.append(property_change_dictionary[match.group(1).upper()])
                    continue
            # if there was no match this part of code will execute:
            modification_class_list.append(None)
            warnings.warn("Part of imported modification are not recognized. Header name is recognized: " + header)
        whole_change_list = list()
        # for every row: for every element in list of subclasses: create objects:
        # class_name(value, header, single_selection)
        for row in rows:
            row_change_list = list()
            # TODO: every modification_class_list must be copied (new_obj = copy(obj) ) for each row
            #  generate (copied_modification_class_list)
            for value, header, class_name, rung_modification_bool in zip(row, headers, modification_class_list,
                                                                         rung_modification):
                # check if class_name was correctly evaluated
                if class_name is not None:
                    # TODO: find proper obj from copied_modification_class_list and insert into constructor (find by
                    #  alphabetical name, or by appear order if it exist and it is that case). If it is the latter, then
                    #  check if it has connected alphabetical order obj, if no, find it and connect to this object
                    # create subclass of ModifierFunction - name stored in class_name
                    modifier_function_object: ModifierFunction = class_name(value, header, rung_modification_bool)
                    # put row_change_list into function check_name_change to make changes in proper tag
                    modifier_function_object.check_name_change(row_change_list)
                    # append to row_change_list
                    row_change_list.append(class_name(value, header, rung_modification_bool))
            whole_change_list.append(row_change_list)
        # return list of changes (in form of objects of different subclasses of ModifierFunction)
        return whole_change_list

    def generate_new_rungs(self, change_list) -> list:
        # TODO: generate new rungs based on template and csv data
        # change_list - list of ModifierFunction (all rows of CSV, each row has list of changes)
        for row_change_list in change_list:
            # MOVE THIS IMPLEMENTATION INTO myQt_rung_generation.mQtItem_rung, call here function from mQtItem_rung
            # copy self.rung_template and all operation (changes) do on copy (copy: rungs_copy)
            rungs_copy = None
            pass
            for single_change in row_change_list:
                single_change: ModifierFunction
                # each single_change of class ModifierFunction do apply_change_in_rung_template
                # on copied self.rung_template
                pass
                single_change.apply_change_in_rung_template(rungs_copy)
        # return list of L5XRung's
        pass
