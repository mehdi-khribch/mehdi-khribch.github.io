from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Preformatted, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

NAVY = HexColor("#1b4f72")
LIGHT_BG = HexColor("#eaf2f8")
DARK_TEXT = HexColor("#2c3e50")
GRAY = HexColor("#7f8c8d")
CODE_BG = HexColor("#f4f6f8")

output_path = "/sessions/elegant-youthful-brahmagupta/mnt/quarto-site/files/quarto-site-workflow-guide.pdf"

doc = SimpleDocTemplate(
    output_path,
    pagesize=letter,
    topMargin=0.8 * inch,
    bottomMargin=0.8 * inch,
    leftMargin=1 * inch,
    rightMargin=1 * inch,
)

styles = getSampleStyleSheet()

# Custom styles
styles.add(ParagraphStyle(
    name='DocTitle',
    parent=styles['Title'],
    fontSize=22,
    textColor=NAVY,
    spaceAfter=6,
    fontName='Helvetica-Bold',
))

styles.add(ParagraphStyle(
    name='DocSubtitle',
    parent=styles['Normal'],
    fontSize=11,
    textColor=GRAY,
    spaceAfter=24,
    alignment=TA_CENTER,
    fontName='Helvetica',
))

styles.add(ParagraphStyle(
    name='SectionHead',
    parent=styles['Heading1'],
    fontSize=16,
    textColor=NAVY,
    spaceBefore=20,
    spaceAfter=10,
    fontName='Helvetica-Bold',
    borderWidth=0,
    borderPadding=0,
))

styles.add(ParagraphStyle(
    name='StepHead',
    parent=styles['Heading2'],
    fontSize=13,
    textColor=NAVY,
    spaceBefore=14,
    spaceAfter=6,
    fontName='Helvetica-Bold',
))

styles.add(ParagraphStyle(
    name='Body',
    parent=styles['Normal'],
    fontSize=10.5,
    textColor=DARK_TEXT,
    spaceAfter=8,
    leading=15,
    fontName='Helvetica',
))

styles.add(ParagraphStyle(
    name='CodeBlock',
    parent=styles['Code'],
    fontSize=9,
    fontName='Courier',
    textColor=HexColor("#1a1a2e"),
    backColor=CODE_BG,
    borderWidth=0.5,
    borderColor=HexColor("#d5dbdb"),
    borderPadding=8,
    leading=13,
    spaceAfter=10,
    spaceBefore=4,
))

styles.add(ParagraphStyle(
    name='Note',
    parent=styles['Normal'],
    fontSize=9.5,
    textColor=HexColor("#6c3483"),
    backColor=HexColor("#f5eef8"),
    borderWidth=0.5,
    borderColor=HexColor("#d2b4de"),
    borderPadding=8,
    spaceAfter=10,
    leading=14,
    fontName='Helvetica-Oblique',
))

styles.add(ParagraphStyle(
    name='FileLabel',
    parent=styles['Normal'],
    fontSize=9.5,
    textColor=HexColor("#117864"),
    fontName='Courier-Bold',
    spaceAfter=2,
))

story = []

# ── Title ──
story.append(Paragraph("Quarto Site Workflow Guide", styles['DocTitle']))
story.append(Paragraph("How to modify, render, and deploy your personal website", styles['DocSubtitle']))
story.append(Spacer(1, 6))

# ── Your Setup ──
story.append(Paragraph("Your Setup", styles['SectionHead']))
story.append(Paragraph(
    "Your website is a <b>Quarto project</b> hosted on <b>GitHub Pages</b>. "
    "You have two important folders on your Mac:",
    styles['Body']
))

data = [
    ["Folder", "Path", "What it is"],
    ["Quarto source", "/Users/mehdikhribch/Desktop/quarto-site", "Where you edit .qmd files, CSS, images, etc."],
    ["Git repository", "/Users/mehdikhribch/Desktop/mehdi-khribch.github.io", "The repo that GitHub Pages deploys from"],
]
t = Table(data, colWidths=[1.1*inch, 2.8*inch, 2.5*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), NAVY),
    ('TEXTCOLOR', (0, 0), (-1, 0), HexColor("#ffffff")),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BACKGROUND', (0, 1), (-1, -1), HexColor("#fdfefe")),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#d5dbdb")),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
    ('FONTNAME', (1, 1), (1, -1), 'Courier'),
]))
story.append(t)
story.append(Spacer(1, 6))

story.append(Paragraph(
    "When you push to the git repo, a <b>GitHub Actions workflow</b> (called \"Quarto Publish\") "
    "automatically renders the .qmd files and deploys the site. You do <b>not</b> need to copy "
    "rendered HTML manually \u2014 just push the source files.",
    styles['Body']
))

story.append(Paragraph(
    "<b>Note:</b> The quarto-site folder on your Desktop is your working copy. "
    "The git repo (mehdi-khribch.github.io) is the one connected to GitHub. "
    "After editing in quarto-site, you copy the changed files to the repo before committing.",
    styles['Note']
))

