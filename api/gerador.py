import requests
import os

def download_neko_image():
    url = 'https://nekos.life/api/neko'

    # Enviar solicitação GET para obter a imagem do neko aleatório
    response = requests.get(url)

    if response.status_code == 200:
        # Extrair a URL da imagem da resposta
        data = response.json()
        image_url = data['neko']

        # Obter o nome do arquivo da URL da imagem
        filename = image_url.split('/')[-1]

        # Definir o caminho completo para salvar o arquivo de imagem
        image_path = os.path.join('img', filename)

        # Baixar a imagem
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            # Salvar a imagem em um arquivo
            with open(image_path, 'wb') as file:
                file.write(image_response.content)
            
            print(f'Imagem salva com sucesso: {filename}')
        else:
            print('Falha ao baixar a imagem.')
    else:
        print('Falha ao obter a imagem do neko.')

# Criar a pasta "img" se ela não existir
if not os.path.exists('img'):
    os.makedirs('img')

# Definir a quantidade de imagens que você deseja baixar
quantidade_imagens = 34

# Loop para baixar as imagens
for i in range(quantidade_imagens):
    print(f'Baixando imagem {i+1}/{quantidade_imagens}')
    download_neko_image()
