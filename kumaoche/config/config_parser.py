# -*- coding: utf-8 -*-

import yaml
import os
import sys

from .config_pack import ConfigPack


class ConfigParser(object):

    @classmethod
    def file_path_list(cls):
        default_config = [os.path.dirname(__file__) + '/presets.yml']
        append_config = os.environ.get('KUMAOCHE_CONFIG_PATH', os.getcwd() + '/kumaoche_config.yml').split(':')

        return default_config + append_config

    @classmethod
    def all_roles(cls, file_path_list=None):
        loaded_yaml = cls.yaml_load(file_path_list)
        loaded_repository_keys = list(loaded_yaml.get('repositories', {}).keys())

        # 順序を維持した重複削除
        return sorted(set(loaded_repository_keys), key=loaded_repository_keys.index)

    @classmethod
    def find(cls, repo: str, file_path_list=None):
        loaded_yaml = cls.yaml_load(file_path_list)
        parsed_yaml = cls.parse_version(loaded_yaml)
        loaded_repository = cls.find_repository_config(parsed_yaml, repo)

        return ConfigPack(loaded_repository)

    @classmethod
    def yaml_load(cls, file_path_list=None):
        if file_path_list is None:
            file_path_list = cls.file_path_list()

        # ファイル存在確認
        for path in file_path_list:
            if not os.path.exists(path):
                print(f'Target config file "{path}" is not exist.')
                sys.exit()

        loaded_yaml = {}
        for file_path in file_path_list:
            with open(file_path) as file:
                loaded_yaml = {**loaded_yaml, **yaml.safe_load(file)}

        return loaded_yaml

    @classmethod
    def parse_version(cls, loaded_yaml):
        version = int(loaded_yaml.get('version', 1))

        if version == 1:
            return loaded_yaml
        else:
            print(f'Yaml version "{version}" is invalid.')
            sys.exit()

    @classmethod
    def find_repository_config(cls, loaded_yaml, repo):
        # 指定リポジトリが設定ファイルに存在するか確認
        loaded_repositories = loaded_yaml.get('repositories', {})
        if repo not in list(loaded_repositories.keys()):
            print(f'Target repository "{repo}" is not exist.')
            sys.exit()

        # 指定リポジトリの設定のyamlフォーマットが正しいか確認
        loaded_repository = loaded_repositories.get(repo, {})
        if type(loaded_repository.get('services')) != list:
            print(f'Syntax Error.')
            sys.exit()

        presets = loaded_yaml.get('presets', {})
        result = {
            "environment": {**presets.get("environment", {}), **loaded_repository.get("environment", {})},
            "shell": {**presets.get("shell", {}), **loaded_repository.get("shell", {})},
            "docker": {**presets.get("docker", {}), **loaded_repository.get("docker", {})},
            "git": {**presets.get("git", {}), **loaded_repository.get("git", {})},
            "php": {**presets.get("php", {}), **loaded_repository.get("php", {})},
            "ruby": {**presets.get("ruby", {}), **loaded_repository.get("ruby", {})},
            "node": {**presets.get("node", {}), **loaded_repository.get("node", {})},
            "services": [],
        }

        # 抽出対象に git リポジトリを上書き
        result['environment']['git_repo'] = repo

        for service in loaded_repository.get('services', []):
            if service is None:
                continue

            env = service.get("environment", {})
            if env is None:
                env = {}

            result['services'].extend([{
                "lang": service.get("lang", ""),
                "env": service.get("env", ""),
                "environment": {**result.get("environment", {}), **env},
                "shell": {**result.get("shell", {}), **service.get("shell", {})},
                "docker": {**result.get("docker", {}), **service.get("docker", {})},
                "git": {**result.get("git", {}), **service.get("git", {})},
                "php": {**result.get("php", {}), **service.get("php", {})},
                "ruby": {**result.get("ruby", {}), **service.get("ruby", {})},
                "node": {**result.get("node", {}), **service.get("node", {})},
            }])

        return result
