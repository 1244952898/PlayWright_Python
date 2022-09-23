import yaml


class ReadYaml:
    @staticmethod
    def readyamlfile(path, encode="utf-8"):
        with open(path, "r",encoding=encode) as f:
            source = yaml.safe_load(f)
            return source

# print(dir(ReadYaml))
# print(ReadYaml.readyamlfile("test.yaml"))