import PyPDF2
from io import BytesIO

def extraer_texto_pdf(archivo_pdf):
    try:
        pdf_reader = PyPDF2.PdfReader(BytesIO(archivo_pdf.read()))
        texto_completo = ""
        
        for numero_pagina, pagina in enumerate(pdf_reader.pages, 1):
            texto_pagina = pagina.extract_text()
            if texto_pagina.strip():  # Solo agregar si hay texto
                texto_completo += f"\n--- Página {numero_pagina} ---\n"
                texto_completo += texto_pagina + "\n"
        texto_completo = texto_completo.strip()

        if not texto_completo:
            return "El PDF no contiene texto extraíble o es un PDF escaneado."
        
        return texto_completo
    except Exception as e:
        print(f"Error al procesar el PDF: {str(e)}")
        return ""
