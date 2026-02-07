# 📄 CV Analyzer - Sistema de Evaluación de Currículums con IA

**Analiza currículums y evalúa candidatos de manera objetiva usando inteligencia artificial**

Un sistema completo que utiliza **LangChain** y **OpenAI GPT-4** para extraer información de CVs en PDF y evaluarlos automáticamente contra descripciones de puestos específicos. Proporciona análisis detallados, objetivos y constructivos sobre candidatos.

---

## ✨ Características

- 📋 **Procesamiento de PDFs**: Extrae texto de currículums en formato PDF
- 🤖 **Análisis con IA**: Utiliza GPT-4 para análisis inteligente y objetivos
- 📊 **Evaluación Estructurada**: Genera reportes en formato estructurado con Pydantic
- 🎯 **Ajuste de Puesto**: Calcula porcentaje de compatibilidad con el perfil requerido
- 💡 **Recomendaciones**: Identifica fortalezas y áreas de mejora del candidato
- 🎨 **Interfaz Intuitiva**: UI moderna y amigable con Streamlit

---

## 🛠️ Requisitos Previos

Antes de instalar el proyecto, asegúrate de tener:

- **Python 3.9+** instalado en tu sistema
  - Verifica con: `python --version`
  - Descarga desde: https://www.python.org/downloads/
  
- **pip** (gestor de paquetes de Python)
  - Generalmente viene incluido con Python
  - Verifica con: `pip --version`

- **Clave de API de OpenAI**
  - Regístrate en https://platform.openai.com
  - Obtén tu clave en https://platform.openai.com/api-keys
  - Asegúrate de tener acceso a GPT-4o-mini o una alternativa disponible

---

## 📦 Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/luis2103/cv_analyzer.git
cd cv_analyzer
```

### 2. Crear y Activar Entorno Virtual

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

✅ Sabrás que el entorno está activado cuando ves `(venv)` al inicio de tu terminal.

### 3. Instalar Dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Dependencias instaladas:**
- `pydantic` - Validación y modelos de datos
- `PyPDF2` - Procesamiento de archivos PDF
- `langchain` - Framework para aplicaciones con LLMs
- `langchain-openai` - Integración con OpenAI
- `streamlit` - Framework para crear la interfaz web

---

## 🔐 Configuración de Variables de Entorno

### Crear archivo `.env`

En la raíz del proyecto, crea un archivo llamado `.env` con tu clave de API de OpenAI:

```bash
# .env
OPENAI_API_KEY=sk-your-api-key-here
```

⚠️ **Importante:**
- **NUNCA** compartas tu clave de API públicamente
- Agrega `.env` a `.gitignore` para evitar subirla al repositorio
- La clave debe comenzar con `sk-`

### Alternativa: Variable de Entorno del Sistema

Si prefieres no crear un archivo `.env`:

**En macOS/Linux:**
```bash
export OPENAI_API_KEY="sk-your-api-key-here"
```

**En Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="sk-your-api-key-here"
```

**En Windows (CMD):**
```cmd
set OPENAI_API_KEY=sk-your-api-key-here
```

---

## 🚀 Ejecutar la Aplicación

### Opción 1: Con el Entorno Virtual Activado

```bash
# Asegúrate de estar en la raíz del proyecto
streamlit run app.py
```

### Opción 2: Usando Python Directamente (Sin Activar venv)

```bash
# macOS/Linux
./venv/bin/python -m streamlit run app.py

# Windows
venv\Scripts\python -m streamlit run app.py
```

### ✅ Resultado Esperado

```
  You can now view your Streamlit app in your browser.

  URL: http://localhost:8501
```

Abre tu navegador y ve a `http://localhost:8501`

---

## 📖 Cómo Usar la Aplicación

1. **Subir CV**: 
   - Selecciona un CV en formato PDF del candidato
   - El archivo debe contener texto extraíble (no escaneado como imagen)

2. **Ingresar Descripción del Puesto**:
   - Describe en detalle los requisitos, responsabilidades y habilidades necesarias
   - Sé específico sobre tecnologías, años de experiencia, etc.

