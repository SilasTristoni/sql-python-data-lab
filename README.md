# 🧪 SQL Python Data Lab

<p align="center">
  <strong>Laboratório prático de SQL, Python e análise de dados</strong><br/>
  Projeto criado para treinar consultas, automações, ETL simples, análise de dados e boas práticas com GitHub.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQL-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-em%20evolu%C3%A7%C3%A3o-7D3C98?style=for-the-badge" />
</p>

---

## 📌 Sobre o projeto

O **SQL Python Data Lab** é um projeto inicial para praticar análise de dados com Python e SQL.

A ideia é simular um pequeno fluxo de dados:

1. carregar uma base CSV;
2. gravar os dados em um banco SQLite;
3. executar consultas SQL;
4. calcular indicadores com Python;
5. evoluir o projeto com novas análises, dashboards e automações.

Este repositório também foi pensado para ser evoluído com commits e pull requests pequenos, úteis e bem documentados.

---

## 🎯 Objetivos

- Praticar **Python** aplicado a dados.
- Criar consultas **SQL** para análise.
- Organizar um projeto com estrutura profissional.
- Treinar versionamento com **Git e GitHub**.
- Evoluir o projeto com pequenas melhorias contínuas.
- Criar material apresentável para portfólio.

---

## 🧱 Estrutura

```text
sql-python-data-lab/
├── data/
│   └── sample_sales.csv
├── docs/
│   └── roadmap.md
├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_basic_queries.sql
│   └── 03_kpis.sql
├── src/
│   ├── __init__.py
│   ├── analysis.py
│   ├── database.py
│   └── main.py
├── tests/
│   └── test_analysis.py
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── ISSUE_TEMPLATE/
│       └── melhoria.md
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🛠️ Tecnologias

- **Python**
- **SQL**
- **SQLite**
- **Git**
- **GitHub**

---

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/sql-python-data-lab.git
cd sql-python-data-lab
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python -m src.main
```

Veja um exemplo de saída em [`docs/exemplo-execucao.md`](docs/exemplo-execucao.md).

O projeto irá:

- criar o banco SQLite em `data/lab.db`;
- carregar os dados de `data/sample_sales.csv`;
- calcular indicadores básicos;
- exibir um resumo no terminal;
- gerar o relatório CSV em `reports/summary.csv`.

---

## 📊 Indicadores iniciais

O projeto calcula inicialmente:

- total de vendas;
- quantidade de pedidos;
- ticket médio;
- produto mais vendido;
- faturamento por categoria.

---

## 🧪 Testes

Execute os testes com:

```bash
pytest
```

## Testes automatizados

O projeto possui um workflow do GitHub Actions em `.github/workflows/tests.yml`.
Ele executa os testes Python automaticamente em eventos de `push` e `pull_request`, usando Python 3.11.

---

## 🚀 Ideias de evolução

Algumas melhorias planejadas:

- adicionar análise por mês;
- criar ranking de clientes;
- gerar gráficos com Matplotlib;
- exportar relatórios em CSV;
- criar dashboard simples;
- adicionar consultas SQL avançadas;
- incluir documentação dos indicadores;
- criar pipeline ETL com etapas separadas.

Veja mais em [`docs/roadmap.md`](docs/roadmap.md).

---

## 📌 Sugestão de evolução por Pull Requests

Para treinar GitHub de forma organizada, evolua o projeto em PRs pequenos:

1. `docs: melhora descrição do projeto`
2. `sql: adiciona consultas de ranking`
3. `python: adiciona cálculo de ticket médio por categoria`
4. `tests: adiciona testes para indicadores`
5. `docs: adiciona exemplos de execução`
6. `python: exporta resumo para csv`
7. `sql: adiciona análise mensal`
8. `python: adiciona gráficos com matplotlib`

---

## 👨🏻‍💻 Autor

Desenvolvido por **Silas Tristoni** como projeto de estudo, portfólio e prática com SQL, Python e GitHub.

---

<p align="center">
  <em>Um laboratório simples, evoluindo uma análise por vez.</em>
</p>
