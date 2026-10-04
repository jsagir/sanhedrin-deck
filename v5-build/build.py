#!/usr/bin/env python3
"""Build v5 (expert team master) from the original deck shell.

Reads  : <deploy>/original.html   (the untouched original deck)
Writes : <deploy>/v5/index.html   (v5, asset paths prefixed with ../)

v5 reuses the original shell (CSS, nav, JS, appendices) and replaces the main slide set.
No em-dashes, no emojis (deck style rules). Hebrew is a first draft for Jonathan to review.
"""
import re, sys, math, pathlib

HERE = pathlib.Path(__file__).resolve().parent
DEPLOY = HERE.parent
SRC = DEPLOY / 'original.html'
OUT = DEPLOY / 'v5' / 'index.html'

s = SRC.read_text(encoding='utf-8')
secs = [m.group(0) for m in re.finditer(r'<section class="slide[^>]*>.*?</section>\n', s, re.S)]
assert len(secs) == 33, len(secs)
first = re.search(r'<section class="slide[^>]*>', s).start()
last_m = list(re.finditer(r'</section>\n', s))[-1].end()
PRE, POST = s[:first], s[last_m:]

ACT1, ACT2, ACT3, ACT4 = ('ACT 1: WHERE WE STAND', 'ACT 2: THE EXPERIENCE',
                          'ACT 3: HOW WE GET THERE', 'ACT 4: WHAT WE NEED')

# ---------------------------------------------------------------- helpers
TAGS = {
    'en': {'closed': 'CLOSED', 'open': 'OPEN', 'proposal': 'TO RATIFY'},
    'he': {'closed': 'סגור', 'open': 'פתוח', 'proposal': 'לאישור'},
}

def tag(kind, lang):
    return '<span class="v5-tag v5-tag--%s">%s</span>' % (kind, TAGS[lang][kind])

def slide(en, he, cls='layout-statement', style=''):
    return ('<section class="slide" data-act="X">\n'
            '  <div class="lang-en">\n    <div class="%s v5-body" style="%s">%s</div>\n  </div>\n'
            '  <div class="lang-he" dir="rtl">\n    <div class="%s v5-body" style="%s">%s</div>\n  </div>\n'
            '</section>\n') % (cls, style, en, cls, style, he)

def head(label, title, size=52, sub=None, tg=None):
    h = '<p class="label reveal">%s</p>' % label
    h += '<h2 class="reveal r1" style="font-size:%dpx;max-width:1100px;margin-bottom:%dpx">%s</h2>' % (
        size, 12 if sub else 18, title)
    if sub:
        h += '<p class="reveal r2 v5-sub">%s</p>' % sub
    if tg:
        h += '<div class="reveal r2" style="margin-bottom:14px">%s</div>' % tg
    return h

def card(title, body, tg='', dark=False):
    cls = 'v5-card' + (' v5-card--dark' if dark else '')
    top = '<div class="v5-card-top"><h3>%s</h3>%s</div>' % (title, tg)
    if body.startswith('<ul'):
        return '<div class="%s">%s%s</div>' % (cls, top, body)
    return '<div class="%s">%s<p>%s</p></div>' % (cls, top, body)

def grid(cards, cols, extra=''):
    return '<div class="v5-grid reveal r3" style="grid-template-columns:repeat(%d,1fr);%s">%s</div>' % (
        cols, extra, ''.join(cards))

def step(n, title, body):
    return '<div class="v5-step"><div class="v5-step-n">%s</div><h3>%s</h3><p>%s</p></div>' % (n, title, body)

def strip(steps, cols=None):
    cols = cols or len(steps)
    return '<div class="v5-grid v5-strip reveal r3" style="grid-template-columns:repeat(%d,1fr)">%s</div>' % (
        cols, ''.join(step(i + 1, t, b) for i, (t, b) in enumerate(steps)))

def note(text):
    return '<p class="reveal r4 v5-note">%s</p>' % text

def lst(items):
    return '<ul class="v5-list">%s</ul>' % ''.join('<li>%s</li>' % x for x in items)

# ---------------------------------------------------------------- slides
main = []

# 1. TITLE ---------------------------------------------------------------
def hero(lang):
    if lang == 'en':
        h1, sub, line, tg = ('The Convergence Lab',
            'The Ancient Sanhedrin as a Multi-player AI-Powered Experience in Discourse',
            'Expert team alignment session - 8 October 2026',
            'WORKING TITLE - THE NAME IS STILL OPEN')
        cid, align = 'heroNetwork', ''
    else:
        h1, sub, line, tg = ('The Convergence Lab',
            'הסנהדרין העתיקה כחוויית שיח רב-משתתפים מבוססת בינה מלאכותית',
            'מפגש כיול צוות מומחים - 8 באוקטובר 2026',
            'שם עבודה - השם עדיין פתוח')
        cid, align = 'heroNetworkHe', 'text-align:right;'
    return ('<div class="layout-hero">'
            '<img src="slides/slide-01/hero.png" alt="" class="hero-bg">'
            '<div class="hero-scrim"></div><div class="hero-glare hero-glare--warm"></div>'
            '<canvas class="deliberation-network" id="%s"></canvas>'
            '<div class="hero-content" style="%s">'
            '<img src="assets/logos/motj-logo-horizontal-white.svg" alt="MOTJ" style="height:56px;margin-bottom:18px" class="reveal">'
            '<h1 class="reveal r1" style="color:#fff;font-size:74px">%s</h1>'
            '<p class="tagline reveal r2" style="color:rgba(255,255,255,0.88);margin-top:10px;font-size:26px;max-width:900px">%s</p>'
            '<p class="reveal r3" style="font-size:22px;color:rgba(255,255,255,0.7);margin-top:12px;font-style:italic">%s</p>'
            '<p class="reveal r4" style="margin-top:16px"><span class="v5-tag v5-tag--onhero">%s</span></p>'
            '</div></div>') % (cid, align, h1, sub, line, tg)

