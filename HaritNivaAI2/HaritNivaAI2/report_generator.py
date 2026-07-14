from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


def create_report(filename, data):

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>Vistaar AI Farm Report</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    for key, value in data.items():

        story.append(
            Paragraph(
                f"<b>{key}:</b> {value}",
                styles["BodyText"]
            )
        )

    doc.build(story)