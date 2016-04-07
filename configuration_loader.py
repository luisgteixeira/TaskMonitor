
class ConfigurationLoader(object):
    """
    Classe ConfigurationLoader. Carrega os dados de configuracao necessarios
    para a execucao do script.
    """
    def __init__(self):
        super(ConfigurationLoader, self).__init__()
        self.configurations = {}


    def load_configurations(self):
        """Carrega dados de configuracao."""
        try:
            # Abre o arquivo de configuracoes
            configuration_file = open('configuration.txt')
            # Le as configuracoes em cada linha (key=value)
            for line in configuration_file:
                info = line.replace('\n','').split('=')
                # info[0] -> chave, info[1] -> valor
                self.configurations[info[0]] = info[1]
            # Fecha o arquivo de configuracoes
            configuration_file.close()
        except Exception as e:
            # Caso ocorra um problema na leitura do arquivo de configuracoes
            # uma alerta de erro e exibido, seguido da excessao ocorrida
            # e o programa e encerrado.
            print("ERRO: Houve um erro na leitura do arquivo de configuracoes.")
            print("")
            print(e)
            exit(1)


    def get_configuration(self, configuration_key):
        """
        Retorna o valor da configuracao para a chave requisitada. Recebe como
        parametro a chave de configuracao requisitada.
        """
        # Verifica se a configuracao solicitada e valida
        if configuration_key in self.configurations.keys():
            # Retorna a configuracao solicitada
            return self.configurations[configuration]