main.append('<section class="slide active" data-act="X">\n  <div class="lang-en">%s</div>\n'
            '  <div class="lang-he" dir="rtl">%s</div>\n</section>\n' % (hero('en'), hero('he')))

# 2. WHY WE ARE IN THIS ROOM ---------------------------------------------
en = (head('Why we are in this room', 'Where we stand', 64,
           'A map of the work done so far, for people joining and for people already inside. Every slide is marked.')
      + grid([
          card('Closed', 'Settled. We build on it and we do not reopen it.', tag('closed', 'en')),
          card('Open', 'Still to decide. Named plainly, so it can be decided.', tag('open', 'en')),
          card('What we ask', 'Your support for the main line. Not a redesign.', '', dark=True),
      ], 3, 'max-width:1100px')
      + note('Questions are welcome. Most have already been worked. The next slide shows how.'))
he = (head('למה אנחנו בחדר הזה', 'איפה אנחנו עומדים', 64,
           'מפה של העבודה עד כה, למי שמצטרף ולמי שכבר בפנים. כל שקף מסומן.')
      + grid([
          card('סגור', 'סוכם. בונים על זה ולא פותחים מחדש.', tag('closed', 'he')),
          card('פתוח', 'עדיין צריך להחליט. מנוסח בבירור כדי שאפשר יהיה להחליט.', tag('open', 'he')),
          card('מה אנחנו מבקשים', 'תמיכה בקו המרכזי. לא עיצוב מחדש.', '', dark=True),
      ], 3, 'max-width:1100px')
      + note('שאלות מתקבלות בברכה. את רובן כבר עבדנו. השקף הבא מראה איך.'))
main.append(slide(en, he))

# 3. QUESTIONS ALREADY WORKED -------------------------------------------
QA_EN = [
    ('Why not an AI coach for each team?',
     'A coach makes visitors wait on a machine, and dead air breaks the experience. Sages speak from the periphery, on dramatic timing, for no team.', ''),
    ('Why does a human conduct the room?',
     'No AI can handle a room of people talking over each other. A charismatic host sets the pace, models the first move, and can stop any AI line.', ''),
    ('Why discourse first, not debate?',
     'If this way of arguing is unique in the world, lead with it. A debate experience can be considered later.', tag('proposal', 'en')),
    ('Why can visitors not pick the topic?',
     'Dilemmas are built from real Talmudic cases, as deliberate gray zones. That prevents tribal defense. Open topics invite it.', ''),
    ('Why up to 80 sages, without 80 film shoots?',
     'Each sage is a character sheet: a voice, a history, a way of arguing. All of them run on one shared engine.', ''),
    ('Why a concept phase before any build?',
     'We know the goal. We do not yet know that the space, the projection and a full group work. Test it first, with real visitors.', ''),
]
QA_HE = [
    ('למה לא מאמן AI לכל קבוצה?',
     'מאמן גורם למבקרים לחכות למכונה, ושקט מת שובר את החוויה. החכמים מדברים מהפריפריה, בתזמון דרמטי, ולא שייכים לאף קבוצה.', ''),
    ('למה אדם מנהל את החדר?',
     'שום AI לא יודע להתמודד עם חדר של אנשים שמדברים אחד על השני. מנחה כריזמטי קובע קצב, מדגים את המהלך הראשון, ויכול לעצור כל שורה של ה-AI.', ''),
    ('למה שיח קודם ולא ויכוח?',
     'אם דרך הוויכוח הזו ייחודית בעולם, פותחים בה. חוויית ויכוח אפשר לשקול בהמשך.', tag('proposal', 'he')),
    ('למה המבקרים לא בוחרים את הנושא?',
     'הדילמות נבנות ממקרים תלמודיים אמיתיים, כאזורי אפור מכוונים. זה מונע הגנה שבטית. נושאים פתוחים מזמינים אותה.', ''),
    ('למה עד 80 חכמים, בלי 80 צילומים?',
     'כל חכם הוא דף דמות: קול, היסטוריה, דרך לטעון. כולם רצים על מנוע משותף אחד.', ''),
    ('למה שלב קונספט לפני בנייה?',
     'המטרה ברורה לנו. עדיין לא ברור לנו שהחלל, ההקרנה וקבוצה מלאה עובדים. בודקים קודם, עם מבקרים אמיתיים.', ''),
]
en = head('Already worked', 'The questions we expect, and why we chose', 44) + grid(
    [card(q, a, t) for q, a, t in QA_EN], 3, 'max-width:1240px')
he = head('כבר עבדנו', 'השאלות שאנחנו מצפים להן, ולמה בחרנו כך', 44) + grid(
    [card(q, a, t) for q, a, t in QA_HE], 3, 'max-width:1240px')
main.append(slide(en, he))

# 4. PROBLEM (reused from original) --------------------------------------
main.append(secs[1])

# 5. WHAT THE WORD MEANS -------------------------------------------------
en = (head('What the word means', 'A framework, not a re-enactment', 56,
           'The historical Sanhedrin was a court of sages. We do not rebuild the court. We borrow its framework.')
      + grid([
          card('What we borrow',
               'Structured, high-stakes, multi-perspective deliberation, built to find truth rather than to persuade.',
               tag('closed', 'en')),
          card('The name',
               'Working title: The Convergence Lab. The word Sanhedrin is not widely known, even in Israel. The name stays open.',
               tag('open', 'en')),
      ], 2, 'max-width:1000px'))
he = (head('מה המילה אומרת', 'מסגרת, לא שחזור', 56,
           'הסנהדרין ההיסטורית הייתה בית דין של חכמים. אנחנו לא בונים מחדש את בית הדין. אנחנו שואלים ממנו את המסגרת.')
      + grid([
          card('מה אנחנו שואלים',
               'דיון מובנה, בעל סיכון גבוה, מכמה נקודות מבט, שנועד למצוא אמת ולא לשכנע.', tag('closed', 'he')),
          card('השם',
               'שם עבודה: The Convergence Lab. המילה סנהדרין לא מוכרת לרבים, גם בישראל. השם נשאר פתוח.', tag('open', 'he')),
      ], 2, 'max-width:1000px'))
