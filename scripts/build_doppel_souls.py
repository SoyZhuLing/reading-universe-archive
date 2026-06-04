import json, os

p_out = r'C:\Users\lingzhu12\AppData\Local\Temp\weread_warehouse\reading-doppelgangers.html'

finished = json.load(open(r'C:\Users\lingzhu12\AppData\Local\Temp\weread_warehouse\finished_books.json', 'rb'))
notebooks = json.load(open(r'C:\Users\lingzhu12\AppData\Local\Temp\weread_warehouse\merged\all_notebooks.json', 'rb'))

# Build note lookup
notes_map = {}
for nb in notebooks:
    t = nb.get('book',{}).get('title','')
    notes_map[t] = {'n': nb.get('noteCount',0), 'r': nb.get('reviewCount',0)}

# Title fuzzy matcher
def find_book(keywords):
    """Find first finished book whose title contains any keyword."""
    kw_list = keywords if isinstance(keywords, list) else [keywords]
    for kw in kw_list:
        for t, info in finished.items():
            if kw.lower() in t.lower():
                n = notes_map.get(t, {})
                return {
                    'title': t,
                    'author': info.get('author','').lstrip('[').split(']')[-1].strip() if info.get('author') else '',
                    'year': info.get('year','?'),
                    'cat': info.get('cat',''),
                    'highlights': n.get('n',0),
                    'reviews': n.get('r',0)
                }
    return None

def find_books(keywords_list, max_results=15):
    """Find multiple books."""
    results = []
    for kw in keywords_list:
        b = find_book([kw])
        if b and b['title'] not in [r['title'] for r in results]:
            results.append(b)
    return results[:max_results]

# ===== Soul 1: 见证者 Witness =====
# Books where the reader inhabits another person's life
witness_books = find_books([
    '十年一觉电影梦', '清算已毕', '昨日的世界', '独自上路',
    '活着为了讲述', '战争中没有女性', '莉莉亚娜', '死在这里也不错',
    '江城', '寻路中国', '在中国大地上', '夜航西飞',
    '秋园', '暮色将尽', '风沙星辰', '额尔古纳河右岸',
    '树犹如此', '旅行之木', '克拉克森的农场', '老女孩'
])

# ===== Soul 2: 倾听者 Listener =====
listener_books = find_books([
    '我灵魂里的女性', '上野千鹤子的私房谈话', '上野千鹤子的私房谈话III',
    '上野千鹤子的午后时光', '始于极限', '身为女性的选择',
    '闭经记', '身后无遗物', '生而为女', '悍妇生育记',
    '盐镇', '岂不怀归', '我的母亲做保洁',
    '82年生的金智英', '绝叫', '莉莉亚娜不可战胜的夏天',
    '战争中没有女性', '巴黎评论·女性作家访谈',
    '服美役', '开场：女性学者访谈', '这是我爱过的男人',
    '老女孩', '明亮的夜晚', '即使以最微弱的光'
])

# ===== Soul 3: 越境者 Border Crosser =====
# Use exact titles from finished_books.json (non-Chinese titles = Spanish/English)
border_titles = [t for t in finished.keys() if not any('一' <= c <= '鿿' for c in t) and t != 'Blue']
border_books = []
for t in border_titles:
    info = finished[t]
    n = notes_map.get(t, {})
    border_books.append({
        'title': t,
        'author': info.get('author','').lstrip('[').split(']')[-1].strip() if info.get('author') else '',
        'year': info.get('year','?'),
        'cat': info.get('cat',''),
        'highlights': n.get('n',0),
        'reviews': n.get('r',0)
    })

# ===== Soul 4: 求道者 Seeker =====
seeker_books = find_books([
    '走出唯一真理观', '人生十二法则', '当下的力量',
    '何为良好生活', '倦怠社会', '沉思的生活',
    '5%的改变', '世界作为参考答案', '宝贵的人生建议',
    '最优解人生', '目光', '人间值得', '幸福课',
    '与焦虑和解', '爱的五种能力', '活出生命的意义',
    '相约星期二', '圆圈正义'
])

