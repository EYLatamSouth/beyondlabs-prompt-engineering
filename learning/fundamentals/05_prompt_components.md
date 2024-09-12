# Componentes de Prompts

## Índice
- [Introdução](#introdução)
- [Componentes Principais](#componentes-principais)
  - [1. Contexto](#1-contexto)
  - [2. Instrução](#2-instrução)
  - [3. Entrada](#3-entrada)
  - [4. Indicador de Saída](#4-indicador-de-saída)
- [Componentes Avançados](#componentes-avançados)
  - [5. Exemplos (Few-shot)](#5-exemplos-few-shot)
  - [6. Persona](#6-persona)
  - [7. Formato de Saída](#7-formato-de-saída)
- [Exemplo Prático Detalhado](#exemplo-prático-detalhado)
- [Melhores Práticas](#melhores-práticas)
- [Navegação](#navegação)

## Introdução

Os componentes de prompts são os elementos fundamentais que compõem uma instrução eficaz para modelos de linguagem. Compreender e utilizar corretamente esses componentes é crucial para obter respostas precisas e relevantes. Neste guia, exploraremos os principais componentes de um prompt e como combiná-los para criar instruções poderosas.

## Componentes Principais

### 1. Contexto

O contexto fornece informações de fundo necessárias para o modelo entender o cenário ou a situação em que a tarefa está inserida.

**Exemplo:**
```
Em um mundo onde a tecnologia avançou rapidamente, carros voadores se tornaram comuns.
```

### 2. Instrução

A instrução é a parte do prompt que diz ao modelo exatamente o que você quer que ele faça.

**Exemplo:**
```
Descreva como seria uma viagem de rotina para o trabalho usando um carro voador.
```

### 3. Entrada

A entrada é a informação específica sobre a qual você quer que o modelo opere ou responda.

**Exemplo:**
```
Distância: 50 km
Hora do dia: 8:00 AM
Clima: Ensolarado
```

### 4. Indicador de Saída

O indicador de saída sinaliza onde o modelo deve começar sua resposta, frequentemente usado para formatar a saída de uma maneira específica.

**Exemplo:**
```
Descrição da viagem:
```

## Componentes Avançados

### 5. Exemplos (Few-shot)

Exemplos demonstram o tipo de resposta esperada, ajudando o modelo a entender melhor o padrão desejado.

### 6. Persona

A persona define o "papel" que o modelo deve assumir ao responder, influenciando o tom e o estilo da resposta.

### 7. Formato de Saída

Especifica como a resposta deve ser estruturada, como em forma de lista, parágrafo, diálogo, etc.

## Exemplo Prático Detalhado

Vamos combinar todos esses componentes em um prompt completo e bem estruturado:

```
Contexto: Em 2050, carros voadores se tornaram o principal meio de transporte nas grandes cidades. Você é um especialista em planejamento de tráfego aéreo urbano.

Instrução: Descreva uma viagem típica de casa para o trabalho usando um carro voador, abordando os desafios e benefícios deste modo de transporte.

Entrada:
- Distância: 50 km
- Hora de partida: 8:00 AM
- Clima: Ensolarado
- Tráfego aéreo: Moderado

Persona: Você é um entusiasta da tecnologia que aprecia eficiência e inovação.

Exemplos:
1. "O percurso de 30 km levou apenas 15 minutos, evitando completamente o congestionamento terrestre."
2. "A decolagem vertical da minha garagem economizou tempo valioso no início da viagem."

Formato de Saída: Forneça sua resposta em forma de um relato em primeira pessoa, dividido em três parágrafos: preparação, viagem e chegada.

Indicador de Saída:
Relato da viagem:
```

Este prompt combina todos os componentes discutidos, proporcionando ao modelo uma estrutura clara e informações detalhadas para gerar uma resposta rica e relevante.

## Melhores Práticas

1. **Clareza**: Seja específico e direto em suas instruções.
2. **Contextualização**: Forneça contexto suficiente, mas evite informações irrelevantes.
3. **Estruturação**: Use formatação clara para separar diferentes componentes do prompt.
4. **Exemplos**: Quando necessário, inclua exemplos para guiar o estilo e conteúdo da resposta.
5. **Iteração**: Refine seus prompts com base nos resultados obtidos.


Para uma compreensão visual dos componentes do prompt, considere adicionar uma imagem que ilustre como cada elemento se encaixa no prompt completo. Isso poderia ser representado como um diagrama de fluxo ou uma estrutura em camadas, mostrando como os diferentes componentes se complementam para formar um prompt eficaz.

## Navegação
- [Anterior: Contexto e Especificidade](04_context_and_specificity.md)
- [Próximo: Erros comuns](06_common_pitfalls.md)
- [Voltar para Fundamentos](.)

## Tópicos Relacionados
- [Introdução à Engenharia de Prompt](01_introduction_to_prompt_engineering.md)
- [Estrutura Básica de Prompts](02_basic_prompt_structure.md)
- [Tipos de Prompts](03_types_of_prompts.md)
- [Contexto e Especificidade](04_context_and_specificity.md)
- [Erros comuns em Prompts](06_common_pitfalls.md)
- [Testes e Iteração de Prompt](../../assets/utils/NOT_FOUND.md)
- [Considerações Éticas em Engenharia de Prompt](../../assets/utils/NOT_FOUND.md)

## Contribuição

Encontrou um erro ou tem uma sugestão? Por favor, abra uma [issue](../../assets/utils/NOT_FOUND.md) ou envie um [pull request](../../assets/utils/NOT_FOUND.md).

---

<div align="center">
  <a href="#índice">Voltar ao Índice</a> |
  <a href="https://github.com/EYLatamSouth/beyondlabs-prompt-engineering">Sobre este Projeto</a> | 
  <a href="https://github.com/EYLatamSouth/beyondlabs-prompt-engineering/blob/main/LICENSE">Licença</a>
</div>