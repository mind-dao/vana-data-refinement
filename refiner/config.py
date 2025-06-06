from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    """Global settings configuration using environment variables"""
    
    INPUT_DIR: str = Field(
        default="input",
        description="Directory containing input files to process"
    )
    
    OUTPUT_DIR: str = Field(
        default="output",
        description="Directory where output files will be written"
    )
    
    REFINEMENT_ENCRYPTION_KEY: str = Field(
        default=None,
        description="Key to symmetrically encrypt the refinement. This is derived from the original file encryption key"
    )
    
    PINATA_API_KEY: Optional[str] = Field(
        default=None,
        description="Pinata API key"
    )
    
    PINATA_API_SECRET: Optional[str] = Field(
        default=None,
        description="Pinata API secret"
    )
    
    SCHEMA_NAME: str = Field(
        default="Weekly Mind Check",
        description="Name of the schema"
    )
    
    SCHEMA_VERSION: str = Field(
        default="1.0.0",
        description="Version of the schema"
    )
    
    SCHEMA_DESCRIPTION: str = Field(
        default="Schema for weekly mind check data using the Positive and Negative Affect Schedule (PANAS) and demographic information",
        description="Description of the schema"
    )
    
    SCHEMA_DIALECT: str = Field(
        default="sqlite",
        description="Dialect of the schema"
    )
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 