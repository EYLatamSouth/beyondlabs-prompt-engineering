# Constitutional AI - Anthropic

## Índice
- [Fonte Principal](#fonte-principal)
- [Pontos-chave](#pontos-chave)
- [Aplicações em Prompt Engineering](#aplicações-em-prompt-engineering)
- [Limitações e Considerações](#limitações-e-considerações)
- [Navegação](#navegação)

## Fonte Principal
Artigo: "Constitutional AI: Harmlessness from AI Feedback"
Autores: Yuntao Bai, et al.
Link: https://arxiv.org/abs/2212.08073

## Pontos-chave

1. **Definição de Regras**: A "constituição" inclui diretrizes sobre comportamento ético, veracidade, respeito aos direitos humanos, etc.

2. **Treinamento em Duas Fases**:
   - Fase 1: Treinamento supervisionado para seguir as regras
   - Fase 2: Refinamento usando aprendizado por reforço

3. **Auto-supervisão**: O modelo é treinado para avaliar e corrigir suas próprias respostas.

4. **Resultados**: Modelos treinados com Constitutional AI demonstraram maior alinhamento com valores humanos e menor propensão a comportamentos prejudiciais.

5. **Implicações**: Esta abordagem pode ser crucial para desenvolver IA mais confiável e ética.

## Aplicações em Prompt Engineering

- Incorporar princípios de Constitutional AI ao projetar prompts para garantir respostas éticas e seguras
- Usar técnicas de auto-avaliação em prompts complexos para melhorar a qualidade das respostas

## Limitações e Considerações

- A eficácia depende da qualidade e abrangência das regras definidas
- Pode haver trade-offs entre aderência estrita às regras e flexibilidade em certos contextos

## Navegação
- [Anterior: Google Prompt Engineering Study](google_prompt_engineering_study.md)
- [Voltar para Articles](..)

<div align="center">
  <a href="#índice">Voltar ao Índice</a> |
  <a href="https://github.com/EYLatamSouth/beyondlabs-prompt-engineering">Sobre este Projeto</a> | 
  <a href="https://github.com/EYLatamSouth/beyondlabs-prompt-engineering/blob/main/LICENSE">Licença</a>
</div>