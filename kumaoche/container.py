# -*- coding: utf-8 -*-

from .config import ConfigParser, ServiceConfig
from .exec_env import DisableEnv, Shell, Docker, StringBuilder
from .service import PackageManager
from .runner import InvokeRunner


class Container(object):
    def __init__(self, role: str):
        config = ConfigParser.find(role)

        self.services = []

        for service in config.services:
            self.services.extend([PackageManager(self.env(service), service)])

    @staticmethod
    def env(config: ServiceConfig):
        if config.env == 'string_builder':
            return StringBuilder(config.string_builder, config.environment, InvokeRunner)
        elif config.env == 'shell':
            return Shell(config.shell, config.environment, InvokeRunner)
        elif config.env == 'docker':
            return Docker(config.docker, config.environment, InvokeRunner)
        else:
            return DisableEnv()

    @classmethod
    def all_role_names(cls):
        return ConfigParser.all_roles()
