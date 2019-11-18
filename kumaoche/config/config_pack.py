# -*- coding: utf-8 -*-

from .exec_env.shell_config import ShellConfig
from .exec_env.docker_config import DockerConfig
from .service.git_config import GitConfig
from .service.db_config import DbConfig
from .service.package_service_config import PackageManagerConfig


class ConfigPack(object):
    def __init__(self, parsed_yaml):
        self.variable = self.assign_dict(parsed_yaml, 'variable')
        self.shell = ShellConfig(parsed_yaml, 'shell')
        self.docker = DockerConfig(parsed_yaml, 'docker')
        self.git = GitConfig(parsed_yaml, 'git')
        self.db = DbConfig(parsed_yaml, 'db')
        self.php = PackageManagerConfig(parsed_yaml, 'php')
        self.ruby = PackageManagerConfig(parsed_yaml, 'ruby')
        self.node = PackageManagerConfig(parsed_yaml, 'node')

    @classmethod
    def assign_dict(cls, parsed_yaml: {}, key: str):
        configs = parsed_yaml.get(key, {})

        dictionary = {}
        for key in configs.keys():
            dictionary.setdefault(key, configs.get(key, ''))

        return dictionary