main.append(slide(en, he))

# 6. COGNITIVE TWIST (reused) --------------------------------------------
main.append(secs[5])

# ---- ACT 2 ----
# 7. ROOM IN ONE MINUTE ---------------------------------------------------
en = (head('The room in one minute', 'From the door to the takeaway', 48, tg=tag('closed', 'en'))
      + strip([
          ('Outside', 'A screen shows the timer, the schedule and a short introduction. Context comes before entering, and the flow stays controlled.'),
          ('Arrive', 'The host welcomes the group and assigns discourse teams and audience. Teams log in by QR code or mobile.'),
          ('Orient', 'A 30-second introduction and how to use the devices. The host confirms the mode. A practice run follows.'),
          ('Live', 'Discourse rounds, conducted by the host. The Civility Scoreboard tracks listening, not winning.'),
          ('Takeaway', 'The room builds a collective verdict. Visitors leave with a way of listening, not a winner.'),
      ])
      + note('Working assumption: a timed experience of about 25 minutes. Exact timings are for the concept phase.'))
he = (head('החדר בדקה', 'מהדלת ועד הסיכום', 48, tg=tag('closed', 'he'))
      + strip([
          ('בחוץ', 'מסך מציג את הטיימר, לוח הזמנים והקדמה קצרה. ההקשר ניתן לפני הכניסה, והזרימה נשארת מבוקרת.'),
          ('הגעה', 'המנחה מקבל את הקבוצה ומחלק קבוצות שיח וקהל. הקבוצות מתחברות בקוד QR או בנייד.'),
          ('התמצאות', 'הקדמה של 30 שניות והסבר על המכשירים. המנחה מאשר את המצב. אחריה מקצה אימון.'),
          ('חי', 'סבבי שיח בהנחיית המנחה. לוח האזרחיות עוקב אחרי הקשבה, לא אחרי ניצחון.'),
          ('סיכום', 'החדר בונה פסק דין משותף. המבקרים יוצאים עם דרך להקשיב, לא עם מנצח.'),
      ])
      + note('הנחת עבודה: חוויה מתוזמנת של כ-25 דקות. התזמונים המדויקים נקבעים בשלב הקונספט.'))
main.append(slide(en, he))

# 8. FOUR CONVERSATIONS ---------------------------------------------------
en = (head('Who talks to whom', 'Four conversations, running at once', 48, tg=tag('closed', 'en'))
      + grid([
          card('Sage to sage', 'Sages challenge and answer each other, on dramatic timing. This is part of the show.'),
          card('Sage to visitor', 'A sage answers one participant, an exchange between two, or the discussion at large. A line that ignores the moment is a defect.'),
          card('Visitor to visitor', 'Teams argue toward the strongest shared truth. This is the heart of the experience.'),
          card('Visitor to host', 'The host breaks the ice, raises and lowers the tension, and steers the room.'),
      ], 2, 'max-width:1100px')
      + note('The audience reacts live on their devices, and the reactions appear on the walls.'))
he = (head('מי מדבר עם מי', 'ארבע שיחות, במקביל', 48, tg=tag('closed', 'he'))
      + grid([
          card('חכם אל חכם', 'החכמים מאתגרים ועונים זה לזה, בתזמון דרמטי. זה חלק מההצגה.'),
          card('חכם אל מבקר', 'חכם עונה למשתתף אחד, לחילופי דברים בין שניים, או לדיון כולו. שורה שמתעלמת מהרגע היא פגם.'),
          card('מבקר אל מבקר', 'הקבוצות מתדיינות לקראת האמת המשותפת החזקה ביותר. זה לב החוויה.'),
          card('מבקר אל מנחה', 'המנחה שובר את הקרח, מעלה ומוריד את המתח, ומכוון את החדר.'),
      ], 2, 'max-width:1100px')
      + note('הקהל מגיב בזמן אמת במכשירים שלו, והתגובות מופיעות על הקירות.'))
main.append(slide(en, he))

# 9. YOU WIN BY LISTENING -------------------------------------------------
CH_EN = ['Listening', 'Clarity', 'Courage', 'Fairness', 'Humility', 'Bridge-building']
CH_HE = ['הקשבה', 'בהירות', 'אומץ', 'הוגנות', 'ענווה', 'בניית גשרים']
chips = lambda L: '<div class="v5-chips reveal r3">%s</div>' % ''.join('<span>%s</span>' % c for c in L)
en = (head('How you win', 'You win by listening', 56, tg=tag('closed', 'en'))
      + '<p class="reveal r2 v5-sub" style="margin-bottom:14px">The Civility Scoreboard tracks six behaviors. It never tracks who is winning.</p>'
      + chips(CH_EN)
      + grid([card('No winner is declared',
                   'The room builds a collective verdict from fragments of both teams: the strongest truth, the unresolved question, the minority concern, and a possible action. It appears on screen as a living page of Talmud.',
                   '', dark=True)], 1, 'max-width:900px;margin-top:22px'))
he = (head('איך מנצחים', 'מנצחים בהקשבה', 56, tg=tag('closed', 'he'))
      + '<p class="reveal r2 v5-sub" style="margin-bottom:14px">לוח האזרחיות עוקב אחרי שש התנהגויות. הוא אף פעם לא עוקב אחרי מי מנצח.</p>'
      + chips(CH_HE)
      + grid([card('אין מנצח מוכרז',
                   'החדר בונה פסק דין משותף מקטעים של שתי הקבוצות: האמת החזקה ביותר, השאלה הפתוחה, החשש של המיעוט, ופעולה אפשרית. הוא מופיע על המסך כדף תלמוד חי.',
                   '', dark=True)], 1, 'max-width:900px;margin-top:22px'))
