import json, os

p_out = r'C:\Users\lingzhu12\AppData\Local\Temp\weread_warehouse\life-stratum-archive.html'
p_data = r'C:\Users\lingzhu12\AppData\Local\Temp\weread_warehouse\stratum_data.json'

data = json.load(open(p_data, 'r', encoding='utf-8'))
strata = data['strata']
transitions = data['transitions']
questions = data['questions']

lines = []
def w(s): lines.append(s)

w('<!DOCTYPE html>')
w('<html lang="zh-CN">')
w('<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">')
w('<title>Life Stratum Archive — 人生地层档案</title>')
w('<style>')
w('*{margin:0;padding:0;box-sizing:border-box}')
w('body{font-family:Georgia,"Noto Serif SC","Source Han Serif SC",serif;background:#f7f4ef;color:#2c2c2c;line-height:1.7}')
w('.cover{min-height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:2rem;position:relative}')
w('.cover::after{content:"";position:absolute;bottom:0;left:10%;right:10%;height:1px;background:#d0ccc4}')
w('.cover .label{font-size:.75rem;letter-spacing:.15em;text-transform:uppercase;color:#99948b;margin-bottom:1rem}')
w('.cover h1{font-size:clamp(2rem,5vw,3.6rem);font-weight:400;letter-spacing:-.02em;color:#2c2c2c}')
w('.cover .sub{font-size:clamp(1rem,2vw,1.25rem);color:#6b665b;margin-top:.75rem;font-style:italic}')
w('.cover .anchor{position:absolute;bottom:2.5rem;font-size:.8rem;color:#99948b;animation:float 2s ease-in-out infinite}')
w('@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(6px)}}')
w('.section{max-width:48rem;margin:0 auto;padding:4rem 1.5rem}')
w('.section-head{display:flex;align-items:baseline;gap:.75rem;margin-bottom:2rem}')
w('.section-head .roman{font-size:1.1rem;font-weight:400;color:#b0a89a;letter-spacing:.05em}')
w('.section-head h2{font-size:1.35rem;font-weight:400;color:#2c2c2c}')
w('.section-head .line{flex:1;height:1px;background:#d0ccc4}')
w('.intro-text{font-size:.95rem;color:#5a5548;line-height:1.9;margin-bottom:2.5rem;padding:1.25rem 1.5rem;background:#fff;border-radius:.75rem;box-shadow:0 1px 4px rgba(0,0,0,.04)}')
w('.stratum{margin-bottom:2rem}')
w('.stratum-card{border-radius:.75rem;overflow:hidden;background:#fff;box-shadow:0 1px 4px rgba(0,0,0,.04);transition:box-shadow .2s}')
w('.stratum-card:hover{box-shadow:0 3px 12px rgba(0,0,0,.08)}')
w('.stratum-bar{height:4px}')
w('.stratum-body{padding:1.5rem 1.75rem}')
w('.stratum-meta{display:flex;flex-wrap:wrap;gap:.35rem .75rem;font-size:.78rem;color:#8f8a7d;margin-bottom:.25rem}')
w('.stratum-meta span{background:#f3f0ea;padding:.1rem .5rem;border-radius:3px}')
w('.stratum-title{font-size:1.2rem;font-weight:500;color:#2c2c2c;margin-bottom:.2rem}')
w('.stratum-en{font-size:.82rem;color:#b0a89a;font-style:italic;margin-bottom:.6rem}')
w('.stratum-question{font-size:.85rem;color:#6b665b;font-style:italic;margin-bottom:.75rem;padding:.5rem .75rem;background:#f7f4ef;border-radius:.4rem;border-left:3px solid}')
w('.stratum-body-text{font-size:.88rem;color:#4a473e;line-height:1.85;margin-bottom:1rem}')
w('.stratum-outcomes{display:grid;grid-template-columns:1fr 1fr 1fr;gap:.75rem;font-size:.78rem}')
w('.stratum-outcomes div{padding:.5rem .65rem;border-radius:.4rem}')
w('.outcome-left{background:#f8f0ef;color:#7a5a55}')
w('.outcome-lost{background:#f3f0ea;color:#6b665b}')
w('.outcome-grew{background:#eef3ed;color:#4a6a4a}')
w('.outcome-label{font-size:.65rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;margin-bottom:.15rem;opacity:.6}')
w('@media(max-width:600px){.stratum-outcomes{grid-template-columns:1fr;gap:.4rem}}')
w('.transition{margin-bottom:1.25rem;padding:1rem 1.25rem;background:#fff;border-radius:.6rem;box-shadow:0 1px 4px rgba(0,0,0,.04);border-left:3px solid #c0b8a8}')
w('.transition .year{font-size:.72rem;color:#99948b;letter-spacing:.05em}')
w('.transition h4{font-size:.95rem;font-weight:500;color:#4a473e;margin-bottom:.25rem}')
w('.transition p{font-size:.85rem;color:#6b665b;line-height:1.8}')
w('.question-section{max-width:48rem;margin:0 auto;padding:2rem 1.5rem 4rem}')
w('.question-item{margin-bottom:1.25rem;padding:1.25rem 1.5rem;background:#fff;border-radius:.6rem;box-shadow:0 1px 4px rgba(0,0,0,.04);border-left:3px solid #b0a89a}')
w('.question-item .q{font-size:.95rem;font-weight:500;color:#2c2c2c;margin-bottom:.2rem}')
w('.question-item .meta{font-size:.72rem;color:#99948b;margin-bottom:.4rem}')
w('.question-item p{font-size:.85rem;color:#6b665b;line-height:1.8}')
w('.root-section{max-width:36rem;margin:0 auto;padding:3rem 1.5rem 4rem;text-align:center}')
w('.root-section .label{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:#99948b;margin-bottom:.75rem}')
w('.root-section .root-q{font-size:clamp(1.1rem,2.5vw,1.4rem);font-weight:400;color:#2c2c2c;line-height:1.6;padding:1.5rem;background:#fff;border-radius:.75rem;box-shadow:0 1px 4px rgba(0,0,0,.04);border:1px solid #e5e0d6}')
w('.footer{text-align:center;padding:3rem 1.5rem;color:#99948b;font-size:.78rem;max-width:36rem;margin:0 auto;line-height:1.7;border-top:1px solid #e5e0d6}')
w('@media print{body{background:#fff}.cover{min-height:auto;padding:3rem 1rem}.cover::after{display:none}.stratum-card{break-inside:avoid;box-shadow:none;border:1px solid #eee}}')
w('@media(max-width:600px){.section{padding:2.5rem 1rem}.stratum-body{padding:1.25rem}}')
w('</style></head><body>')

