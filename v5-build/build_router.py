#!/usr/bin/env python3
"""Write the version router (index.html). Add a version = add a dict to VERSIONS."""
import pathlib, html
HERE = pathlib.Path(__file__).resolve().parent
DEPLOY = HERE.parent
VERSIONS = [
    dict(href='v5/', badge='CURRENT', cls='current', n='v5', title='Expert team master',
         text='The full deck for the 8 October 2026 alignment session: what is closed, what is open, and what we ask of the team.',
         meta=['22 slides', 'EN / HE', 'With appendix']),
    dict(href='original.html', badge='ARCHIVE', cls='archive', n='Original', title='Original deck',
         text='The deck as last updated on 25 May 2026, kept exactly as it was.',
         meta=['23 slides', 'EN / HE', 'With narration']),
]
ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
cards = ''
for v in VERSIONS:
    cards += ('    <a class="v v--%s" href="%s">\n      <span class="badge badge--%s">%s</span>\n'
              '      <span class="vn">%s</span>\n      <h2>%s</h2>\n      <p>%s</p>\n'
              '      <div class="meta">%s</div>\n      <span class="open">Open this version %s</span>\n    </a>\n') % (
        v['cls'] if v['cls'] == 'current' else 'archive', v['href'], v['cls'], v['badge'], html.escape(v['n']),
        html.escape(v['title']), html.escape(v['text']), ''.join('<span>%s</span>' % html.escape(m) for m in v['meta']), ARROW)
tpl = (HERE / 'router.template.html').read_text(encoding='utf-8')
clarity = pathlib.Path('/tmp/claude-1000/-home-jsagi/f5e0a63a-b50b-4c4e-845f-83d58d2d8b8f/scratchpad/clarity.txt')
snippet = clarity.read_text() if clarity.exists() else (HERE / 'clarity.txt').read_text()
(HERE / 'clarity.txt').write_text(snippet)
out = tpl.replace('%%CLARITY%%', snippet).replace('%%CARDS%%', cards)
(DEPLOY / 'index.html').write_text(out, encoding='utf-8')
print('router written', len(out))