main.append(slide(en, he))

# 10. MODE AND AUDIENCE ---------------------------------------------------
en = (head('Mode and audience', 'Discourse first. Two audiences.', 52)
      + grid([
          card('Discourse mode',
               'No declared winners or losers. The goal is the strongest shared truth, not defeating the other side. The team proposes leading with it. A debate experience can be considered later.',
               tag('proposal', 'en')),
          card('Two audiences',
               'Trained groups from the School of Public Discourse, with a pre-visit training period. And walk-in visitors with no preparation. Different experience, different outcome. The host confirms the mode before the round.',
               tag('closed', 'en')),
      ], 2, 'max-width:1100px')
      + note('To ratify on 8 October: discourse only for launch.'))
he = (head('מצב וקהל', 'שיח קודם. שני קהלים.', 52)
      + grid([
          card('מצב שיח',
               'אין מנצחים או מפסידים מוכרזים. המטרה היא האמת המשותפת החזקה ביותר, לא ניצחון על הצד השני. הצוות מציע לפתוח בו. חוויית ויכוח אפשר לשקול בהמשך.',
               tag('proposal', 'he')),
          card('שני קהלים',
               'קבוצות מאומנות מבית הספר לשיח ציבורי, עם תקופת הכנה לפני הביקור. ומבקרים מזדמנים ללא הכנה. חוויה שונה, תוצאה שונה. המנחה מאשר את המצב לפני הסבב.',
               tag('closed', 'he')),
      ], 2, 'max-width:1100px')
      + note('לאישור ב-8 באוקטובר: שיח בלבד לפתיחה.'))
main.append(slide(en, he))

# 11. THE SAGES -----------------------------------------------------------
LIB_EN = '<a class="v5-link reveal r4" href="#" onclick="goToSageLibrary();return false;">Browse the sage library</a>'
LIB_HE = '<a class="v5-link reveal r4" href="#" onclick="goToSageLibrary();return false;">לעיון בספריית החכמים</a>'
en = (head('The sages', 'Up to 80 voices. None on a team.', 52, tg=tag('closed', 'en'))
      + grid([
          card('Character sheets', 'A voice, a history and a way of arguing, plugged into one shared engine.'),
          card('Unaligned', 'They answer what is said, not who said it. No sage helps a team win.'),
          card('On the periphery', 'They appear on the surrounding walls, enter on dramatic timing, and hand the floor back.'),
          card('Distinct', 'A relentless Talmudic questioner. A strategic contemporary communicator. Thinkers the audience respects.'),
      ], 4, 'max-width:1240px')
      + '<p class="reveal r4 v5-note">%s How many at launch: being decided.</p>' % tag('open', 'en') + LIB_EN)
he = (head('החכמים', 'עד 80 קולות. אף אחד לא בקבוצה.', 52, tg=tag('closed', 'he'))
      + grid([
          card('דפי דמות', 'קול, היסטוריה ודרך לטעון, מחוברים למנוע משותף אחד.'),
          card('לא מזוהים', 'הם עונים למה שנאמר, לא למי שאמר. אף חכם לא עוזר לקבוצה לנצח.'),
          card('בפריפריה', 'הם מופיעים על הקירות מסביב, נכנסים בתזמון דרמטי, ומחזירים את הרשות לדבר.'),
          card('שונים זה מזה', 'מקשה תלמודי בלתי נלאה. מתקשר עכשווי אסטרטגי. הוגים שהקהל מכבד.'),
      ], 4, 'max-width:1240px')
      + '<p class="reveal r4 v5-note">%s כמה חכמים בפתיחה: בהחלטה.</p>' % tag('open', 'he') + LIB_HE)
main.append(slide(en, he))

# 12. SIX ROLES -----------------------------------------------------------
en = (head('How the room runs', 'Six roles, one experience', 48, tg=tag('closed', 'en'))
      + grid([
          card('The Stage and the Room', 'The physical setup, the participant stations, the host dashboard, and the surfaces where sages and audience appear.'),
          card('The Conductor (Nasi)', 'Decides which sages are relevant and who speaks, and calls for a challenge, a concession, a story or a hard question.'),
          card('The Quality Check (Av Beit Din)', 'Enforces the rules: state the other side fairly, attack the argument not the person, ground claims in something real.'),
          card('The Sages', 'Eighty distinct voices with historical grounding, driven in real time.'),
          card('Invisible Helpers', 'A background layer checking what the room never sees: accuracy, tone, and whether anyone is left out.'),
          card('The Scoreboard', 'Real-time signals for the room and the host: engagement, one-sidedness, shifting positions.'),
      ], 3, 'max-width:1240px'))
he = (head('איך החדר פועל', 'שישה תפקידים, חוויה אחת', 48, tg=tag('closed', 'he'))
      + grid([
          card('הבמה והחדר', 'ההתקנה הפיזית, עמדות המשתתפים, לוח הבקרה של המנחה, והמשטחים שעליהם מופיעים החכמים והקהל.'),
          card('המנצח (הנשיא)', 'מחליט אילו חכמים רלוונטיים ומי מדבר, וקורא לאתגר, להודאה, לסיפור או לשאלה קשה.'),
          card('בקרת האיכות (אב בית דין)', 'אוכף את הכללים: להציג את הצד השני בהגינות, לתקוף את הטיעון ולא את האדם, לעגן טענות במשהו אמיתי.'),
          card('החכמים', 'שמונים קולות שונים עם עיגון היסטורי, מונעים בזמן אמת.'),
          card('עוזרים בלתי נראים', 'שכבת רקע שבודקת מה שהחדר לא רואה: דיוק, טון, והאם מישהו נשאר בחוץ.'),
          card('לוח התוצאות', 'אותות בזמן אמת לחדר ולמנחה: מעורבות, חד-צדדיות, ותזוזת עמדות.'),
      ], 3, 'max-width:1240px'))
main.append(slide(en, he))

