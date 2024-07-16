#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse 
import shlex

from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

import cmd

import render_manager as rm
from ARFglobals import *
import master_database as db

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--nogui",action='store_true', help="runs the app as a cli app")
args = vars(ap.parse_args())


# ----- Gui -----

class GuiInterface(QDialog):
    def __init__(self, parent=None):
        super(GuiInterface, self).__init__(parent)

        # make dark theme palette
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(53,53,53))
        palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Base, QColor(42,42,42))
        palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Dark, QColor(35,35,35))
        palette.setColor(QPalette.ColorRole.Shadow, QColor(20,20,20))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.black)
        palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
        palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(127,127,127))
        app.setPalette(palette)
        app.setStyle("Fusion") # Force the style to be the same on all OSs:

        mainLayout = QGridLayout()

        self.setLayout(mainLayout)
        
        self.setWindowTitle("ARF Master")

# ----- Cli ----- 
class CliInterface(cmd.Cmd):

    intro = r"""
    _____/\\\\\\\\\_______/\\\\\\\\\______/\\\\\\\\\\\\\\\_        
     ___/\\\\\\\\\\\\\___/\\\///////\\\___\/\\\///////////__       
      __/\\\/////////\\\_\/\\\_____\/\\\___\/\\\_____________      
       _\/\\\_______\/\\\_\/\\\\\\\\\\\/____\/\\\\\\\\\\\_____     
        _\/\\\\\\\\\\\\\\\_\/\\\//////\\\____\/\\\///////______    
         _\/\\\/////////\\\_\/\\\____\//\\\___\/\\\_____________   
          _\/\\\_______\/\\\_\/\\\_____\//\\\__\/\\\_____________  
           _\/\\\_______\/\\\_\/\\\______\//\\\_\/\\\_____________ 
            _\///________\///__\///________\///__\///______________
"""
    prompt = '>> '
    config = None

    def do_addslave(self, arg):
        'Add a rendering slave: addslave --name <name> [--ip <ip>]'
        try:
            parser = argparse.ArgumentParser(prog='addslave')
            parser.add_argument('name', help='Name of the rendering slave')
            parser.add_argument('--ip', help='IP address of the rendering slave')
            args = parser.parse_args(shlex.split(arg))

            name = args.name
            ip = args.ip if args.ip else '0.0.0.0'  # Default IP address if not provided

            db.insert_renderSlave(name, ip)
            
        except SystemExit:
            pass  # argparse throws a SystemExit exception after parsing

    def do_listslaves(self, arg):
        'Add a rendering slave: addslave --name <name> [--ip <ip>]'
        try:
            parser = argparse.ArgumentParser(prog='listslaves')
            args = parser.parse_args(shlex.split(arg))

            
            print(formatTable(db.get_renderSlaves(), reverse=True)) # reverse to make name at front

        except SystemExit:
            pass   

    def emptyline(self):
        pass  # Do nothing on empty input line

    
# ----- main -----
if __name__ == '__main__':
    # run cli or gui app
    if args["nogui"]:
        app = CliInterface()
        app.cmdloop()
    else:
        app = QApplication(sys.argv)
        master = GuiInterface()
        master.show()
        sys.exit(app.exec())
