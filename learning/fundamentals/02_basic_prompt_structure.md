# Estrutura Básica de Prompts

## Índice
- [Estrutura Básica de Prompts](#estrutura-básica-de-prompts)
  - [Índice](#índice)
  - [Componentes de um Prompt](#componentes-de-um-prompt)
    - [1. Contexto](#1-contexto)
    - [2. Instrução](#2-instrução)
    - [3. Entrada](#3-entrada)
    - [4. Formato de Saída](#4-formato-de-saída)
  - [Combinando Componentes](#combinando-componentes)
  - [Fluxo de Criação de Prompts](#fluxo-de-criação-de-prompts)
  - [Conclusão](#conclusão)
  - [Navegação](#navegação)
  - [Tópicos Relacionados](#tópicos-relacionados)
  - [Contribuição](#contribuição)

A estrutura de um prompt eficaz é fundamental para obter os melhores resultados de um modelo de linguagem. Neste capítulo, exploraremos os componentes essenciais de um prompt bem estruturado e como combiná-los para máxima eficácia.

## Componentes de um Prompt

1. **Contexto**
2. **Instrução**
3. **Entrada**
4. **Formato de Saída**

Vamos explorar cada um desses componentes em detalhes.

### 1. Contexto

O contexto fornece informações de fundo e estabelece o "cenário" para o modelo. Isso pode incluir:

- Papel ou persona que o modelo deve assumir
- Informações relevantes para a tarefa

**Técnica: Role Prompting**
```
PROMPT:
Você é um historiador especializado em civilizações antigas. 
{instrução}
```

### 2. Instrução

A instrução é o coração do prompt, onde você especifica exatamente o que deseja que o modelo faça.

**Técnica: Task Decomposition**
```
PROMPT:
Analise o seguinte texto sobre a civilização maia:
1. Identifique as principais características da sua arquitetura
2. Liste três de suas maiores realizações
3. Explique brevemente seu sistema de escrita
{entrada}
```

### 3. Entrada

A entrada é o material específico sobre o qual o modelo deve operar, como um texto para análise, dados para processar, ou um problema para resolver.

**Técnica: Few-Shot Learning**
```
PROMPT:
Classifique os seguintes comentários como positivos ou negativos:

Exemplo 1:
Entrada: "Este produto excedeu minhas expectativas!"
Saída: Positivo

Exemplo 2:
Entrada: "Não recomendo, qualidade muito baixa."
Saída: Negativo

Agora, classifique:
{entrada}
```

### 4. Formato de Saída

Especificar o formato de saída ajuda a garantir que a resposta do modelo seja estruturada da maneira que você precisa.

**Técnica: Output Structuring**
```
PROMPT:
{instrução}
{entrada}

Formate sua resposta como um objeto JSON com as seguintes chaves:
- "resumo": Uma breve síntese em 50 palavras
- "pontos_principais": Uma lista de 3 pontos-chave
- "conclusao": Uma frase de conclusão
```

## Combinando Componentes

Agora, vamos ver como podemos combinar esses componentes em um prompt completo e bem estruturado:

**Exemplo: Análise de Texto Histórico**

```xml
<prompt>
  <contexto>
    <papel>Você é um historiador especializado em civilizações antigas</papel>
    <background>Estamos analisando textos históricos para entender melhor as práticas culturais de civilizações antigas</background>
  </contexto>
  
  <instrucao>
    <principal>Analise o seguinte texto sobre a civilização maia</principal>
    <subtarefas>
      <tarefa>Identifique as principais características da sua arquitetura</tarefa>
      <tarefa>Liste três de suas maiores realizações</tarefa>
      <tarefa>Explique brevemente seu sistema de escrita</tarefa>
    </subtarefas>
  </instrucao>
  
  <entrada>
    [Insira aqui o texto sobre a civilização maia]
  </entrada>
  
  <formato_saida>
    <estrutura>JSON</estrutura>
    <campos>
      <campo>arquitetura</campo>
      <campo>realizacoes</campo>
      <campo>sistema_escrita</campo>
    </campos>
    <estilo>Acadêmico, mas acessível</estilo>
    <comprimento>Máximo de 300 palavras no total</comprimento>
  </formato_saida>
</prompt>
```

Este exemplo combina várias técnicas:
- **Role Prompting**: Estabelecendo o papel de historiador
- **Task Decomposition**: Dividindo a análise em subtarefas específicas
- **Output Structuring**: Especificando um formato JSON para a saída

## Fluxo de Criação de Prompts

1. **Definir Objetivo**: Determine claramente o que você quer alcançar com o prompt
2. **Estabelecer Contexto**: Forneça informações de fundo relevantes
3. **Formular Instrução**: Crie uma instrução clara e específica
4. **Incluir Entrada**: Adicione os dados ou informações necessários
5. **Especificar Saída**: Defina o formato e a estrutura da resposta desejada
6. **Refinar**: Teste e ajuste o prompt para otimizar os resultados

## Conclusão

A estruturação eficaz de prompts é uma habilidade fundamental em Prompt Engineering. Ao combinar contexto, instruções claras, entradas relevantes e especificações de saída, você pode guiar modelos de linguagem para produzir resultados mais precisos e úteis. Pratique combinando diferentes técnicas e componentes para criar prompts poderosos e eficazes.

## Navegação
- [Anterior: Introdução à Engenharia de Prompt](01_introduction_to_prompt_engineering.md)
- [Próximo: Estrutura Básica de Prompts](03_types_of_prompts.md)

## Tópicos Relacionados

- [Estrutura Básica de Prompts](01_introduction_to_prompt_engineering.md)
- [Tipos de Prompts](03_types_of_prompts.md)
- [Contexto e Especificidade](04_context_and_specificity.md)
- [Componentes do Prompt](05_prompt_components.md)
- [Erros comuns em Prompts](06_common_pitfalls.md)
- [Testes e iteração de Prompt](07_prompt_testing_and_iteration.md)
- [Considerações Éticas em Engenhência de Prompt](08_ethical_considerations.md)

## Contribuição

Encontrou um erro ou tem uma sugestão? Por favor, abra uma [issue](https://github.com/EYLatamSouth/beyondlabs-prompt-engineering/issues) ou envie um [pull request](https://github.com/EYLatamSouth/beyondlabs-prompt-engineering/pulls).

---

<div align="center">
  <a href="#índice">Voltar ao Índice</a> |
  <a href="https://github.com/EYLatamSouth/beyondlabs-prompt-engineering">Sobre este Projeto</a> | 
  <a href="https://github.com/EYLatamSouth/beyondlabs-prompt-engineering/blob/main/LICENSE">Licença</a>
</div>