"""Pydantic models — single source of truth for the data contracts.

The files in ``schemas/*.schema.json`` are GENERATED from these models
(``fichamento schemas``). Never hand-edit the generated schemas; change
the model here and regenerate.
"""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Literal

from pydantic import BaseModel, Field, model_validator

SCHEMA_VERSION = "1.0.0"

SectionName = Literal[
    "executive_summary",
    "research_question",
    "theories",
    "key_concepts",
    "methodology",
    "main_findings",
    "contribution",
]
SECTIONS: list[str] = list(SectionName.__args__)  # type: ignore[attr-defined]

ErrorCode = Literal[
    "hallucination",
    "omission",
    "misinterpretation",
    "misattribution",
    "terminology",
    "extrapolation",
    "invalid_source_ref",
    "other",
]
ERROR_CODES: list[str] = list(ErrorCode.__args__)  # type: ignore[attr-defined]

# Provenance pointer into the line-marked markdown. Lines are numbered
# GLOBALLY across the document (L001…Lnnn); pages via p.N. Accepts ranges:
# "p.3", "p.104-106", "L302", "L161-180", "p.3/L12", "p.3/L12-15"
SourceRef = Annotated[
    str, Field(pattern=r"^(p\.\d+(-\d+)?(/L\d+(-\d+)?)?|L\d+(-\d+)?)$")
]
Score = Annotated[int, Field(ge=1, le=7, description="BARS 1-7")]


# ---------------------------------------------------------------- articles

class ArticleEntry(BaseModel):
    """One row of data/articles/registry.jsonl."""

    article_id: str = Field(pattern=r"^A\d{2}$")
    round: Literal[1, 2]
    nominated_by: str = Field(pattern=r"^J[1-4]$")
    title: str
    authors: list[str] = []
    year: int | None = None
    venue: str = ""
    doi: str = ""
    language: str = "en"
    pdf_path: str = ""
    notes: str = ""


# ------------------------------------------------------- ingestion manifest

class PageIngest(BaseModel):
    page: int
    n_lines: int
    n_chars: int
    method: Literal["text", "ocr", "empty", "manual"] = "text"
    needs_review: bool = False
    warnings: list[str] = []


class ManifestOverride(BaseModel):
    reason: str
    by: str = ""
    at: datetime


class IngestionManifest(BaseModel):
    """Proof that 100% of the PDF was converted to line-marked markdown."""

    schema_version: str = SCHEMA_VERSION
    article_id: str
    pdf_path: str
    pdf_sha256: str
    md_path: str
    md_sha256: str
    tool: str                       # e.g. "pymupdf 1.24.10"
    ocr_tool: str | None = None     # e.g. "tesseract 5.3.4"
    pages_pdf: int
    pages_extracted: int
    est_tokens: int = 0
    pages: list[PageIngest]
    coverage_complete: bool
    overrides: list[ManifestOverride] = []
    created_at: datetime


# ----------------------------------------------------- candidate pool
# For the "theories" section the instrument is CLOSED: a pool of candidate
# theories is extracted first (by AI, optionally curated), then students
# AND the AI (separate call) classify each item uses/discusses/does_not_use.

class CandidateItem(BaseModel):
    item_id: str = Field(pattern=r"^[A-Z]\d+$")   # T1, T2, …
    kind: Literal["theory", "concept"] = "theory"
    name: str
    definition: str = ""
    tradition: str = ""
    origin: Literal["ai", "judge", "researcher", "corpus"] = "ai"
    source_refs: list[SourceRef] = []
    active: bool = True  # curator deactivates instead of deleting


class PoolGenerator(BaseModel):
    provider: str
    model: str
    prompt_version: str
    at: datetime
    md_sha256: str = ""


class CandidatePool(BaseModel):
    schema_version: str = SCHEMA_VERSION
    article_id: str = Field(pattern=r"^A\d{2}$")
    round: Literal[1, 2]
    kind: Literal["theory"] = "theory"
    generated_by: PoolGenerator | None = None
    items: list[CandidateItem] = []
    curated: bool = False
    curated_by: str = ""
    notes: str = ""


class TheoryVerdict(BaseModel):
    """uses = theory structures the argument; discusses = debated/cited
    substantively; does_not_use = absent or merely decorative mention."""

    item_id: str
    name: str                    # echoed for readability of the JSON
    verdict: Literal["uses", "discusses", "does_not_use"]
    source_refs: list[SourceRef] = []
    quote: str = ""              # verbatim evidence supporting the verdict
    note: str = ""

    @model_validator(mode="after")
    def _positive_verdict_requires_evidence(self) -> "TheoryVerdict":
        if self.verdict in ("uses", "discusses") and not self.source_refs:
            raise ValueError(
                f"{self.item_id}: verdict '{self.verdict}' exige >=1 "
                "source_ref (p.N[/Lnn]) — aponte onde a teoria aparece"
            )
        return self


# -------------------------------------------------------------- fichamento

class Theory(BaseModel):
    name: str
    tradition: str = ""
    role: str = ""
    source_refs: list[SourceRef] = []


