# Zero, One e Few Shots: Técnicas Avançadas em Engenharia de Prompt

## Índice

- [Zero, One e Few Shots: Técnicas Avançadas em Engenharia de Prompt](#zero-one-e-few-shots-técnicas-avançadas-em-engenharia-de-prompt)
  - [Índice](#índice)
  - [Introdução](#introdução)
  - [O que são Zero, One e Few Shots?](#o-que-são-zero-one-e-few-shots)
    - [Definição Técnica](#definição-técnica)
  - [Importância das Técnicas de Shot Learning](#importância-das-técnicas-de-shot-learning)
  - [Estrutura e Componentes](#estrutura-e-componentes)
    - [Exemplo de Estrutura](#exemplo-de-estrutura)
  - [Componentes Básicos:](#componentes-básicos)
  - [Formatação dos Prompts:](#formatação-dos-prompts)
  - [Casos de Uso e Exemplos Práticos](#casos-de-uso-e-exemplos-práticos)
    - [1. Classificação de Texto com Different Shots](#1-classificação-de-texto-com-different-shots)
      - [Zero-shot](#zero-shot)
      - [One-shot](#one-shot)
      - [Few-shot](#few-shot)
    - [2. Tradução com Contexto Cultural](#2-tradução-com-contexto-cultural)
    - [3. Análise de Sentimento Multilingue](#3-análise-de-sentimento-multilingue)
  - [Embasamento Científico e Pesquisas](#embasamento-científico-e-pesquisas)
  - [Melhores Práticas para Implementação](#melhores-práticas-para-implementação)
    - [1. Seleção de Exemplos](#1-seleção-de-exemplos)
    - [2. Estruturação do Contexto](#2-estruturação-do-contexto)
    - [3. Balanceamento de Exemplos](#3-balanceamento-de-exemplos)
    - [4. Validação de Resultados](#4-validação-de-resultados)
    - [5. Adaptação ao Domínio](#5-adaptação-ao-domínio)
    - [6. Gestão de Complexidade](#6-gestão-de-complexidade)
  - [Desafios e Limitações](#desafios-e-limitações)
  - [Conclusão](#conclusão)
  - [Navegação](#navegação)
  - [Tópicos Relacionados](#tópicos-relacionados)
  - [Contribuição](#contribuição)

## Introdução

Zero, One e Few Shots representam técnicas fundamentais na engenharia de prompt que permitem aos modelos de linguagem realizar tarefas com diferentes níveis de contexto e exemplos. Estas abordagens são cruciais para otimizar o desempenho dos modelos em diversos cenários, desde situações sem exemplos prévios até casos com múltiplos exemplos de referência.

## O que são Zero, One e Few Shots?

As técnicas de shot learning referem-se a diferentes abordagens para fornecer contexto e exemplos aos modelos de linguagem:

- **Zero-shot**: O modelo realiza a tarefa sem exemplos prévios
- **One-shot**: Um único exemplo é fornecido como referência
- **Few-shot**: Múltiplos exemplos (geralmente 2-5) são fornecidos

### Definição Técnica

Cada técnica pode ser definida formalmente como:

```markdown
Zero-shot:
Nesta abordagem, fornecemos apenas a descrição da tarefa e os dados de entrada, sem nenhum exemplo. O prompt é estruturado de forma simples:

- Primeiro, apresentamos a descrição da tarefa
- Em seguida, fornecemos os dados de entrada
- Por fim, solicitamos a saída
```

```markdown
One-shot:
Esta técnica utiliza um único exemplo de referência antes de apresentar o novo caso. A estrutura inclui:

- A descrição da tarefa
- Um exemplo completo com entrada e saída
- Os novos dados de entrada para processamento
- Solicitação da nova saída
```

```markdown
Few-shot:
Esta abordagem utiliza múltiplos exemplos (tipicamente de 2 a 5) antes de apresentar o novo caso. O prompt é organizado da seguinte forma:

- Começa com a descrição da tarefa
- Apresenta uma série de exemplos numerados, cada um com sua entrada e saída correspondente
- Após os exemplos, fornece os novos dados de entrada
- Solicita a saída para o novo caso
```

## Importância das Técnicas de Shot Learning

1. **Flexibilidade de Implementação**: Permite adaptar o nível de contexto à complexidade da tarefa
2. **Otimização de Recursos**: Equilibra o uso de tokens com a necessidade de contexto
3. **Melhoria de Precisão**: Fornece exemplos relevantes para guiar o modelo
4. **Adaptabilidade**: Facilita a adaptação do modelo a diferentes domínios e tarefas

## Estrutura e Componentes

Um sistema de shot learning típico consiste em:

1. **Descrição da Tarefa**: Especificação clara do objetivo
2. **Exemplos (quando aplicável)**: Casos de referência bem selecionados
3. **Formato de Entrada/Saída**: Estrutura consistente para dados
4. **Instruções Específicas**: Diretrizes para processamento

### Exemplo de Estrutura

Um sistema de Shot Learning pode ser estruturado da seguinte forma:
## Componentes Básicos:

1. O sistema é inicializado com dois elementos principais:
   - Uma descrição da tarefa a ser realizada
   - Uma coleção de exemplos (opcional, dependendo do tipo de shot)


2. O sistema possui uma função principal que formata os prompts de acordo com três possíveis cenários:

   - Se não houver exemplos, gera um prompt zero-shot
   - Se houver apenas um exemplo, gera um prompt one-shot
   - Se houver múltiplos exemplos, gera um prompt few-shot

## Formatação dos Prompts:
Para Zero-shot:
  - Inclui a descrição da tarefa
  - Apresenta os dados de entrada
  - Solicita a saída

Para One-shot:
  - Começa com a descrição da tarefa
  - Inclui um exemplo com sua entrada e saída
  - Apresenta os novos dados
  - Solicita a nova saída

## Casos de Uso e Exemplos Práticos

### 1. Classificação de Texto com Different Shots

#### Zero-shot
Classifique o seguinte texto como positivo, negativo ou neutro:
Texto: "O novo restaurante tem um ambiente agradável, mas o serviço é muito lento."
Classificação:

#### One-shot
Classifique o texto como positivo, negativo ou neutro.

**Exemplo:**
Texto: "O filme foi incrível, adorei cada minuto!"
Classificação: positivo

**Agora:**
Texto: "O novo restaurante tem um ambiente agradável, mas o serviço é muito lento."
Classificação:

#### Few-shot
Classifique o texto como positivo, negativo ou neutro.

**Exemplo 1:**
Texto: "O filme foi incrível, adorei cada minuto!"
Classificação: positivo

**Exemplo 2:**
Texto: "O atendimento foi péssimo e a comida estava fria."
Classificação: negativo

**Exemplo 3:**
Texto: "O clima hoje está nublado com temperatura amena."
Classificação: neutro

**Agora:**
Texto: "O novo restaurante tem um ambiente agradável, mas o serviço é muito lento."
Classificação:

### 2. Tradução com Contexto Cultural

Traduza o texto mantendo o contexto cultural apropriado.

**Exemplo 1:**
Inglês: "It's raining cats and dogs!"
Português: "Está chovendo canivetes!"
*[mantém a ideia de chuva intensa usando uma expressão local]*

**Exemplo 2:**
Inglês: "Break a leg!"
Português: "Boa sorte!"
*[adapta a expressão idiomática para o equivalente cultural]*

**Exemplo 3:**
Inglês: "I'm feeling under the weather"
Português: "Estou meio indisposto"
*[adapta a expressão mantendo o significado]*

**Agora traduza:**
Inglês: "That's a piece of cake!"
Português:

### 3. Análise de Sentimento Multilingue

Analise o sentimento dos textos em diferentes idiomas.

**Exemplo 1:**
Texto: "I love this product!" [en]
Sentimento: Positivo (Confiança: Alta)

**Exemplo 2:**
Texto: "Я очень разочарован" [ru]
Sentimento: Negativo (Confiança: Alta)

**Exemplo 3:**
Texto: "Das ist ganz okay" [de]
Sentimento: Neutro (Confiança: Média)

**Analise:**
Texto: "Questo ristorante è incredibile!" [it]
Sentimento:

---

## Embasamento Científico e Pesquisas

1. **Zero-Shot Learning**
   - Brown, T., et al. (2020). "Language Models are Few-Shot Learners"
   - [Link](https://arxiv.org/abs/2005.14165)

2. **Few-Shot Learning em NLP**
   - Gao, T., et al. (2021). "Making Pre-trained Language Models Better Few-shot Learners"
   - [Link](https://arxiv.org/abs/2012.15723)

## Melhores Práticas para Implementação

### 1. Seleção de Exemplos
- Escolha exemplos representativos e diversos
- Mantenha consistência no formato
- Evite exemplos ambíguos

### 2. Estruturação do Contexto
- Forneça instruções claras e específicas
- Mantenha um formato consistente
- Use marcadores claros entre exemplos

### 3. Balanceamento de Exemplos
- Distribua exemplos equilibradamente entre classes/casos
- Varie a complexidade dos exemplos
- Inclua casos edge quando relevante

### 4. Validação de Resultados
- Implemente verificações de qualidade
- Monitore a consistência das respostas
- Estabeleça métricas de avaliação

### 5. Adaptação ao Domínio
- Personalize exemplos para o domínio específico
- Considere terminologia especializada
- Adapte o nível de detalhe ao contexto

### 6. Gestão de Complexidade
- Equilibre o número de exemplos com a complexidade da tarefa
- Considere o limite de tokens do modelo
- Otimize o uso de contexto

## Desafios e Limitações

1. **Limitações de Contexto**
   - Restrições no número de tokens
   - Balanceamento entre quantidade e qualidade de exemplos

2. **Variabilidade de Desempenho**
   - Resultados podem variar com diferentes exemplos
   - Sensibilidade à ordem dos exemplos

3. **Complexidade de Implementação**
   - Necessidade de seleção cuidadosa de exemplos
   - Manutenção de consistência entre exemplos

4. **Escalabilidade**
   - Dificuldade em manter conjuntos grandes de exemplos
   - Custo computacional em few-shot learning

5. **Transferência de Conhecimento**
   - Limitações na generalização entre domínios
   - Dependência da qualidade dos exemplos

## Conclusão

As técnicas de Zero, One e Few Shots representam ferramentas fundamentais na engenharia de prompt moderna. Cada abordagem oferece vantagens específicas e pode ser aplicada estrategicamente dependendo do contexto, recursos disponíveis e complexidade da tarefa.

A escolha entre as diferentes técnicas deve ser baseada em uma análise cuidadosa dos requisitos do projeto, considerando fatores como disponibilidade de exemplos, restrições de recursos e necessidade de precisão. A implementação bem-sucedida requer atenção aos detalhes, compreensão profunda do domínio e aplicação consistente das melhores práticas.

## Navegação

- [Voltar: Engenharia de Prompt](..)
- [Tree of Thought](./tree_of_thought.md)
- [Prompt Chaining](./prompt_chaining.md)

## Tópicos Relacionados

- [Raciocínio em IA](../../assets/utils/NOT_FOUND.md)
- [Aprendizado por Transferência](../../assets/utils/NOT_FOUND.md)

## Contribuição

Encontrou um erro ou tem uma sugestão? Por favor, abra uma [issue](https://github.com/EYLatamSouth/beyondlabs-prompt-engineering/issues) ou envie um [pull request](https://github.com/EYLatamSouth/beyondlabs-prompt-engineering/pulls).

---

<div align="center">
  <a href="#índice">Voltar ao Índice</a> |
  <a href="https://github.com/EYLatamSouth/beyondlabs-prompt-engineering">Sobre este Projeto</a> |
  <a href="https://github.com/EYLatamSouth/beyondlabs-prompt-engineering/blob/main/LICENSE">Licença</a>
</div>