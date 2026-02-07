from pydantic import BaseModel, Field

class AnalisisCV(BaseModel):
    nombre_candidato: str = Field(description="Nombre del candidato")
    experiencia_anios: int = Field(description="Años de experiencia laboral")
    habilidades_clave: list[str] = Field(description="Lista de habilidades del candidato")
    educacion : str = Field(description="Nivel educativo del candidato y especialización")
    experiencia_relevante: str = Field(description="Descripción de la experiencia laboral más relevante")
    fortalezas: list[str] = Field(description="3-5 principales fortalezas del candidato")
    areas_mejora: list[str] = Field(description="2-4 áreas de mejora del candidato")
    porcentaje_ajuste: int = Field(description="Porcentaje de ajuste (0-100) del candidato al perfil requerido, basado en las habilidades")
