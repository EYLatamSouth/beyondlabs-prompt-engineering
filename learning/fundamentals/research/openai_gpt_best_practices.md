# OpenAI GPT Best Practices

## Fonte Principal
Documento: "GPT Best Practices"
Autor: OpenAI
Link: https://platform.openai.com/docs/guides/gpt-best-practices

## Resumo

A OpenAI fornece um guia abrangente de melhores práticas para usar efetivamente seus modelos GPT. Este documento cobre estratégias para melhorar a qualidade das respostas, lidar com limitações do modelo e otimizar o desempenho em várias tarefas.

## Pontos-chave

1. **Estratégias de Prompting**:
   - Seja claro e específico
   - Divida tarefas complexas em etapas menores
   - Use delimitadores para separar diferentes partes do input

2. **Técnicas Avançadas**:
   - Few-shot learning: Fornecer exemplos no prompt
   - Chain-of-Thought: Guiar o modelo através de etapas de raciocínio

3. **Lidar com Limitações**:
   - Verificação de fatos: Pedir ao modelo para citar fontes
   - Redução de alucinações: Instruir o modelo a dizer "Não sei" quando apropriado

4. **Otimização de Desempenho**:
   - Ajustar a temperatura e outros parâmetros
   - Usar fine-tuning para tarefas específicas

5. **Considerações Éticas**:
   - Evitar conteúdo prejudicial ou tendencioso
   - Respeitar a privacidade e os direitos autorais

## Aplicações em Prompt Engineering

- Implementar estratégias de clareza e especificidade em todos os prompts
- Utilizar técnicas como Few-shot learning para melhorar a precisão
- Incorporar verificações e balanços para reduzir erros e vieses

## Limitações e Considerações

- As práticas podem precisar de ajustes para diferentes versões do modelo
- Algumas técnicas podem aumentar o uso de tokens, afetando custos e velocidade