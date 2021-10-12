from L5XModifier_functions import *
# from main import *


L5XMod = L5XModifier()

L5XMod.open_file(r"C:\Users\plc\Documents\PythonProj\L5X_app\SD168700_31MAY2021.L5X")

path = r"C:\Users\plc\Documents\PythonProj\L5X_app\aaa.csv"
L5XMod.import_tag_from_csv(path, file_encoding="UTF-8", encoding="Windows-1250")
