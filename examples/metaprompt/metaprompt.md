# META-PROMPT SCHEMA
## QUICK-START
## 🚀 Como Usar o Meta-Prompt em 5 Passos

1. **Identifique sua Necessidade**
    - Qual o objetivo principal?
    - Quem é o público-alvo?
    - Qual o resultado esperado?
2. **Escolha um Template**
    - Use um template base da seção Templates ou escolha 1 entre basic, intermediate ou advanced
    - OU comece com o template minimal
    - OU use o template completo para casos complexos
3. **Preencha as Seções Essenciais** Mínimo necessário:
```
   role: {seu papel}
	primary_goal: {objetivo principal}
	audience: {público-alvo}
	output_format: artifact
```
4. **Adicione Contexto**
    - Preencha seções adicionais relevantes
    - Remova seções não aplicáveis
    - Mantenha apenas o necessário
5. **Valide e Execute**
    - Verifique se todas as seções essenciais estão preenchidas
    - Confirme se o objetivo está claro
    - Submeta à LLM

## PROMPT:
!IMPORTANTE! Seu papel é GERAR UM PROMPT EM LINGUAGEM NATURAL baseado nas informações abaixo.

- Analise todas as informações fornecidas
- Construa um prompt claro e objetivo
- O prompt deve ser auto-contido e executável
- Gere o prompt em formato de artifact
- NÃO execute a tarefa em si

## CONTEXTO BASE
role: {defina o papel específico que a LLM deve assumir}
expertise_level: {defina o nível de expertise necessário}
knowledge_domains: {liste as áreas de conhecimento necessárias}
domain_context: {especifique o contexto do domínio}
industry_sector: {defina o setor ou área de atuação}
target_market: {especifique o mercado-alvo se aplicável}

## OBJETIVOS E RESTRIÇÕES
primary_goal: {defina o objetivo principal}
secondary_goals: {liste objetivos secundários se houver}
constraints: {liste as restrições ou limitações}
non_goals: {especifique o que NÃO deve ser incluído}
success_criteria: {defina critérios mensuráveis de sucesso}
risk_factors: {identifique potenciais riscos}
expected_impact: {descreva o impacto esperado}

## ESTILO E COMUNICAÇÃO
tone: {defina o tom da comunicação}
audience: {especifique o público-alvo}
communication_style: {defina o estilo de comunicação}
complexity_level: {especifique o nível de complexidade: básico, intermediário, avançado}
cultural_aspects: {considere aspectos culturais relevantes}
accessibility_requirements: {especifique requisitos de acessibilidade}

## ESTRUTURA DE SAÍDA
output_format: {especifique o formato desejado}
primary_sections: {liste as seções principais}
secondary_sections: {liste seções complementares}
visualization_needs: {especifique necessidades de visualização}
supplementary_materials: {liste materiais complementares necessários}
localization_needs: {especifique necessidades de localização}

## CRITÉRIOS DE QUALIDADE
quality_standards: {defina padrões de qualidade}
validation_criteria: {especifique critérios de validação}
compliance_needs: {especifique requisitos de conformidade}
performance_indicators: {defina indicadores de performance}
quality_assurance_steps: {liste etapas de garantia de qualidade}

## CONTEXTUALIZAÇÃO OPERACIONAL
operational_context: {descreva o contexto operacional}
stakeholders: {identifique as partes interessadas}
dependencies: {liste dependências importantes}
constraints_operational: {especifique restrições operacionais}
resource_requirements: {liste recursos necessários}

## FRAMEWORK DE CONHECIMENTO
methodologies: {liste metodologias relevantes}
industry_standards: {especifique padrões da indústria}
reference_sources: {liste fontes de referência}
domain_specific_requirements: {requisitos específicos do domínio}

## CICLO DE EVOLUÇÃO
feedback_mechanisms: {especifique mecanismos de feedback}
improvement_criteria: {defina critérios para melhorias}
review_requirements: {especifique requisitos de revisão}
adaptation_guidelines: {diretrizes para adaptação}
version_control: {requisitos de controle de versão}

## VALIDATION RULES
input_validation:
  required_fields:
    - role
    - primary_goal
    - output_format
  format_rules:
    - expertise_level deve ser especificado em anos ou nível
    - tone deve ser um dos: formal, informal, técnico

## QUALITY GATES
Antes de gerar:
  □ Todos campos obrigatórios preenchidos
  □ Formatos válidos
  □ Consistência entre seções

Após gerar:
  □ Prompt está em formato artifact
  □ Instruções são claras e executáveis
  □ Output atende objetivo principal

## ERROR HANDLING
validation_steps:
  1. Verificar campos obrigatórios
  2. Validar formatos específicos
  3. Confirmar consistência entre seções

recovery_actions:
  missing_fields:
    - Solicitar informação adicional
    - Usar valores default quando apropriado
  invalid_format:
    - Sugerir formato correto
    - Oferecer exemplos válidos

## OUTPUT RULES
1. Esta é uma instrução para GERAR UM PROMPT, não para executar a tarefa
2. O output DEVE ser estruturado como um prompt que será usado posteriormente
3. NÃO execute a tarefa solicitada
4. NÃO forneça a solução direta
5. NÃO simule ser o papel solicitado
6. SEMPRE retorne apenas o prompt em formato de artifact
7. O prompt gerado DEVE seguir estritamente o formato:

## FORMATO DO OUTPUT ESPERADO
```
{aqui deverá ser exposto o prompt em linguagem natural seguindo as instruções e informações acima.}
```