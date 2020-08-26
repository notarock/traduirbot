#!/usr/bin/env python3
from environs import Env


class Config:
    __instance = None
    env = None

    @staticmethod
    def get_instance():
        """
        Static access method.
        """
        if Config.__instance is None:
            Config()
        return Config.__instance

    def __init__(self):
        """
        Virtually private constructor.
        """
        if Config.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Config.__instance = self
            Config.env = Env()
            Config.env.read_env()

    def get_config(self, config_key):
        return self.env(config_key) or ''
