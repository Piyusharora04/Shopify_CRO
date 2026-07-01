from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


class PDFExporter:

    def export(
        self,
        report,
        homepage,
        products,
        filepath,
    ):

        doc = SimpleDocTemplate(filepath)

        story = []

        story.append(
            Paragraph(
                "<b>Shopify CRO Audit Report</b>",
                styles["Heading1"],
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                f"<b>Overall Score:</b> {report.score}/100",
                styles["Heading2"],
            )
        )

        story.append(Spacer(1, 12))

        story.append(
            Paragraph(
                "<b>Homepage</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                homepage.title,
                styles["BodyText"],
            )
        )

        story.append(Spacer(1, 12))

        story.append(
            Paragraph(
                f"Products Analysed: {len(products)}",
                styles["BodyText"],
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                "<b>Recommendations</b>",
                styles["Heading2"],
            )
        )

        for rec in report.opportunities:

            story.append(
                Paragraph(
                    f"<b>{rec.title}</b>",
                    styles["Heading3"],
                )
            )

            story.append(
                Paragraph(
                    rec.evidence,
                    styles["BodyText"],
                )
            )

            story.append(
                Paragraph(
                    f"Recommendation: {rec.recommendation}",
                    styles["BodyText"],
                )
            )

            story.append(
                Paragraph(
                    f"Impact: {rec.impact} | Confidence: {rec.confidence} | Effort: {rec.effort}",
                    styles["BodyText"],
                )
            )

            story.append(Spacer(1, 12))

        doc.build(story)