# 📊 API de Grafos

Este projeto é uma biblioteca em Python voltada para a criação, manipulação e execução de algoritmos clássicos em Teoria dos Grafos (como BFS, DFS, Componentes Conectados e Fecho Transitivo). A arquitetura foi projetada de forma modular, separando a estrutura de dados (Lista de Adjacência e Matriz de Adjacência) das implementações dos algoritmos.

---

## 🚀 Como Executar os Arquivos (Scripts e Testes)

Como o projeto utiliza uma estrutura de pacotes interdependentes (onde os scripts de teste importam módulos que estão em outras pastas), **você nunca deve executar os arquivos diretamente** com:

```bash
python caminho/do/arquivo.py
```

Para que o Python resolva corretamente os imports internos do projeto, execute os scripts como **módulos**, sempre a partir da raiz do projeto.

### 🛠️ Passo a Passo

1. Abra o terminal e navegue até a pasta raiz do projeto:

```bash
cd /caminho/para/API-DE-GRAFOS
```

2. Execute o módulo desejado utilizando a flag `-m`.

### ▶️ Executar BFS

```bash
python -m teste.teste_bfs
```

### ▶️ Executar DFS

```bash
python -m teste.teste_dfs
```

### ▶️ Executar Componentes Conectados

```bash
python -m teste.teste_componentes
```

### ▶️ Executar Fecho Transitivo

```bash
python -m teste.teste_fecho
```

---

## ⚠️ Erros Comuns

### 1. ModuleNotFoundError: No module named 'grafo_estrutura'

**Por que acontece?**

Você tentou executar o script dentro da pasta `teste/` ou executou o arquivo diretamente.

Exemplo incorreto:

```bash
python teste_bfs.py
```

**Como corrigir?**

Volte para a raiz do projeto e execute utilizando `-m`:

```bash
python -m teste.teste_bfs
```

---

### 2. ValueError: Empty module name

**Por que acontece?**

Você colocou a extensão `.py` no comando.

Exemplo incorreto:

```bash
python -m teste.teste_bfs.py
```

**Como corrigir?**

Remova a extensão `.py`:

```bash
python -m teste.teste_bfs
```

---

## 📁 Estrutura do Projeto

```text
API-DE-GRAFOS/
│
├── grafo_estrutura/
│   ├── Grafo.py
│   ├── GrafoLista.py
│   ├── GrafoMatriz.py
│   └── _GrafoFactory.py
│
├── algoritmos/
│   ├── bfs.py
│   ├── dfs.py
│   ├── componente_conexa.py
│   └── fecho_transitivo.py
│
├── teste/
│   ├── teste_bfs.py
│   ├── teste_dfs.py
│   ├── teste_componente_conexa.py
│   └── teste_fecho.py
│
└── README.md
```

---

## ✨ Funcionalidades

- Representação por Lista de Adjacência
- Representação por Matriz de Adjacência
- Grafos direcionados e não direcionados
- Grafos ponderados e não ponderados
- Busca em Largura (BFS)
- Busca em Profundidade (DFS)
- Componentes Conectados
- Fecho Transitivo
- Arquitetura modular baseada em abstrações
- Factory para criação de grafos

---

## 📚 Referências

Os algoritmos implementados seguem as definições clássicas apresentadas em:

- Cormen, Thomas H.; Leiserson, Charles E.; Rivest, Ronald L.; Stein, Clifford.
  **Introduction to Algorithms (CLRS)**.

---

## 🎓 Objetivo

Este projeto foi desenvolvido para fins acadêmicos, visando o estudo prático de Estruturas de Dados, Projeto Orientado a Objetos e Algoritmos em Grafos.

Além de servir como ferramenta de aprendizado, a biblioteca foi projetada para permitir a expansão futura com novos algoritmos e representações de grafos.

---

Desenvolvido para estudos e experimentação em Teoria dos Grafos. 🚀