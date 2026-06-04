import os, json, textwrap

# Build the HTML content line by line to avoid escaping issues
lines = []
def w(s):
    lines.append(s)

w('<!DOCTYPE html>')
w('<html lang="zh-CN">')
w('<head>')
w('<meta charset="UTF-8">')
w('<meta name="viewport" content="width=device-width,initial-scale=1.0">')
w('<title>Reading Doppelgängers — 你的阅读分身</title>')
w('<style>')
w('*{margin:0;padding:0;box-sizing:border-box}')
w('body{font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Helvetica Neue",sans-serif;background:#f8f6f2;color:#1a1a1a;line-height:1.6;min-height:100vh}')
w('.container{max-width:88rem;margin:0 auto;padding:0 1.5rem}')
w('header{text-align:center;padding:4rem 1.5rem 1.5rem}')
w('header h1{font-size:clamp(2rem,5vw,3.2rem);font-weight:700;letter-spacing:-.03em;background:linear-gradient(135deg,#3a3a5c,#6a4e7a,#b5686a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}')
w('header .sub{font-size:1.05rem;color:#6b6b6b;margin-top:.5rem}')
w('header .stats{font-size:.85rem;color:#8f8f8f;margin-top:.3rem}')
w('.filter-bar{display:flex;justify-content:center;flex-wrap:wrap;gap:.5rem;padding:1.5rem 0;position:sticky;top:0;z-index:10;background:#f8f6f2;padding-bottom:.75rem}')
w('.filter-btn{padding:.4rem 1rem;border-radius:999px;border:1.5px solid #ddd;background:transparent;cursor:pointer;font-size:.82rem;transition:all .2s;color:#555}')
w('.filter-btn:hover{background:#eee}')
w('.filter-btn.active{color:#fff;border-color:transparent}')
w('.filter-btn.all.active{background:#3a3a5c}')
w('.filter-btn.puzzle.active{background:#4a6fa5}')
w('.filter-btn.cosmo.active{background:#3a8a7a}')
w('.filter-btn.seeker.active{background:#c4934a}')
w('.filter-btn.archivist.active{background:#b5686a}')
w('.filter-btn.bilingual.active{background:#7c6ba0}')
w('.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(24rem,1fr));gap:1.5rem;padding-bottom:2rem}')
w('@media(max-width:540px){.grid{grid-template-columns:1fr}}')
w('.card{border-radius:1.25rem;overflow:hidden;box-shadow:0 2px 12px rgba(0,0,0,.06);transition:transform .2s,box-shadow .2s;display:none}')
w('.card.visible{display:block}')
w('.card:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(0,0,0,.1)}')
w('.card-inner{padding:1.75rem;position:relative}')
w('.card .accent{height:5px}')
w('.card .type-label{font-size:.72rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;margin-top:.25rem;margin-bottom:.15rem}')
w('.card h2{font-size:1.35rem;font-weight:700;letter-spacing:-.01em}')
w('.card .desc{font-size:.88rem;color:#4a4a4a;line-height:1.75;margin:1rem 0}')
w('.card .question{margin-bottom:.75rem}')
w('.card .question-inner{font-size:.8rem;font-style:italic;padding:.75rem 1rem;border-radius:.5rem;background:rgba(0,0,0,.03);line-height:1.6;border-left:3px solid}')
w('.book-count{font-size:.78rem;margin-bottom:.75rem;color:#6b6b6b}')
w('.book-list{list-style:none;max-height:18rem;overflow-y:auto;scrollbar-width:thin}')
w('.book-list::-webkit-scrollbar{width:4px}')
w('.book-list::-webkit-scrollbar-thumb{background:#ddd;border-radius:2px}')
w('.book-item{display:flex;align-items:center;padding:.45rem .65rem;border-radius:.5rem;cursor:pointer;transition:background .15s;gap:.5rem;font-size:.85rem}')
w('.book-item:hover{background:rgba(0,0,0,.04)}')
w('.book-item .title{flex:1;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}')
w('.book-item .yr{font-size:.72rem;color:#8f8f8f;flex-shrink:0;min-width:2.2rem;text-align:right}')
w('.book-detail{font-size:.78rem;color:#6b6b6b;padding:0 .65rem .65rem;display:none;line-height:1.7}')
w('.book-detail.open{display:block}')
w('.book-detail .author{font-weight:500}')
w('.book-detail .tags{margin-top:.3rem}')
w('.book-detail .tag{display:inline-block;font-size:.65rem;padding:.12rem .5rem;border-radius:999px;margin-right:.25rem}')
w('.tag.valid{background:#d4edda;color:#155724}')
w('.tag.questionable{background:#fff3cd;color:#856404}')
w('.footer{text-align:center;padding:2.5rem 1.5rem 3rem;color:#8f8f8f;font-size:.82rem;max-width:36rem;margin:0 auto;line-height:1.7}')
w('@media(max-width:600px){header{padding:2.5rem 1rem 1rem}.container{padding:0 1rem}.card-inner{padding:1.25rem}.grid{gap:1rem}}')
w('</style>')
w('</head>')
w('<body>')

