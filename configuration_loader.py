

class ConfigurationLoader(object):
    """docstring for ConfigurationLoader"""
    def __init__(self):
        super(ConfigurationLoader, self).__init__()
        self.configurations = {}


    def load_configurations(self):
        """"""
        # Abre o arquivo de configuracoes
        configuration_file = open('configuration.txt')
        # Le as configuracoes em cada linha (key=value)
        for line in configuration_file:
            info = line.split('=').replace('\n','')
            # info[0] -> chave, info[1] = valor
            self.configurations[info[0]] = info[1]
        # Fecha o arquivo de configuracoes
        configuration_file.close()


    def get_configuration(self, configuration):
        """"""
        # Verifica se a configuracao solicitada e valida
        if configuration in self.configurations.keys():
            # Retorna a configuracao solicitada
            return self.configurations[configuration]
