# -*- coding: utf-8 -*-

from .config.config_parser import ConfigParser
from .config.service.service_config import ServiceConfig
from .exec_env.disable import DisableEnv
from .exec_env.shell import Shell
from .exec_env.docker import Docker
from .service.git import Git
from .service.db import DB
from .service.package_manager import PackageManager
from .runner.invoke_runner import InvokeRunner


class Container(object):
    def __init__(self, role: str):
        config = ConfigParser.find(role)

        self.name = config.git.repo
        self.shell = Shell(config.shell, config.variable, InvokeRunner)
        self.docker = Docker(config.docker, config.variable, InvokeRunner)

        self.git = Git(self.env(config.git, config.variable), config.git)
        self.db = DB(self.env(config.db, config.variable), config.db)
        self.php = PackageManager(self.env(config.php, config.variable), config.php)
        self.ruby = PackageManager(self.env(config.ruby, config.variable), config.ruby)
        self.node = PackageManager(self.env(config.node, config.variable), config.node)

        self.package_managers = [
            self.php,
            self.ruby,
            self.node
        ]

    @staticmethod
    def env(config: ServiceConfig, variable: {}):
        if config.env.name == 'shell' and config.env.work_dir != '':
            return Shell(config.env, variable, InvokeRunner)
        elif config.env.name == 'docker' and config.env.work_dir != '':
            return Docker(config.env, variable, InvokeRunner)
        else:
            return DisableEnv()

    @classmethod
    def all_role_names(cls):
        return ConfigParser.all_roles()
