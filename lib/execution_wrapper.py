import subprocess


class ExecutionWrapper:

    @staticmethod
    def execute_command(args):
        command = subprocess.run(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return [command.returncode, command.stdout]

    @staticmethod
    def execute_command_popen(cmd):
        command = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        return command.communicate()[0]

    @staticmethod
    def execute_command_with_option(args, input_option=""):
        command = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return command.communicate(input=input_option.encode('utf-8'))
