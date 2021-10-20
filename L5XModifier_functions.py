from L5XeTree import L5XeTree as L5X
from L5XeTree.modules.RSLogixEncoding import RSLogixEncoding
from modules.myQt import *
from widgets.custom_QStandardItems.myQt_rung_generation import *

from encodings.aliases import aliases
import csv
import re


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

    def generate_tree_appear_order(self, tree_model):
        routine = self.root.any_program().any_routine()
        i = 0
        for rung in routine.rungs:
            rung_name = "Rung " + str(i)
            rung_item = mQtItem_rung(self.root, rung_name, rung.comment, rung.code)
            tree_model.appendRow(rung_item.get_row())
            i += 1
