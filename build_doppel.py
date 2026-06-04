import os, json

p = r'C:\Users\lingzhu12\AppData\Local\Temp\weread_warehouse\reading-doppelgangers.html'

notes = {}
try:
    nd = json.loads(open(r'C:\Users\lingzhu12\AppData\Local\Temp\weread_warehouse\merged\all_notebooks.json','rb').read())
    for b in nd:
        t = b.get('book',{}).get('title','')
        notes[t] = {'n': b.get('noteCount',0)+b.get('reviewCount',0)+b.get('bookmarkCount',0),
                    'h': b.get('noteCount',0), 'r': b.get('reviewCount',0)}
except: pass

finished_books = {}
try:
    fb = json.loads(open(r'C:\Users\lingzhu12\AppData\Local\Temp\weread_warehouse\finished_books.json','rb').read())
    finished_books = fb
except: pass

# Define 5 doppelgängers with their books
doppels = [
    {
        'name': '解谜人',
        'subtitle': 'Puzzle Solver',
        'color': '#4a6fa5',
        'bg': '#f0f4fa',
        'desc': '为一个精心构建的叙事而生。你读悬疑推理不是为了打发时间，而是为了享受解谜的智力快感——线索如何铺设、结构如何收束、真相如何在最后一刻翻转。41本已读完的悬疑推理小说，从本格派到社会派，从日式致郁到意式优雅，你的书架本身就是一座犯罪博物馆。',
        'question': '什么样的谜题让你愿意在深夜继续翻页？',
        'books': [
            ('Blue', '叶真中显', 2024),
            ('阳光劫匪倒转地球', '伊坂幸太郎', 2024),
            ('十万分之一的偶然', '松本清张', 2021),
            ('箱庭图书馆', '乙一', 2021),
            ('D坂杀人事件', '江户川乱步', 2020),
            ('哈利·波特与阿兹卡班囚徒', 'J.K.罗琳', 2023),
            ('哈利波特與密室', 'J·K·羅琳', 2021),
            ('哈利·波特与凤凰社', 'J.K.罗琳', 2024),
            ('醉步男', '小林泰三', 2023),
            ('无人生还', '阿加莎·克里斯蒂', 2021),
        ]
    },
    {
        'name': '世界公民',
        'subtitle': 'Cosmopolitan',
        'color': '#3a8a7a',
        'bg': '#f0f8f5',
        'desc': '不满足于单一文化的声音。你通过翻译文学在世界各地旅行——从拉美的魔幻现实到日本的物哀幽玄，从英伦的优雅克制到韩国的锋利冷峻。略萨的结构迷宫、马尔克斯的家族史诗、石黑一雄的记忆叙事、金爱烂的日常锋利——你的阅读护照上盖满了各国的印章。',
        'question': '下一个想通过文学抵达的国家是哪里？',
        'books': [
            ('没有人给他写信的上校', '加西亚·马尔克斯', 2025),
            ('番石榴飘香', '加西亚·马尔克斯', 2026),
            ('略萨作品：城市与狗', '马里奥·巴尔加斯·略萨', 2025),
            ('长日将尽', '石黑一雄', 2025),
            ('埃莱娜·费兰特作品系列：暗处的女儿', '埃莱娜·费兰特', 2025),
            ('外面是夏天', '金爱烂', 2024),
            ('滔滔生活', '金爱烂', 2024),
            ('编舟记', '三浦紫苑', 2020),
            ('如雪如山', '张天翼', 2024),
            ('时间的针脚', '玛丽亚·杜埃尼亚斯', 2024),
            ('不止魔幻：拉美文学第一课', '侯健', 2026),
            ('我的职业是小说家', '村上春树', 2026),
        ]
    },
    {
        'name': '求道者',
        'subtitle': 'Seeker',
        'color': '#c4934a',
        'bg': '#faf6ed',
        'desc': '阅读是一种自我审视的方式。你读哲学、心理学、女性主义、社会批判——不只是为了获取知识，而是为了回答一个更根本的问题："我该如何生活？"从陈嘉映的哲学沉思到上野千鹤子的尖锐剖析，从韩炳哲的社会诊断到乔丹·彼得森的人生法则，你在不同思想体系之间寻找属于自己的答案。',
        'question': '你真正想问自己的问题是什么？',
        'books': [
            ('走出唯一真理观', '陈嘉映', 2020),
            ('人生十二法则', '乔丹·彼得森', 2020),
            ('当下的力量', '埃克哈特·托利', 2021),
            ('爱的五种能力', '赵永久', 2021),
            ('人间值得', '中村恒子', 2023),
            ('与焦虑和解', '汪淑媛', 2024),
            ('目光', '陶勇', 2020),
            ('上野千鹤子的私房谈话', '上野千鹤子', 2024),
            ('上野千鹤子的私房谈话III', '上野千鹤子', 2025),
            ('倦怠社会', '韩炳哲', 2024),
            ('宝贵的人生建议', '凯文·凯利', 2024),
            ('人生复本', '布莱克·克劳奇', 2024),
        ]
    },
    {
        'name': '档案员',
        'subtitle': 'Archivist',
        'color': '#b5686a',
        'bg': '#faf2f2',
        'desc': '一个人的故事就是时代的历史。你读传记、回忆录、纪实文学——不是为了消遣，而是为了见证。李安的隐忍与爆发、波伏瓦的清醒与自由、茨威格笔下消逝的欧洲、阿列克谢耶维奇记录的战火中的女性——你在他人生命中寻找历史的纹理。每一本读完的传记，都是你与一个灵魂的长谈。',
        'question': '记忆被书写之后，会变成什么？',
        'books': [
            ('十年一觉电影梦：李安传', '张靓蓓/李安', 2020),
            ('清算已毕：波伏瓦自传', '西蒙娜·德·波伏瓦', 2025),
            ('昨日的世界', '茨威格', 2025),
            ('独自上路', '哈维尔·萨莫拉', 2024),
            ('莉莉亚娜不可战胜的夏天', '克里斯蒂娜·里韦拉·加尔萨', 2026),
            ('战争中没有女性', 'S.A.阿列克谢耶维奇', 2022),
            ('Cuando hablo de correr', '村上春树', 2024),
            ('活着为了讲述', '加西亚·马尔克斯', 2023),
            ('死在这里也不错', '马家辉', 2021),
            ('老女孩', '玛丽·科克', 2025),
        ]
    },
    {
        'name': '双语者',
        'subtitle': 'Bilingual',
        'color': '#7c6ba0',
        'bg': '#f4f0fa',
        'desc': '阅读不依赖翻译。你已经用西班牙语读完了从科幻到自传、从科普到心理学的十几本书——有些甚至是在中译本之前读完的。这不仅仅是一项语言技能，而是一种阅读身份的转变：当你可以直接进入另一种语言的思想世界时，你就不再只是一个中国读者，而是一个用西班牙语思考、感受和质疑的人。',
        'question': '用另一种语言阅读时，你变成了谁？',
        'books': [
            ('Cuatro mil semanas', 'Oliver Burkeman', 2025),
            ('Deberías hablar con alguien', 'Lori Gottlieb', 2026),
            ('Entiende tu mente', 'Mónica González', 2025),
            ('Nosotras. Historias de mujeres', 'Rosa Montero', 2025),
            ('Harry Potter y el cáliz de fuego', 'J.K. Rowling', 2021),
            ('De qué hablo cuando hablo de correr', 'Haruki Murakami', 2024),
            ('Proyecto Hail Mary', 'Andy Weir', 2024),
            ('Yo tuve un sueño', 'Juan Pablo Villalobos', 2025),
            ('Física para dummies', 'Steven Holzner', 2024),
            ('Dos soledades', 'García Márquez & Vargas Llosa', 2024),
            ('El amor en los tiempos del cólera', 'Gabriel García Márquez', 2023),
        ]
    }
]