# 13. THE HOST ------------------------------------------------------------
KNOBS_EN = ['Sage frequency', 'Floor control', 'Scoring override', 'The gold buzzer', 'Kill switch on any AI line']
KNOBS_HE = ['תדירות החכמים', 'שליטה ברשות הדיבור', 'עקיפת הניקוד', 'הזמזם הזהוב', 'מתג כיבוי לכל שורה של AI']
en = (head('The host', 'A conductor of people, not a guide', 48, tg=tag('closed', 'en'))
      + grid([
          card('Why a human', 'Hand a person a microphone and say "just argue", and they freeze. When a room is shouting, no AI knows whom to answer. A charismatic human does. A performer, not a docent.'),
          card('The host console', lst(KNOBS_EN)),
      ], 2, 'max-width:1100px'))
he = (head('המנחה', 'מנצח של אנשים, לא מדריך', 48, tg=tag('closed', 'he'))
      + grid([
          card('למה אדם', 'תנו לאדם מיקרופון ותגידו לו "תתווכח", והוא קופא. כשחדר צועק, אף AI לא יודע למי לענות. אדם כריזמטי יודע. מבצע, לא מדריך.'),
          card('לוח הבקרה של המנחה', lst(KNOBS_HE)),
      ], 2, 'max-width:1100px'))
main.append(slide(en, he))

# 14. DILEMMAS ------------------------------------------------------------
def dil(lang):
    if lang == 'en':
        a = card('The case (sugya)', 'The goring ox, from Bava Kamma: liability, negligence and foreseeability when something you own causes harm. Is it a first offense, or an established pattern of danger?')
        b = card('The modern transformation', 'Liability when an autonomous vehicle hits someone. Same structure, new surface.', dark=True)
        t = head('The dilemmas', 'Built from real cases, not picked from headlines', 44, tg=tag('closed', 'en'))
        n = note('Each dilemma is built by a pair: an expert who knows the sugya, and an expert who knows its live modern analogue. Thirteen are already built.')
    else:
        a = card('המקרה (סוגיה)', 'השור הנוגח, מבבא קמא: אחריות, רשלנות וצפיות כשמשהו שבבעלותך גורם נזק. האם זו עבירה ראשונה, או דפוס סכנה מבוסס?')
        b = card('הטרנספורמציה המודרנית', 'אחריות כשרכב אוטונומי פוגע במישהו. אותו מבנה, משטח חדש.', dark=True)
        t = head('הדילמות', 'נבנות ממקרים אמיתיים, לא נבחרות מכותרות', 44, tg=tag('closed', 'he'))
        n = note('כל דילמה נבנית בזוג: מומחה שמכיר את הסוגיה, ומומחה שמכיר את המקבילה המודרנית החיה שלה. שלוש עשרה כבר נבנו.')
    flip = ' style="transform:scaleX(-1)"' if lang == 'he' else ''
    arrow = ('<div class="v5-arrow"><svg width="48" height="24" viewBox="0 0 48 24" fill="none" stroke="currentColor" '
             'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"%s><path d="M3 12h36M31 4l9 8-9 8"/></svg></div>') % flip
    return t + '<div class="v5-row reveal r3">%s%s%s</div>' % (a, arrow, b) + n
main.append(slide(dil('en'), dil('he')))

# 15. SAMPLE SESSION (reused) ---------------------------------------------
main.append(secs[11])

# 16. THE PHYSICAL ROOM ---------------------------------------------------
def room_svg(lang='en'):
    L = {'en': ('projection wall: virtual audience and sages', 'HOST', 'seating behind the stations'),
         'he': ('קיר הקרנה: קהל וירטואלי וחכמים', 'מנחה', 'ישיבה מאחורי העמדות')}[lang]
    cx, cy = 300, 250
    dots = []
    for row, r in enumerate((125, 170)):
        for i in range(6):
            ang = math.radians(212 + i * 23)
            dots.append('<circle cx="%.0f" cy="%.0f" r="9" fill="%s"/>' % (
                cx + r * math.cos(ang), cy + r * math.sin(ang), '#003057' if row == 0 else '#776E64'))
    return ('<svg viewBox="0 0 600 330" width="100%%" role="img" aria-label="Plan of the room: a three-quarter surround with two arcs of six stations, a host station, seating behind, and projection walls around.">'
            '<path d="M60 250 A240 240 0 0 1 540 250" fill="none" stroke="#BDD6E6" stroke-width="16" stroke-linecap="round"/>'
            '<path d="M95 250 A205 205 0 0 1 505 250" fill="none" stroke="#776E64" stroke-width="2" stroke-dasharray="6 6"/>'
            + ''.join(dots) +
            '<rect x="270" y="262" width="60" height="22" rx="4" fill="#003057"/>'
            '<text x="300" y="277" text-anchor="middle" font-size="11" fill="#fff" font-family="Montserrat,sans-serif">%s</text>'
            '<text x="300" y="30" text-anchor="middle" font-size="12" fill="#003057" font-family="Montserrat,sans-serif">%s</text>'
            '<text x="300" y="316" text-anchor="middle" font-size="12" fill="#776E64" font-family="Montserrat,sans-serif">%s</text>'
            '</svg>') % (L[1], L[0], L[2])

