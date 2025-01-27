import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Caminho do arquivo CSV
caminho = "Eso8266_Reciever - Sheet1.csv"
df = pd.read_csv(caminho)

# Gerando os arquivos Excel e JSON
df.to_excel("Esteira_Zennit.xlsx", index=False)
df.to_json("esteria_zennit.json", index=False)

# Criando o PDF
canva = canvas.Canvas("esteira_zennit.pdf", pagesize=letter)

# Título da página no PDF
canva.setFont("Times-Roman", 18)
canva.drawString(x=200, y=750, text="ESTEIRA DA LOJA ZENNIT")

# Nomes das colunas do PDF
colunas = ["date", "time", "esteira1", "esteira2", "esteira3"]
canva.setFont("Helvetica-Bold", 12)

# Definindo as dimensões do PDF
largura, altura = letter
largura_coluna = largura / 5  # Dividindo a largura da página em 5 colunas

# Títulos das colunas
for i, titulo in enumerate(colunas):
    canva.drawString(x=largura_coluna * i + 50, y=730, text=titulo)

# Posição inicial para os dados (logo abaixo dos títulos)
a = 700

# Percorrendo as linhas 
for index, linha in df.iterrows():
    # Se a posição y estiver muito baixa, cria uma nova página
    if a < 60:
        canva.showPage()
        a = 700  # Resetando a posição y para o topo

        # imprimindo os titulos de novo
        for i, titulo in enumerate(colunas):
            canva.drawString(x=largura_coluna * i + 50, y=730, text = titulo)
    
    # Pegando os valores das colunas para cada linha
    date = linha["date"]
    time = linha["time"]
    e1 = linha["esteira1"]
    e2 = linha["esteira2"]
    e3 = linha["esteria3"]
    
    # Desenhando os valores nas colunas
    canva.setFont("Helvetica", 10)
    canva.drawString(x=50, y=a, text=str(date))  
    canva.drawString(x=largura_coluna + 50, y=a, text=str(time)) 
    canva.drawString(x=largura_coluna * 2 + 50, y=a, text=str(e1))  
    canva.drawString(x=largura_coluna * 3 + 50, y=a, text=str(e2))  
    canva.drawString(x=largura_coluna * 4 + 50, y=a, text=str(e3))  

    # pulando linha de y
    a -= 20

canva.save()
