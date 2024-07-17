#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse 
import shlex
import cmd

from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

import render_manager as rm
from ARFglobals import *
import master_database as db
import master_network_manager as nm

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
                  __    __    ______    ______    ______   ______    ______           
              ___/\ "-./  \__/\  __ \__/\  ___\__/\__  _\_/\  ___\__/\  == \__   
               __\ \ \-./\ \_\ \  __ \_\ \___  \_\/_/\ \/_\ \  __\__\ \  __<___   
                __\ \_\ \ \_\_\ \_\ \_\_\/\_____\___\ \_\__\ \_____\_\ \_\ \_\__ 
                 __\/_/  \/_/__\/_/\/_/__\/_____/____\/_/___\/_____/__\/_/ /_/___                    
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
    
    def do_render(self, arg):
        'submitt render job to all rendering slaves: render --blend <path> '
        try:
            parser = argparse.ArgumentParser(prog='addslave')
            parser.add_argument('-b', '--blend', help='Set path of blend file')
            parser.add_argument('-f', '--frame', help='render a single frame and set frame number to render. by defult 1')
            #parser.add_argument('-a', '--animation', help='render an animation')
            args = parser.parse_args(shlex.split(arg))

            blendpath = args.blend

            if args.frame:
                frame = args.frame if args.frame else '1'
            elif args.animation:
                pass
            
        except SystemExit:
            pass  # argparse throws a SystemExit exception after parsing

    def do_statuscheck(self, arg):
        try:
            parser = argparse.ArgumentParser(prog='addslave')
            parser.add_argument('-s', '--slave', help='name of slave to check status of')
            args = parser.parse_args(shlex.split(arg))

            ipOfSlave = db.get_renderSlave(args.slave)
            nm.checkStatus(ipOfSlave)

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
