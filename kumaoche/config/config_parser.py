# -*- coding: utf-8 -*-

import yaml
import os
import sys

from .config_pack import ConfigPack


class ConfigParser(object):

    @classmethod
    def file_path_list(cls):
        path_list = os.environ.get('KUMAOCHE_CONFIG_PATH', os.getcwd() + '/kumaoche_config.yml').split(':')

        # ファイル存在確認
        for path in path_list:
            if not os.path.exists(path):
                print(f'Target config file "{path}" is not exist.')
                sys.exit()

        return path_list

    @classmethod
    def all_roles(cls, file_path_list=None):
        if file_path_list is None:
            file_path_list = cls.file_path_list()

        loaded_roles = []

        for file_path in file_path_list:
            with open(file_path) as file:
                loaded_roles += list(filter(lambda x: x != 'defaults', yaml.safe_load(file).keys()))

        # 順序を維持した重複削除
        return sorted(set(loaded_roles), key=loaded_roles.index)

    @classmethod
    def find(cls, role: str, file_path_list=None):
        if file_path_list is None:
            file_path_list = cls.file_path_list()

        if role not in cls.all_roles(file_path_list):
            print(f'Target role "{role}" is not exist.')
            sys.exit()

        loaded_yaml = {}

        for file_path in file_path_list:
            with open(file_path) as file:
                loaded_yaml = {**loaded_yaml, **yaml.safe_load(file)}

        return ConfigPack(loaded_yaml.get(role, {}))