def room(lang):
    if lang == 'en':
        t = head('The room', 'The Yazdani design, kept', 46, tg=tag('closed', 'en'))
        li = lst(['Three-quarter surround theater',
                  '12 participant stations, six per team, in a semi-circle',
                  'A host station',
                  'Touchscreen and/or mobile input, to be proposed',
                  'Seating behind the stations',
                  'A smooth scrim in front of the perforated wall panels carries the virtual audience and the sages'])
        o = '<p class="reveal r4 v5-note">%s How many people per session: being confirmed. Earlier renderings are for reference only.</p>' % tag('open', 'en')
    else:
        t = head('החדר', 'עיצוב יזדני, נשמר', 46, tg=tag('closed', 'he'))
        li = lst(['תיאטרון מקיף שלושה רבעים',
                  '12 עמדות משתתפים, שש לכל קבוצה, בחצי עיגול',
                  'עמדת מנחה',
                  'קלט במסך מגע ו/או בנייד, להצעה',
                  'ישיבה מאחורי העמדות',
                  'מסך הקרנה חלק מול לוחות הקיר המחוררים נושא את הקהל הווירטואלי ואת החכמים'])
        o = '<p class="reveal r4 v5-note">%s כמה אנשים בסשן: בבירור. הדמיות קודמות הן לעיון בלבד.</p>' % tag('open', 'he')
    return t + '<div class="v5-split reveal r3"><div class="v5-plan">%s</div><div>%s</div></div>' % (room_svg(lang), li) + o
main.append(slide(room('en'), room('he')))

# ---- ACT 3 ----
# 17. PROOF (reused) ------------------------------------------------------
main.append(secs[16])

# 18. HONEST RISK ---------------------------------------------------------
en = (head('Honest risk', '70% solved. 30% ahead.', 56, tg=tag('closed', 'en'))
      + grid([
          card('Solved', 'Agent quality, protocols, 80 characters and the core framework.'),
          card('Ahead: orchestration', 'Agent-to-Agent-to-Human: getting agents to debate each other while synthesizing for the humans.'),
          card('Ahead: drama in the room', 'Does the experience produce real tension, engagement and emotional stakes?'),
      ], 3, 'max-width:1200px')
      + grid([card('How we reduce it', 'A proof-of-concept phase, tested with real visitors in focus groups, before anything is built.', '', dark=True)],
             1, 'max-width:1200px;margin-top:18px'))
he = (head('סיכון בכנות', '70% פתור, 30% לפנינו', 56, tg=tag('closed', 'he'))
      + grid([
          card('פתור', 'איכות הסוכנים, הפרוטוקולים, 80 דמויות והמסגרת המרכזית.'),
          card('לפנינו: תזמור', 'סוכן-לסוכן-לאדם: לגרום לסוכנים להתדיין זה עם זה ולסנתז לבני האדם.'),
          card('לפנינו: דרמה בחדר', 'האם החוויה יוצרת מתח אמיתי, מעורבות ומשקל רגשי?'),
      ], 3, 'max-width:1200px')
      + grid([card('איך מקטינים את זה', 'שלב הוכחת היתכנות, שנבדק עם מבקרים אמיתיים בקבוצות מיקוד, לפני שנבנה משהו.', '', dark=True)],
             1, 'max-width:1200px;margin-top:18px'))
main.append(slide(en, he))

# 19. PROCESS -------------------------------------------------------------
en = (head('How we find the partner', 'A concept phase before any build', 44,
           tg=tag('closed', 'en') + ' ' + tag('open', 'en') + ' <span class="v5-inline">Drafted and held. Not yet issued.</span>')
      + strip([
          ('Discover', 'Stakeholder interviews, audience analysis, comparable experiences.'),
          ('Define', 'Experience vision, visitor journey, who plays what.'),
          ('Design', 'Narrative, gameplay, AI experience, accessibility.'),
          ('Test the space', 'Projection, sound and light in the real room.'),
          ('Prove', 'A focus group package and a low-fidelity playtest.'),
      ])
      + grid([
          card('Concept only', 'No production, no fabrication.'),
          card('Time', '3 to 4 months for the concept phase. About one year for the whole path.'),
          card('Who', 'About 15 firms on the invitation list.'),
          card('Room to push back', 'Bidders do not get our ideas, so they can challenge them. The chosen firm keeps a role after the proof of concept.'),
      ], 4, 'max-width:1240px;margin-top:16px'))
he = (head('איך מוצאים את השותף', 'שלב קונספט לפני כל בנייה', 44,
           tg=tag('closed', 'he') + ' ' + tag('open', 'he') + ' <span class="v5-inline">מנוסח ומוחזק. עדיין לא יצא.</span>')
      + strip([
          ('גילוי', 'ראיונות בעלי עניין, ניתוח קהל, חוויות דומות.'),
          ('הגדרה', 'חזון החוויה, מסע המבקר, מי משחק מה.'),
          ('עיצוב', 'נרטיב, משחקיות, חוויית AI, נגישות.'),
          ('בדיקת החלל', 'הקרנה, סאונד ותאורה בחדר האמיתי.'),
          ('הוכחה', 'חבילת קבוצת מיקוד ומשחק ניסיון ברמת דיוק נמוכה.'),
      ])
      + grid([
          card('קונספט בלבד', 'ללא הפקה, ללא ייצור.'),
          card('זמן', '3 עד 4 חודשים לשלב הקונספט. כשנה לכל הדרך.'),
          card('מי', 'כ-15 משרדים ברשימת ההזמנה.'),
          card('מקום להתנגד', 'המציעים לא מקבלים את הרעיונות שלנו, כדי שיוכלו לאתגר אותם. המשרד שייבחר ממשיך בתפקיד אחרי הוכחת ההיתכנות.'),
      ], 4, 'max-width:1240px;margin-top:16px'))
main.append(slide(en, he))

# 20. SEQUENCE ------------------------------------------------------------
en = (head('What happens next', 'The path, without dates', 48,
           tg=tag('open', 'en') + ' <span class="v5-inline">Dates to be reset. Not yet confirmed.</span>')
      + strip([
          ('Now', 'This alignment session, 8 October.'),
          ('Funder', 'A response is expected after the holiday.'),
          ('Issue', 'The concept RFP goes out.'),
          ('Select', 'A firm is chosen.'),
          ('Concept', 'Three to four months of concept work.'),
          ('Test', 'A focus group, then the decision on the full build.'),
      ], 6))