class KeyConcept(BaseModel):
    concept: str
    definition: str
    quote: str = ""              # verbatim quote anchoring the definition
    source_refs: list[SourceRef] = []


class Methodology(BaseModel):
    study_type: str = ""         # teórico | empírico | simulação | ...
    design: str                  # delineamento (survey, case study, conceptual…)
    sample_type: str = ""        # tipo de amostra ( firms, students, N/A…)
    sample_size: int | None = None
    sector: str = ""
    period: str = ""
    methods: list[str] = []      # técnicas de análise (tags p/ KG)
    analysis_note: str = ""      # descrição livre do método de análise
    source_refs: list[SourceRef] = []


class Finding(BaseModel):
    finding: str
    type: Literal["empirical", "proposition", "model"] = "empirical"
    quote: str = ""              # verbatim evidence
    source_refs: list[SourceRef] = []


class Contribution(BaseModel):
    theoretical: str
    practical: str = ""


class FichamentoContent(BaseModel):
    """The payload judges actually read — the same contract for AI and humans."""

    executive_summary: str
    research_question: str
    theories: list[Theory] = []
    theory_verdicts: list[TheoryVerdict] = []
    key_concepts: list[KeyConcept] = Field(min_length=3, max_length=4)
    methodology: Methodology
    main_findings: list[Finding] = Field(min_length=1)
    contribution: Contribution


class AIGenerator(BaseModel):
    kind: Literal["ai"] = "ai"
    provider: str
    model: str
    prompt_version: str
    temperature: float | None = None
    seed: int | None = None
    generated_at: datetime
    input_tokens: int | None = None
    output_tokens: int | None = None
    latency_s: float | None = None
    md_sha256: str = ""     # binds generation to the exact ingested document
    forced: bool = False    # True when generate ran with --force override
    verdicts_prompt_version: str | None = None  # prompt da classificação do pool


class HumanGenerator(BaseModel):
    kind: Literal["human"] = "human"
    participant_id: str = Field(pattern=r"^S\d{2}$")
    elapsed_minutes: int | None = None
    submitted_at: datetime | None = None


Generator = Annotated[
    AIGenerator | HumanGenerator, Field(discriminator="kind")
]


class HumanReview(BaseModel):
    """Post-calibration human review of an AI fichamento (scale phase)."""

    reviewed: bool = False
    reviewer_id: str = ""
    reviewed_at: datetime | None = None
    changes_summary: str = ""


class Fichamento(BaseModel):
    schema_version: str = SCHEMA_VERSION
    fichamento_id: str = Field(pattern=r"^F-R[12]-A\d{2}-(AI|HUM)$")
    article_id: str = Field(pattern=r"^A\d{2}$")
    round: Literal[1, 2]
    source: Literal["ai", "human"]
    generator: Generator
    content: FichamentoContent
    human_review: HumanReview = HumanReview()

    @model_validator(mode="after")
    def _generator_matches_source(self) -> "Fichamento":
        if self.generator.kind != self.source:
            raise ValueError(
                f"source={self.source!r} but generator.kind={self.generator.kind!r}"
            )
        return self


# -------------------------------------------------------------- evaluation

class SectionScores(BaseModel):
    executive_summary: Score
    research_question: Score
    theories: Score
    key_concepts: Score
    methodology: Score
    main_findings: Score
    contribution: Score


class ErrorFlag(BaseModel):
    code: ErrorCode
    sections: list[SectionName] = []
    note: str = ""


class Rating(BaseModel):
    """A judge's assessment of ONE blinded fichamento (position A or B)."""

    blind_id: str = Field(pattern=r"^B\d{2,}$")
    position: Literal["A", "B"]
    scores: SectionScores
    errors: list[ErrorFlag] = []
    would_question: str = ""
    missing: str = ""


class Preference(BaseModel):
    choice: Literal["A", "B", "tie"]
    reason: str = ""


class Evaluation(BaseModel):
    """One submission = one (judge x article): rates both blind fichamentos."""

    schema_version: str = SCHEMA_VERSION
    evaluation_id: str = Field(pattern=r"^E-R[12]-A\d{2}-J[1-4]$")
    round: Literal[1, 2]
    article_id: str = Field(pattern=r"^A\d{2}$")
    judge_id: str = Field(pattern=r"^J[1-4]$")
    confidence: int | None = Field(default=None, ge=1, le=3)
    ratings: list[Rating] = Field(min_length=2, max_length=2)
    preference: Preference
    submitted_at: datetime | None = None


# --------------------------------------------------------------- blinding

class BlindEntry(BaseModel):
    blind_id: str = Field(pattern=r"^B\d{2,}$")
    article_id: str
    fichamento_id: str
    source: Literal["ai", "human"]
    position: Literal["A", "B"]


class BlindingMap(BaseModel):
    """PRIVATE — lives under data/private/, published only after unblinding."""

    schema_version: str = SCHEMA_VERSION
    round: Literal[1, 2]
    seed: int
    created_at: datetime
    entries: list[BlindEntry]