w('<header>')
w('<h1>Reading Doppelgängers</h1>')
w('<p class="sub">你的阅读分身 — 基于已读完书籍的深度阅读人格分析</p>')
w('<p class="stats" id="global-stats"></p>')
w('</header>')

w('<div class="container">')
w('<div class="filter-bar" id="filter-bar"></div>')
w('<div class="grid" id="grid"></div>')
w('<div class="footer">')
w('这些分身展示了你在不同阶段与心境下的阅读人格和精神兴趣。<br>')
w('每个分身对应若干已读完书籍，一本书可能出现在多个分身中，<br>')
w('但主要归类在最匹配的角色下。<br><br>')
w('<span style="color:#6b6b6b">基于微信读书数据 · 2020–2026</span>')
w('</div>')
w('</div>')

# Build the JS data and render logic
doppels = [
    {
        'id': 'puzzle', 'name': '解谜人', 'en': 'Puzzle Solver',
        'color': '#4a6fa5', 'bg': '#f0f4fa',
        'desc': '为一个精心构建的叙事而生。你读悬疑推理不是为了打发时间，而是为了享受解谜的智力快感——线索如何铺设、结构如何收束、真相如何在最后一刻翻转。从本格派到社会派，从日式致郁到意式优雅，你的书架本身就是一座犯罪博物馆。',
        'question': '什么样的谜题让你愿意在深夜继续翻页？',
        'books': [
            ('十万分之一的偶然', '松本清张', 2021, 7, 0),
            ('箱庭图书馆', '乙一', 2021, 0, 0),
            ('D坂杀人事件', '江户川乱步', 2020, 3, 0),
            ('哈利波特與密室', 'J·K·羅琳', 2021, 1, 0),
            ('Blue', '叶真中显', 2024, 1, 0),
            ('阳光劫匪倒转地球', '伊坂幸太郎', 2024, 3, 0),
            ('哈利·波特与凤凰社', 'J.K.罗琳', 2024, 0, 0),
        ]
    },
    {
        'id': 'cosmo', 'name': '世界公民', 'en': 'Cosmopolitan',
        'color': '#3a8a7a', 'bg': '#f0f8f5',
        'desc': '不满足于单一文化的声音。你通过翻译文学在世界各地旅行——从拉美的魔幻现实到日本的物哀幽玄，从英伦的优雅克制到韩国的锋利冷峻。略萨的结构迷宫、马尔克斯的家族史诗、石黑一雄的记忆叙事、金爱烂的日常锋利——你的阅读护照上盖满了各国的印章。',
        'question': '下一个想通过文学抵达的国家是哪里？',
        'books': [
            ('外面是夏天', '金爱烂', 2024, 26, 0),
            ('滔滔生活', '金爱烂', 2024, 7, 0),
            ('如雪如山', '张天翼', 2024, 5, 0),
            ('时间的针脚', '玛丽亚·杜埃尼亚斯', 2024, 0, 0),
            ('没有人给他写信的上校', '加西亚·马尔克斯', 2025, 0, 0),
            ('城市与狗', '马里奥·巴尔加斯·略萨', 2025, 3, 0),
            ('长日将尽', '石黑一雄', 2025, 0, 0),
            ('暗处的女儿', '埃莱娜·费兰特', 2025, 5, 0),
            ('番石榴飘香', '加西亚·马尔克斯', 2026, 25, 0),
            ('不止魔幻：拉美文学第一课', '侯健', 2026, 2, 0),
            ('我的职业是小说家', '村上春树', 2026, 6, 0),
            ('编舟记', '三浦紫苑', '?', 1, 0),
        ]
    },
    {
        'id': 'seeker', 'name': '求道者', 'en': 'Seeker',
        'color': '#c4934a', 'bg': '#faf6ed',
        'desc': '阅读是一种自我审视的方式。你读哲学、心理学、女性主义、社会批判——不只是为了获取知识，而是为了回答一个更根本的问题：我该如何生活？从陈嘉映的哲学沉思到上野千鹤子的尖锐剖析，从韩炳哲的社会诊断到乔丹·彼得森的人生法则，你在不同思想体系之间寻找属于自己的答案。',
        'question': '你真正想问自己的问题是什么？',
        'books': [
            ('走出唯一真理观', '陈嘉映', 2024, 211, 55),
            ('人生十二法则', '乔丹·彼得森', 2024, 207, 23),
            ('当下的力量', '埃克哈特·托利', 2024, 117, 14),
            ('爱的五种能力', '赵永久', 2024, 114, 8),
            ('人间值得', '中村恒子', 2024, 98, 20),
            ('与焦虑和解', '爱丽丝·博伊斯', 2024, 91, 6),
            ('目光', '陶勇', 2024, 51, 25),
            ('上野千鹤子的私房谈话', '上野千鹤子', 2024, 5, 0),
            ('倦怠社会', '韩炳哲', 2024, 13, 0),
            ('宝贵的人生建议', '凯文·凯利', 2024, 31, 0),
            ('人生复本', '布莱克·克劳奇', 2024, 4, 0),
            ('上野千鹤子的私房谈话III', '上野千鹤子', 2025, 12, 0),
        ]
    },
    {
        'id': 'archivist', 'name': '档案员', 'en': 'Archivist',
        'color': '#b5686a', 'bg': '#faf2f2',
        'desc': '一个人的故事就是时代的历史。你读传记、回忆录、纪实文学——不是为了消遣，而是为了见证。李安的隐忍与爆发、波伏瓦的清醒与自由、茨威格笔下消逝的欧洲、阿列克谢耶维奇记录的战火中的女性——你在他人生命中寻找历史的纹理。每一本读完的传记，都是你与一个灵魂的长谈。',
        'question': '记忆被书写之后，会变成什么？',
        'books': [
            ('死在这里也不错', '马家辉', 2021, 70, 40),
            ('十年一觉电影梦：李安传', '张靓蓓/李安', 2024, 103, 56),
            ('活着为了讲述', '加西亚·马尔克斯', 2024, 2, 0),
            ('昨日的世界', '茨威格', 2025, 13, 0),
            ('独自上路：一个九岁男孩的边境历险', '哈维尔·萨莫拉', 2025, 170, 1),
            ('战争中没有女性', '阿列克谢耶维奇', 2025, 23, 0),
            ('老女孩：另一种生活方式', '玛丽·科克', 2025, 21, 0),
            ('清算已毕：波伏瓦自传', '西蒙娜·德·波伏瓦', 2026, 24, 0),
            ('莉莉亚娜不可战胜的夏天', '克里斯蒂娜·里韦拉·加尔萨', 2026, 5, 61),
        ]
    },
    {
        'id': 'bilingual', 'name': '双语者', 'en': 'Bilingual',
        'color': '#7c6ba0', 'bg': '#f4f0fa',
        'desc': '阅读不依赖翻译。你已经用西班牙语读完了从科幻到自传、从科普到心理学的十几本书——有些甚至是在中译本之前读完的。这不仅仅是一项语言技能，而是一种阅读身份的转变：当你可以直接进入另一种语言的思想世界时，你就不再只是一个中文读者，而是一个用西班牙语思考、感受和质疑的人。',
        'question': '用另一种语言阅读时，你变成了谁？',
        'books': [
            ('Proyecto Hail Mary', 'Andy Weir', 2024, 4, 0),
            ('Dos soledades', 'Garcia Marquez & Vargas Llosa', 2024, 14, 0),
            ('Mujeres del alma mia', 'Isabel Allende', 2024, 72, 1),
            ('Yo tuve un sueno', 'Juan Pablo Villalobos', 2025, 169, 1),
            ('Apuntes sobre un planeta estresado', 'Matt Haig', 2025, 96, 6),
            ('Harry Potter y el caliz de fuego', 'J.K. Rowling', '?', 2, 0),
            ('De que hablo cuando hablo de correr', 'Haruki Murakami', '?', 19, 0),
            ('Deberias hablar con alguien', 'Lori Gottlieb', '?', 3, 0),
            ('Entiende tu mente', 'Monica Gonzalez', '?', 4, 0),
            ('Fisica para dummies', 'Steven Holzner', '?', 7, 0),
            ('El amor en los tiempos del colera', 'Gabriel Garcia Marquez', '?', 4, 0),
        ]
    }
]

