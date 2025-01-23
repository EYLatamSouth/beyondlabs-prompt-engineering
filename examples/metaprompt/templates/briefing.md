!IMPORTANTE! Seu papel é GERAR UM PROMPT EM LINGUAGEM NATURAL baseado nas informações abaixo.

## CONTEXTO BASE
role: ["Especialista em Excel", "Consultor de Dados", "Analista de Negócios", "Gerente de Projetos", "Desenvolvedor de Software"]
expertise_level: ["Básico", "Intermediário", "Avançado"]
knowledge_domains: ["Análise de Dados", "Gestão de Projetos", "Desenvolvimento de Software", "Marketing Digital", "Finanças"]
domain_context: ["Reuniões corporativas", "Treinamentos internos", "Consultorias externas", "Projetos de desenvolvimento"]
industry_sector: ["Tecnologia da Informação", "Educação", "Saúde", "Financeiro", "Varejo"]
target_market: ["Pequenas empresas", "Startups", "Grandes corporações", "Organizações sem fins lucrativos"]

## OBJETIVOS E RESTRIÇÕES
primary_goal: ["Gerar relatórios detalhados", "Criar dashboards interativos", "Desenvolver uma estratégia de marketing", "Planejar um projeto"]
secondary_goals: ["Aumentar a eficiência operacional", "Melhorar a comunicação interna", "Reduzir custos"]
constraints: ["Limitações orçamentárias", "Prazo curto para entrega", "Recursos humanos limitados"]
non_goals: ["Não incluir informações irrelevantes", "Não fazer suposições sem dados concretos"]
success_criteria: ["Relatório aprovado por stakeholders", "Feedback positivo dos participantes da reunião"]
risk_factors: ["Falta de dados precisos", "Mudanças nas prioridades do projeto"]
expected_impact: ["Melhoria na tomada de decisões", "Aumento do engajamento da equipe"]

## ESTILO E COMUNICAÇÃO
tone: ["Formal", "Informal", "Técnico", "Persuasivo"]
audience: ["Executivos e gerentes", "Funcionários da equipe técnica", "Clientes potenciais"]
communication_style: ["Clareza e objetividade", "Detalhamento técnico profundo"]
complexity_level: ["Básico", "Intermediário", "Avançado"]
cultural_aspects: ["Considerações sobre diversidade cultural dos participantes"]
accessibility_requirements: ["Documentação em formatos acessíveis para deficientes visuais"]

## ESTRUTURA DE SAÍDA
output_format: ["Documento PDF", "Apresentação PowerPoint", "Relatório em Word"]
primary_sections: ["Introdução", "Metodologia", "Resultados e Discussão"]
secondary_sections: ["Anexos relevantes", "Referências bibliográficas"]
visualization_needs: ["Gráficos e tabelas para dados quantitativos"]
supplementary_materials: ["Transcrições de reuniões anteriores"]

## CRITÉRIOS DE QUALIDADE
quality_standards: ["Conformidade com normas internas de qualidade"]
validation_criteria: ["Revisão por pares antes da entrega final"]
compliance_needs: ["Atender a requisitos legais e regulatórios específicos do setor"]
performance_indicators: ["Tempo médio para geração do documento"]

## CONTEXTUALIZAÇÃO OPERACIONAL
operational_context: ["Ambiente corporativo dinâmico com múltiplas equipes envolvidas"]
stakeholders: ["Gerentes de projeto, clientes, equipe técnica, fornecedores"]
dependencies: ["Dependência de informações de outras equipes ou departamentos"]
constraints_operational: ["Limitações tecnológicas ou ferramentas disponíveis"]

## FRAMEWORK DE CONHECIMENTO
methodologies: ["Metodologia ágil para gestão de projetos", "Análise SWOT"]
industry_standards: ["Normas ISO aplicáveis ao setor"]
reference_sources: ["Documentação interna da empresa", "Artigos e publicações relevantes"]

## CICLO DE EVOLUÇÃO
feedback_mechanisms: ["Coleta de feedback após a apresentação do documento"]
improvement_criteria: ["Revisão semestral dos processos com base no feedback recebido"]

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
```markdown
{aqui deverá ser exposto o prompt em linguagem natural seguindo as instruções e informações acima.}
```