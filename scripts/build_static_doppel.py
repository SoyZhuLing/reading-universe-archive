import json, os

p_out = r'C:\Users\lingzhu12\AppData\Local\Temp\weread_warehouse\reading-doppelgangers.html'

finished = json.load(open(r'C:\Users\lingzhu12\AppData\Local\Temp\weread_warehouse\finished_books.json', 'rb'))
notebooks = json.load(open(r'C:\Users\lingzhu12\AppData\Local\Temp\weread_warehouse\merged\all_notebooks.json', 'rb'))

notes_map = {}
for nb in notebooks:
    t = nb.get('book',{}).get('title','')
    notes_map[t] = nb.get('noteCount',0)+nb.get('reviewCount',0)

def find_books(keywords):
    results = []
    for kw in keywords:
        for t, info in finished.items():
            if kw.lower() in t.lower():
                n = notes_map.get(t, 0)
                y = info.get('year', '?')
                results.append({'title': t, 'year': y, 'notes': n})
                break
    return results

souls_data = [
    ('witness', '见证者', 'the Witness', '#b5686a', '#fdf2f2',
     '不断通过进入他人的生命来理解世界的人。读传记、回忆录、纪实文学——不是为了消遣，而是为了亲历另一种人生。不追求情节的快感，而在意经验的密度：读李安传不是为了知道故事，是为了感受一个人如何在巨大成功中保持清醒；读波伏瓦不是为了学术，是为了见证一个女人终其一生审视自己；读茨威格是为了理解一个文明如何在一个人眼前消逝。\n阅读方式：在别人的故事里长久停留。每一本读完的传记，都是一次与另一个灵魂的长谈。对他人的生命经验保持彻底的开放——不是关于"后来发生了什么"，而是关于"那是怎样的感觉"。\n心理特征：有一种深入的好奇心——愿意被别人的生命改变。对他人的内在世界感到真正的兴趣，这种兴趣既非窥探也非评判，而是一种安静的在场。',
     '另一个人的生活是什么样子？',
     ['十年一觉电影梦','清算已毕','昨日的世界','独自上路','活着为了讲述','战争中没有女性','莉莉亚娜','死在这里也不错','夜航西飞','秋园','风沙星辰','旅行之木','老女孩','江城','树犹如此','克拉克森的农场','暮色将尽']),
    ('listener', '倾听者', 'the Listener', '#c4934a', '#faf6ed',
     '在众声喧哗中反复走到沉默者身边的人。女性写作、边缘叙事、少数群体的声音——不是学术兴趣，而是一种伦理上的倾斜：总是倾向于听见弱者的声音。上野千鹤子读了17本（从私房谈话到学术著作，从生育到死亡），阿连德的愤怒与爱（79条想法——全年最高），金爱烂的日常疲倦，阿列克谢耶维奇的战争女性。\n阅读方式：最活跃的互动发生在那让他/她听见另一个人的书里。不是被动接收而是主动对话——划线少而想法多，说明在回应而非收集。这些书不是信息输入，是关系建立。\n心理特征：有一种对沉默的敏感。在主流叙事之外寻找被忽略的频道。这种倾听不是旁观，是参与——听见别人的声音之后，就无法再假装不知道。这不是知识选择，是人格倾向。',
     '谁的声音被淹没了？',
     ['我灵魂里的女性','上野千鹤子的私房谈话','上野千鹤子的私房谈话III','盐镇','岂不怀归','我的母亲做保洁','82年生的金智英','绝叫','闭经记','身后无遗物','巴黎评论·女性作家访谈','服美役','明亮的夜晚','老女孩','战争中没有女性','莉莉亚娜不可战胜的夏天','开场：女性学者访谈','身为女性的选择']),
    ('border', '越境者', 'the Border Crosser', '#7c6ba0', '#f4f0fa',
     '对陌生不恐惧，甚至主动寻找边界的人。阅读不依赖翻译——在另一种语言里重新成为读者，不是学习语言，是选择在另一种思想体系里生活。用西班牙语读科幻（Proyecto Hail Mary——全平台阅读最久的书，25小时）、读自传（De qué hablo cuando hablo de correr）、读科普（Física para dummies）、读心理（Deberías hablar con alguien），有些书甚至在中译本之前读完。\n阅读方式：同一本书读两个语言版本（村上春树的跑步书），像是在测试自己能在另一个语言里走多远。每一次跨语言阅读都在重新经历身份的不稳定感——读西语版的你，和读中文版的你，不是同一个人。\n心理特征：驱动越境者的不是好奇而是勇气。愿意在陌生中保持阅读能力，愿意接受"在这个语言里我不那么聪明"的事实。越境者在每一次阅读中做出选择：不退回舒适区。',
     '边界那边有什么？',
     ['Los niños perdidos','Yo tuve un sueño','Dos soledades','Mujeres del alma mía','El coronel','Harry Potter y el prisionero de Azkaban','Proyecto Hail Mary','Apuntes sobre un planeta estresado','De Qué Hablo Cuando Hablo De Correr']),
    ('seeker', '求道者', 'the Seeker', '#4a6fa5', '#f0f4fa',
     '在每一本书里寻找"如何生活"答案的人——即使那本书并不是写给他的。哲学、心理学、社会批判——不是知识收集，而是一种存在的追问：我该怎么活？我选择的理由站得住吗？走出唯一真理观（211条划线+55条想法——全书最高互动数据），人生十二法则（207条划线），当下的力量（117条划线）。这些不是"喜欢的书"，而是曾经救过命的文本。\n阅读方式：带着根本问题进入阅读。而且求道者可以在任何类型中找到滋养——从陈嘉映的沉思到韩炳哲的诊断，从彼得森的人生法则到上野的私房谈话。不经过反思的阅读是不完整的。\n心理特征：有一种无法被满足的意义饥渴。经验必须转化为意义才算完整。这种追问背后不是焦虑，而是一种认真——认真地生活需要知道自己为什么这样生活。求道者与栖息者生活在同一个读者体内，在追问的间隙里寻找修复。',
     '我该如何生活？',
     ['走出唯一真理观','人生十二法则','当下的力量','倦怠社会','沉思的生活','5%的改变','世界作为参考答案','宝贵的人生建议','最优解人生','目光','人间值得','与焦虑和解','爱的五种能力','何为良好生活','活出生命的意义','幸福课','相约星期二','圆圈正义']),
    ('analyst', '解构者', 'the Analyst', '#3a8a7a', '#f0f8f5',
     '不仅接受世界的样子，还要理解它为什么是这样。对叙事结构和思想系统本身着迷——拆解盒子比消费盒子更有趣。读略萨的结构迷宫六年之久（从2022到2025），还读了写作之癖和略萨谈博尔赫斯——不消费故事，是研究作者如何工作。读伊坂幸太郎的多线叙事（11本），读帕慕克的小说家心智，读项飙的社会结构分析，读韩炳哲的社会诊断。\n阅读方式：即使在娱乐时也无法关闭分析的开关。这不是冷冰冰的技术拆解，而是一种更深层的尊重——理解事物如何运作，才能理解事物为何重要。从文学结构到社会结构，解构者的目光始终在表层之下。\n心理特征：有一种对表面的不信任。倾向于问"这是怎么造出来的"——无论面对的是小说、社会现象还是人生选择。但解构最终通向的不是虚无，而是理解之后的敬畏：知道一切有多复杂之后，仍然愿意阅读。',
     '这是怎么造出来的？',
     ['略萨作品：城市与狗','略萨作品：胡利娅姨妈和作家','略萨作品：公羊的节日','略萨作品：坏女孩的恶作剧','略萨作品：潘达雷昂上尉和劳军女郎','写作之癖','不止魔幻','献灯使','石黑一雄访谈录','制造消费者','太阳与少女','博尔赫斯：最后的访谈','天真的和感伤的小说家','把自己作为方法','输出力']),
    ('rest', '栖息者', 'the One Who Rests', '#d480aa', '#fdf0f5',
     '知道什么时候需要停下来的人。在文字中寻找庇护——阅读不是为了获取什么，而是为了回到一个安全的地方。根西岛文学与土豆皮馅饼俱乐部（47条想法——全年第三高互动，但这是一本温暖治愈的小书）、三浦紫苑的认真与温柔（编舟记、强风吹拂）、村上春树的日常碎碎念（爱吃沙拉的狮子、大萝卜和难挑的鳄梨）、森见登美彦的太阳与少女、吉卜力的造梦者们的幕后故事。\n阅读方式：不质问，不分析，只是陪伴。与求道者完全相反——不是找问题，是找安慰。读这些书的时候不需要成长、不需要顿悟、不需要改变，只需要感到安全。\n心理特征：栖息者与求道者生活在同一个读者体内，这是一个重要的结构性事实。在持续性追问和结构性分析带来的疲惫之后，需要修复性的阅读来恢复。这不是逃避，是生存策略——知道什么时候需要停下来的人，才能持续地走下去。',
     '哪里可以让我停下来？',
     ['根西岛文学与土豆皮馅饼俱乐部','太阳与少女','爱吃沙拉的狮子','大萝卜和难挑的鳄梨','编舟记','哪啊哪啊神去村','强风吹拂','生活蒙太奇','吉卜力的天才们','焦虑的人','我的天才朋友','当值神明','四叠半神话大系','太白金星有点烦','克拉克森的农场','奥斯卡与玫瑰奶奶','一个人的小繁华'])
]

