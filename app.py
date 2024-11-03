from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

app = Flask(__name__)

URL ="https://mais.cpb.com.br/?post_type=meditacao&p=63166"

@app.route('/extract_text')
def extract_text():
    options = Options()
    options.add_argument("--headless")
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        navegador.get(URL)

        # Extrai data da meditacao
        diaMesMeditacao = navegador.find_element(By.CLASS_NAME, 'diaMesMeditacao').text

        # Extrai dia da meditacao
        diaSemanaMeditacao = navegador.find_element(By.CLASS_NAME, 'diaSemanaMeditacao').text

        # Extrair o título
        titulo = navegador.find_element(By.CLASS_NAME, 'titleMeditacao').text

        # Extrair verso biblico
        versoBiblico = navegador.find_element(By.CLASS_NAME, 'versoBiblico').text

        # Extrair todos os parágrafos
        paragrafos = navegador.find_elements(By.TAG_NAME, 'p')
        
        # Juntar todos os parágrafos em uma única string
        textoPrincipal = "\n\n".join([p.text for p in paragrafos if p.text.strip()])

        return jsonify({
            "diaMesMeditacao": diaMesMeditacao,
            "diaSemanaMeditacao": diaSemanaMeditacao,
            "titulo": titulo,
            "versoBiblico": versoBiblico,
            "textoPrincipal": textoPrincipal
        })
    finally:
        navegador.quit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)