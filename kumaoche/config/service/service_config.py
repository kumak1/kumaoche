# -*- coding: utf-8 -*-

from ..exec_env.exec_env_config import ExecEnvConfig
from ..exec_env.shell_config import ShellConfig
from ..exec_env.docker_config import DockerConfig


class ServiceConfig(object):
    def __init__(self, parsed_yaml: {}, key: str):
        configs = parsed_yaml.get(key, {})
        env_name = configs.get('env', {}).get('name', '')

        if env_name == 'shell':
            self.env = ShellConfig(configs, 'env')
        elif env_name == 'docker':
            self.env = DockerConfig(configs, 'env')
        else:
            self.env = ExecEnvConfig(configs, 'env')

        self.run = configs.get('run', '')
        self.setup = configs.get('setup', '')
        self.update = configs.get('update', '')
