import sys

# scripts

from commands.generate import GenerateCommand
from commands.listfiles import ListFilesCommand
from commands.registry import CommandRegistry

# load csv: "csv"
# send rport extraction: "report"

def main():
  
    CommandRegistry.register("generate", GenerateCommand)
    CommandRegistry.register("list", ListFilesCommand)
    
    one_arg_command = sys.argv[0]

    command_cls = CommandRegistry.get(one_arg_command)

    if not command_cls:
        raise ValueError("Unknown command")

    command = command_cls()
    command.execute()




if __name__ == "__main__":
    main()