# ===== Soul 5: 解构者 Analyst =====
analyst_books = find_books([
    '略萨作品：城市与狗', '略萨作品：胡利娅姨妈', '略萨作品：公羊的节日',
    '略萨作品：坏女孩', '略萨作品：潘达雷昂', '略萨谈博尔赫斯',
    '写作之癖', '天真的和感伤的小说家', '不止魔幻',
    '献灯使', '石黑一雄访谈录', '制造消费者',
    '太阳与少女', '多谈谈问题', '项飙',
    '跨越边界的社区', '博尔赫斯：最后的访谈',
    '输出力', '把自己作为方法'
])

# ===== Soul 6: 栖息者 Rest =====
rest_books = find_books([
    '根西岛文学与土豆皮馅饼俱乐部', '太阳与少女', '爱吃沙拉的狮子',
    '大萝卜和难挑的鳄梨', '编舟记', '哪啊哪啊神去村',
    '强风吹拂', '生活蒙太奇', '吉卜力的天才们',
    '吉卜力的伙伴们', '焦虑的人', '我的天才朋友',
    '当值神明', '四叠半神话大系', '奥斯卡与玫瑰奶奶',
    '太白金星有点烦', '克拉克森的农场', '一个人的小繁华'
])

souls = [
    {
        'id': 'witness',
        'name': '见证者',
        'en': 'The Witness',
        'color': '#b5686a',
        'bg': '#faf2f2',
        'question': '另一个人的生活是什么样子？',
        'label': '在别人的故事里停留',
        'books': witness_books
    },
    {
        'id': 'listener',
        'name': '倾听者',
        'en': 'The Listener',
        'color': '#c4934a',
        'bg': '#faf6ed',
        'question': '谁的声音被淹没了？',
        'label': '倾向于听见弱者的声音',
        'books': listener_books
    },
    {
        'id': 'border-crosser',
        'name': '越境者',
        'en': 'The Border Crosser',
        'color': '#7c6ba0',
        'bg': '#f4f0fa',
        'question': '边界那边有什么？',
        'label': '对陌生不恐惧，主动寻找',
        'books': border_books
    },
    {
        'id': 'seeker',
        'name': '求道者',
        'en': 'The Seeker',
        'color': '#4a6fa5',
        'bg': '#f0f4fa',
        'question': '我该如何生活？',
        'label': '经验必须转化为意义',
        'books': seeker_books
    },
    {
        'id': 'analyst',
        'name': '解构者',
        'en': 'The Analyst',
        'color': '#3a8a7a',
        'bg': '#f0f8f5',
        'question': '这是怎么造出来的？',
        'label': '理解事物为什么是这样',
        'books': analyst_books
    },
    {
        'id': 'rest',
        'name': '栖息者',
        'en': 'The One Who Rests',
        'color': '#d480aa',
        'bg': '#fdf0f5',
        'question': '哪里可以让我停下来？',
        'label': '知道什么时候需要休息',
        'books': rest_books
    }
]

# Count total and year range
all_books_set = set()
min_y, max_y = 9999, 0
for s in souls:
    for b in s['books']:
        all_books_set.add((b['title'], b['year']))
        y = b.get('year', '?')
        if y != '?':
            min_y = min(min_y, int(y))
            max_y = max(max_y, int(y))

total_unique = len(all_books_set)

# Remove duplicates across souls (keep in primary soul, remove from secondary)
seen_titles = set()
for s in souls:
    unique = []
    for b in s['books']:
        if (b['title'], str(b['year'])) not in seen_titles:
            seen_titles.add((b['title'], str(b['year'])))
            unique.append(b)
        elif len(unique) < 4:
            # Still include but mark as cross-reference
            b['cross'] = True
            unique.append(b)
    s['books'] = unique

