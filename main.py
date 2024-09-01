import xmltodict
import os 
import pandas as pd

def pegar_info(arquivo):
    print(f'Pegou informação do arquivo: {arquivo}')
    with open(f'nfs/{arquivo}', 'rb') as arquivo_xml:
        dict_arq = xmltodict.parse(arquivo_xml)
        # print(json.dumps(dict_arq, indent=4))
        
        if 'NFe' in dict_arq:
            info_nfe = dict_arq['NFe']['infNFe']
            id_xml = info_nfe['@Id']
            empresa_emissora = info_nfe['emit']['xNome']
            nome_cliente = info_nfe['dest']['xNome']
            endereco = info_nfe['dest']['enderDest']
            peso = info_nfe['transp']['vol']['pesoB']
            # print(id_xml, empresa_emissora,nome_cliente, endereco, peso, sep='\n')
        else:
            info_nfe = dict_arq['nfeProc']['NFe']['infNFe'] 
            id_xml = info_nfe['@Id']
            empresa_emissora = info_nfe['emit']['xNome']
            nome_cliente = info_nfe['dest']['xNome']
            endereco = info_nfe['dest']['enderDest']
            if 'vol' in info_nfe['transp']:
                peso = info_nfe['transp']['vol']['pesoB']
            else:
                peso = 'Não informado'
        valores.append([id_xml, empresa_emissora,nome_cliente, endereco, peso])
        
colunas =  ['id_xml', 'empresa_emissora', 'nome_cliente', 'endereco', 'peso bruto']
valores = []

# pegando arquivos 
lista_arquivos = os.listdir("nfs")
for arquivo in lista_arquivos:
    pegar_info(arquivo)
    # break

tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel('NotaFiscal.xlsx', index=False)