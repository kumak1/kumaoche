# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class ExecEnv(metaclass=ABCMeta):
    @abstractmethod
    def name(self):
        raise NotImplementedError()

    @abstractmethod
    def assign_variables(self):
        raise NotImplementedError()

    @abstractmethod
    def run(self, command: str, work_dir=''):
        raise NotImplementedError()
