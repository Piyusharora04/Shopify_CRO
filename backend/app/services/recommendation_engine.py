from app.models.evidence import HomepageEvidence
from app.models.pdp import PDPEvidence
from app.models.recommendation import (
    AuditReport,
    ExperimentBrief,
    Recommendation,
)


class RecommendationEngine:

    def generate(
        self,
        homepage: HomepageEvidence,
        products: list[PDPEvidence],
    ) -> AuditReport:

        strengths = []

        recommendations = []

        score = 100

        #
        # Homepage
        #

        if homepage.search_present:
            strengths.append("Site search is available.")

        else:

            score -= 8

            recommendations.append(
                Recommendation(
                    title="Search is Missing",
                    category="Homepage",
                    evidence="Search field was not detected.",
                    impact=8,
                    confidence=9,
                    effort=2,
                    recommendation="Expose search prominently in the header.",
                    experiment=ExperimentBrief(
                        hypothesis="Increasing search visibility will improve product discovery.",
                        primary_metric="Search Usage Rate",
                        duration="2 weeks",
                    ),
                )
            )
            
        #
        # Announcement Bar
        #

        if homepage.announcement_bar:

            strengths.append(
                "Announcement bar is present."
            )

        else:

            score -= 4

            recommendations.append(
                Recommendation(
                    title="Missing Announcement Bar",
                    category="Homepage",
                    evidence="No announcement bar detected.",
                    impact=4,
                    confidence=9,
                    effort=1,
                    recommendation="Add an announcement bar for promotions or shipping offers.",
                    experiment=ExperimentBrief(
                        hypothesis="Announcements improve campaign visibility.",
                        primary_metric="CTR",
                        duration="2 weeks",
                    ),
                )
            )


        #
        # Newsletter
        #

        if homepage.newsletter_present:

            strengths.append(
                "Newsletter signup detected."
            )

        else:

            score -= 5

            recommendations.append(
                Recommendation(
                    title="Newsletter Missing",
                    category="Homepage",
                    evidence="Newsletter signup could not be detected.",
                    impact=5,
                    confidence=8,
                    effort=2,
                    recommendation="Capture visitors before they leave.",
                    experiment=ExperimentBrief(
                        hypothesis="Email capture increases returning visitors.",
                        primary_metric="Email Signup Rate",
                        duration="3 weeks",
                    ),
                )
            )


        #
        # Footer
        #

        if homepage.footer_present:

            strengths.append(
                "Footer detected."
            )

        else:

            score -= 5

            recommendations.append(
                Recommendation(
                    title="Footer Missing",
                    category="Homepage",
                    evidence="Footer section missing.",
                    impact=5,
                    confidence=9,
                    effort=2,
                    recommendation="Provide navigation, policies and trust information in the footer.",
                    experiment=ExperimentBrief(
                        hypothesis="Complete footers increase trust.",
                        primary_metric="Bounce Rate",
                        duration="2 weeks",
                    ),
                )
            )


        #
        # Featured Collections
        #

        if len(homepage.featured_collections) >= 4:

            strengths.append(
                "Featured collections are highlighted."
            )

        else:

            score -= 4

            recommendations.append(
                Recommendation(
                    title="Few Featured Collections",
                    category="Homepage",
                    evidence=f"Only {len(homepage.featured_collections)} featured collections detected.",
                    impact=4,
                    confidence=8,
                    effort=2,
                    recommendation="Promote more popular collections on the homepage.",
                    experiment=ExperimentBrief(
                        hypothesis="Collection discovery increases browsing.",
                        primary_metric="Collection CTR",
                        duration="2 weeks",
                    ),
                )
            )


        #
        # Trust Signals
        #

        if homepage.trust_signals:

            strengths.append(
                "Homepage trust signals detected."
            )

        else:

            score -= 4

            recommendations.append(
                Recommendation(
                    title="Homepage Trust Signals Missing",
                    category="Homepage",
                    evidence="No homepage trust indicators detected.",
                    impact=4,
                    confidence=8,
                    effort=2,
                    recommendation="Highlight guarantees, reviews or secure checkout near the hero.",
                    experiment=ExperimentBrief(
                        hypothesis="Trust messaging increases confidence.",
                        primary_metric="Conversion Rate",
                        duration="2 weeks",
                    ),
                )
            )

        #
        # PDP
        #

        atc = sum(
            p.add_to_cart_present
            for p in products
        )

        if atc == len(products):

            strengths.append(
                "All analyzed PDPs contain an Add To Cart button."
            )

        else:

            score -= 10

            recommendations.append(
                Recommendation(
                    title="Missing Add To Cart",
                    category="PDP",
                    evidence=f"{len(products)-atc} of {len(products)} products lack an Add To Cart button.",
                    impact=10,
                    confidence=9,
                    effort=2,
                    recommendation="Ensure every PDP exposes a primary purchase action.",
                    experiment=ExperimentBrief(
                        hypothesis="Visible purchase CTAs improve conversion.",
                        primary_metric="Conversion Rate",
                        duration="2 weeks",
                    ),
                )
            )

        sticky = sum(
            p.sticky_add_to_cart
            for p in products
        )

        if sticky == 0:

            score -= 8

            recommendations.append(
                Recommendation(
                    title="No Sticky Add To Cart",
                    category="PDP",
                    evidence="Sticky purchase controls were not detected.",
                    impact=9,
                    confidence=8,
                    effort=4,
                    recommendation="Introduce a sticky Add To Cart bar on scroll.",
                    experiment=ExperimentBrief(
                        hypothesis="Persistent purchase actions reduce friction.",
                        primary_metric="Add To Cart Rate",
                        duration="3 weeks",
                    ),
                )
            )
        
        #
        # Reviews
        #

        reviewed = sum(
            p.review_count is not None
            for p in products
        )

        if reviewed < len(products):

            score -= 5

            recommendations.append(
                Recommendation(
                    title="Missing Product Reviews",
                    category="PDP",
                    evidence=f"{len(products)-reviewed} products have no reviews.",
                    impact=6,
                    confidence=8,
                    effort=3,
                    recommendation="Display customer reviews consistently.",
                    experiment=ExperimentBrief(
                        hypothesis="Reviews improve purchase confidence.",
                        primary_metric="Conversion Rate",
                        duration="3 weeks",
                    ),
                )
            )


        #
        # Shipping Information
        #

        shipping = sum(
            p.shipping_information
            for p in products
        )

        if shipping < len(products):

            score -= 4

            recommendations.append(
                Recommendation(
                    title="Shipping Information Missing",
                    category="PDP",
                    evidence=f"{len(products)-shipping} products lack shipping information.",
                    impact=5,
                    confidence=8,
                    effort=2,
                    recommendation="Display shipping information close to the CTA.",
                    experiment=ExperimentBrief(
                        hypothesis="Transparent shipping reduces abandonment.",
                        primary_metric="Checkout Rate",
                        duration="2 weeks",
                    ),
                )
            )


        #
        # Returns
        #

        returns = sum(
            p.returns_information
            for p in products
        )

        if returns < len(products):

            score -= 4

            recommendations.append(
                Recommendation(
                    title="Returns Information Missing",
                    category="PDP",
                    evidence=f"{len(products)-returns} products lack return information.",
                    impact=5,
                    confidence=8,
                    effort=2,
                    recommendation="Surface return policy near Add To Cart.",
                    experiment=ExperimentBrief(
                        hypothesis="Easy returns reduce purchase anxiety.",
                        primary_metric="Conversion Rate",
                        duration="2 weeks",
                    ),
                )
            )


        #
        # Size Guide
        #

        size_guides = sum(
            p.size_guide_present
            for p in products
        )

        if size_guides < len(products):

            score -= 4

            recommendations.append(
                Recommendation(
                    title="Missing Size Guide",
                    category="PDP",
                    evidence=f"{len(products)-size_guides} products lack a size guide.",
                    impact=6,
                    confidence=9,
                    effort=2,
                    recommendation="Provide a visible size guide.",
                    experiment=ExperimentBrief(
                        hypothesis="Size guidance reduces returns.",
                        primary_metric="Return Rate",
                        duration="4 weeks",
                    ),
                )
            )


        #
        # Product Images
        #

        low_images = sum(
            p.image_count < 6
            for p in products
        )

        if low_images:

            score -= 3

            recommendations.append(
                Recommendation(
                    title="Low Product Image Count",
                    category="PDP",
                    evidence=f"{low_images} products contain fewer than 6 images.",
                    impact=4,
                    confidence=7,
                    effort=3,
                    recommendation="Use multiple product images showing different angles.",
                    experiment=ExperimentBrief(
                        hypothesis="More imagery improves buyer confidence.",
                        primary_metric="Conversion Rate",
                        duration="3 weeks",
                    ),
                )
            )


        #
        # Variants
        #

        variant_products = sum(
            len(p.variants) > 0
            for p in products
        )

        if variant_products < len(products):

            score -= 3

            recommendations.append(
                Recommendation(
                    title="Variant Selection Missing",
                    category="PDP",
                    evidence=f"{len(products)-variant_products} products expose no selectable variants.",
                    impact=4,
                    confidence=7,
                    effort=2,
                    recommendation="Clearly display size and color options.",
                    experiment=ExperimentBrief(
                        hypothesis="Visible variants reduce friction.",
                        primary_metric="Add To Cart Rate",
                        duration="2 weeks",
                    ),
                )
            )


        #
        # Trust Badges
        #

        trust = sum(
            len(p.trust_badges) > 0
            for p in products
        )

        if trust < len(products):

            score -= 4

            recommendations.append(
                Recommendation(
                    title="Trust Badges Missing",
                    category="PDP",
                    evidence=f"{len(products)-trust} products lack trust badges.",
                    impact=5,
                    confidence=8,
                    effort=2,
                    recommendation="Display secure checkout and payment trust badges.",
                    experiment=ExperimentBrief(
                        hypothesis="Trust badges reduce hesitation.",
                        primary_metric="Conversion Rate",
                        duration="2 weeks",
                    ),
                )
            )

        return AuditReport(
            score=max(0, min(score, 100)),
            strengths=strengths,
            opportunities=recommendations,
        )