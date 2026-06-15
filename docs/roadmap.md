# Roadmap do SQL Python Data Lab

Este roadmap organiza a evolução do projeto em fases simples, com entregas pequenas e verificáveis. A ideia é manter um histórico claro para estudo, prática com GitHub e apresentação em portfólio.

Recomendação: crie uma branch e um Pull Request para cada melhoria relevante.

## Fundamentos

- [x] Estruturar pastas do projeto: separar `data`, `docs`, `sql`, `src` e `tests`.
- [x] Criar base CSV inicial: usar `data/sample_sales.csv` como fonte de dados para as análises.
- [x] Criar fluxo principal de execução: carregar dados, gravar no SQLite e exibir indicadores no terminal.
- [x] Documentar execução do projeto: incluir comando principal e exemplo em `docs/exemplo-execucao.md`.
- [ ] Melhorar descrição do README: destacar objetivo, contexto de negócio e aprendizados demonstrados.

## SQL

- [x] Criar consultas básicas: listar vendas, calcular faturamento e agrupar dados por categoria.
- [x] Criar KPIs em SQL: calcular ticket médio, faturamento mensal e rankings iniciais.
- [x] Criar ranking de clientes: consultar pedidos, faturamento total e ticket médio em `sql/04_customer_ranking.sql`.
- [x] Criar análise mensal de faturamento: agrupar pedidos por mês em `sql/05_monthly_revenue.sql`.
- [ ] Criar ranking de produtos: identificar produtos com maior volume vendido e maior faturamento.
- [ ] Criar consultas com `JOIN`: evoluir o modelo para mais de uma tabela e praticar relacionamentos.

## Python

- [x] Calcular indicadores principais: total de pedidos, faturamento total, ticket médio e produto mais vendido.
- [x] Criar ranking de clientes em Python: ordenar clientes por faturamento com total de pedidos e ticket médio.
- [x] Exibir Top 3 clientes no terminal: tornar a saída da execução mais útil para análise rápida.
- [ ] Criar função para análise mensal: replicar em Python a análise mensal já disponível em SQL.
- [ ] Melhorar tratamento de erros: validar ausência de CSV, colunas inválidas e dados inconsistentes.
- [ ] Adicionar logs simples: registrar etapas do pipeline de carga, cálculo e exportação.

## Relatórios

- [x] Exportar resumo em CSV: gerar `reports/summary.csv` com os principais indicadores.
- [ ] Criar relatório em Markdown: consolidar indicadores, rankings e observações em um arquivo legível.
- [ ] Exportar ranking de clientes: salvar o ranking completo em `reports/customer_ranking.csv`.
- [ ] Gerar gráficos básicos: criar visualizações de faturamento por categoria e por mês.
- [ ] Organizar pasta `reports`: separar saídas tabulares, gráficos e relatórios finais.

## Qualidade

- [x] Criar testes para indicadores: validar cálculos principais em `tests/test_analysis.py`.
- [x] Criar testes para ranking de clientes: validar ordenação, pedidos, faturamento e ticket médio.
- [x] Criar teste para exportação CSV: validar geração do arquivo de resumo.
- [ ] Aumentar cobertura de testes: incluir cenários vazios, valores repetidos e múltiplos itens por pedido.
- [ ] Adicionar GitHub Actions: executar testes automaticamente a cada Pull Request.
- [ ] Padronizar formatação: configurar Ruff ou Black para manter estilo consistente.

## Próximos passos para portfólio

- [ ] Criar seção de resultados no README: mostrar exemplos de indicadores e arquivos gerados.
- [ ] Adicionar prints da execução: incluir imagens do terminal, CSV exportado ou gráficos.
- [ ] Explicar decisões técnicas: documentar por que o projeto usa SQLite, CSV e funções separadas.
- [ ] Criar um estudo de caso curto: apresentar problema, abordagem, resultados e próximos passos.
- [ ] Revisar linguagem final: deixar o projeto claro para recrutadores, pares técnicos e visitantes do GitHub.
