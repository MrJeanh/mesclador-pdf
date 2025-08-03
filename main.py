import os
from PyPDF2 import PdfMerger

def mesclar_pdfs(diretorio='.', nome_saida='Pdf_Combinados.pdf'):
    pdf_combinado = PdfMerger()

    # Lista e ordena todos os arquivos .pdf no diretório informado
    arquivos_pdf = sorted(
        [f for f in os.listdir(diretorio) if f.lower().endswith('.pdf')]
    )

    if not arquivos_pdf:
        print("Nenhum arquivo PDF encontrado no diretório.")
        return

    print(f"Mesclando os seguintes arquivos:\n{arquivos_pdf}\n")

    for arquivo in arquivos_pdf:
        caminho_pdf = os.path.join(diretorio, arquivo)
        try:
            pdf_combinado.append(caminho_pdf)
        except Exception as e:
            print(f"Erro ao adicionar {arquivo}: {e}")
    caminho_saida = os.path.join(diretorio, nome_saida)
    pdf_combinado.write(caminho_saida)
    pdf_combinado.close()
    print(f"Pdf combinado criado com sucesso: {nome_saida}")

if __name__ == "__main__":
    # Pega o diretório onde o script está salvo
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    mesclar_pdfs(diretorio=diretorio_script)