# ── The Workflow ──
story.append(Paragraph("The Workflow: Step by Step", styles['SectionHead']))

# Step 1
story.append(Paragraph("Step 1: Make your changes", styles['StepHead']))
story.append(Paragraph(
    "Open the file you want to edit in your Quarto source folder. "
    "You can use any text editor (VS Code, Sublime Text, TextEdit, nano, vim, etc.).",
    styles['Body']
))
story.append(Paragraph("Example: editing the publications page", styles['FileLabel']))
story.append(Preformatted(
    "open /Users/mehdikhribch/Desktop/quarto-site/publications.qmd",
    styles['CodeBlock']
))
story.append(Paragraph(
    "Common files you might edit:",
    styles['Body']
))
files_data = [
    ["File", "What it controls"],
    ["index.qmd", "Your homepage / About page"],
    ["publications.qmd", "Publications list"],
    ["education.qmd", "Education section"],
    ["teaching.qmd", "Teaching section"],
    ["talks.qmd", "Talks section"],
    ["cv.qmd", "CV page"],
    ["blog.qmd", "Blog listing page"],
    ["latex.css", "Custom CSS styling"],
    ["styles.scss", "SCSS theme overrides"],
    ["_quarto.yml", "Site-wide config (navbar, footer, etc.)"],
    ["posts/*/index.qmd", "Individual blog posts"],
    ["images/*", "Site images"],
]
ft = Table(files_data, colWidths=[1.8*inch, 4.5*inch])
ft.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), NAVY),
    ('TEXTCOLOR', (0, 0), (-1, 0), HexColor("#ffffff")),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (0, -1), 'Courier'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BACKGROUND', (0, 1), (-1, -1), HexColor("#fdfefe")),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#d5dbdb")),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
]))
story.append(ft)
story.append(Spacer(1, 4))

# Step 2
story.append(Paragraph("Step 2: Preview locally (optional but recommended)", styles['StepHead']))
story.append(Paragraph(
    "Before pushing, you can preview how the site will look by running Quarto's live preview server:",
    styles['Body']
))
story.append(Preformatted(
    "cd /Users/mehdikhribch/Desktop/quarto-site\nquarto preview",
    styles['CodeBlock']
))
story.append(Paragraph(
    "This opens a browser window at http://localhost:4200 (or similar) with a live-reloading preview. "
    "Press <b>Ctrl+C</b> in the terminal to stop it when you're done.",
    styles['Body']
))

# Step 3
story.append(PageBreak())
story.append(Paragraph("Step 3: Copy changed files to the git repo", styles['StepHead']))
story.append(Paragraph(
    "Copy only the files you changed from the Quarto source into the git repository. "
    "For example, if you edited publications.qmd and latex.css:",
    styles['Body']
))
story.append(Preformatted(
    "cp /Users/mehdikhribch/Desktop/quarto-site/publications.qmd \\\n"
    "   /Users/mehdikhribch/Desktop/mehdi-khribch.github.io/\n\n"
    "cp /Users/mehdikhribch/Desktop/quarto-site/latex.css \\\n"
    "   /Users/mehdikhribch/Desktop/mehdi-khribch.github.io/",
    styles['CodeBlock']
))
story.append(Paragraph(
    "For new folders (like files/bib/), use <b>cp -r</b> to copy recursively:",
    styles['Body']
))
story.append(Preformatted(
    "cp -r /Users/mehdikhribch/Desktop/quarto-site/files/bib \\\n"
    "      /Users/mehdikhribch/Desktop/mehdi-khribch.github.io/files/",
    styles['CodeBlock']
))
story.append(Paragraph(
    "<b>Tip:</b> If you're unsure what changed, run this to compare the two folders:<br/>"
    "<font face='Courier' size='9'>diff -rq quarto-site/ mehdi-khribch.github.io/ --exclude='.git' --exclude='docs' --exclude='_site'</font>",
    styles['Note']
))

# Step 4
story.append(Paragraph("Step 4: Stage and commit", styles['StepHead']))
story.append(Paragraph(
    "Navigate to the git repo, stage your changes, and create a commit:",
    styles['Body']
))
story.append(Preformatted(
    "cd /Users/mehdikhribch/Desktop/mehdi-khribch.github.io\n\n"
    "# Check what changed\n"
    "git status\n\n"
    "# Stage specific files\n"
    "git add publications.qmd latex.css\n\n"
    "# Or stage everything that changed\n"
    "git add -A\n\n"
    "# Commit with a descriptive message\n"
    'git commit -m "Update publications abstract"',
    styles['CodeBlock']
))

story.append(Paragraph(
    "<b>Note:</b> If git warns about your name/email, fix it once with:<br/>"
    "<font face='Courier' size='9'>git config --global user.name \"Mehdi Khribch\"</font><br/>"
    "<font face='Courier' size='9'>git config --global user.email \"french.montana67100@gmail.com\"</font>",
    styles['Note']
))

