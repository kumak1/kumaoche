# -*- coding: utf-8 -*-

from .exec_env import ExecEnv
from ..runner import Runner
from ..config import StringBuilderConfig


class StringBuilder(ExecEnv):
    def __init__(self, config: StringBuilderConfig, variable: {}, runner: Runner):
        self.__config = config
        self.__default_var = variable
        self.__runner = runner

    def name(self):
        return self.__config.name

    def assign_variables(self):
        return self.__default_var

    def run(self, command: str, work_dir=''):
        if work_dir == '':
            work_dir = self.__runner.path_filter(self.__config.work_dir.format(**self.assign_variables()))
        cmd = self.__config.run.format(**self.assign_variables(), **{'command': command})

        return f'cd {work_dir} && {cmd}'