3. **Analizar**:
   - Haz clic en "🔍 Analizar Candidato"
   - La IA evaluará el CV contra el puesto en ~5-10 segundos

4. **Revisar Resultados**:
   - Nombre y años de experiencia
   - Habilidades clave identificadas
   - Educación y formación
   - Fortalezas y áreas de mejora
   - **Porcentaje de Ajuste** (0-100)

---

## 📁 Estructura del Proyecto

```
cv_analyzer/
├── app.py                      # Punto de entrada principal
├── requirements.txt            # Dependencias del proyecto
├── .env                        # Variables de entorno (no incluir en Git)
├── .gitignore                  # Archivos ignorados por Git
│
├── models/
│   └── cv_model.py            # Modelos Pydantic para respuestas estructuradas
│
├── services/
│   ├── pdf_processor.py        # Extracción de texto de PDFs
│   └── cv_evaluator.py         # Lógica de evaluación con IA
│
├── prompts/
│   └── cv_prompts.py           # Plantillas de prompts para OpenAI
│
└── ui/
    └── streamlit_ui.py         # Interfaz de usuario con Streamlit
```

---

## 🐛 Troubleshooting

### Error: `ModuleNotFoundError: No module named 'pydantic'`

**Solución:**
```bash
# Asegúrate de estar dentro del entorno virtual
pip install -r requirements.txt
```

### Error: `OPENAI_API_KEY not found`

**Solución:**
1. Verifica que el archivo `.env` existe en la raíz del proyecto
2. Comprueba que la clave no tiene espacios adicionales
3. Si usas variables del sistema, reinicia la terminal después de configurarla

### Error: `StreamlitAPIException: Invalid OpenAI API key`

**Solución:**
- Confirma que tu clave es válida en https://platform.openai.com/api-keys
- Verifica que tienes acceso a GPT-4o-mini
- Asegúrate de tener créditos disponibles en tu cuenta

### El PDF no muestra texto extraíble

**Solución:**
- El PDF podría estar escaneado (imagen). Necesita OCR
- Prueba con otro PDF con texto seleccionable
- Convierte el PDF escaneado usando herramientas OCR como Tesseract

### Error de conexión a OpenAI

**Solución:**
```bash
# Verifica tu conexión a internet
ping api.openai.com

# Verifica que no haya firewall bloqueando
# Si usas VPN, intenta desactivarla temporalmente
```

---

## 📊 Ejemplo de Uso

### Entrada
- **CV**: Documento PDF con experiencia del candidato
- **Puesto**: "Desarrollador Python Senior con 5+ años de experiencia en FastAPI"

### Salida
```json
{
  "nombre_candidato": "Juan García",
  "experiencia_anios": 6,
  "habilidades_clave": ["Python", "FastAPI", "PostgreSQL", "Docker"],
  "educacion": "Licenciatura en Ingeniería de Sistemas",
  "experiencia_relevante": "6 años trabajando con Python...",
  "fortalezas": [
    "Sólida experiencia en backend",
    "Conocimiento de arquitecturas modernas",
    "Capacidad de liderazgo técnico"
  ],
  "areas_mejora": [
    "Experiencia limitada en DevOps",
    "Poca exposición a sistemas distribuidos"
  ],
  "porcentaje_ajuste": 82
}
```

---

## 🔄 Detener la Aplicación

En la terminal donde está corriendo Streamlit, presiona:
```
CTRL + C
```

Para desactivar el entorno virtual:
```bash
deactivate
```

---

## 📝 Notas Importantes

- **Costos**: Cada evaluación consume tokens de OpenAI. Monitorea tu uso en https://platform.openai.com/usage
- **Privacidad**: Los CVs procesados se envían a OpenAI. Asegúrate de cumplir políticas de privacidad
- **Modelos**: El sistema usa `gpt-4o-mini`. Puedes cambiar el modelo en `services/cv_evaluator.py`

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios mayores:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

---

## 📧 Soporte

Para reportar problemas o sugerencias, abre un issue en el repositorio.

---

**Desarrollado con ❤️ usando Python, LangChain y Streamlit**