# Resolve books from finished data
souls = []
all_titles = set()
total_books = 0
min_y, max_y = 9999, 0

for sid, name, en, color, bg, desc, question, keywords in souls_data:
    books = []
    for kw in keywords:
        for t, info in finished.items():
            if kw.lower() in t.lower():
                n = notes_map.get(t, 0)
                y = info.get('year', '?')
                author = info.get('author','')
                if author:
                    author = author.lstrip('[').split(']')[-1].strip()
                if (t, str(y)) not in all_titles:
                    all_titles.add((t, str(y)))
                books.append({'title': t, 'year': y, 'notes': n, 'author': author})
                total_books += 1
                if y != '?':
                    min_y = min(min_y, int(y))
                    max_y = max(max_y, int(y))
                break
    souls.append({'id': sid, 'name': name, 'en': en, 'color': color, 'bg': bg, 'desc': desc, 'question': question, 'books': books})

lines = []
def w(s): lines.append(s)

# ---- HTML ----
w('<!DOCTYPE html>')
w('<html lang="zh-CN">')
w('<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">')
w('<title>Reading Doppelgängers — 阅读分身</title>')
w('<style>')
w('*{margin:0;padding:0;box-sizing:border-box}')
w('body{font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Helvetica Neue",sans-serif;background:#f8f6f2;color:#1a1a1a;line-height:1.5}')
w('.page{max-width:100rem;margin:0 auto;padding:2rem 1.5rem 2rem}')
w('@media(max-width:700px){.page{padding:1.25rem 1rem}}')
w('')
w('/* Header */')
w('header{text-align:center;margin-bottom:1.75rem}')
w('header h1{font-size:clamp(1.6rem,3.5vw,2.6rem);font-weight:700;letter-spacing:-.02em;background:linear-gradient(135deg,#b5686a,#7c6ba0,#4a6fa5);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}')
w('header .sub{font-size:.92rem;color:#6b6b6b;margin-top:.25rem}')
w('header .stats{font-size:.8rem;color:#8f8f8f;margin-top:.15rem}')
w('')
w('/* Grid */')
w('.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.25rem}')
w('@media(max-width:960px){.grid{grid-template-columns:repeat(2,1fr)}}')
w('@media(max-width:640px){.grid{grid-template-columns:1fr;gap:1rem}}')
w('')
w('/* Card */')
w('.card{border-radius:1rem;overflow:hidden;box-shadow:0 2px 10px rgba(0,0,0,.05);transition:transform .2s;break-inside:avoid}')
w('.card:hover{transform:translateY(-2px);box-shadow:0 6px 18px rgba(0,0,0,.08)}')
w('.card-inner{padding:1.25rem 1.25rem .9rem;position:relative}')
w('.card .bar{height:4px}')
w('')
w('/* Card header */')
w('.card .label{font-size:.68rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;margin-top:.15rem;margin-bottom:.05rem;opacity:.7}')
w('.card h2{font-size:1.15rem;font-weight:700;letter-spacing:-.01em;margin-bottom:.35rem}')
w('')
w('/* Description */')
w('.card .desc{font-size:.8rem;color:#4a4a4a;line-height:1.65;margin-bottom:.5rem}')
w('')
w('/* Question */')
w('.card .q{font-size:.75rem;font-style:italic;padding:.4rem .6rem;border-radius:.4rem;background:rgba(0,0,0,.03);margin-bottom:.5rem;line-height:1.5;border-left:3px solid}')
w('')
w('/* Book chips */')
w('.book-count{font-size:.72rem;color:#8f8f8f;margin-bottom:.3rem}')
w('.chips{display:flex;flex-wrap:wrap;gap:.3rem}')
w('.chip{font-size:.7rem;padding:.15rem .5rem;border-radius:999px;background:#fff;border:1px solid #e5e5e5;color:#555;white-space:nowrap;max-width:100%;overflow:hidden;text-overflow:ellipsis}')
w('.chip .y{font-size:.6rem;color:#999;margin-left:.1rem}')
w('')
w('/* Footer */')
w('.footer{text-align:center;padding:1.5rem 0 0;color:#999;font-size:.78rem;border-top:1px solid #eee;margin-top:1.25rem}')
w('.footer .pill{display:inline-block;padding:.15rem .55rem;border-radius:999px;font-size:.65rem;margin:.1rem;color:#fff}')
w('@media(max-width:640px){.footer .pill{font-size:.6rem}}')
w('@media print{body{background:#fff}.card{break-inside:avoid;box-shadow:none;border:1px solid #eee}}')
w('</style></head><body>')

