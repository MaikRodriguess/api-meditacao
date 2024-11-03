FROM python:3.12

# Instala o Poetry
RUN pip install poetry

# Copia todos os arquivos para o contêiner
COPY . /src

# Define o diretório de trabalho
WORKDIR /src

# Instala as dependências do projeto usando o Poetry
RUN poetry install

# Expõe a porta que o Flask usará
EXPOSE 5000

# Define o entrypoint para iniciar o servidor Flask
ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=5000"]
