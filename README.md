# L5XModifier

## Intro

Application for modifying L5X files - exported projects of Allen-Bradley PLC programs (exported from Studio 5000 or
RSLogix5000). App design is modified version of project made by
[Wanderson M. Pimenta](https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6).
GUI is made in PySide6 and QtDesigner. Modification of L5X files are made by
[L5XeTree](https://github.com/MateuszKon/L5XeTree) library

## Creating standalone

For creating standalone version of application (tested with Windows7/10) use PyInstaller and L5XModifier.spec file. From command line in project folder use *pyinstaller L5XModifier.spec* command.

## Used modules/frameworks

- lxml
- PySide6 + QtDesigner
