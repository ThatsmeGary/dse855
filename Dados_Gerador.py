from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException


# Configurações da conexão

host = 'IP' # Aqui você deve configurar o seu IP  
port = 502  # A porta padrão é 502, mas ela pode mudar conforme configurações              

# Configurar cliente Modbus
client = ModbusTcpClient(host, port)

def read_modbus_registers(client: ModbusTcpClient):
    try:
        TEMPERATURA_LIQUIDO_REFRIGERADOR = client.read_holding_registers(1025, 1).registers[0]
        COMBUSTIVEL = client.read_holding_registers(1027, 1).registers[0]
        ALTERNADOR_CARGA = client.read_holding_registers(1028, 1).registers[0]
        ENERGIA_MOTOR = client.read_holding_registers(1029, 1).registers[0]
        VELOCIDADE_MOTOR = client.read_holding_registers(1030, 1).registers[0]
        STATUS_GERADOR = client.read_holding_registers(772, 1).registers[0]
        
        return {            
            "Status": STATUS_GERADOR,
            "Temperatura Liquido Refrigerador": f"{TEMPERATURA_LIQUIDO_REFRIGERADOR}ºC",
            "Combustivel": f"{COMBUSTIVEL}%",
            "Alternador": f"{ALTERNADOR_CARGA*0.1:.1f}V",
            "Energia": f"{ENERGIA_MOTOR*0.1:.1f}V",
            "RPM": f"{VELOCIDADE_MOTOR} RPM",
        }

    except ModbusException as e:
        print(f"Erro na comunicação Modbus: {e}")
        return None

if client.connect():
    data = read_modbus_registers(client)
    print(data)

client.close()


