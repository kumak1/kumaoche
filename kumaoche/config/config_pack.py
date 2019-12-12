# -*- coding: utf-8 -*-

from .service import GitConfig, PackageManagerConfig
import yaml

class ConfigPack(object):
    def __init__(self, parsed_yaml):
        if parsed_yaml is None:
            parsed_yaml = {}

        # 全設定共有のテンプレート用変数
        self.environment = self.assign_dict(parsed_yaml, 'environment')
        #
        # self.string_builder = StringBuilderConfig(parsed_yaml, 'string_builder')
        # self.shell = ShellConfig(parsed_yaml, 'shell')
        # self.docker = DockerConfig(parsed_yaml, 'docker')

        self.git = GitConfig(parsed_yaml)

        # self.php = PackageManagerConfig(parsed_yaml, 'php')
        # self.ruby = PackageManagerConfig(parsed_yaml, 'ruby')
        # self.node = PackageManagerConfig(parsed_yaml, 'node')

        self.services = []

        # print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        # print(yaml.dump(parsed_yaml))

        for service in parsed_yaml.get('services', []):
            if service is None:
                continue

            self.services.extend([PackageManagerConfig(service)])

    @classmethod
    def assign_dict(cls, parsed_yaml: {}, key: str):
        configs = parsed_yaml.get(key, {})
        presets_configs = parsed_yaml.get('presets', {}).get(key, {})

        dictionary = {}
        for key in configs.keys():
            dictionary.setdefault(key, configs.get(key, ''))

        for key in presets_configs.keys():
            dictionary.setdefault(key, presets_configs.get(key, ''))

        return dictionary
