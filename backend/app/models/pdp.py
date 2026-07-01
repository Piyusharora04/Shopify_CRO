from pydantic import BaseModel, Field


class PDPEvidence(BaseModel):
    url: str

    title: str | None = None

    currency: str | None = None

    price: float | None = None

    compare_at_price: float | None = None

    discount_percent: int | None = None

    rating: float | None = None

    review_count: int | None = None

    add_to_cart_present: bool = False

    sticky_add_to_cart: bool = False

    shipping_information: bool = False

    returns_information: bool = False

    size_guide_present: bool = False

    breadcrumbs_present: bool = False

    image_count: int = 0

    variants: list[str] = Field(default_factory=list)

    trust_badges: list[str] = Field(default_factory=list)