import cv2

minha_imagem = cv2.imread('carro.jpg')
#cv2.imshow('janela', minha_imagem)
print('Largura da imagem é de %d' %(minha_imagem.shape[1]))
