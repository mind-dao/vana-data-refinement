from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class PanasRating(BaseModel):
    interested: int = Field(ge=1, le=5, default=3)
    distressed: int = Field(ge=1, le=5, default=3)
    excited: int = Field(ge=1, le=5, default=3)
    upset: int = Field(ge=1, le=5, default=3)
    strong: int = Field(ge=1, le=5, default=3)
    guilty: int = Field(ge=1, le=5, default=3)
    scared: int = Field(ge=1, le=5, default=3)
    hostile: int = Field(ge=1, le=5, default=3)
    enthusiastic: int = Field(ge=1, le=5, default=3)
    proud: int = Field(ge=1, le=5, default=3)
    irritable: int = Field(ge=1, le=5, default=3)
    alert: int = Field(ge=1, le=5, default=3)
    ashamed: int = Field(ge=1, le=5, default=3)
    inspired: int = Field(ge=1, le=5, default=3)
    nervous: int = Field(ge=1, le=5, default=3)
    determined: int = Field(ge=1, le=5, default=3)
    attentive: int = Field(ge=1, le=5, default=3)
    jittery: int = Field(ge=1, le=5, default=3)
    active: int = Field(ge=1, le=5, default=3)
    afraid: int = Field(ge=1, le=5, default=3)


class Location(str, Enum):
    NORTH_AMERICA = "North America"
    SOUTH_AMERICA = "South America"
    EUROPE = "Europe"
    AFRICA = "Africa"
    ASIA = "Asia"
    AUSTRALIA_PACIFIC = "Australia and Pacific"
    MIDDLE_EAST_NORTH_AFRICA = "Middle East and North Africa"
    CARIBBEAN = "Caribbean"
    MULTIPLE_REGIONS = "Multiple regions"
    PREFER_NOT_TO_SAY = "Prefer not to say"


class RaceEthnicity(str, Enum):
    AMERICAN_INDIAN_ALASKA_NATIVE = "American Indian or Alaska Native"
    ASIAN = "Asian"
    BLACK_AFRICAN_AMERICAN = "Black or African American"
    HISPANIC_LATINO = "Hispanic or Latino"
    MIDDLE_EASTERN_NORTH_AFRICAN = "Middle Eastern or North African"
    NATIVE_HAWAIIAN_PACIFIC_ISLANDER = "Native Hawaiian or Other Pacific Islander"
    WHITE = "White"
    MULTIPLE_ETHNICITIES = "Multiple ethnicities"
    PREFER_NOT_TO_SAY = "Prefer not to say"


class GenderIdentity(str, Enum):
    WOMAN = "Woman"
    MAN = "Man"
    NON_BINARY = "Non-binary"
    TRANSGENDER = "Transgender"
    GENDERQUEER = "Genderqueer"
    AGENDER = "Agender"
    ANOTHER_GENDER = "Another gender identity"
    PREFER_NOT_TO_SAY = "Prefer not to say"


class MindCheck(BaseModel):
    panas: PanasRating
    bestThing: str = Field(max_length=500)
    worstThing: str = Field(max_length=500)
    location: Location
    raceEthnicity: RaceEthnicity
    genderIdentity: GenderIdentity
