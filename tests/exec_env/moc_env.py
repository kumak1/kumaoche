# -*- coding: utf-8 -*-

from kumaoche.exec_env.exec_env import ExecEnv


class MocEnv(ExecEnv):
    def __init__(self, variable: {}):
        self.__default_var = variable

    def name(self):
        return ''

    def assign_variables(self):
        return self.__default_var

    def run(self, command: str, work_dir=''):
        return f'work_dir:{work_dir},command:{command}'
