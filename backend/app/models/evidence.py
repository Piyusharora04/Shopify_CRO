from pydantic import BaseModel, Field


class HomepageEvidence(BaseModel):
    title: str | None = None

    hero_heading: str | None = None

    hero_subheading: str | None = None

    hero_cta: str | None = None

    announcement_bar: bool = False

    search_present: bool = False

    account_present: bool = False

    wishlist_present: bool = False

    cart_present: bool = False

    navigation_links: list[str] = Field(default_factory=list)

    featured_collections: list[str] = Field(default_factory=list)

    trust_signals: list[str] = Field(default_factory=list)

    newsletter_present: bool = False

    footer_present: bool = False