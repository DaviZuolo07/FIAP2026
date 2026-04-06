import os
import pygame

def reproduzir_mp3(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print("Erro: o arquivo não foi encontrado.")
        return

    try:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(caminho_arquivo)
        pygame.mixer.music.play()

        print("Reproduzindo áudio...")

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as erro:
        print(f"Ocorreu um erro ao reproduzir o áudio: {erro}")

# Exemplo de uso
reproduzir_mp3("musica.mp3")