lines = []
def w(s):
    lines.append(s)

w('<!DOCTYPE html>')
w('<html lang="zh-CN">')
w('<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">')
w('<title>Reading Doppelgängers — 阅读分身</title>')
w('<style>')
w('*{margin:0;padding:0;box-sizing:border-box}')
w('body{font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Helvetica Neue",sans-serif;background:#f8f6f2;color:#1a1a1a;line-height:1.6}')
w('header{text-align:center;padding:4rem 1.5rem 1.5rem}')
w('header h1{font-size:clamp(2rem,5vw,3.2rem);font-weight:700;letter-spacing:-.03em;background:linear-gradient(135deg,#b5686a,#7c6ba0,#4a6fa5);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}')
w('header .sub{font-size:1rem;color:#6b6b6b;margin-top:.4rem}')
w('header .stats{font-size:.85rem;color:#8f8f8f;margin-top:.2rem}')
w('header .intro{max-width:36rem;margin:1.5rem auto 0;font-size:.85rem;color:#6b6b6b;line-height:1.7;padding:1rem 1.5rem;background:#fff;border-radius:1rem;box-shadow:0 1px 6px rgba(0,0,0,.06)}')
w('.container{max-width:90rem;margin:0 auto;padding:0 1.5rem}')
w('.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(26rem,1fr));gap:1.5rem;padding:1.5rem 0 2rem}')
w('@media(max-width:580px){.grid{grid-template-columns:1fr}}')
w('.card{border-radius:1.25rem;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,.06);transition:transform .2s,box-shadow .2s}')
w('.card:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(0,0,0,.1)}')
w('.card-inner{padding:1.75rem;position:relative}')
w('.card .accent{height:5px}')
w('.card .type-label{font-size:.72rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;margin-top:.25rem;margin-bottom:.1rem}')
w('.card .soul-label{font-size:.82rem;color:#6b6b6b;margin-bottom:.5rem;padding:.35rem .7rem;border-radius:.4rem;display:inline-block;background:rgba(0,0,0,.03)}')
w('.card h2{font-size:1.35rem;font-weight:700;letter-spacing:-.01em;margin-bottom:.6rem}')
w('.card .question{margin-bottom:.8rem}')
w('.card .question-inner{font-size:.82rem;font-style:italic;padding:.6rem .85rem;border-radius:.5rem;background:rgba(0,0,0,.03);line-height:1.6;border-left:3px solid}')
w('.book-count{font-size:.78rem;margin-bottom:.6rem;color:#6b6b6b;padding:.2rem 0}')
w('.book-list{list-style:none;max-height:20rem;overflow-y:auto;scrollbar-width:thin}')
w('.book-list::-webkit-scrollbar{width:4px}')
w('.book-list::-webkit-scrollbar-thumb{background:#ddd;border-radius:2px}')
w('.book-item{display:flex;align-items:center;padding:.4rem .65rem;border-radius:.5rem;cursor:pointer;transition:background .12s;gap:.5rem;font-size:.84rem}')
w('.book-item:hover{background:rgba(0,0,0,.04)}')
w('.book-item .title{flex:1;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}')
w('.book-item .yr{font-size:.7rem;color:#8f8f8f;flex-shrink:0;min-width:2rem;text-align:right}')
w('.book-item .highlight-dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}')
w('.book-detail{font-size:.78rem;color:#6b6b6b;padding:0 .65rem .55rem;display:none;line-height:1.7}')
w('.book-detail.open{display:block}')
w('.book-detail .author{font-weight:500}')
w('.book-detail .tags{margin-top:.25rem}')
w('.book-detail .tag{display:inline-block;font-size:.64rem;padding:.1rem .45rem;border-radius:999px;margin-right:.25rem}')
w('.tag.valid{background:#d4edda;color:#155724}')
w('.tag.questionable{background:#fff3cd;color:#856404}')
w('.tag.cross{background:#e8e8e8;color:#777;font-style:italic}')
w('.footer{text-align:center;padding:2.5rem 1.5rem 3rem;color:#8f8f8f;font-size:.82rem;max-width:36rem;margin:0 auto;line-height:1.8}')
w('.footer .pill{display:inline-block;padding:.2rem .7rem;border-radius:999px;font-size:.7rem;margin:.15rem;background:#eee}')
w('@media(max-width:600px){header{padding:2.5rem 1rem 1rem}.container{padding:0 1rem}.card-inner{padding:1.25rem}.grid{gap:1rem}}')
w('</style></head><body>')

