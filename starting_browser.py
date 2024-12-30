from selenium import webdriver
from selenium.common.exceptions import * #importando os tipos de exceções
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait #importando a espera
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as condicao_esperada
from webdriver_manager.chrome import ChromeDriverManager


def start_driver(address_driver, address_download, background=False, use_default_download=False):
    """
    Inicializa o driver do navegador Chrome com opções personalizadas.
    
    Parâmetros:
    - address_driver: Caminho para o driver do Chrome.
    - address_download: Caminho para salvar os arquivos baixados.
    - background: Se True, o navegador será iniciado no modo headless.
    - use_default_download: Se True, utiliza o diretório padrão do navegador para downloads.
    """
   
    chrome_options = Options()  # Cria o objeto de configuração para o Chrome.

    # Define argumentos com base no modo (headless ou normal).
    if background:
        arguments = [
            '--lang=pt-BR', '--headless', '--disable-infobars',
            '--no-sandbox', '--disable-gpu', '--start-maximized'
        ]
    else:
        arguments = ['--lang=pt-BR', '--start-maximized', '--disable-infobars']
        """
        Para abrir o navegador utilizaando um perfil do CHROME já existente, utilize o argumento: f"user-data-dir={chrome_profile_path}"
        
        #Definição do Path do perfil do Chrome
        chrome_profile_path = "C:\\Users\\92028887\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
        
        arguments = ['--lang=pt-BR', '--start-maximized', '--disable-infobars',f"user-data-dir={chrome_profile_path}"]

        """

    # Adiciona os argumentos ao objeto chrome_options.
    for argument in arguments:
        chrome_options.add_argument(argument)

    # Configura preferências do navegador.
    prefs = {
        'profile.default_content_setting_values.notifications': 2,  # Bloqueia notificações.
        'profile.default_content_setting_values.automatic_downloads': 1,  # Permite múltiplos downloads automáticos.
        'plugins.always_open_pdf_externally': True  # Sempre baixa PDFs em vez de abri-los.
    }

    if not use_default_download:  # Se NÃO usar o diretório padrão, configura um caminho personalizado.
        prefs.update({
            'download.default_directory': address_download,  # Define a pasta padrão de downloads.
            'savefile.default_directory': address_download,  # Alternativa para compatibilidade.
            'download.directory_upgrade': True,  # Atualiza automaticamente a pasta de download.
            'download.prompt_for_download': False  # Não exibe caixa de diálogo para downloads.
        })

    chrome_options.add_experimental_option('prefs', prefs)
    
    # Tenta iniciar o driver com configurações automáticas.
    try:
        driver = webdriver.Chrome(options=chrome_options)

    except:  # Caso falhe, tenta usar o caminho manual especificado.
        driver = webdriver.Chrome(service=ChromeService(address_driver), options=chrome_options)
      
    
    # Configura espera explícita para interações com elementos.
    wait = WebDriverWait(
        driver,
        30,  # Tempo máximo de espera (em segundos).
        poll_frequency=1,  # Frequência de verificação (em segundos).
        ignored_exceptions=[
            NoSuchElementException,  # Ignora exceção se o elemento não for encontrado.
            ElementNotVisibleException,  # Ignora exceção se o elemento não for visível.
            ElementNotSelectableException,  # Ignora exceção se o elemento não for selecionável.
        ]
    )
    return driver,wait  # Retorna o driver e o objeto de espera.


driver, wait = start_driver('','')

driver.get("https://www.google.com")