# Cover
w('<div class="cover">')
w('<div class="label">Life Stratum Archive</div>')
w('<h1>人生地层档案</h1>')
w('<div class="sub">2017 — 2026 · 从秘鲁到巴塞罗那到中国</div>')
w('<div class="anchor">&darr;</div>')
w('</div>')

# Introduction
w('<div class="section">')
w('<div class="section-head"><span class="roman">&mdash;</span><h2>阅读指南</h2><span class="line"></span></div>')
w('<div class="intro-text">')
w('这不是一份简历。不是时间线，不是大事记，甚至不是传记。<br><br>')
w('这是把人生当作地层来考察的尝试。<strong>地层</strong>（stratum）不是一个年份，而是一段具有共同问题、共同身份和共同方向的时期。一个地层由三样东西定义：你在问什么？你是谁？你往哪里去？<br><br>')
w('以下页面中，地层从最老到最新排列。最老的地层最深，最新地层仍在沉积。每一个地层都留下了它带走的东西和它留下的东西——以及它变成了什么。')
w('</div>')
w('</div>')

# Strata I to V (oldest first)
colors_bar = ['#8a7a6a', '#6b8a7a', '#8a7a9a', '#6b7a8a', '#9a7a6a']
strata_display = list(reversed(strata))

for i, s in enumerate(strata_display):
    c = colors_bar[i]
    w('<div class="section">')
    w('<div class="section-head"><span class="roman">' + s['idx'] + '.</span><h2>' + s['name'] + '</h2><span class="line"></span></div>')
    w('<div class="stratum">')
    w('<div class="stratum-card">')
    w('<div class="stratum-bar" style="background:' + c + '"></div>')
    w('<div class="stratum-body">')
    w('<div class="stratum-meta"><span>' + s['time'] + '</span><span>' + s['loc'] + '</span></div>')
    w('<div class="stratum-title">' + s['name'] + '</div>')
    w('<div class="stratum-en">' + s['en'] + '</div>')
    w('<div class="stratum-question" style="border-left-color:' + c + '">' + s['question'] + '</div>')
    w('<div class="stratum-body-text">' + s['body'].replace('\n', '<br>') + '</div>')
    w('<div class="stratum-outcomes">')
    w('<div class="outcome-left"><div class="outcome-label">留下的</div>' + s['left'] + '</div>')
    w('<div class="outcome-lost"><div class="outcome-label">失去的</div>' + s['lost'] + '</div>')
    w('<div class="outcome-grew"><div class="outcome-label">生长出的</div>' + s['grew'] + '</div>')
    w('</div></div></div></div>')
    w('</div>')

# Transitions section
w('<div class="section">')
w('<div class="section-head"><span class="roman">&mdash;</span><h2>转折</h2><span class="line"></span></div>')
w('<div class="intro-text" style="margin-bottom:1.5rem">')
w('每一个地层的边界由一次转折标记。以下是五次关键的转折——不是事件列表，而是沉积方向改变的瞬间。')
w('</div>')
for t in transitions:
    w('<div class="transition">')
    w('<div class="year">' + t['year'] + '</div>')
    w('<h4>' + t['name'] + '</h4>')
    w('<p>' + t['body'] + '</p>')
    w('</div>')
w('</div>')

# Root question
w('<div class="root-section">')
w('<div class="label">根问题</div>')
w('<div class="root-q">&#x201c;我如何在变化中保存一个连续的自己？&#x201d;</div>')
w('</div>')

# Long questions
w('<div class="section">')
w('<div class="section-head"><span class="roman">&mdash;</span><h2>贯穿地层的问题</h2><span class="line"></span></div>')
for q in questions:
    w('<div class="question-item">')
    w('<div class="q">' + q['q'] + '</div>')
    w('<div class="meta">' + q['meta'] + '</div>')
    w('<p>' + q['body'] + '</p>')
    w('</div>')
w('</div>')

# Footer
w('<div class="footer">')
w('Life Stratum Archive · 人生地层档案<br>')
w('基于个人经历与阅读数据 · 2017&ndash;2026<br><br>')
w('每一个地层都没有真正消失。它们只是沉积在下面，成为后来所有地层的基础。')
w('</div>')

w('</body></html>')

with open(p_out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Written ' + str(len(lines)) + ' lines to ' + p_out)
