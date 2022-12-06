import sxw.gui.ui as ui
import scj.code.initialization as ini
import os

ROOT = os.getcwd()

if __name__ == "__main__":
    ini.directory_ini()
    ui.ui()
    print(ROOT)
