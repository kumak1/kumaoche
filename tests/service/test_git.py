import unittest
from kumaoche.service import Git
from ..exec_env import MocEnv
from ..config import StubConfig


class TestGit(unittest.TestCase):
    def setUp(self):
        self.config = StubConfig.find('variable_assign_test_role')
        self.env = MocEnv(self.config.variable)
        self.git = Git(self.env, self.config.git)
        self.src_text = 'git_host:{git_host},git_org:{git_org},git_repo:{git_repo},db_host:{db_host},db_port:{db_port},db_user:{db_user},db_database:{db_database}'
        self.dst_text = 'git_host:github.com,git_org:kumak1,git_repo:kumaoche,db_host:db,db_port:3306,db_user:root,db_database:db'

    def test_run(self):
        self.assertEqual(f"work_dir:repo {self.dst_text},command:test_command", self.git.run("test_command"))
        self.assertEqual(f"work_dir:repo {self.dst_text},command:{self.dst_text}", self.git.run(self.src_text))

    def test_setup(self):
        self.assertEqual(f"work_dir:,command:setup {self.dst_text}", self.git.setup())

    def test_update(self):
        self.assertEqual(f"work_dir:,command:update {self.dst_text}", self.git.update())


if __name__ == '__main__':
    unittest.main()