# Enrich books with note data
for d in doppels:
    for i, (t, a, y) in enumerate(d['books']):
        n = notes.get(t, {})
        d['books'][i] = (t, a, y, n.get('n', 0), n.get('h', 0), n.get('r', 0))

css = """
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Helvetica Neue",sans-serif;background:#faf8f5;color:#1a1a1a;line-height:1.6}
header{text-align:center;padding:4rem 1.5rem 2rem;max-width:48rem;margin:0 auto}
header h1{font-size:clamp(1.8rem,4vw,2.8rem);font-weight:600;letter-spacing:-.02em;margin-bottom:.75rem}
header .sub{font-size:1rem;color:#6b6b6b;line-height:1.7}
.content{max-width:80rem;margin:0 auto;padding:0 1.5rem 3rem}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(22rem,1fr));gap:1.5rem}
.card{border-radius:1rem;padding:1.75rem;position:relative;overflow:hidden}
.card .accent{position:absolute;top:0;left:0;right:0;height:4px}
.card h2{font-size:1.3rem;font-weight:600;letter-spacing:-.01em;margin-top:.25rem}
.card .sub{font-size:.75rem;font-weight:400;color:#6b6b6b;margin-bottom:.75rem;letter-spacing:.05em;text-transform:uppercase}
.card .desc{font-size:.85rem;color:#4a4a4a;line-height:1.7;margin-bottom:1rem}
.card .question{font-size:.78rem;color:#8b7355;font-style:italic;padding:.75rem;border-radius:.5rem;margin-bottom:1rem;background:rgba(0,0,0,.03)}
.book-list{list-style:none}
.book-item{padding:.5rem .65rem;border-radius:.5rem;cursor:pointer;transition:background .2s;font-size:.85rem;display:flex;justify-content:space-between;align-items:center}
.book-item:hover{background:rgba(0,0,0,.04)}
.book-item .title{font-weight:500}
.book-item .yr{font-size:.72rem;color:#8f8f8f}
.book-detail{font-size:.78rem;color:#6b6b6b;padding:.5rem .65rem .65rem;display:none;line-height:1.6;border-top:1px solid rgba(0,0,0,.06);margin-top:0}
.book-detail.open{display:block}
.book-detail .tag{display:inline-block;font-size:.65rem;padding:.15rem .5rem;border-radius:999px;margin-right:.3rem;margin-top:.25rem}
.tag.valid{background:#d4edda;color:#155724}
.tag.questionable{background:#fff3cd;color:#856404}
.footer{text-align:center;padding:3rem 1.5rem;color:#8f8f8f;font-size:.8rem;max-width:36rem;margin:0 auto;line-height:1.7}
@media(max-width:600px){.grid{grid-template-columns:1fr}header{padding:2.5rem 1rem 1.5rem}.content{padding:0 1rem 2rem}.card{padding:1.25rem}}
"""