he = (head('מה קורה עכשיו', 'הדרך, בלי תאריכים', 48,
           tg=tag('open', 'he') + ' <span class="v5-inline">תאריכים ייקבעו מחדש. עדיין לא מאושרים.</span>')
      + strip([
          ('עכשיו', 'מפגש הכיול הזה, 8 באוקטובר.'),
          ('מממן', 'תגובה צפויה אחרי החג.'),
          ('הוצאה', 'הצעת המחיר לקונספט יוצאת.'),
          ('בחירה', 'נבחר משרד.'),
          ('קונספט', 'שלושה עד ארבעה חודשים של עבודת קונספט.'),
          ('בדיקה', 'קבוצת מיקוד, ואז ההחלטה על הבנייה המלאה.'),
      ], 6))
main.append(slide(en, he))

# ---- ACT 4 ----
# 21. CLOSED VS OPEN ------------------------------------------------------
CL_EN = ['A framework, not a re-enactment of the court',
         'You win by listening. No winner is declared',
         'Sages on the periphery, unaligned, up to 80 character sheets',
         'A human host conducts the room',
         'Two audiences: trained and walk-in',
         'Dilemmas built from real cases',
         'The Yazdani physical design is kept',
         'Concept phase and focus group before any build']
OP_EN = ['The name',
         'Discourse only for launch (to ratify)',
         'How many people per session',
         'How many sages at launch',
         'When the concept RFP is issued',
         'Minute-by-minute gameplay: the concept phase will propose it, and focus groups will test it']
CL_HE = ['מסגרת, לא שחזור של בית הדין',
         'מנצחים בהקשבה. אין מנצח מוכרז',
         'חכמים בפריפריה, לא מזוהים, עד 80 דפי דמות',
         'מנחה אנושי מנהל את החדר',
         'שני קהלים: מאומנים ומזדמנים',
         'דילמות שנבנות ממקרים אמיתיים',
         'העיצוב הפיזי של יזדני נשמר',
         'שלב קונספט וקבוצת מיקוד לפני כל בנייה']
OP_HE = ['השם',
         'שיח בלבד לפתיחה (לאישור)',
         'כמה אנשים בסשן',
         'כמה חכמים בפתיחה',
         'מתי יוצאת הצעת המחיר לקונספט',
         'משחקיות דקה אחר דקה: שלב הקונספט יציע אותה וקבוצות המיקוד יבדקו אותה']
en = (head('The one-page summary', 'What is closed. What is open.', 44)
      + grid([card('Closed', lst(CL_EN), tag('closed', 'en')), card('Open', lst(OP_EN), tag('open', 'en'))],
             2, 'max-width:1240px;align-items:start'))
he = (head('סיכום בעמוד אחד', 'מה סגור. מה פתוח.', 44)
      + grid([card('סגור', lst(CL_HE), tag('closed', 'he')), card('פתוח', lst(OP_HE), tag('open', 'he'))],
             2, 'max-width:1240px;align-items:start'))
main.append(slide(en, he))

# 22. THE ASK -------------------------------------------------------------
en = ('<p class="label reveal">What we need</p>'
      '<h2 class="reveal r1" style="font-size:84px">Back the main line.</h2>'
      '<p class="tagline reveal r2" style="margin-top:6px">Here is where we stand. Now we move.</p>'
      '<p class="body-text reveal r3" style="max-width:860px;margin-top:22px;font-size:21px">We ask for your support, not a redesign. If you have a question, ask it now. We have probably worked it already, and we can say why we chose this and not that. If it is new, we will take it.</p>'
      '<p class="pull-quote reveal r4" style="max-width:900px;margin-top:28px;font-size:30px">"In Judaism, disagreement was never the problem. It was always the method."</p>')
he = ('<p class="label reveal">מה אנחנו צריכים</p>'
      '<h2 class="reveal r1" style="font-size:84px">תמכו בקו המרכזי.</h2>'
      '<p class="tagline reveal r2" style="margin-top:6px">כאן אנחנו עומדים. עכשיו מתקדמים.</p>'
      '<p class="body-text reveal r3" style="max-width:860px;margin-top:22px;font-size:21px">אנחנו מבקשים תמיכה, לא עיצוב מחדש. אם יש לכם שאלה, שאלו עכשיו. כנראה כבר עבדנו עליה, ואפשר להסביר למה בחרנו כך ולא אחרת. אם היא חדשה, ניקח אותה.</p>'
      '<p class="pull-quote reveal r4" style="max-width:900px;margin-top:28px;font-size:30px">"ביהדות, מחלוקת מעולם לא הייתה הבעיה. היא תמיד הייתה השיטה."</p>')
main.append(slide(en, he))

# act labels for every main slide (reused sections get retagged too)
ACTS = [ACT1] * 6 + [ACT2] * 10 + [ACT3] * 4 + [ACT4] * 2
assert len(main) == len(ACTS) == 22, (len(main), len(ACTS))
main = [re.sub(r'data-act="[^"]*"', 'data-act="%s"' % ACTS[i], m, count=1) for i, m in enumerate(main)]
main = [m if i == 0 else m.replace('class="slide active"', 'class="slide"', 1) for i, m in enumerate(main)]

# ---------------------------------------------------------------- appendix
def with_id(sec, new_id):
    return sec.replace('data-appendix="true">', 'data-appendix="true" id="%s">' % new_id, 1)

