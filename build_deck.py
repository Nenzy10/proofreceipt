#!/usr/bin/env python3
"""ProofReceipt pitch deck — built ONLY from approved copy in INVESTOR_EMAIL.md / PROMOTION.md."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, HRFlowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

OUT = "/home/hatch/workspace/crypto-earn/saas/ProofReceipt_Pitch_Deck.pdf"

INK = HexColor("#101418")
ACCENT = HexColor("#0B7285")
LIGHT = HexColor("#5B6770")
BG = HexColor("#F4F7F8")

def st(name, size, leading, color=INK, bold=False, space=6):
    return ParagraphStyle(name, fontName="Helvetica-Bold" if bold else "Helvetica",
                          fontSize=size, leading=leading, textColor=color,
                          alignment=TA_LEFT, spaceAfter=space)

H1 = st("H1", 30, 36, bold=True, space=10)
H2 = st("H2", 20, 26, bold=True, space=8)
BODY = st("BODY", 12.5, 18, space=8)
SMALL = st("SMALL", 10.5, 15, color=LIGHT, space=6)
BIG = st("BIG", 15, 21, space=8)

def foot(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 8.5)
    canv.setFillColor(LIGHT)
    canv.drawString(20*mm, 12*mm, "ProofReceipt — proof-of-delivery for the agent economy")
    canv.drawRightString(A4[0]-20*mm, 12*mm, "proofreceipt.netlify.app")
    canv.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=22*mm, bottomMargin=20*mm,
                        title="ProofReceipt — Pitch Deck", author="Nenzy Brown")
E = []

# Page 1 — Title
E.append(Spacer(1, 30*mm))
E.append(Paragraph("ProofReceipt", H1))
E.append(Paragraph("The proof-of-delivery layer for the agent economy.", BIG))
E.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceAfter=10))
E.append(Paragraph(
    "A seller seals any deliverable into a SHA-256 receipt bound to the client, the job and the amount. "
    "Anyone can verify byte-identical delivery — free, forever.", BODY))
E.append(Spacer(1, 8*mm))
E.append(Paragraph("Live today: https://proofreceipt.netlify.app", BODY))
E.append(Paragraph("Founder: Nenzy Brown · Dubai, UAE · njakoiemmanuel10@gmail.com", BODY))
E.append(PageBreak())

# Page 2 — Problem
E.append(Paragraph("The problem", H2))
E.append(Paragraph(
    "AI agents and freelancers now get paid instantly — stablecoins, x402, escrow — but delivery is "
    "still \u201ctrust me.\u201d Identity (ERC-8004) and payment rails are solved; verifying the work "
    "itself is not.", BODY))
E.append(Paragraph(
    "A 2026 study of the ERC-8004 agent registry found <b>86.8%</b> of rated agents had no valid "
    "feedback after Sybil filtering.", BODY))
E.append(Paragraph(
    "Only <b>~5%</b> of users trust AI platforms to process agent payments.", BODY))
E.append(Paragraph(
    "When a client disputes, everyone re-litigates \u201cwhat was actually sent.\u201d There is no "
    "neutral, checkable record of the delivery itself.", BODY))
E.append(PageBreak())

# Page 3 — Product
E.append(Paragraph("The product", H2))
E.append(Paragraph("<b>Seal.</b> At delivery, the seller hashes the deliverable together with the "
                   "client, job and amount into a single SHA-256 receipt.", BODY))
E.append(Paragraph("<b>Share.</b> The receipt travels with the delivery — a link anyone can open.", BODY))
E.append(Paragraph("<b>Verify.</b> The client re-runs the check at any time. One byte different = no match.", BODY))
E.append(Paragraph(
    "Hashing runs entirely in the browser: files never leave the device, and infrastructure cost is $0. "
    "Verification is free, forever — for anyone.", BODY))
E.append(PageBreak())

# Page 4 — Business model
E.append(Paragraph("Business model", H2))
tbl = Table([
    ["Free", "5 receipts — verification always free"],
    ["Pro — $9/mo (USDC)", "For freelancers & individual agents"],
    ["Teams — $29/mo (USDC)", "Client countersign + verification API"],
], colWidths=[45*mm, 115*mm])
tbl.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), BG),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 11.5),
    ("LEADING", (0, 0), (-1, -1), 16),
    ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
]))
E.append(tbl)
E.append(Spacer(1, 6*mm))
E.append(Paragraph(
    "<b>The wedge:</b> every escrow, marketplace and agent platform needs a neutral delivery check. "
    "We sell the check — not another marketplace.", BODY))
E.append(Paragraph(
    "<b>Moat path:</b> the receipt standard, the verification API (Teams tier), and platform integrations.", BODY))
E.append(PageBreak())

# Page 5 — Status
E.append(Paragraph("Where we are — stated plainly", H2))
E.append(Paragraph("\u2022 Product live: https://proofreceipt.netlify.app", BODY))
E.append(Paragraph("\u2022 Launch coverage: dev.to and Hashnode (search \u201cProofReceipt\u201d); "
                   "open repo: github.com/Nenzy10/proofreceipt", BODY))
E.append(Paragraph("\u2022 Distribution running: content, directories, direct platform outreach", BODY))
E.append(Paragraph("\u2022 Infrastructure cost: $0 (browser-side hashing)", BODY))
E.append(Paragraph("\u2022 Revenue: $0 today — pre-revenue, first customers being onboarded now. "
                   "This is day one: product live, distribution running, no inflated traction claims.", BODY))
E.append(PageBreak())

# Page 6 — Founder / ask
E.append(Paragraph("Founder & the conversation", H2))
E.append(Paragraph(
    "<b>Nenzy Brown</b> — Dubai-based blockchain developer; founder of Cryptohost USD; years in smart "
    "contracts, DeFi and crypto-fiat integration.", BODY))
E.append(Paragraph(
    "We are opening a small number of investor conversations: pre-seed interest and angel intros for "
    "the verification layer of the agent economy. Dubai base, USDC-native revenue.", BODY))
E.append(Paragraph("Product: https://proofreceipt.netlify.app", BODY))
E.append(Paragraph("Contact: njakoiemmanuel10@gmail.com", BODY))

doc.build(E, onFirstPage=foot, onLaterPages=foot)
print("built", OUT)
