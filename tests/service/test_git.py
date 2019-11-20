import unittest
from kumaoche.service import Git
from ..exec_env import MocEnv
from ..config import StubConfig


class TestGit(unittest.TestCase):
    def test_run(self):
        config = StubConfig.find('test_role')
        git = Git(MocEnv(config.variable), config.git)

        print(git.setup())
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