LOTS = [
    ('A. Creative Studio', 'Art direction and style guide, sage character design and animation, visitor experience and UI, projection and media content, gamification skin.', 'Paid concept phase with 3 to 4 competing firms.'),
    ('B. Content and Research', 'Four expert desks (Jewish law, dilemma translation, discourse, persona creation), dilemma library, sage corpora, civility rubric.', 'Direct expert hiring per desk.'),
    ('C. AI and Software', 'The Conductor, sage runtime, discourse engine, Hebrew speech, render pipeline, host console, content system, evaluation.', 'Systems integrator.'),
    ('D. Physical', '12 stations with per-person mics, spotlights, projection and scrim, sage screens, spatial audio, show control.', 'Procurement.'),
    ('E. Integration', 'Interface management, three integration cycles, acoustics, calibration, commissioning, host training, year-one operations.', 'Open: bundle with C, or split.'),
    ('F. AI Graphics', 'AI graphics and integration with the physical space, around human-machine interaction.', 'Not further specified in the source.'),
]
rows = ''.join('<tr><td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>' % r for r in LOTS)
LOTS_SEC = ('<section class="slide" data-act="APPENDIX" data-appendix="true" id="appendix-lots">\n'
            '  <div class="lang-en">\n    <div class="layout-statement" style="align-items:flex-start;text-align:left;max-width:1100px;margin:0 auto;">\n'
            '      <p class="appendix-label reveal">Appendix G</p>\n'
            '      <h2 class="reveal r1" style="font-size:44px">Full-build lot structure</h2>\n'
            '      <p class="reveal r2 v5-sub">July 2026 working draft. Status to confirm: it is not part of the concept RFP, and amounts are held in the room file, not shown here.</p>\n'
            '      <table class="v5-table reveal r3"><thead><tr><th>Lot</th><th>What is inside</th><th>Route</th></tr></thead><tbody>%s</tbody></table>\n'
            '    </div>\n  </div>\n'
            '  <div class="lang-he" dir="rtl">\n    <div class="layout-statement" style="align-items:flex-start;text-align:right;max-width:1100px;margin:0 auto;">\n'
            '      <p class="appendix-label reveal">נספח G</p>\n'
            '      <h2 class="reveal r1" style="font-size:44px">מבנה חבילות לבנייה המלאה</h2>\n'
            '      <p class="reveal r2 v5-sub">טיוטת עבודה מיולי 2026. הסטטוס לאישור. היא לא חלק מהצעת המחיר לקונספט, והסכומים נשמרים בקובץ החדר ולא מוצגים כאן.</p>\n'
            '      <p class="reveal r3 v5-note" dir="ltr" style="text-align:left">Lots A-F: see the English view for the table.</p>\n'
            '    </div>\n  </div>\n</section>\n') % rows

app = [secs[23], secs[24], secs[25], secs[26],
       with_id(secs[27], 'appendix-dilemmas'), with_id(secs[28], 'appendix-personas'),
       secs[29], LOTS_SEC]
N = len(main)
body = ''.join(main) + ''.join(app)

# ---------------------------------------------------------------- quick nav
QN = [
    ('Act 1: Where we stand', ['Title', 'Why we are here', 'Questions already worked', 'The problem', 'What the word means', 'The cognitive twist']),
    ('Act 2: The experience', ['The room in one minute', 'Four conversations', 'You win by listening', 'Mode and audience', 'The sages', 'Six roles', 'The host', 'The dilemmas', 'Sample session', 'The physical room']),
    ('Act 3: How we get there', ['Proof: Rambam', 'Honest risk', 'Finding the partner', 'What happens next']),
    ('Act 4: What we need', ['Closed vs open', 'The ask']),
]
APPX = [('appendix-architecture', 'ARCH', 'Architecture v3.1'), ('appendix-research', 'R', 'Tech landscape research'),
        ('appendix-tech', 'A', 'Terms and terminology'), ('appendix-modes', 'B', '13 thinking modes'),
        ('appendix-dilemmas', 'C', 'Pre-built dilemmas'), ('appendix-personas', 'D', 'Visitor personas'),
        ('sage-library', 'E', 'Sage library (80)'), ('appendix-lots', 'G', 'Full-build lot structure')]
qn, idx = '', 0
for grp, items in QN:
    qn += '        <div class="qn-group">%s</div>\n' % grp
    for name in items:
        qn += '        <button class="qn-item" onclick="qnGo(%d)"><span class="qn-num">%02d</span>%s</button>\n' % (idx, idx + 1, name)
        idx += 1
assert idx == N, (idx, N)
qn += '        <div class="qn-group">Appendix</div>\n'
for aid, k, name in APPX:
    qn += '        <button class="qn-item" onclick="qnGo(\'%s\')"><span class="qn-num" style="font-size:10px">%s</span>%s</button>\n' % (aid, k, name)

POST, n = re.subn(r'<div class="quick-nav-menu" id="quickNavMenu">.*?\n      </div>\n    </div>\n    <button class="lang-toggle"',
                  lambda m: '<div class="quick-nav-menu" id="quickNavMenu">\n' + qn + '      </div>\n    </div>\n    <button class="lang-toggle"',
                  POST, count=1, flags=re.S)
assert n == 1, 'quick nav not found'
POST = POST.replace('01 / 22', '01 / %02d' % N).replace('ACT 1: THE HOOK', ACT1)
POST = POST.replace('<img src="assets/logos/motj-logo-horizontal.png" alt="MOTJ" class="nav-logo">',
                    '<a href="../" class="v5-versions" title="All versions"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>Versions</a>'
                    '<img src="assets/logos/motj-logo-horizontal.png" alt="MOTJ" class="nav-logo">', 1)
# no auto tour (it describes the old deck); narration audio is not shipped with v5
POST = POST.replace("if (!localStorage.getItem('sanhedrin-tour-done'))", 'if (false)')

CSS = (HERE / 'v5.css').read_text(encoding='utf-8')
PRE = PRE.replace('<title>The Sanhedrin Educational Experience | MOTJ</title>',
                  '<title>The Convergence Lab | MOTJ - v5 expert team master</title>', 1)
PRE = PRE.replace('</head>', '<style>\n' + CSS + '\n</style>\n</head>', 1)

html = PRE + body + POST
# asset paths: v5 lives one folder below the shared assets
html = re.sub(r'(["\'(=])(slides|assets|audio|video|docs)/', r'\1../\2/', html)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html, encoding='utf-8')
print('v5 written: %s  main=%d appendix=%d  bytes=%d' % (OUT, N, len(app), len(html)))
assert '—' not in ''.join(main) + LOTS_SEC, 'em-dash in new content'