w('<div class="page">')

w('<header>')
w('<h1>Reading Doppelgängers</h1>')
w('<p class="sub">你的阅读分身 — 六种精神角色</p>')
w('<p class="stats">' + str(total_books) + ' 本已读完书籍 · ' + str(min_y) + '–' + str(max_y) + '</p>')
w('</header>')

w('<div class="grid">')

for s in souls:
    w('<div class="card">')
    w('<div class="bar" style="background:' + s['color'] + '"></div>')
    w('<div class="card-inner" style="background:' + s['bg'] + '">')
    w('<div class="label" style="color:' + s['color'] + '">' + s['en'] + '</div>')
    w('<h2 style="color:' + s['color'] + '">' + s['name'] + '</h2>')
    w('<div class="desc">' + s['desc'] + '</div>')
    w('<div class="q" style="border-left-color:' + s['color'] + '">' + s['question'] + '</div>')
    w('<div class="book-count">' + str(len(s['books'])) + ' 本</div>')
    w('<div class="chips">')
    for b in s['books']:
        cls = 'chip'
        y = str(b['year']) if b['year'] != '?' else ''
        yr_part = ' <span class="y">' + y + '</span>' if y else ''
        w('<span class="' + cls + '" title="' + b.get('author','') + '">' + b['title'] + yr_part + '</span>')
    w('</div></div></div>')

w('</div>')  # grid

w('<div class="footer">')
pill_colors = {'#b5686a':'在场','#c4934a':'倾斜','#7c6ba0':'打开','#4a6fa5':'反思','#3a8a7a':'拆解','#d480aa':'恢复'}
for s in souls:
    w('<span class="pill" style="background:' + s['color'] + '">' + pill_colors[s['color']] + ' · ' + s['name'] + '</span> ')
w('<br><br>')
w('每个分身代表一种长期反复出现的精神角色。一本书可能属于多个分身。<br>')
w('基于微信读书数据 · ' + str(total_books) + ' 本已读完书籍 · ' + str(min_y) + '–' + str(max_y))
w('</div>')

w('</div>')  # page
w('</body></html>')

with open(p_out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Written ' + str(len(lines)) + ' lines to ' + p_out)
print('Book counts per soul:')
for s in souls:
    print(f'  {s["name"]:10s} {len(s["books"]):2d} books')
print(f'Total unique: {len(all_titles)}')
