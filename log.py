import paho.mqtt.client as mqtt
import datetime

# Defina o broker e o tópico que você quer subscrever
BROKER = "54.235.203.118"  # substitua pelo seu broker
TOPIC = "readings/"

# Função chamada quando uma mensagem é recebida
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    topic = msg.topic
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Formatação da mensagem
    formatted_message = f"--------------------------------\n"
    formatted_message += f"[{timestamp}] Tópico: '{topic}' \n Mensagem: \n{message}"
    formatted_message += f"\n--------------------------------\n"
    print(formatted_message)
    
    # Salva a mensagem em um arquivo .txt
    with open("mensagens.txt", "a") as file:
        file.write(formatted_message + "\n")

# Configurações do cliente MQTT
client = mqtt.Client() 
client.on_message = on_message

# Conectar ao broker
client.connect(BROKER)

# Subscrever ao tópico
client.subscribe(TOPIC)

print("Você está conectado ao broker: ", BROKER, "no tópico: ", TOPIC)
print("Esperando mensagens...")

# Iniciar o loop do cliente
client.loop_forever()
