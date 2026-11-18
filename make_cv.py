from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.HexColor("#666666"))
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(40, 755, 572, 755)
        self.drawString(40, 760, "Truptimayee Majhi — Curriculum Vitae (IIT Madras Internship Application)")
        self.line(40, 42, 572, 42)
        self.drawString(40, 30, "Utkal University | Independent Computational Biology & Ecology Research")
        self.drawRightString(572, 30, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

doc = SimpleDocTemplate(
    "Truptimayee_Majhi_CV.pdf",
    pagesize=letter,
    leftMargin=40,
    rightMargin=40,
    topMargin=46,
    bottomMargin=46
)

styles = getSampleStyleSheet()
name_style = ParagraphStyle("Name", fontName="Helvetica-Bold", fontSize=15, leading=17, textColor=colors.HexColor("#111111"))
contact_style = ParagraphStyle("Contact", fontName="Helvetica", fontSize=8, leading=11, textColor=colors.HexColor("#444444"))
sec_style = ParagraphStyle("Section", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=colors.HexColor("#002B49"), spaceBefore=7, spaceAfter=3, keepWithNext=True)
body_style = ParagraphStyle("Body", fontName="Helvetica", fontSize=8, leading=11, textColor=colors.HexColor("#222222"), spaceAfter=3)
proj_title = ParagraphStyle("ProjTitle", fontName="Helvetica-Bold", fontSize=8.5, leading=11.5, textColor=colors.HexColor("#111111"), spaceBefore=4, spaceAfter=1.5, keepWithNext=True)
bullet_style = ParagraphStyle("Bullet", fontName="Helvetica", fontSize=7.8, leading=10.8, textColor=colors.HexColor("#222222"), leftIndent=12, firstLineIndent=-12, spaceAfter=2)

story = []

# --- Header with Clickable Links ---
story.append(Paragraph("TRUPTIMAYEE MAJHI", name_style))
header_line = (
    'Bhubaneswar, Odisha, India | '
    '<a href="mailto:truptimayeemajhi5@gmail.com" color="#004488"><u>truptimayeemajhi5@gmail.com</u></a> | '
    '<a href="https://github.com/truptimayeemajhi5-cmd" color="#004488"><u>github.com/truptimayeemajhi5-cmd</u></a>'
)
story.append(Paragraph(header_line, contact_style))
story.append(Spacer(1, 4))

# --- Research Objective ---
story.append(Paragraph("RESEARCH OBJECTIVE", sec_style))
story.append(Paragraph("Aspiring computational biologist and field researcher seeking a Research Internship in Dr. Anushka Gupta’s laboratory at IIT Madras. Eager to combine rigorous empirical field observation, foundational Zoology training, and reproducible computational workflows (Python, Scanpy, data pipelining) to advance high-resolution biological modeling, community ecology, and single-cell genomics.", body_style))

# --- Education ---
story.append(Paragraph("EDUCATION", sec_style))
edu_data = [
    ["DEGREE / EXAMINATION", "INSTITUTION", "YEAR", "PERFORMANCE"],
    ["B.Sc. (Hons.) in Zoology", "Utkal University, Bhubaneswar, Odisha", "2023", "74.0% (First Class Distinction)"]
]
edu_table = Table(edu_data, colWidths=[150, 240, 50, 92])
edu_table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#F4F6F8")),
    ("TEXTCOLOR", (0,0), (-1,0), colors.HexColor("#002B49")),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 7.5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ("TOPPADDING", (0,0), (-1,-1), 3),
    ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#D0D0D0")),
    ("ALIGN", (2,0), (-1,-1), "CENTER"),
]))
story.append(edu_table)
story.append(Spacer(1, 2))
story.append(Paragraph("<b>Relevant Coursework:</b> Cell & Molecular Biology, Genetics & Evolutionary Biology, Animal Physiology, Biostatistics & Research Methodology, Ecology & Environmental Management.", bullet_style))

# --- Research & Computational Projects ---
story.append(Paragraph("RESEARCH & COMPUTATIONAL PROJECTS", sec_style))

