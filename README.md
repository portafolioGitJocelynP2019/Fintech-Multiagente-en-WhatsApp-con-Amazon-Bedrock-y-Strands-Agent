# Fintech-Multiagente-en-WhatsApp-con-Amazon-Bedrock-y-Strands-Agent
Codigo de la presentacion del Community Day Bolivia

# 🚀 Asistente Fintech Multiagente en WhatsApp
### AWS Community Day Bolivia 2026 - Santa Cruz de la Sierra

¡Bienvenidos al repositorio oficial de la demo! Qué felicidad más grande poder compartir todo este conocimiento con ustedes. Participar por segunda vez en uno de los mejores Community Days a los que he asistido me llena de una alegría inmensa y de muchísima gratitud. Se me hace mucha felicidad compartir con el público de esta hermosa comunidad y seguir construyendo juntos.

Este repositorio contiene el código y la infraestructura necesarios para desplegar un **Asistente Fintech Multiagente** utilizando una arquitectura *Serverless* y *Generative AI* en AWS. 

El objetivo principal de esta demostración es resolver la fricción en servicios financieros, llevando la atención directamente a un canal asíncrono como WhatsApp y orquestando agentes de inteligencia artificial de forma nativa, segura y escalable.

## 🏗️ Arquitectura de la Solución

El proyecto demuestra un flujo completo ("El Puente"), desde el dispositivo móvil del usuario hasta la ejecución de transacciones financieras mediante APIs simuladas, pasando por un riguroso ciclo algorítmico de razonamiento.

<img width="1408" height="768" alt="Gemini_Generated_Image_3" src="https://github.com/user-attachments/assets/b0765af7-96e0-48f1-b376-532afa29b6f7" />


*   **Canal de Entrada:** WhatsApp Business conectado nativamente vía **AWS End User Messaging** [cite: 1].
*   **Capa de Ingesta Asíncrona:** Amazon API Gateway + AWS Lambda + Amazon DynamoDB. Implementa un patrón de *Tumbling Window* (ventana de tiempo de 20 segundos) para agrupar mensajes fragmentados del usuario y optimizar tokens [cite: 1].
*   **Orquestación Nativa:** **Strands Agent Framework** actuando como el cerebro del sistema, sin depender de consolas legacy [cite: 1].
*   **Agente Supervisor:** Potenciado por **Anthropic Claude 3.5 Haiku** en Amazon Bedrock, operando bajo estricto control de inferencia y protegido por **Bedrock Guardrails** [cite: 1].
*   **Sub-Agentes (Child Agents):**
    *   *Agente Transbank (Transacciones):* Ejecuta el *Tool Use* con llamadas a APIs simuladas para consultas de estado de pagos (Claude 3.5 Haiku) [cite: 1].
 
      <img width="1408" height="768" alt="Gemini_Generated_Image_4" src="https://github.com/user-attachments/assets/285b51f9-ded3-437f-9aab-0a348772e844" />

    *   *Agente Promociones:* Consulta bases de datos y documentos de promociones usando RAG (Amazon Nova Micro) [cite: 1].
*   **Gestión de Estado y Contexto:** Retención de contexto a largo y corto plazo mediante **AgentCore Memory** (almacenado en DynamoDB), permitiendo retomar conversaciones horas después sin perder el hilo [cite: 1].

## 📂 Contenido del Repositorio

1.  `demo-infra.yaml`: Plantilla de AWS CloudFormation que despliega toda la infraestructura "satélite" de soporte. Incluye las tablas DynamoDB con TTL, Buckets S3 para RAG, Lambdas, el Mock del API Gateway para Transbank y el Guardrail de Seguridad.
2.  `app.py`: Script en Python demostrando la instanciación limpia y minimalista del Supervisor y los Child Agents utilizando el SDK de Strands. Muestra en acción el protocolo A2A (Agent-to-Agent) aislando responsabilidades [cite: 1].

## 🚀 Cómo utilizar este proyecto

1.  Despliega la plantilla `demo-infra.yaml` en la consola de AWS CloudFormation dentro de tu cuenta.
2.  Una vez desplegado el stack, copia la URL del Endpoint del API de Transbank y el ID del Guardrail desde la pestaña de *Outputs*.
3.  Configura tus credenciales de AWS localmente (por ejemplo, en Kiro IDE).
4.  Reemplaza los valores de URL e ID en el archivo `app.py`.
5.  Ejecuta el script para observar la magia de la orquestación y el flujo A2A en la terminal.

---
**Desarrollado por:** Jocelyn Poblete  
*Solution Architect Cloud*  
🎙️ Host de **CloudWise** en <a href="https://www.youtube.com/@Cloud_Wise">YouTube</a> y <a href="https://open.spotify.com/show/5eFDsRAExLBnwitqrjW1Rp">Spotify</a>
