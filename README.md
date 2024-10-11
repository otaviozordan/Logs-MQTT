# Formato de Mensagens

As mensagens devem seguir o seguinte formato JSON:

```json
{
  "reading": 24092026,
  "date": "1234567890",
  "reading_senId": 40
}

Detalhes dos Campos
reading: Um número inteiro representando a leitura (exemplo: 24092026).
date: Uma string representando a data em formato Unix timestamp (exemplo: "1234567890").
reading_senId: Um número inteiro que identifica o sensor (exemplo: 40).
QoS
As mensagens devem ser enviadas com QoS 1, garantindo que a mensagem seja entregue pelo menos uma vez.

O tópico para subir leituras é "readings/"