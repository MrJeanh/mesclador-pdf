import os
from PyPDF2 import PdfMerger

def mesclar_pdfs(diretorio='.', nome_saida='Pdf_Combinados.pdf'):
    merger = PdfMerger()

    # Lista e ordena todos os arquivos .pdf (sem distinguir maiúsculas/minúsculas)
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
            merger.append(caminho_pdf)
        except Exception as e:
            print(f"Erro ao adicionar {arquivo}: {e}")

    merger.write(nome_saida)
    merger.close()
    print(f"PDF combinado criado com sucesso: {nome_saida}")

if __name__ == "__main__":
    mesclar_pdfs()