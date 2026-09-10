import argparse
from http.server import HTTPServer,BaseHTTPRequestHandler

def crear_servidor(version,puerto):
    class Manejador(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path==' /health' :
                respuesta = f"OK -Version: { version }"
                codigo=200
            else:
                respuesta =f"Aplicacion ejecutandose-version: { version }"
                codigo=200

            self.send_response(codigo)
            self.send_header(' Conten-type' ,' text/plain' )
            self.end_headers()
            self.wfile.write(respuesta.encode())

        def log_message(self, formato, *argumentos):
            return #Desactivar el registro de solicitudes en la consola 
        
    return HTTPServer(('127.0.0.1',puerto),Manejador)     
  
#Funcion Principal 
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(' --version',required=True)
    parser.add_argument('--puerto',type=int,required=True)

    servidor = crear_servidor(servidor.version,servidor.puerto)

    print(f"Servidor{ servidor.version}en el puerto { servidor.puerto }")

    servidor.serve_forever()
if __name__ ==  '_main_':
    main()  