html = []
html.append('<!DOCTYPE html>')
html.append('<html lang="zh-CN">')
html.append('<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">')
html.append('<title>Reading Doppelgängers — 你的阅读分身</title>')
html.append('<style>' + css.strip() + '</style>')
html.append('</head><body>')

html.append('<header>')
html.append('<h1>Reading Doppelgängers</h1>')
html.append('<p class="sub">你的阅读分身 — 基于 ' + str(len(finished_books)) + ' 本已读完书籍的分析</p>')
html.append('</header>')

html.append('<div class="content"><div class="grid">')

for d in doppels:
    html.append('<div class="card" style="background:' + d['bg'] + '">')
    html.append('<div class="accent" style="background:' + d['color'] + '"></div>')
    html.append('<div class="sub">' + d['subtitle'] + '</div>')
    html.append('<h2 style="color:' + d['color'] + '">' + d['name'] + '</h2>')
    html.append('<div class="desc">' + d['desc'] + '</div>')
    html.append('<div class="question">' + d['question'] + '</div>')
    html.append('<ul class="book-list">')
    for t, a, y, nt, h, rv in d['books']:
        html.append('<li>')
        html.append('<div class="book-item" onclick="toggle(this)">')
        html.append('<span class="title">' + t + '</span>')
        html.append('<span class="yr">' + (str(y) if y else '?') + '</span>')
        html.append('</div>')
        html.append('<div class="book-detail">')
        html.append('<div>作者：' + a + '</div>')
        if nt > 0:
            html.append('<div>笔记：' + str(nt) + ' 条（划线 ' + str(h) + ' + 想法 ' + str(rv) + '）</div>')
            html.append('<span class="tag valid">VALID</span>')
        else:
            html.append('<div>笔记：数据未获取</div>')
            html.append('<span class="tag questionable">QUESTIONABLE</span>')
        html.append('</div>')
        html.append('</li>')
    html.append('</ul></div>')

html.append('</div></div>')

html.append('<div class="footer">')
html.append('这些分身展示了你在不同阶段与心境下的阅读人格和精神兴趣。')
html.append('每个分身对应若干已读完书籍，一本书可能出现在多个分身中，但主要归类在最匹配的角色下。<br><br>')
html.append('基于微信读书API数据 · 2020-2026 · ' + str(len(finished_books)) + '本已读完书籍')
html.append('</div>')

html.append('<script>function toggle(el){var d=el.nextElementSibling;if(d){d.classList.toggle("open")}}</script>')
html.append('</body></html>')

with open(p, 'w', encoding='utf-8') as f:
    f.write('\n'.join(html))

print('Written: ' + str(len(html)) + ' lines to ' + p)