w('<header>')
w('<h1>Reading Doppelgängers</h1>')
w('<p class="sub">你的阅读分身 — 六种精神角色的书籍肖像</p>')
w('<p class="stats" id="global-stats"></p>')
w('<div class="intro">')
w('这不是按类别或题材划分的书单。<br>')
w('而是你在阅读中反复成为的六种精神角色。<br>')
w('每一本书是你曾经成为那个人的证据。')
w('</div>')
w('</header>')

w('<div class="container"><div class="grid">')

for s in souls:
    w('<div class="card">')
    w('<div class="accent" style="background:' + s['color'] + '"></div>')
    w('<div class="card-inner" style="background:' + s['bg'] + '">')
    w('<div class="type-label" style="color:' + s['color'] + '">' + s['en'] + '</div>')
    w('<h2 style="color:' + s['color'] + '">' + s['name'] + '</h2>')
    w('<div class="soul-label">' + s['label'] + '</div>')
    w('<div class="question"><div class="question-inner" style="border-left-color:' + s['color'] + '">' + s['question'] + '</div></div>')
    w('<div class="book-count">' + str(len(s['books'])) + ' 本相关书籍</div>')
    w('<ul class="book-list">')
    for b in s['books']:
        y = str(b.get('year', '?'))
        h = b.get('highlights', 0)
        rv = b.get('reviews', 0)
        has_data = h + rv > 0
        is_cross = b.get('cross', False)
        if has_data:
            tag = '<span class="tag valid">' + str(h) + '划线 · ' + str(rv) + '想法</span>'
        elif is_cross:
            tag = '<span class="tag cross">也出现在其他分身</span>'
        else:
            tag = '<span class="tag questionable">数据未获取</span>'
        w('<li>')
        w('<div class="book-item" onclick="toggle(this)">')
        w('<span class="title">' + b['title'] + '</span>')
        w('<span class="yr">' + y + '</span>')
        w('</div>')
        w('<div class="book-detail">')
        w('<div class="author">' + (b.get('author','') or '作者未知') + '</div>')
        w('<div class="tags">' + tag + '</div>')
        w('</div>')
        w('</li>')
    w('</ul></div></div>')

w('</div></div>')

w('<div class="footer">')
w('这些分身不是阅读偏好，而是长期反复出现的精神角色。<br>')
w('一本书可能属于多个分身，但主要出现在最匹配的灵魂中。<br><br>')
w('<span class="pill">打开 · 越境者</span> ')
w('<span class="pill">在场 · 见证者</span> ')
w('<span class="pill">倾斜 · 倾听者</span> ')
w('<span class="pill">反思 · 求道者</span> ')
w('<span class="pill">拆解 · 解构者</span> ')
w('<span class="pill">恢复 · 栖息者</span>')
w('<br><br>')
w('基于微信读书数据 · ' + str(total_unique) + ' 本已读完书籍 · ' + str(min_y) + '–' + str(max_y))
w('</div>')

w('<script>')
w('function toggle(el){var d=el.nextElementSibling;if(d)d.classList.toggle("open")}')
w('</script>')
w('</body></html>')

with open(p_out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Written ' + str(len(lines)) + ' lines to ' + p_out)
