# -*- coding: utf-8 -*-

from ..config import DbConfig
from ..exec_env import ExecEnv
from .service import Service


class DB(Service):
    def __init__(self, env: ExecEnv, config: DbConfig):
        self.env = env
        self.__config = config

    def run(self, command: str):
        var_command = {'command': self.env.var_assign(command)}
        return self.env.run(self.env.var_assign(self.__config.run,  var_command))

    def setup(self):
        return self.env.run(self.env.var_assign(self.__config.setup))

    def update(self):
        return self.env.run(self.env.var_assign(self.__config.update))