p1_heading = (
    '<b>NeuroGenesis: In Silico Single-Cell Manifold Benchmarking</b> | '
    '<a href="https://github.com/truptimayeemajhi5-cmd/NeuroGenesis" color="#004488"><u>GitHub Repo</u></a> '
    '<font color="#666666">(2026)</font>'
)
story.append(Paragraph(p1_heading, proj_title))
story.append(Paragraph("• Architected an automated single-cell RNA-sequencing (scRNA-seq) workflow in Python utilizing <b>Scanpy, AnnData</b>, NumPy, and SciPy.", bullet_style))
story.append(Paragraph("• Benchmarked high-dimensional manifold learning and dimensionality reduction algorithms across open-access neurogenomic datasets (SEA-AD and NCBI GEO).", bullet_style))
story.append(Paragraph("• Engineered end-to-end data processing: adaptive cell quality control, highly variable gene (HVG) selection, PCA, neighbor graph construction, and UMAP trajectory visualization.", bullet_style))
zenodo_bullet = (
    '• Authored full open-access monograph archived on Zenodo (DOI: '
    '<a href="https://doi.org/10.5281/zenodo.23970631" color="#004488"><u>10.5281/zenodo.23970631</u></a>).'
)
story.append(Paragraph(zenodo_bullet, bullet_style))

p2_heading = (
    '<b>Avian Community Ecology & Microhabitat Partitioning</b> | '
    '<a href="https://github.com/truptimayeemajhi5-cmd/Avian_Ecotone_Odisha" color="#004488"><u>GitHub Repo</u></a> '
    '<font color="#666666">(2024–2026)</font>'
)
story.append(Paragraph(p2_heading, proj_title))
story.append(Paragraph("• Conducted systematic field censuses across coastal wetland–terrestrial ecotones in Odisha, enumerating 1,557 detections across five comprehensive field checklists.", bullet_style))
story.append(Paragraph("• Standardized avian taxonomy adhering strictly to <b>IOC World Bird List (v14.1)</b>, mapping species to five specialized trophic guilds and microhabitat zones.", bullet_style))
story.append(Paragraph("• Developed an automated image processing pipeline (<code>make_plates.py</code>) using Python (PIL) to curate high-resolution composite taxonomic voucher plates with empirical behavioral metadata.", bullet_style))
story.append(Paragraph("• Established fully reproducible analysis scripts (<code>make_matrix.py</code>, <code>run_analysis.py</code>) for biodiversity index calculations and guild relative abundance modeling.", bullet_style))

# --- Technical Skills ---
story.append(Paragraph("TECHNICAL & METHODOLOGICAL SKILLS", sec_style))
skills_data = [
    ["Computational Biology:", "Python, Scanpy, AnnData, NumPy, Pandas, SciPy, Matplotlib, ReportLab"],
    ["Bioinformatics Tooling:", "scRNA-seq preprocessing, cell filtering, HVG selection, clustering, UMAP/PCA"],
    ["Field & Ecological Biology:", "Line transects, point counts, voucher curation, avian taxonomy (IOC 14.1), guild zoning"],
    ["Version Control & Open Science:", "Git, GitHub (public data workflows), Linux/Bash, Markdown, LaTeX formatting"]
]
skills_table = Table(skills_data, colWidths=[140, 392])
skills_table.setStyle(TableStyle([
    ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 7.5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ("TOPPADDING", (0,0), (-1,-1), 2),
    ("LEFTPADDING", (0,0), (-1,-1), 2),
    ("RIGHTPADDING", (0,0), (-1,-1), 2),
    ("TEXTCOLOR", (0,0), (0,-1), colors.HexColor("#002B49")),
    ("TEXTCOLOR", (1,0), (1,-1), colors.HexColor("#222222")),
]))
story.append(skills_table)

# --- Field Experience & Scientific Leadership ---
story.append(Paragraph("FIELD EXPERIENCE & SCIENTIFIC LEADERSHIP", sec_style))
story.append(Paragraph("<b>Volunteer Field Guide & Avian Monitor</b> | Nandankanan Wetlands, Odisha <font color=\"#666666\">(2024 – Present)</font>", proj_title))
story.append(Paragraph("• Conduct systematic weekly bird censuses, public natural history walks, and waterfowl monitoring across wetland peripheries.", bullet_style))
story.append(Paragraph("• Track breeding, nesting, and foraging phenology of resident aquatic specialists, including IUCN Near Threatened taxa (<i>Anhinga melanogaster</i>).", bullet_style))

story.append(Paragraph("<b>Founder & President</b> | Ambika Impact Foundation <font color=\"#666666\">(Jan 2024 – Present)</font>", proj_title))
story.append(Paragraph("• Spearhead grassroots ecological literacy, biodiversity conservation drives, and community education workshops across peri-urban and rural Odisha.", bullet_style))

