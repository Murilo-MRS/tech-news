# Projeto Tech News

Projeto realizado durante módulo de Ciência da Computação do curso de desenvolvimento web da Trybe.

<details>
  <summary><strong>👨‍💻 O que foi feito</strong></summary></br>

Neste projeto foi desenvolvido uma aplicação para raspagem e manipulação de dados de um site de notícias sobre tecnologia. Esses dados são armazenados no banco de dados MongoDB para serem persistidos.

A raspagem de dados tem sido muito útil em trabalhos jornalísticos, fornecendo dados para embasar matérias, mas também pode ser útil para outros fins, como comparar preços de produtos com a concorrência; automatização de processos maçantes como buscar artigos científicos em bases acadêmicas; recuperação de documentos em sites jurídicos; analisar perfis de redes sociais; recuperar dados públicos do governo e muitos outros lugares.

</details>
<details>
  <summary><strong>🛼 Como rodar o projeto</strong></summary></br>
  
  Configurações mínimas para execução do projeto:

- Docker
- Docker-compose versão >=1.29.2

  **Com Docker:**

  **:warning: Antes de começar, seu docker-compose precisa estar na versão 1.29 ou superior. [Veja aqui](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-pt) ou [na documentação](https://docs.docker.com/compose/install/) como instalá-lo. No primeiro artigo, você pode substituir onde está com `1.26.0` por `1.29.2`.**

- `docker-compose up -d mongodb` para iniciar o container do banco de dados;
- `python3 -m venv .venv && source .venv/bin/activate`
- `python3 -m pip install -r dev-requirements.txt`
- `tech-news-analyzer` para executar o script.

O menu exibido no terminal escolha primeiro a opção 0 para popular o banco de dados e depois escolha uma das opções de 1 a 4 para realizar as consultas:

```bash
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
```

</details>

<details>
  <summary><strong>📄 Tecnologias utilizadas</strong></summary><br />
  
- `Python`
- `Pytest`
- `Pymongo`
- `parsel`
- `BeatifulSoup`

</details>
<details>
  <summary><strong>🚵 Habilidades</strong></summary><br />

- Utilizar o terminal interativo do Python
- Escrever seus próprios módulos e importá-los em outros códigos
- Aplicar técnicas de raspagem de dados
- Extrair dados de conteúdo HTML
- Armazenar os dados obtidos em um banco de dados

</details>

<details>
  <summary><strong>👥 Devs responsáveis</strong></summary>

- [@Murilo-MRS](https://github.com/Murilo-MRS)

</details>

<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto.
É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->