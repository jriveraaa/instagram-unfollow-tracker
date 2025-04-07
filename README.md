# Instagram Unfollow Tracker
Este programa te ayuda a descubrir quiénes no te siguen en Instagram.

## ¿Qué hace este programa?
1. Lee tus datos descargados de Instagram.
2. Compara tu lista de seguidores con tu lista de seguidos.
3. Crea un archivo con los nombres de las personas que no te siguen de vuelta.

## Requisitos antes de empezar
- Tener Python instalado en tu computadora.
- Haber descargado tus datos de Instagram.

## Instrucciones paso a paso
### 1) Descarga tus datos de Instagram:
1. Abre Instagram en tu teléfono o computadora
2. Ve a tu perfil
3. Toca las tres líneas (menú) y selecciona "Configuración y privacidad"
4. Ve a Centro de cuentas y luego selecciona Tu información y permisos.
5. Ve a Descargar tu información.
6. Selecciona Descargar o transferir información.
7. Selecciona Parte de tu información.
8. Luego marca Seguidores y seguidos, después toca siguiente, y Descargar al dispositivo.
9. En Rango de fechas selecciona Todo el tiempo.
10. En formato selecciona JSON, luego Crear archivos.
11. Tendrás que esperar un tiempo, y más tarde recibirás un correo electrónico indicando que tu información está lista.
12. Cuando esté listo, descarga tus archivos a tu computadora.

### 2) Prepara los archivos necesarios:
1. Dentro de los archivos extraídos de Instagram, busca:
   - El archivo `followers_1.json` (tus seguidores)
   - El archivo `following.json` (personas que sigues)
2. Copia estos dos archivos y colócalos en la misma carpeta donde guardaste el programa `main.py`

### 3) Instala Python (si no lo tienes ya):
1. Ve a [python.org](https://www.python.org/downloads/)
2. Descarga e instala la última versión para tu sistema operativo
3. Durante la instalación, marca la casilla "Añadir Python al PATH"

### 4) Ejecuta el programa:
#### En Windows:
1. Abre la carpeta donde guardaste el programa `main.py` y los archivos de Instagram
2. Mantén presionada la tecla Shift y haz clic derecho en un espacio vacío de la carpeta
3. Selecciona "Abrir ventana de PowerShell aquí" o "Abrir ventana de comandos aquí"
4. Escribe `python main.py` y presiona Enter

#### En Mac:
1. Abre la aplicación Terminal
2. Escribe `cd ` (con un espacio al final) y arrastra la carpeta donde guardaste el programa a la ventana de Terminal
3. Presiona Enter
4. Escribe `python main.py` y presiona Enter

#### En Visual Studio Code:
1. Descarga e instala [VS Code](https://code.visualstudio.com/download).
2. Instala la [extensión de Python]([https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items/?itemName=ms-python.python)).
3. Abre la carpeta donde guardaste el programa `main.py` y los archivos de Instagram en VS Code.
4. Presiona el botón de reproducción en la parte superior derecha de VS Code.

### 5) Revisa los resultados:
1. El programa creará un archivo llamado `non_followers.csv` en la misma carpeta
2. Puedes abrir este archivo con Excel, Google Sheets o cualquier programa de hojas de cálculo
3. Ahí verás la lista de personas que no te siguen de vuelta

## Solución de problemas comunes
- **Error: No se pueden encontrar los archivos** - Asegúrate de que `followers_1.json` y `following.json` estén en la misma carpeta que `main.py`
- **Error: Python no es reconocido** - Reinstala Python y asegúrate de marcar "Añadir Python al PATH"
- **Archivo vacío o incompleto** - Verifica que hayas descargado correctamente tus datos de Instagram

## Nota importante
Este programa respeta tu privacidad y funciona localmente en tu computadora. Tus datos de Instagram no se comparten con nadie.
