from strands import Agent, BedrockModel

# 1. Definimos los modelos según la arquitectura
haiku_model = BedrockModel(
    model_id="anthropic.claude-3-5-haiku-20241022-v1:0", 
    temperature=0.1
)

nova_model = BedrockModel(
    model_id="amazon.nova-micro-v1:0", 
    temperature=0.3
)

# 2. Instanciamos los Child Agents
transbank = Agent(
    name="transbank", 
    model=haiku_model, 
    tools=[transbank_query] # Esta tool apuntará al API Gateway que creamos en el CFN
)

promociones = Agent(
    name="promociones", 
    model=nova_model, 
    tools=[rag_search] # Esta tool consultará la tabla DynamoDB de Promociones
)

# 3. Instanciamos el Orchestrator Agent (Supervisor)
supervisor = Agent(
    name="supervisor",
    model=haiku_model,
    sub_agents=[transbank, promociones],
    guardrail_id="<AQUI_PEGAS_EL_ID_DEL_GUARDRAIL_DEL_OUTPUT>"
)

# Ejecución del ciclo algorítmico de razonamiento
respuesta = supervisor.run(
    user_input="Hola, quiero revisar mi pago de ayer y saber si hay promociones con tarjeta de crédito."
)
print(respuesta)
