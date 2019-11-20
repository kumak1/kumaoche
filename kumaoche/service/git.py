# -*- coding: utf-8 -*-

from ..config import GitConfig
from ..exec_env import ExecEnv
from .service import Service


class Git(Service):
    def __init__(self, env: ExecEnv, config: GitConfig):
        self.env = env
        self.__config = config

    def run(self, command: str):
        repo_dir = self.__config.repo_dir.format(**self.env.assign_variables())

        return self.env.run(command.format(**self.env.assign_variables()), work_dir=repo_dir)

    def setup(self):
        return self.env.run(self.__config.setup.format(**self.env.assign_variables()))

    def update(self):
        return self.env.run(self.__config.update.format(**self.env.assign_variables()))
