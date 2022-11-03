from configparser import ConfigParser
from scj.code import initialization


def get_system_ini(key):
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    if conf.has_option("path_config", key):
        return conf.get("path_config", key)
    elif conf.has_option("processing", key):
        return conf.get("processing", key)
    return ""


if __name__ == '__main__':
    print(get_system_ini("video"))
