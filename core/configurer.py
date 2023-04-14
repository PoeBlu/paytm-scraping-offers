import os
import configparser


class Configurer:
    def __init__(self, filename="config.ini"):
        self.abs_filename = self.get_abs_filename(filename)
        self.config = configparser.ConfigParser()
        self.config.read(self.abs_filename)
        self.sections = self.config.sections()

    @staticmethod
    def get_abs_filename(filename):
        return os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            os.path.pardir,
                                            filename))

    @staticmethod
    def get_abs_parent_directory():
        return os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            os.path.pardir))

    def get_configuration(self, key, section="DATABASE"):
        try:
            value = self.config[section][key]
        except KeyError:
            print(f"Key FOR '{key}' is not provided in the config.ini file.")
            return False
        if value:
            return value
        print(f"Something went wrong with {key} key.")
        return False

    def write_configuration(self, key, value, section="DATABASE"):
        self.config.set(section, key, value)
        with open(self.abs_filename, 'w') as configfile:
            self.config.write(configfile)
            configfile.close()
        return value


config = Configurer()
