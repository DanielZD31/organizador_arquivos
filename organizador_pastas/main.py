import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title= "selecione uma pasta")

lista_arquivos = os.listdir(caminho)
print(lista_arquivos)


locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".ico", ".raw", ".svg", ".webp"],
    "planilhas": [".xlsx", ".xls", ".ods", ".csv", ".tsv"],
    "pdfs": [".pdf"],
    "textos": [".txt", ".doc", ".docx", ".rtf", ".odt", ".tex", ".md", ".markdown"],
    "apresentacoes": [".ppt", ".pptx", ".key", ".odp"],
    "arquivos_zip": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "codigo": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".php", ".rb", ".swift", ".sh", ".pl"],
    "audio": [".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a", ".alac"],
    "video": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".webm", ".mpg", ".mpeg"],
    "executaveis": [".exe", ".app", ".bat", ".sh", ".bin", ".msi"],
    "backup": [".bak", ".backup", ".sql", ".sav", ".tar.gz"],
    "arquivos_dados": [".json", ".xml", ".yaml", ".ini", ".csv", ".sqlite", ".db"],
    "fontes": [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    "livros": [".epub", ".mobi", ".azw3", ".pdf", ".cbz", ".cbr"],
    "arquivos_dados_binarios": [".dat", ".bin", ".db"],
    "logs": [".log"],
    "scripts": [".ps1", ".vbs", ".pl", ".sh", ".bat", ".cmd"],
    "arquivos_markdown": [".md", ".markdown"],
    "arquivos_latex": [".tex", ".sty", ".cls"],
    "arquivos_graficos": [".svg", ".ai", ".eps", ".ps"],
    "arquivos_desktop": [".desktop"],
    "arquivos_web": [".json", ".xml", ".yml", ".yaml", ".html", ".xhtml"],
    "arquivos_configuracao": [".conf", ".cfg", ".properties"],
    "arquivos_virtualizacao": [".ova", ".vmdk", ".vdi", ".vhd", ".vbox"],
    "arquivos_contabilidade": [".qbw", ".qbx", ".ofx"],
    "arquivos_modelagem": [".stl", ".obj", ".fbx"],
    "arquivos_cad": [".dwg", ".dxf"],
    "arquivos_gis": [".shp", ".kml", ".geojson"],
    "arquivos_documento": [".doc", ".docx", ".dot", ".dotx"],
    "arquivos_aplicacao": [".apk", ".ipa"],
    "arquivos_web_design": [".psd", ".ai", ".xd"],
    "arquivos_3d": [".3ds", ".dae", ".blend"],
    "arquivos_editor_imagem": [".xcf", ".kra"],
    "arquivos_codigo_web": [".php", ".asp", ".jsp"],
    "arquivos_compressao": [".ar", ".lzh"],
}

for arquivo in lista_arquivos:
    # 01. Arquivo.pdf
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")