# Build JS
w('<script>')
w('var DATA = ' + json.dumps(doppels, ensure_ascii=False) + ';')
w('''
var grid = document.getElementById("grid");
var filterBar = document.getElementById("filter-bar");
var stats = document.getElementById("global-stats");
var total = 0, minY = 9999, maxY = 0;

// Build filter buttons
var btns = [{id:"all",label:"All",cls:"all"}];
DATA.forEach(function(d){btns.push({id:d.id,label:d.name,cls:d.id})});
filterBar.innerHTML = btns.map(function(f){
  return '<button class="filter-btn '+f.cls+' active" data-filter="'+f.id+'">'+f.label+'</button>';
}).join("");

// Build cards
grid.innerHTML = DATA.map(function(d){
  var booksHtml = d.books.map(function(b){
    var yr = b[2] || "?";
    var hasNotes = b[3]+b[4] > 0;
    var tag = hasNotes
      ? '<span class="tag valid">'+b[3]+'划线 &middot; '+b[4]+'想法</span>'
      : '<span class="tag questionable">数据未获取</span>';
    return '<li><div class="book-item" onclick="toggle(this)"><span class="title">'+b[0]+'</span><span class="yr">'+yr+'</span></div><div class="book-detail"><div class="author">'+b[1]+'</div><div class="tags">'+tag+'</div></div></li>';
  }).join("");
  total += d.books.length;
  d.books.forEach(function(b){if(b[2]!=="?"&&b[2]){if(+b[2]<minY)minY=+b[2];if(+b[2]>maxY)maxY=+b[2]}});
  return '<div class="card visible" data-type="'+d.id+'"><div class="accent" style="background:'+d.color+'"></div><div class="card-inner" style="background:'+d.bg+'"><div class="type-label" style="color:'+d.color+'">'+d.en+'</div><h2 style="color:'+d.color+'">'+d.name+'</h2><div class="desc">'+d.desc+'</div><div class="question"><div class="question-inner" style="border-left-color:'+d.color+'">'+d.question+'</div></div><div class="book-count">📚 '+d.books.length+' 本已读完</div><ul class="book-list">'+booksHtml+'</ul></div></div>';
}).join("");

stats.textContent = "共 "+total+" 本书 &middot; "+minY+"-"+maxY;

// Filter
document.querySelectorAll(".filter-btn").forEach(function(btn){
  btn.addEventListener("click",function(){
    var filter = this.dataset.filter;
    document.querySelectorAll(".filter-btn").forEach(function(b){b.classList.remove("active")});
    this.classList.add("active");
    document.querySelectorAll(".card").forEach(function(c){
      c.classList.toggle("visible", filter==="all" || c.dataset.type===filter);
    });
  });
});

function toggle(el){
  var d = el.nextElementSibling;
  if(d) d.classList.toggle("open");
}
''')
w('</script>')
w('</body>')
w('</html>')

p = r'C:\Users\lingzhu12\AppData\Local\Temp\weread_warehouse\reading-doppelgangers.html'
with open(p, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('Written: ' + str(len(lines)) + ' lines to ' + p)
