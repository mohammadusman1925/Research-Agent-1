# -*- coding: utf-8 -*-
"""Convert a Master Concept guide page into Markdown and PDF.

Usage: python html_to_md_pdf.py <file.html> [<file.html> ...]
Writes <file>.md and <file>.pdf beside the source.
"""
import io, os, re, sys, html
from html.parser import HTMLParser
from fpdf import FPDF
from fpdf.fonts import FontFace
from fpdf.enums import TableCellFillMode

# ------------------------------------------------------------------ parse


class Guide(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks = []
        self.buf = []
        self.stack = []
        self.row = None
        self.table = None
        self.head = None
        self.in_cell = False
        self.cell_hl = False
        self.mode = None      # current text sink
        self.col = None       # 'a' or 'b' inside a script block
        self.skip_style = False

    # --- helpers
    def cls(self, attrs):
        d = dict(attrs)
        return d.get("class", ""), d

    def flush(self, kind):
        t = "".join(self.buf).strip()
        t = re.sub(r"[ \t]+", " ", t)
        t = re.sub(r"\n{3,}", "\n\n", t)
        self.buf = []
        if t:
            self.blocks.append((kind, t))

    # --- tags
    def handle_starttag(self, tag, attrs):
        c, d = self.cls(attrs)
        if tag == "style":
            self.skip_style = True
        elif tag in ("h1", "h2", "h4"):
            self.buf = []
            self.mode = tag
        elif tag == "p":
            self.buf = []
            self.mode = "note" if "note" in c or "legend" in c else (
                "standfirst" if "standfirst" in c else "p")
        elif tag == "div":
            if "eyebrow" in c:
                self.buf = []; self.mode = "eyebrow"
            elif "beatline" in c:
                self.buf = []; self.mode = "beatline"
            elif "tagline" in c:
                self.buf = []; self.mode = "tagline"
            elif "meta" in c:
                self.buf = []; self.mode = "meta"
            elif "col a" in c:
                self.col = "a"
            elif "col b" in c:
                self.col = "b"
            elif "side old" in c:
                self.col = "a"
            elif "side new" in c:
                self.col = "b"
            elif "summary" in c:
                self.blocks.append(("hr", ""))
        elif tag == "span" and "hl" in c:
            self.cell_hl = True
            self.buf.append("<<HL>>")
        elif tag == "table":
            self.table = []; self.head = None
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th"):
            self.buf = []; self.in_cell = True
        elif tag == "li":
            self.buf = []; self.mode = "li"
        elif tag == "br":
            self.buf.append(" ")
        elif tag == "footer":
            self.buf = []; self.mode = "footer"

    def handle_endtag(self, tag):
        if tag == "style":
            self.skip_style = False
            self.buf = []
            return
        if tag == "span" and self.cell_hl:
            self.buf.append("<<-HL>>")
            self.cell_hl = False
            return
        if tag in ("td", "th"):
            t = "".join(self.buf).strip()
            t = re.sub(r"\s*\n\s*", " / ", t)
            t = re.sub(r"[ \t]+", " ", t)
            if self.row is not None:
                self.row.append(t)
            self.buf = []
            self.in_cell = False
        elif tag == "tr":
            if self.row:
                if self.head is None:
                    self.head = self.row
                else:
                    self.table.append(self.row)
            self.row = None
        elif tag == "table":
            if self.head is not None:
                self.blocks.append(("table", (self.head, self.table or [])))
            self.table = None; self.head = None
        elif tag in ("h1", "h2", "h4"):
            self.flush(tag)
            self.mode = None
        elif tag == "p":
            self.flush(self.mode or "p")
            self.mode = None
        elif tag == "li":
            self.flush("li")
            self.mode = None
        elif tag == "footer":
            self.flush("footer")
            self.mode = None
        elif tag == "div":
            if self.mode in ("eyebrow", "beatline", "tagline", "meta"):
                self.flush(self.mode)
                self.mode = None
            if self.col:
                self.col = None

    def handle_data(self, data):
        if self.skip_style:
            return
        if self.mode or self.in_cell:
            if self.col and self.in_cell is False and self.mode == "p":
                pass
            self.buf.append(data)

    # column-aware paragraph capture
    def handle_startendtag(self, tag, attrs):
        pass


def parse(path):
    src = io.open(path, encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", src, re.S)
    title = html.unescape(title.group(1).strip()) if title else os.path.basename(path)
    # tag the column paragraphs before parsing so we know which side they are
    src = re.sub(r'<div class="col a"[^>]*><p>', '<div class="col a"><p>@@A@@', src)
    src = re.sub(r'<div class="col b"[^>]*><p>', '<div class="col b"><p>@@B@@', src)
    src = re.sub(r'<div class="side old"[^>]*>', '<div class="side old">', src)
    g = Guide()
    g.feed(src)
    return title, g.blocks


# ------------------------------------------------------------------ markdown

def md_inline(t, side=None):
    t = t.replace("@@A@@", "").replace("@@B@@", "")
    if side == "a":
        t = t.replace("<<HL>>", "~~").replace("<<-HL>>", "~~")
    else:
        t = t.replace("<<HL>>", "**").replace("<<-HL>>", "**")
    return t.strip()


def to_md(title, blocks):
    out = []
    pend_side = None
    for kind, val in blocks:
        if kind == "table":
            head, rows = val
            head = [md_inline(h) or " " for h in head]
            out.append("| " + " | ".join(head) + " |")
            out.append("|" + "|".join([" --- "] * len(head)) + "|")
            for r in rows:
                r = [md_inline(c).replace("\n", " ") or " " for c in r]
                r += [" "] * (len(head) - len(r))
                out.append("| " + " | ".join(r[:len(head)]) + " |")
            out.append("")
            continue
        if kind == "hr":
            out.append("---"); out.append(""); continue
        t = val
        side = "a" if "@@A@@" in t else ("b" if "@@B@@" in t else None)
        t = md_inline(t, side)
        if not t:
            continue
        if kind == "h1":
            out += ["", "# " + t, ""]
        elif kind == "h2":
            out += ["", "## " + t, ""]
        elif kind == "eyebrow":
            out += ["*" + t + "*", ""]
        elif kind == "standfirst":
            out += ["**" + t + "**", ""]
        elif kind == "meta":
            out += [t, ""]
        elif kind in ("beatline", "tagline"):
            out += ["", "### " + t, ""]
        elif kind == "h4":
            out += ["**" + t + "**", ""]
        elif kind == "li":
            out.append("- " + t)
        elif kind == "footer":
            out += ["", "---", "", t, ""]
        else:
            if side == "a":
                out += ["**Control**", "", "> " + t.replace("\n", "\n> "), ""]
            elif side == "b":
                out += ["**New**", "", "> " + t.replace("\n", "\n> "), ""]
            else:
                out += [t, ""]
    md = "\n".join(out)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md


# ------------------------------------------------------------------ pdf

INK = (26, 26, 26)
MUTED = (110, 110, 110)
RED = (170, 45, 25)
HEAD_BG = (238, 238, 238)
LINE = (200, 200, 200)


def lat(t):
    rep = {"‘": "'", "’": "'", "“": '"', "”": '"',
           "–": "-", "—": "-", " ": " ", "…": "...",
           "→": "->", "·": "-"}
    for k, v in rep.items():
        t = t.replace(k, v)
    return t.encode("latin-1", "replace").decode("latin-1")


class PDFDoc(FPDF):
    def __init__(self, title):
        super().__init__(orientation="L", unit="mm", format="A4")
        self.doc_title = title

    def footer(self):
        self.set_y(-11)
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*MUTED)
        self.cell(0, 5, lat(self.doc_title) + "   |   page " + str(self.page_no()), align="C")


def to_pdf(title, blocks, out_path):
    pdf = PDFDoc(title)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(10, 10, 10)
    pdf.add_page()
    bold = FontFace(emphasis="BOLD")

    def para(t, size=9, style="", color=INK, gap=1.5):
        pdf.set_font("Helvetica", style, size)
        pdf.set_text_color(*color)
        pdf.multi_cell(0, size * 0.5 + 0.8, lat(t), new_x="LMARGIN", new_y="NEXT")
        pdf.ln(gap)

    for kind, val in blocks:
        if kind == "table":
            head, rows = val
            n = len(head)
            if not n:
                continue
            pdf.ln(1)
            pdf.set_font("Helvetica", "", 7.5)
            pdf.set_draw_color(*LINE)
            with pdf.table(line_height=4.2, text_align="LEFT", padding=1.2,
                           cell_fill_color=HEAD_BG, cell_fill_mode=TableCellFillMode.NONE,
                           first_row_as_headings=True, repeat_headings=1) as tb:
                hr = tb.row()
                for h in head:
                    hr.cell(lat(md_inline(h)) or " ", style=bold)
                for r in rows:
                    tr = tb.row()
                    r = list(r) + [""] * (n - len(r))
                    for c in r[:n]:
                        txt = md_inline(c)
                        st = bold if ("CHANGE" in txt or txt.strip() in ("NO",)) else None
                        tr.cell(lat(txt) or " ", style=st)
            pdf.ln(3)
            continue

        t = val
        side = "a" if "@@A@@" in t else ("b" if "@@B@@" in t else None)
        t = md_inline(t, None).replace("**", "").replace("~~", "")
        if not t:
            continue
        if kind == "h1":
            pdf.ln(1); para(t, 18, "B", INK, 1)
        elif kind == "h2":
            pdf.ln(4)
            pdf.set_draw_color(*LINE)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(2)
            para(t, 13, "B", INK, 1)
        elif kind == "eyebrow":
            para(t.upper(), 7.5, "", MUTED, 0.5)
        elif kind == "standfirst":
            para(t, 11, "I", MUTED, 1)
        elif kind == "meta":
            para(t, 8, "", MUTED, 2)
        elif kind in ("beatline", "tagline"):
            pdf.ln(2); para(t.upper(), 8, "B", RED, 0.5)
        elif kind == "h4":
            para(t.upper(), 7.5, "B", MUTED, 0.5)
        elif kind == "li":
            para("  -  " + t, 9, "", INK, 1)
        elif kind == "footer":
            pdf.ln(3); para(t, 8, "I", MUTED, 0)
        elif kind == "hr":
            pdf.ln(2)
        else:
            if side == "a":
                para("CONTROL", 7, "B", MUTED, 0.4)
                para(t, 9, "", MUTED, 2)
            elif side == "b":
                para("NEW", 7, "B", RED, 0.4)
                para(t, 9, "", INK, 3)
            else:
                para(t, 9, "", INK, 2)

    pdf.output(out_path)
    return pdf.page_no()


# ------------------------------------------------------------------ main

if __name__ == "__main__":
    for p in sys.argv[1:]:
        title, blocks = parse(p)
        base = os.path.splitext(p)[0]
        io.open(base + ".md", "w", encoding="utf-8").write(to_md(title, blocks))
        pages = to_pdf(title, blocks, base + ".pdf")
        print("%-34s md ok   pdf %d pages   %d KB" %
              (os.path.basename(base), pages, os.path.getsize(base + ".pdf") // 1024))
