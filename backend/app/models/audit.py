from pydantic import BaseModel, Field
from typing import List, Literal


class AnalyzeRequest(BaseModel):
    url: str


class StoreStats(BaseModel):
    products: int
    collections: int
    pagesAnalyzed: int


class Opportunity(BaseModel):
    id: str
    title: str
    category: Literal[
        "PDP",
        "Collections",
        "Cart",
        "Merchandising",
    ]

    evidence: str
    recommendation: str

    impact: int = Field(ge=1, le=10)
    confidence: int = Field(ge=1, le=10)
    effort: int = Field(ge=1, le=10)

    priority: int


class AuditResponse(BaseModel):
    storeName: str
    overallScore: int

    stats: StoreStats

    opportunities: List[Opportunity]