story.append(Paragraph("<b>Youth Delegate & Ambassador</b> | International Youth Conference (IYC14), New York <font color=\"#666666\">(Sept 2026)</font>", proj_title))
story.append(Paragraph("• Selected as IOY Global Ambassador; collaborated with international delegates on environmental stewardship, biodiversity policy, and grassroots scientific leadership.", bullet_style))

# --- Fellowships, Certifications & Military Training ---
story.append(Paragraph("FELLOWSHIPS, CERTIFICATIONS & MILITARY TRAINING", sec_style))
story.append(Paragraph("• <b>Aspire Leaders Program Fellow (2026):</b> Selected for leadership development founded by Harvard Business School faculty; focusing on systems thinking and cross-disciplinary impact.", bullet_style))
story.append(Paragraph("• <b>Handshake AI Fellowship Contributor (Project Seal, 2026):</b> Evaluated domain-specific biological reasoning and prompt data calibration for computational models.", bullet_style))
story.append(Paragraph("• <b>Elements of AI Certification:</b> University of Helsinki / Reaktor (Computational logic and algorithms).", bullet_style))
story.append(Paragraph("• <b>National Cadet Corps (NCC, 2020 – 2023):</b> Senior Under Officer (SUO); awarded <b>NCC 'C' Certificate</b>. Commanded a contingent of 70+ cadets; led state-level training camps, disaster response drills, and environmental conservation operations.", bullet_style))

# --- Publications & Scholarly Preprints ---
story.append(Paragraph("PUBLICATIONS & SCHOLARLY PREPRINTS", sec_style))
zenodo_pub = (
    '• Majhi, T. (2026). Comparative Single-Cell Manifold Benchmarking in Neurogenomics. <i>Zenodo Open Research Archive</i>. DOI: '
    '<a href="https://doi.org/10.5281/zenodo.23970631" color="#004488"><u>10.5281/zenodo.23970631</u></a>.'
)
story.append(Paragraph(zenodo_pub, bullet_style))

avian_pub = (
    '• Majhi, T. (2026). Microhabitat Partitioning, Trophic Guild Structure, and Avian Community Assembly Across a Wetland–Terrestrial Ecotone in Coastal Odisha. '
    '(<a href="https://github.com/truptimayeemajhi5-cmd/Avian_Ecotone_Odisha" color="#004488"><u>Preprint & Open Data Archive, GitHub</u></a>).'
)
story.append(Paragraph(avian_pub, bullet_style))
story.append(Paragraph("• Majhi, T. (2024). The Unspoken Curriculum: Childhood, Masculinity, and the Making of Modern India. <i>Youth Ki Awaaz</i>.", bullet_style))

# --- ACADEMIC REFERENCES ---
story.append(Paragraph("ACADEMIC REFERENCES", sec_style))

ref_data = [
    [
        Paragraph(
            "<b>Dr. Jyotsnarani Pradhan</b><br/>"
            "Assistant Professor (Stage-II), Dept. of Biotechnology<br/>"
            "Utkal University, Vani Vihar, Bhubaneswar, Odisha<br/>"
            "Email: jyotsna.biotech@utkaluniversity.ac.in<br/>"
            "Mobile: +91 98534 1196",
            body_style
        ),
        Paragraph(
            "<b>Dr. Sanatan Majhi</b><br/>"
            "Assistant Professor, Dept. of Biotechnology<br/>"
            "Utkal University, Vani Vihar, Bhubaneswar, Odisha<br/>"
            "Email: sanatan.biotech@utkaluniversity.ac.in<br/>"
            "Mobile: +91 93379 40244",
            body_style
        )
    ]
]

ref_table = Table(ref_data, colWidths=[200, 332])
ref_table.setStyle(TableStyle([
    ("FONTNAME", (0,0), (-1,-1), "Helvetica"),
    ("FONTSIZE", (0,0), (-1,-1), 7.5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ("TOPPADDING", (0,0), (-1,-1), 2),
    ("TEXTCOLOR", (0,0), (-1,-1), colors.HexColor("#333333")),
]))
story.append(ref_table)

doc.build(story, canvasmaker=NumberedCanvas)
print("SUCCESS: Hyperlinks embedded and active!")