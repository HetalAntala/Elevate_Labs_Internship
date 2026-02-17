import json
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet


def save_json(report, filename):
    Path("reports").mkdir(exist_ok=True)
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)


def save_pdf(report, filename):
    styles = getSampleStyleSheet()
    elements = []

    doc = SimpleDocTemplate(filename)

    elements.append(Paragraph("Web Vulnerability Scan Report", styles["Heading1"]))
    elements.append(Spacer(1, 20))

    elements.append(Paragraph(f"Target: {report['target']}", styles["Normal"]))
    elements.append(Paragraph(f"Risk Score: {report['risk_score']} ({report['rating']})", styles["Normal"]))
    elements.append(Spacer(1, 20))

    items = []
    for v in report["vulnerabilities"]:
        txt = f"{v['severity']} - {v['type']} - {v['evidence']}"
        items.append(ListItem(Paragraph(txt, styles["Normal"])))

    elements.append(ListFlowable(items))
    doc.build(elements)