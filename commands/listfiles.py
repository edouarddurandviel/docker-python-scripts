

import os

from commands.base import Command


class ListFileCommand(Command):
    def execute(self):
      for file in os.listdir("."):
          print(file)