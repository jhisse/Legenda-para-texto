# coding: utf-8

import re

while True:
    try:
        arquivo = input('Qual o nome do arquivo de legendas com a extensão (ex: legenda.srt):')
        arquivoLegenda = open(arquivo, 'r')
    except FileNotFoundError:
        print('Arquivo não encontrado!\n')
    else:
        break

arquivoLegenda = open(arquivo, 'r')
textoParaConverter = arquivoLegenda.read()
arquivoLegenda.close()

textoParaConverter = re.sub(r'[0-9]{1,}\n[0-9,:]{10,12} --> [0-9,:]{10,12}','',textoParaConverter)

textoParaConverter = re.sub(r'<.*?>','',textoParaConverter)

textoParaConverter = re.sub(r'(\n){1,}',' ',textoParaConverter)

saida = open('convertido_' + arquivo, 'w')

saida.write(textoParaConverter)
saida.close()