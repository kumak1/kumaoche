import unittest
from kumaoche.service import Git
from kumaoche.config import GitConfig, ConfigParser
from ..exec_env import MocEnv
from ..config import StubConfig


class TestGit(unittest.TestCase):
    def test_run(self):
        config = StubConfig.find('test_role')
        print(config.git.repo_dir)

        Git(MocEnv, config)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
