#!/usr/bin/env python3
"""The Daily Orbit - Saturday 21 November 2026 front page.

Draws one 1024x1024 PNG newspaper front page with 50 dated, sourced
stories from Saturday 21 November 2026 across 7 regions, a UTC timeline,
a world map with numbered pins, a DATE CHECK box and a BY THE NUMBERS
strip. Pure Pillow + DejaVu fonts; no network, no external assets.
Run:  python3 gen.py   -> writes entry.png next to this file.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (20, 20, 20)
MUTED = (90, 86, 76)
RED = (176, 42, 30)
BLUE = (29, 78, 137)
TEAL = (14, 110, 110)
GOLD = (176, 132, 30)
RULE = (60, 58, 50)
PANEL = (255, 255, 255)
PANEL_LINE = (180, 175, 160)
SEA = (214, 230, 238)
LAND = (232, 222, 190)
LAND_LINE = (150, 140, 115)

FD = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)


F_MAST = font("DejaVuSerif-Bold.ttf", 46)
F_MAST_SMALL = font("DejaVuSerif-Bold.ttf", 20)
F_SUB = font("DejaVuSans-Bold.ttf", 13)
F_SEC = font("DejaVuSans-Bold.ttf", 11)
F_HEAD = font("DejaVuSans-Bold.ttf", 13)
F_BODY = font("DejaVuSans.ttf", 11)
F_SMALL = font("DejaVuSans.ttf", 10)
F_SMALL_B = font("DejaVuSans-Bold.ttf", 10)
F_TINY = font("DejaVuSans.ttf", 9)
F_NUM = font("DejaVuSans-Bold.ttf", 15)
F_LIST = font("DejaVuSans.ttf", 10)
F_LIST_B = font("DejaVuSans-Bold.ttf", 10)
F_TIME = font("DejaVuSans-Bold.ttf", 10)
F_FOOT = font("DejaVuSans.ttf", 9)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to a pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text(draw, xy, s, fnt, fill=INK, anchor="la"):
    draw.text(xy, s, font=fnt, fill=fill, anchor=anchor)


def centre(draw, cx, y, s, fnt, fill=INK):
    draw.text((cx, y), s, font=fnt, fill=fill, anchor="ma")


# ---------------------------------------------------------------- stories
# (number, region, headline, source) -- every story happened, or was first
# reported, on Saturday 21 November 2026. Region codes: NA, EU, ME, AS,
# SA, AF, OC.
STORIES = [
    (1, "NA", "S&P 500 falls into correction, Nasdaq -5.3% in AI sell-off", "AP"),
    (2, "NA", "FBI crime database and USDA payment system hacked", "CNN"),
    (3, "NA", "Trump weighs new strikes on Iran as Israel presses", "NYT"),
    (4, "NA", "Trump tells Europe to defund Ukraine after Putin summit", "Telegraph"),
    (5, "NA", "Trump orders contractors to report Congress requests", "AP"),
    (6, "NA", "Second judge blocks Trump's 250-ft triumphal arch", "AP"),
    (7, "NA", "Trump threatens tax on US firms building AI centres abroad", "Reuters"),
    (8, "NA", "Florida floods: 28 in of rain soaks Brevard County", "AP"),
    (9, "NA", "Bayer to pay $7.25bn to settle Roundup suits", "Reuters"),
    (10, "NA", "Anthropic mathematician claims Riemann proof using AI", "Horizon"),
    (11, "NA", "Mamdani to close Rikers Island by 2032", "NYT"),
    (12, "EU", "Russia fires 400+ drones, 110 missiles at Kyiv; 8 killed", "AP"),
    (13, "EU", "Two Russian missiles and a drone land in Poland", "BBC"),
    (14, "EU", "UK and EU sign three post-Brexit deals in Brussels", "Reuters"),
    (15, "EU", "Denmark expels Russian attache over plot to kill rapper", "AP"),
    (16, "EU", "Drone attack sets Russian cargo ship ablaze, Gulf of Finland", "Wires"),
    (17, "EU", "Costa proposes 3% EU digital tax on big tech", "Wires"),
    (18, "EU", "EU disburses EUR 7.9bn to Ukraine, its largest payment", "Wires"),
    (19, "EU", "Spain heads to 29 Nov snap election; banking tax planned", "Wires"),
    (20, "EU", "Costa Concordia captain Schettino freed after nine years", "Wires"),
    (21, "EU", "Geneva: 128 nations agree to draft killer-robot rules", "AP"),
    (22, "EU", "COP31 in overtime in Antalya; draft drops fossil fuels", "Reuters"),
    (23, "ME", "Saudi coalition intercepts 3 Houthi missiles over Riyadh", "SPA"),
    (24, "ME", "Projectiles hit tankers near Oman; no casualties", "UKMTO"),
    (25, "ME", "Basra power-plant fire kills at least four", "Wires"),
    (26, "ME", "Israeli fire kills Palestinians in Gaza; West Bank tense", "Wires"),
    (27, "ME", "Europeans push to replace UN peacekeepers in Lebanon", "Wires"),
    (28, "ME", "US-Iran talks stall as Hormuz tankers are hit", "Wires"),
    (29, "AS", "Cyclone Akvan makes landfall in Odisha", "IMD"),
    (30, "AS", "Indonesia hit by massive forest fires", "Wires"),
    (31, "AS", "India: 11 dead, 180+ in hospital after tainted alcohol", "Straits Times"),
    (32, "AS", "India lead New Zealand in Test cricket", "Wires"),
    (33, "AS", "Vietnam abolishes death penalty for drug trafficking", "Wires"),
    (34, "AS", "Vietnam passes law speeding land expropriation", "Wires"),
    (35, "AS", "Timor-Leste M6.8 quake, 09:42 UTC; no tsunami", "USGS"),
    (36, "AS", "BepiColombo captured into Mercury orbit, 18:24 UTC", "ESA"),
    (37, "AS", "JPMorgan, Visa, Mastercard report vendor cyberattack", "Wires"),
    (38, "AS", "Trump, Putin, Xi release peace declaration", "Wires"),
    (39, "SA", "M6.7 quake shakes Peru; felt in Lima, no deaths", "USGS"),
    (40, "SA", "Mexico captures El Chapo Isidro, FBI most wanted", "Wires"),
    (41, "SA", "Bolsonaro hospitalised with intestinal issue", "Wires"),
    (42, "SA", "Lula backs Sanchez ahead of Spain snap election", "Wires"),
    (43, "SA", "Hegseth in Caracas; US-Venezuela military deal", "Wires"),
    (44, "AF", "Somalia expels UAE ambassador in diplomatic row", "Wires"),
    (45, "AF", "Some 700,000 displaced by conflict in southern Ethiopia", "Wires"),
    (46, "AF", "Nigeria states approve local police reform", "Wires"),
    (47, "AF", "WHO warns of child deaths in Congo Ebola outbreak", "WHO"),
    (48, "OC", "Cyclone Xavier weakens near Samoa", "JTWC"),
    (49, "OC", "Australia storms, heatwave warnings in NSW", "BOM"),
    (50, "OC", "Tuvalu challenges COP31 over fossil fuels", "Wires"),
]

REGIONS = [
    ("N. AMERICA", 11, RED),
    ("EUROPE", 11, BLUE),
    ("MIDDLE EAST", 6, TEAL),
    ("ASIA", 10, (120, 70, 140)),
    ("S. AMERICA", 5, (180, 90, 20)),
    ("AFRICA", 4, (90, 120, 30)),
    ("OCEANIA", 3, (20, 120, 160)),
]

TIMELINE = [
    ("00:09", "M6.7 quake shakes Peru", "39"),
    ("OVERNIGHT", "Russia fires 400 drones at Kyiv", "12"),
    ("09:42", "M6.8 quake off Timor-Leste", "35"),
    ("MIDDAY", "100 groups: COP31 is 'worst COP ever'", "22"),
    ("18:24", "BepiColombo enters Mercury orbit", "36"),
    ("EVENING", "Riyadh intercepts 3 missiles", "23"),
]

FEATURED = [
    (12, "KYIV UNDER FIRE",
     "Russia fires 400+ drones and 110 missiles at Kyiv; 8 killed, "
     "bridges and rail hit, power cut in ten regions.",
     "AP", "missile"),
    (22, "COP31 IN OVERTIME",
     "Talks in Antalya pass the deadline with no deal; the draft drops "
     "fossil fuels and a $120bn finance target.",
     "Reuters", "globe"),
    (1, "MARKETS ROUT",
     "S&P 500 falls into correction at -3.7%; Nasdaq -5.3%, Nikkei "
     "-5.1% as the AI sell-off sweeps the world.",
     "AP", "chart"),
    (39, "PERU QUAKE",
     "M6.7 shakes the Andes near Junin at 00:09 UTC; felt in Lima, "
     "no deaths, six minor injuries reported.",
     "USGS", "quake"),
]

DATE_CHECK_LEFT_OUT = [
    "Anthropic's $2tn IPO debut - Thursday 19 Nov.",
    "Xi-Trump-Putin Shenzhen summit itself - Thursday 19 Nov.",
    "Mlambo-Ngcuka died Friday evening, announced Friday night.",
    "Palisades fire verdict - Friday 20 Nov.",
    "EU-Indonesia trade deal signed - Friday 20 Nov.",
    "FAA ground stop - 13 Nov.  Tanker hits in Hormuz - 16 Nov.",]
DATE_CHECK_NOT_YET = ("Not yet: a COP31 final deal - talks still deadlocked "
                      "on Saturday night.")

NUMBERS = [
    ("400+", "drones over Kyiv"),
    ("110", "missiles fired"),
    ("-3.7%", "S&P 500"),
    ("M6.7", "Peru quake"),
    ("$7.25bn", "Bayer deal"),
    ("128", "nations in Geneva"),
]

# Map pins: (story number, lon, lat, label)
PINS = [
    (12, 30.5, 50.5), (13, 21.0, 52.2), (22, 30.7, 36.9), (14, 4.4, 50.8),
    (23, 46.7, 24.6), (39, -76.0, -11.0), (29, 85.0, 20.0), (35, 126.0, -8.5),
    (40, -107.0, 25.0), (30, 106.8, -6.2), (44, 45.3, 2.0), (48, -172.0, -13.8),
]

CONTINENTS = [
    # North America
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 70),
     (-75, 62), (-65, 60), (-55, 52), (-60, 46), (-70, 42), (-75, 35),
     (-80, 26), (-85, 20), (-90, 15), (-95, 17), (-105, 20), (-115, 28),
     (-125, 40), (-125, 49), (-140, 60), (-155, 58), (-165, 60)],
    # Greenland
    [(-45, 60), (-30, 68), (-22, 70), (-25, 76), (-40, 80), (-55, 76),
     (-58, 64)],
    # South America
    [(-80, 10), (-75, 12), (-65, 10), (-55, 5), (-50, 0), (-45, -5),
     (-38, -8), (-35, -15), (-40, -22), (-48, -28), (-55, -35), (-65, -40),
     (-70, -50), (-73, -53), (-70, -45), (-73, -35), (-72, -20),
     (-78, -10), (-80, 0), (-80, 8)],
    # Africa
    [(-17, 15), (-10, 30), (-5, 35), (10, 37), (20, 32), (32, 31), (35, 28),
     (40, 15), (48, 11), (51, 10), (45, 0), (40, -10), (35, -18),
     (30, -28), (20, -35), (15, -30), (12, -18), (10, -5), (8, 4),
     (-8, 5), (-15, 10)],
    # Eurasia
    [(-10, 36), (-5, 44), (0, 46), (-2, 50), (5, 53), (8, 57), (10, 59),
     (18, 56), (21, 60), (25, 65), (30, 70), (40, 68), (55, 70), (70, 72),
     (90, 75), (110, 76), (130, 72), (150, 70), (170, 67), (178, 65),
     (170, 60), (160, 55), (158, 50), (150, 45), (142, 40), (135, 35),
     (130, 33), (122, 30), (120, 25), (110, 20), (105, 10), (100, 8),
     (95, 15), (90, 22), (85, 20), (80, 13), (75, 10), (72, 20), (66, 25),
     (60, 25), (55, 26), (50, 29), (48, 30), (44, 29), (40, 32), (36, 36),
     (30, 36), (25, 38), (20, 40), (15, 44), (10, 38), (5, 37), (0, 36)],
    # Australia
    [(113, -22), (114, -30), (115, -35), (120, -34), (130, -32), (135, -35),
     (140, -38), (145, -38), (150, -37), (153, -32), (153, -27), (150, -22),
     (146, -19), (142, -15), (142, -11), (136, -12), (132, -12), (126, -14),
     (122, -17), (118, -20)],
    # Britain
    [(-5, 50), (-3, 53), (-5, 56), (-2, 58), (0, 53)],
    # Japan
    [(130, 31), (133, 34), (137, 35), (140, 38), (141, 42), (144, 44),
     (142, 40), (139, 37)],
    # New Zealand
    [(167, -45), (170, -42), (174, -40), (177, -38), (175, -36), (172, -35),
     (168, -44)],
]


# ---------------------------------------------------------------- pictograms
def pic_missile(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 228, 215), outline=PANEL_LINE)
    cx, cy = x + w // 2, y + h // 2
    # sky burst
    for r, col in ((34, (255, 214, 130)), (24, (255, 170, 60)),
                   (14, (220, 80, 40))):
        d.ellipse([cx - r, cy - 26 - r, cx + r, cy - 26 + r], fill=col)
    # rocket body, diagonal
    d.line([x + 30, y + h - 22, x + w - 34, y + 26], fill=INK, width=7)
    d.polygon([(x + w - 34, y + 26), (x + w - 14, y + 18),
               (x + w - 26, y + 44)], fill=RED)
    d.line([x + 30, y + h - 22, x + 16, y + h - 8], fill=(255, 170, 60),
           width=5)
    # bridge arcs below
    for i in range(3):
        bx = x + 18 + i * 62
        d.arc([bx, y + h - 34, bx + 56, y + h - 2], 180, 360, fill=BLUE,
              width=3)
        d.line([bx + 4, y + h - 18, bx + 52, y + h - 18], fill=BLUE, width=2)


def pic_globe(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 228, 215), outline=PANEL_LINE)
    cx, cy = x + w // 2, y + h // 2 - 6
    r = 34
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(170, 205, 225),
              outline=BLUE, width=2)
    d.ellipse([cx - 12, cy - r, cx + 12, cy + r], outline=BLUE, width=2)
    d.line([cx - r, cy, cx + r, cy], fill=BLUE, width=2)
    d.arc([cx - r, cy - 16, cx + r, cy + 16], 0, 360, fill=BLUE, width=2)
    d.ellipse([cx - 22, cy - 6, cx - 8, cy + 10], fill=(90, 160, 90))
    d.ellipse([cx + 6, cy - 16, cx + 22, cy - 2], fill=(90, 160, 90))
    d.rectangle([x + 14, y + h - 26, x + w - 14, y + h - 10], fill=RED)
    centre(d, cx, y + h - 25, "NO DEAL YET", F_SMALL_B, (255, 255, 255))


def pic_chart(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 228, 215), outline=PANEL_LINE)
    ox, oy = x + 16, y + h - 18
    d.line([ox, y + 12, ox, oy], fill=INK, width=2)
    d.line([ox, oy, x + w - 12, oy], fill=INK, width=2)
    pts = [(ox + 6, y + 18), (ox + 34, y + 26), (ox + 62, y + 22),
           (ox + 92, y + 40), (ox + 122, y + 52), (ox + 152, y + 66),
           (ox + 178, y + 78)]
    d.line(pts, fill=RED, width=4)
    for px, py in pts:
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=RED)
    d.polygon([(ox + 178, y + 78), (ox + 178, y + 64), (ox + 192, y + 78)],
              fill=RED)
    d.text((x + w - 58, y + 8), "-5.3%", font=F_HEAD, fill=RED)


def pic_quake(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 228, 215), outline=PANEL_LINE)
    # mountains
    d.polygon([(x + 10, y + h - 16), (x + 70, y + 34), (x + 120, y + h - 16)],
              fill=(120, 110, 90))
    d.polygon([(x + 90, y + h - 16), (x + 150, y + 44), (x + 210, y + h - 16)],
              fill=(90, 85, 70))
    d.polygon([(x + 58, y + 46), (x + 70, y + 34), (x + 82, y + 46)],
              fill=(255, 255, 255))
    # seismic trace
    pts = []
    xx = x + 12
    yy = y + h - 52
    for i, dy in enumerate([0, -14, 10, -26, 18, -8, 4, 0]):
        pts.append((xx + i * 26, yy + dy))
    d.line(pts, fill=RED, width=3)
    d.text((x + 12, y + 8), "M6.7", font=F_HEAD, fill=RED)


PICS = {"missile": pic_missile, "globe": pic_globe, "chart": pic_chart,
        "quake": pic_quake}


# ---------------------------------------------------------------- map
def lonlat_to_xy(lon, lat, x0, y0, mw, mh):
    px = x0 + (lon + 180.0) / 360.0 * mw
    py = y0 + (90.0 - lat) / 150.0 * mh
    return px, py


def draw_map(d, x0, y0, mw, mh):
    d.rectangle([x0, y0, x0 + mw, y0 + mh], fill=SEA, outline=PANEL_LINE)
    for poly in CONTINENTS:
        pts = [lonlat_to_xy(lon, lat, x0, y0, mw, mh) for lon, lat in poly]
        d.polygon(pts, fill=LAND, outline=LAND_LINE)
    for num, lon, lat in PINS:
        px, py = lonlat_to_xy(lon, lat, x0, y0, mw, mh)
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED,
                  outline=(255, 255, 255), width=1)
        centre(d, px, py - 6, str(num), F_TINY, (255, 255, 255))


# ---------------------------------------------------------------- layout
def draw_header(d):
    text(d, (14, 8), "THE DAILY ORBIT", F_MAST, INK)
    tw = d.textlength("SATURDAY, 21 NOVEMBER 2026", font=F_SUB)
    text(d, (1010 - tw, 16), "SATURDAY, 21 NOVEMBER 2026", F_SUB, RED)
    tw2 = d.textlength("50 STORIES  ·  7 REGIONS", font=F_SMALL_B)
    text(d, (1010 - tw2, 38), "50 STORIES  ·  7 REGIONS", F_SMALL_B, INK)
    d.line([14, 62, 1010, 62], fill=RULE, width=2)
    centre(d, 512, 66,
           "EVERY STORY HAPPENED, OR WAS FIRST REPORTED, ON THIS SATURDAY"
           "  —  SOURCED, DATED, CHECKED", F_SMALL_B, INK)
    d.line([14, 86, 1010, 86], fill=RED, width=3)


def draw_timeline(d):
    text(d, (14, 92), "UTC TIMELINE  —  SATURDAY 21 NOVEMBER 2026",
         F_SEC, RED)
    y = 124
    d.line([40, y, 984, y], fill=RULE, width=2)
    xs = [90, 250, 410, 570, 730, 890]
    for (t, ev, num), cx in zip(TIMELINE, xs):
        d.ellipse([cx - 6, y - 6, cx + 6, y + 6], fill=RED,
                  outline=(255, 255, 255), width=1)
        centre(d, cx, 102, t, F_TIME, RED)
        lines = wrap(d, ev + "  (#" + num + ")", F_SMALL, 150)
        ly = 134
        for ln in lines[:2]:
            centre(d, cx, ly, ln, F_SMALL, INK)
            ly += 11


def draw_featured(d):
    y0, ph, pw = 156, 204, 244
    for i, (num, kick, body, src, pic) in enumerate(FEATURED):
        x0 = 14 + i * (pw + 6)
        d.rectangle([x0, y0, x0 + pw, y0 + ph], fill=PANEL,
                    outline=PANEL_LINE)
        PICS[pic](d, x0 + 8, y0 + 8, pw - 16, 88)
        text(d, (x0 + 8, y0 + 102), "No. %d  —  %s" % (num, kick),
             F_SMALL_B, RED)
        lines = wrap(d, body, F_BODY, pw - 16)
        ly = y0 + 118
        for ln in lines[:4]:
            text(d, (x0 + 8, ly), ln, F_BODY, INK)
            ly += 13
        sw = d.textlength("Source: " + src, font=F_TINY)
        text(d, (x0 + pw - 8 - sw, y0 + ph - 14), "Source: " + src,
             F_TINY, MUTED)


def draw_map_panel(d):
    y0 = 364
    text(d, (14, y0), "WHERE IT HAPPENED  —  12 STORIES PINNED",
         F_SEC, RED)
    draw_map(d, 14, y0 + 20, 660, 140)
    # region key, right side
    kx = 692
    text(d, (kx, y0), "7 REGIONS", F_SEC, INK)
    yy = y0 + 20
    for name, count, col in REGIONS:
        d.rectangle([kx, yy + 2, kx + 12, yy + 12], fill=col)
        text(d, (kx + 18, yy), "%s  —  %d" % (name, count), F_SMALL, INK)
        yy += 18
    text(d, (kx, yy + 4), "Numbers on the map = story numbers.",
         F_TINY, MUTED)


def draw_list(d):
    y0 = 528
    text(d, (14, y0),
         "THE DAY IN 50 STORIES  —  NUMBERED, SOURCED", F_SEC, RED)
    d.line([14, y0 + 16, 1010, y0 + 16], fill=RULE, width=1)
    cols = [STORIES[0:16], STORIES[16:31], STORIES[31:50]]
    xs = [14, 350, 686]
    row_h = 20
    for ci, col in enumerate(cols):
        x = xs[ci]
        y = y0 + 24
        for num, region, head, src in col:
            label = "%d. %s" % (num, head)
            # headline gets its own gutter; the source lives in the
            # right-hand gutter so the two can never overlap
            lines = wrap(d, label, F_LIST, 264)
            ly = y
            for ln in lines[:2]:
                text(d, (x, ly), ln, F_LIST, INK)
                ly += 10
            sw = d.textlength(src, font=F_TINY)
            text(d, (x + 322 - sw, y + 5), src, F_TINY, MUTED)
            y += row_h


def draw_datecheck(d):
    y0 = 876
    d.rectangle([14, y0, 1010, y0 + 58], fill=(255, 238, 232),
                outline=RED)
    text(d, (24, y0 + 6), "DATE CHECK  —  LEFT OUT ON PURPOSE",
         F_SMALL_B, RED)
    left = "  ·  ".join(DATE_CHECK_LEFT_OUT)
    lines = wrap(d, left, F_SMALL, 968)
    ly = y0 + 22
    for ln in lines[:2]:
        text(d, (24, ly), ln, F_SMALL, INK)
        ly += 11
    text(d, (24, y0 + 44), DATE_CHECK_NOT_YET, F_SMALL_B, INK)


def draw_numbers(d):
    y0 = 940
    cw = (1010 - 14) // 6
    for i, (big, label) in enumerate(NUMBERS):
        x0 = 14 + i * cw
        centre(d, x0 + cw // 2, y0, big, F_NUM, RED)
        centre(d, x0 + cw // 2, y0 + 20, label, F_TINY, MUTED)
        if i:
            d.line([x0, y0 + 2, x0, y0 + 34], fill=PANEL_LINE, width=1)
    d.line([14, y0 + 38, 1010, y0 + 38], fill=RULE, width=1)


def draw_footer(d):
    centre(d, 512, 984,
           "Every story here happened, or was first reported, on Saturday "
           "21 November 2026; claims are attributed.", F_FOOT, MUTED)
    centre(d, 512, 998,
           "THE DAILY ORBIT  ·  make.fun news-image-20261121  ·  "
           "One front page for one day of world news.", F_FOOT, MUTED)


def main():
    assert len(STORIES) == 50, len(STORIES)
    assert len({n for n, _, _, _ in STORIES}) == 50
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, 3], fill=RED)
    draw_header(d)
    draw_timeline(d)
    draw_featured(d)
    draw_map_panel(d)
    draw_list(d)
    draw_datecheck(d)
    draw_numbers(d)
    draw_footer(d)
    img.save(OUT, format="PNG")
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
