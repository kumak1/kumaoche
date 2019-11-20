# -*- coding: utf-8 -*-

from .exec_env import ExecEnv
from ..runner import Runner
from ..config import DockerConfig


class Docker(ExecEnv):
    def __init__(self, config: DockerConfig, variable: {}, runner: Runner):
        self.__config = config
        self.__default_var = variable
        self.__runner = runner

    def name(self):
        return self.__config.name

    def assign_variables(self):
        return self.__default_var

    def exec(self, command: str, work_dir='', append_var={'default': 0}):
        if work_dir != '':
            work_dir = self.__runner.path_filter(work_dir.format(**self.assign_variables()))
            cmd = command.format(**self.assign_variables(), **append_var)
            return self.__runner.run(f'cd {work_dir} && {cmd}')

    def build(self):
        return self.exec(self.__config.build, work_dir=self.__config.work_dir)

    def up(self):
        return self.exec(self.__config.up, work_dir=self.__config.work_dir)

    def down(self):
        return self.exec(self.__config.down, work_dir=self.__config.work_dir)

    def ps(self):
        return self.exec(self.__config.ps, work_dir=self.__config.work_dir)

    def run(self, command: str, work_dir='', container=''):
        if work_dir == '':
            work_dir = self.__config.work_dir

        if container == '':
            container = self.__config.container

        if container != '':
            return self.exec(self.__config.run, work_dir=work_dir, append_var={'container': container, 'command': command})