# Step 5
story.append(Paragraph("Step 5: Push to GitHub", styles['StepHead']))
story.append(Preformatted(
    "git push",
    styles['CodeBlock']
))
story.append(Paragraph(
    "Once pushed, the <b>Quarto Publish</b> GitHub Action will automatically render and deploy your site. "
    "It typically takes about 1 minute. You can monitor the build at:<br/>"
    "<font face='Courier' size='9'>https://github.com/mehdi-khribch/mehdi-khribch.github.io/actions</font>",
    styles['Body']
))

# Step 6
story.append(Paragraph("Step 6: Verify", styles['StepHead']))
story.append(Paragraph(
    "After the GitHub Action completes (green checkmark), hard-refresh your site to see the changes:",
    styles['Body']
))
story.append(Preformatted(
    "# Your site URL\nhttps://mehdi-khribch.github.io\n\n# Hard refresh in browser: Cmd + Shift + R",
    styles['CodeBlock']
))

# ── Quick Reference ──
story.append(PageBreak())
story.append(Paragraph("Quick Reference: Copy-Paste Commands", styles['SectionHead']))
story.append(Paragraph(
    "Here is the full sequence you can paste into Terminal every time you make changes. "
    "Replace the filenames with whatever you actually changed:",
    styles['Body']
))
story.append(Preformatted(
    "# 1. Go to your Quarto source and preview (optional)\n"
    "cd /Users/mehdikhribch/Desktop/quarto-site\n"
    "quarto preview\n"
    "# Press Ctrl+C when done previewing\n\n"
    "# 2. Copy changed files to git repo\n"
    "cp publications.qmd /Users/mehdikhribch/Desktop/mehdi-khribch.github.io/\n"
    "cp latex.css /Users/mehdikhribch/Desktop/mehdi-khribch.github.io/\n\n"
    "# 3. Go to repo, stage, commit, push\n"
    "cd /Users/mehdikhribch/Desktop/mehdi-khribch.github.io\n"
    "git add -A\n"
    'git commit -m "Your commit message here"\n'
    "git push",
    styles['CodeBlock']
))

# ── Troubleshooting ──
story.append(Paragraph("Troubleshooting", styles['SectionHead']))

troubles = [
    ['"fatal: not a git repository"',
     "You're in the wrong folder. Make sure you cd into\n"
     "/Users/mehdikhribch/Desktop/mehdi-khribch.github.io\n"
     "before running any git commands."],
    ['"nothing to commit"',
     "You forgot to copy the changed files from quarto-site\n"
     "to mehdi-khribch.github.io, or the files are identical."],
    ["Site not updating after push",
     "Wait 1-2 minutes for GitHub Actions to finish. Check\n"
     "the Actions tab on GitHub for errors. Then hard-refresh\n"
     "your browser with Cmd+Shift+R."],
    ["Authentication error on push",
     "Your GitHub token may have expired. Generate a new\n"
     "Personal Access Token at github.com/settings/tokens\n"
     "and use it as your password when prompted."],
]
trouble_data = [["Problem", "Solution"]] + troubles
tt = Table(trouble_data, colWidths=[2.2*inch, 4.2*inch])
tt.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), NAVY),
    ('TEXTCOLOR', (0, 0), (-1, 0), HexColor("#ffffff")),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (0, -1), 'Courier'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BACKGROUND', (0, 1), (-1, -1), HexColor("#fdfefe")),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#d5dbdb")),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('LEFTPADDING', (0, 0), (-1, -1), 6),
]))
story.append(tt)

# ── Key Concepts ──
story.append(Spacer(1, 14))
story.append(Paragraph("Key Concepts", styles['SectionHead']))

story.append(Paragraph(
    "<b>Quarto (.qmd files)</b> \u2014 Your source files are written in Quarto markdown, which "
    "combines regular text, LaTeX math, and special formatting directives. Quarto renders these "
    "into HTML, which is what visitors see on your website.",
    styles['Body']
))
story.append(Paragraph(
    "<b>Git</b> \u2014 A version control system that tracks every change you make. Each \"commit\" "
    "is a snapshot of your project. \"Push\" sends your commits to GitHub.",
    styles['Body']
))
story.append(Paragraph(
    "<b>GitHub Actions</b> \u2014 An automation service on GitHub. Your repo has a workflow called "
    "\"Quarto Publish\" that triggers on every push: it installs Quarto, renders the .qmd files "
    "into HTML, and deploys the result to GitHub Pages.",
    styles['Body']
))
story.append(Paragraph(
    "<b>GitHub Pages</b> \u2014 A free hosting service from GitHub. Your site at "
    "mehdi-khribch.github.io is served from whatever the GitHub Action produces.",
    styles['Body']
))

doc.build(story)
print(f"PDF created at {output_path}")
