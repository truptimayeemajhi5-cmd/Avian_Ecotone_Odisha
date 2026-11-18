import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak

doc = SimpleDocTemplate(
    "Avian_Ecotone_Odisha_Draft.pdf",
    pagesize=letter,
    leftMargin=54,
    rightMargin=54,
    topMargin=54,
    bottomMargin=54
)

styles = getSampleStyleSheet()
title_style = ParagraphStyle("Title", fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=colors.HexColor("#111111"), spaceAfter=8)
h1_style = ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=11.5, leading=15, textColor=colors.HexColor("#002B49"), spaceBefore=12, spaceAfter=4, keepWithNext=True)
h2_style = ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=colors.HexColor("#222222"), spaceBefore=8, spaceAfter=3, keepWithNext=True)
body_style = ParagraphStyle("Body", fontName="Helvetica", fontSize=9.5, leading=13.5, textColor=colors.HexColor("#222222"), spaceAfter=6)
caption_style = ParagraphStyle("Caption", fontName="Helvetica-Oblique", fontSize=8.5, leading=11.5, textColor=colors.HexColor("#444444"), spaceBefore=4, spaceAfter=12)

story = []

# Read the Markdown Manuscript
md_file = "Avian_Ecotone_Odisha_Manuscript.md"
if os.path.exists(md_file):
    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        text = line.strip()
        if not text:
            continue
        # Convert basic markdown bold/italics to ReportLab XML tags
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
        text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)

        if text.startswith("# "):
            story.append(Paragraph(text[2:], title_style))
        elif text.startswith("## "):
            story.append(Paragraph(text[3:], h1_style))
        elif text.startswith("### "):
            story.append(Paragraph(text[4:], h2_style))
        elif text.startswith("|"):
            # Render markdown table rows cleanly in monospace/compact text
            story.append(Paragraph(f"<font name='Courier' size='7.5'>{text}</font>", body_style))
        else:
            story.append(Paragraph(text, body_style))
else:
    story.append(Paragraph("Avian Community Ecology & Microhabitat Partitioning in Coastal Odisha (Working Draft)", title_style))

# Append High-Resolution Voucher Plates
plates = [
    ("figures/Plate_1_Wetland_Specialists.png", "Plate 1: Wetland Specialists & Littoral Foragers documented across coastal Odisha ecotones."),
    ("figures/Plate_2_Canopy_Guilds.png", "Plate 2: Arboreal Canopy & Terrestrial Trophic Guilds documented across coastal Odisha ecotones.")
]

for img_path, caption in plates:
    if os.path.exists(img_path):
        story.append(PageBreak())
        # Scale width to fit cleanly within page margins (max width ~480pt)
        img = Image(img_path, width=480, height=340, kind='proportional')
        story.append(img)
        story.append(Paragraph(caption, caption_style))

doc.build(story)
print("SUCCESS: Avian_Ecotone_Odisha_Draft.pdf created!")