#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import argparse 
import shlex
import yaml
import cmd

import render_manager as rm
from ARFglobals import *
import slave_network_manager as nm

config = yaml.safe_load(open("slave_config.yaml"))

ap = argparse.ArgumentParser()
args = vars(ap.parse_args())

# ------ Functions ------


def networkCallback(client, clentIp, message):

    messageType = message

    print(client, message)


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
                  ______     __         ______     __    __  ______    
              ___/\  ___\___/\ \_______/\  __ \___/\ \  / /_/\  ___\__   
               __\ \___  \__\ \ \____ _\ \  __ \__\ \ \' /__\ \  __\___ 
                __\/\_____\__\ \_____\__\ \_\ \_\__\ \__/____\ \_____\__
                 __\/_____/___\/_____/___\/_/\/_/___\/_/______\/_____/___                                                                     
"""
    prompt = '>> '
    config = None

    def emptyline(self):
        pass  # Do nothing on empty input line

    
# ----- main -----
if __name__ == '__main__':
    nm.startNetworkManager(networkCallback)
    app = CliInterface()
    app.cmdloop()
   