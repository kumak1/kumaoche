# -*- coding: utf-8 -*-

from invoke import task
from kumaoche import Container


@task
def test(c):
    for role in Container.all_repository_names():
        print(role)

    print('end')
