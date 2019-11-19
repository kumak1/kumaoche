# -*- coding: utf-8 -*-

from invoke import task
from kumaoche import Container
import os

@task
def test(c):
    print(os.getcwd())
    for role in Container.all_role_names():
        print(role)

    print('end')
