from pydantic import BaseModel


class ExperimentBrief(BaseModel):
    hypothesis: str
    primary_metric: str
    duration: str


class Recommendation(BaseModel):
    title: str
    category: str
    evidence: str

    impact: int
    confidence: int
    effort: int

    recommendation: str

    experiment: ExperimentBrief


class AuditReport(BaseModel):
    score: int

    strengths: list[str]

    opportunities: list[Recommendation]