# -*- coding: utf-8 -*-
from rez.utils.lint_helper import env, building


name = "mtoa_cryptomatte"

version = "2.0.0b4"

authors = [""]

description = ""

variants = [["platform-linux", "arch-x86_64"]]

plugin_for = ["maya", "mtoa"]

uuid = "repository.mtoa_cryptomatte"


def commands():

    env.ARNOLD_PLUGIN_PATH.append("{root}/bin")
    env.MTOA_TEMPLATES_PATH.append("{root}/ae")
    env.MAYA_CUSTOM_TEMPLATE_PATH.append("{root}/aexml")
