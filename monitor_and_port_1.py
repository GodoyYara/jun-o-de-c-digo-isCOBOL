# %%

# Combinação dos dois códigos

# Importação de bibliotecas
import psutil, time, pyodbc, socket

# Funções:
## Função monitoramento:
def getService(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        status = str()
    return service

## Função para chegar a porta
def is_port_open(port):
   # criação de um objeto
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   # definição do tempo limite de 1 segundo
   s. settimeout(1)
   try:
      # tentativa para tentar se conectar a porta 
      s.connect(('127.0.0.1', 10999))
      # porta está aberta
      print(f"Port{10999}is open")
      return True
   except:
      # porta está fechada
      print(f"Port{10999} is closed")
      return False
   finally:
      # final objeto
      s.close()
# verifica se a porta está aberta       
is_port_open(80)

service = getService('isCOBOL Server 2023R2')

if service:
  if service['status'] == 'running':
    status = "Serviço isCOBOL está rodando"
    # Additionally check port if service is running
    if is_port_open(10999):
      print(f"Port {10999} is also open (potentially used by isCOBOL)")
    else:
      print(f"Port {10999} is closed")
  else:
    status = "Serviço isCOBOL não está em execução"
else:
  status = "Serviço isCOBOL não encontrado"

print(status)
# %%