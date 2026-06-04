#!/usr/bin/env python3
"""Build script for Reading Universe Archive HTML page."""

import os

OUTPUT = r"C:\Users\lingzhu12\AppData\Local\Temp\weread_warehouse\reading-universe-archive.html"

CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  background: #f5f3ef;
  font-family: "Georgia", "Noto Serif SC", "Source Han Serif SC", serif;
  color: #1a1a1a;
  line-height: 1.7;
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
}
.wrapper {
  max-width: 880px;
  margin: 0 auto;
  padding: 0 24px;
}
.section {
  padding: 80px 0;
  border-bottom: 1px solid #e2ddd4;
}
.section:last-child { border-bottom: none; }
.section-number {
  font-family: "Georgia", serif;
  font-size: 13px;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #9a8c7e;
  margin-bottom: 24px;
}
.section-title {
  font-size: 24px;
  font-weight: normal;
  color: #2c2c2c;
  margin-bottom: 40px;
  letter-spacing: 1px;
}
/* Cover */
.cover {
  min-height: 85vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 100px 24px 80px;
  border-bottom: none;
}
.cover-title {
  font-size: 42px;
  font-weight: normal;
  letter-spacing: 6px;
  color: #1a1a1a;
  margin-bottom: 12px;
}
.cover-subtitle {
  font-size: 18px;
  color: #8a7e72;
  letter-spacing: 8px;
  margin-bottom: 48px;
}
.cover-tagline {
  font-size: 20px;
  color: #6a5e52;
  font-style: italic;
  max-width: 500px;
}
.cover-line {
  width: 40px;
  height: 1px;
  background: #c0b4a6;
  margin: 40px auto;
}
/* Cards */
.card {
  background: #ffffff;
  border-radius: 12px;
  padding: 36px;
  margin-bottom: 28px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04), 0 1px 3px rgba(0,0,0,0.03);
  transition: box-shadow 0.2s;
}
.card:hover { box-shadow: 0 4px 20px rgba(0,0,0,0.06), 0 2px 6px rgba(0,0,0,0.04); }
.card-soul { border-left: 4px solid; }
.card-soul .soul-name { font-size: 20px; margin-bottom: 4px; }
.card-soul .soul-name-en { font-size: 14px; color: #888; margin-bottom: 16px; }
.card p { margin-bottom: 14px; color: #3a3a3a; font-size: 15px; }
.card p:last-child { margin-bottom: 0; }
.soul-question {
  margin-top: 16px;
  padding: 14px 18px;
  background: #f8f6f2;
  border-radius: 8px;
  font-size: 14px;
  color: #5a4e42;
}
.soul-question span { font-weight: bold; }
.soul-books {
  margin-top: 12px;
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.soul-books span {
  font-size: 12px;
  padding: 4px 10px;
  background: #f5f3ef;
  border-radius: 4px;
  color: #5a4e42;
}
/* Stratum layers */
.stratum {
  position: relative;
  padding: 24px 28px;
  margin-bottom: 4px;
  border-radius: 0;
  cursor: default;
}
.stratum:first-child { border-radius: 12px 12px 0 0; }
.stratum:last-child { border-radius: 0 0 12px 12px; }
.stratum .layer-label { font-size: 13px; color: #666; margin-bottom: 4px; }
.stratum .layer-title { font-size: 17px; margin-bottom: 6px; }
.stratum .layer-desc { font-size: 14px; opacity: 0.85; }
.stratum-0 { background: #e8e0d6; }
.stratum-1 { background: #ddd4c8; }
.stratum-2 { background: #d0c6b8; }
.stratum-3 { background: #c4b8a8; }
.stratum-4 { background: #b8aa98; color: #fff; }
.stratum-5 { background: #a89a88; color: #fff; }
.stratum-6 { background: #9a8a78; color: #fff; }
.stratum-0 .layer-desc, .stratum-1 .layer-desc, .stratum-2 .layer-desc, .stratum-3 .layer-desc { color: #3a3a3a; }
.stratum-4 .layer-desc, .stratum-5 .layer-desc, .stratum-6 .layer-desc { color: #eee; }
.stratum-4 .layer-label, .stratum-5 .layer-label, .stratum-6 .layer-label { color: #ccc; }
/* Questions */
.find {
  background: #fff;
  border-radius: 12px;
  padding: 30px;
  margin-bottom: 20px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}
.find-q { font-size: 19px; margin-bottom: 8px; }
.find-meta { font-size: 13px; color: #999; margin-bottom: 12px; }
.find-desc { font-size: 15px; color: #444; }
/* Turning points */
.turning {
  background: #fff;
  border-radius: 12px;
  padding: 30px;
  margin-bottom: 20px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}
.turning h4 { font-size: 17px; margin-bottom: 4px; }
.turning .turning-meta { font-size: 13px; color: #999; margin-bottom: 14px; }
.turning-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.turning-item h5 { font-size: 13px; color: #999; margin-bottom: 4px; font-weight: normal; }
.turning-item p { font-size: 14px; color: #444; }
/* Root question */
.root-box {
  background: #fff;
  border-radius: 12px;
  padding: 48px 40px;
  text-align: center;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}
.root-question {
  font-size: 24px;
  color: #1a1a1a;
  margin-bottom: 28px;
  letter-spacing: 2px;
}
.root-explanation {
  font-size: 15px;
  color: #555;
  max-width: 640px;
  margin: 0 auto;
  line-height: 2;
}
/* Directions */
.dir-card {
  background: #fff;
  border-radius: 12px;
  padding: 28px;
  margin-bottom: 16px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}
.dir-card h4 { font-size: 16px; margin-bottom: 8px; }
.dir-card p { font-size: 14px; color: #555; }
/* Responsive */
@media (max-width: 640px) {
  .cover-title { font-size: 28px; letter-spacing: 4px; }
  .cover-subtitle { font-size: 14px; letter-spacing: 4px; }
  .cover-tagline { font-size: 16px; }
  .section { padding: 48px 0; }
  .section-title { font-size: 20px; }
  .card { padding: 24px; }
  .root-box { padding: 32px 24px; }
  .root-question { font-size: 20px; }
  .turning-grid { grid-template-columns: 1fr; }
}
/* Annotation */
.annotation {
  text-align: center;
  padding: 40px 0 60px;
  font-size: 13px;
  color: #aaa;
}
"""

def html(tag, content="", cls="", style="", **attrs):
    parts = [f"<{tag}"]
    if cls:
        parts.append(f' class="{cls}"')
    if style:
        parts.append(f' style="{style}"')
    for k, v in attrs.items():
        parts.append(f' {k}="{v}"')
    parts.append(">")
    if content:
        parts.append(str(content))
        parts.append(f"</{tag}>")
    return "".join(parts)

def wrap(tag, content, cls=""):
    return html(tag, content, cls)


# ============================================================
# SECTION II: Reading Doppelgängers
# ============================================================
SOULS = [
    {
        "name_en": "the Witness",
"name_cn": "见证者",
        "color": "#b5686a",
        "bg": "#fdf2f2",
        "paragraphs": [
            "不断通过进入他人的生命来理解世界的人。读传记、回忆录、纪实文学——不是为了消遣，而是为了亲历另一种人生。不追求情节的快感，而在意经验的密度：读李安传不是为了知道故事，是为了感受一个人如何在巨大成功中保持清醒；读波伏瓦不是为了学术，是为了见证一个女人终其一生审视自己；读茨威格是为了理解一个文明如何在一个人眼前消逝。",
"在别人的故事里长久停留。每一本读完的传记，都是一次与另一个灵魂的长谈。对他人的生命经验保持彻底的开放——不是关于“后来发生了什么”，而是关于“那是怎样的感觉”。",
            "有一种深入的好奇心——愿意被别人的生命改变。对他人的内在世界感到真正的兴趣，这种兴趣既非窥探也非评判，而是一种安静的在场。"
        ],
"question": "另一个人的生活是什么样子？",
"books": ["十年一觉电影梦","清算已毕","昨日的世界","独自上路","活着为了讲述","战争中没有女性","莉莉亚娜","死在这里也不错","夜航西飞","秋园","风沙星辰","旅行之木","老女孩","江城","树犹如此","克拉克森的农场","暮色将尽"]
    },
    {
        "name_en": "the Listener",
"name_cn": "倾听者",
        "color": "#c4934a",
        "bg": "#faf6ed",
        "paragraphs": [
            "在众声喧哗中反复走到沉默者身边的人。女性写作、边缘叙事、少数群体的声音——不是学术兴趣，而是一种伦理上的倾斜：总是倾向于听见弱者的声音。上野千鹤子读了17本（从私房谈话到学术著作，从生育到死亡），阿连德的愤怒与爱（79条想法——全年最高），金爱烂的日常疲倦，阿列克谢耶维奇的战争女性。",
            "最活跃的互动发生在那让他/她听见另一个人的书里。不是被动接收而是主动对话——划线少而想法多，说明在回应而非收集。这些书不是信息输入，是关系建立。",
            "有一种对沉默的敏感。在主流叙事之外寻找被忽略的频道。这种倾听不是旁观，是参与——听见别人的声音之后，就无法再假装不知道。这不是知识选择，是人格倾向。"
        ],
"question": "谁的声音被淹没了？",
"books": ["我灵魂里的女性","上野千鹤子的私房谈话","上野千鹤子的私房谈话III","盐镇","岂不怀归","我的母亲做保洁","82年生的金智英","绝叫","闭经记","身后无遗物","巴黎评论·女性作家访谈","服美役","明亮的夜晚","老女孩","战争中没有女性","莉莉亚娜不可战胜的夏天","开场：女性学者访谈","身为女性的选择"]
    },
    {
        "name_en": "the Border Crosser",
"name_cn": "越境者",
        "color": "#7c6ba0",
        "bg": "#f4f0fa",
        "paragraphs": [
            "对陌生不恐惧，甚至主动寻找边界的人。阅读不依赖翻译——在另一种语言里重新成为读者，不是学习语言，是选择在另一种思想体系里生活。用西班牙语读科幻（Proyecto Hail Mary——全平台阅读最久的书，25小时）、读自传（De qué hablo cuando hablo de correr）、读科普（Física para dummies）、读心理（Deberías hablar con alguien），有些书甚至在中译本之前读完。",
            "同一本书读两个语言版本（村上春树的跑步书），像是在测试自己能在另一个语言里走多远。每一次跨语言阅读都在重新经历身份的不稳定感——读西语版的你，和读中文版的你，不是同一个人。",
"驱动越境者的不是好奇而是勇气。愿意在陌生中保持阅读能力，愿意接受“在这个语言里我不那么聪明”的事实。越境者在每一次阅读中做出选择：不退回舒适区。"
        ],
"question": "边界那边有什么？",
        "books": ["Los niños perdidos","Yo tuve un sueño","Dos soledades","Mujeres del alma mía","El coronel","Harry Potter y el prisionero de Azkaban","Proyecto Hail Mary","Apuntes sobre un planeta estresado","De Qué Hablo Cuando Hablo De Correr"]
    },
    {
        "name_en": "the Seeker",
"name_cn": "求道者",
        "color": "#4a6fa5",
        "bg": "#f0f4fa",
        "paragraphs": [
"在每一本书里寻找“如何生活”答案的人——即使那本书并不是写给他的。哲学、心理学、社会批判——不是知识收集，而是一种存在的追问：我该怎么活？我选择的理由站得住吗？走出唯一真理观（211条划线+55条想法——全书最高互动数据），人生十二法则（207条划线），当下的力量（117条划线）。这些不是“喜欢的书”，而是曾经救过命的文本。",
            "带着根本问题进入阅读。而且求道者可以在任何类型中找到滋养——从陈嘉映的沉思到韩炳哲的诊断，从彼得森的人生法则到上野的私房谈话。不经过反思的阅读是不完整的。",
            "有一种无法被满足的意义饥渴。经验必须转化为意义才算完整。这种追问背后不是焦虑，而是一种认真——认真地生活需要知道自己为什么这样生活。求道者与栖息者生活在同一个读者体内，在追问的间隙里寻找修复。"
        ],
"question": "我该如何生活？",
"books": ["走出唯一真理观","人生十二法则","当下的力量","倦怠社会","沉思的生活","5%的改变","世界作为参考答案","宝贵的人生建议","最优解人生","目光","人间值得","与焦虑和解","爱的五种能力","何为良好生活","活出生命的意义","幸福课","相约星期二","圆圈正义"]
    },
    {
        "name_en": "the Analyst",
"name_cn": "解构者",
        "color": "#3a8a7a",
        "bg": "#f0f8f5",
        "paragraphs": [
            "不仅接受世界的样子，还要理解它为什么是这样。对叙事结构和思想系统本身着迷——拆解盒子比消费盒子更有趣。读略萨的结构迷宫六年之久（从2022到2025），还读了写作之癖和略萨谈博尔赫斯——不消费故事，是研究作者如何工作。读伊坂幸太郎的多线叙事（11本），读帕慕克的小说家心智，读项飙的社会结构分析，读韩炳哲的社会诊断。",
            "即使在娱乐时也无法关闭分析的开关。这不是冷冰冰的技术拆解，而是一种更深层的尊重——理解事物如何运作，才能理解事物为何重要。从文学结构到社会结构，解构者的目光始终在表层之下。",
"有一种对表面的不信任。倾向于问“这是怎么造出来的”——无论面对的是小说、社会现象还是人生选择。但解构最终通向的不是虚无，而是理解之后的敬畏：知道一切有多复杂之后，仍然愿意阅读。"
        ],
"question": "这是怎么造出来的？",
"books": ["略萨作品：城市与狗","略萨作品：胡利娅姨妈和作家","略萨作品：公羊的节日","略萨作品：坏女孩的恶作剧","略萨作品：潘达雷昂上尉和劳军女郎","写作之癖","不止魔幻","献灯使","石黑一雄访谈录","制造消费者","太阳与少女","博尔赫斯：最后的访谈","天真的和感伤的小说家","把自己作为方法","输出力"]
    },
    {
        "name_en": "the One Who Rests",
"name_cn": "栖息者",
        "color": "#d480aa",
        "bg": "#fdf0f5",
        "paragraphs": [
            "知道什么时候需要停下来的人。在文字中寻找庇护——阅读不是为了获取什么，而是为了回到一个安全的地方。根西岛文学与土豆皮馅饼俱乐部（47条想法——全年第三高互动，但这是一本温暖治愈的小书）、三浦紫苑的认真与温柔（编舟记、强风吹拂）、村上春树的日常碎碎念（爱吃沙拉的狮子、大萝卜和难挑的鳄梨）、森见登美彦的太阳与少女、吉卜力的造梦者们的幕后故事。",
            "不质问，不分析，只是陪伴。与求道者完全相反——不是找问题，是找安慰。读这些书的时候不需要成长、不需要顿悟、不需要改变，只需要感到安全。",
            "栖息者与求道者生活在同一个读者体内，这是一个重要的结构性事实。在持续性追问和结构性分析带来的疲惫之后，需要修复性的阅读来恢复。这不是逃避，是生存策略——知道什么时候需要停下来的人，才能持续地走下去。"
        ],
"question": "哪里可以让我停下来？",
"books": ["根西岛文学与土豆皮馅饼俱乐部","太阳与少女","爱吃沙拉的狮子","大萝卜和难挑的鳄梨","编舟记","哪啊哪啊神去村","强风吹拂","生活蒙太奇","吉卜力的天才们","焦虑的人","我的天才朋友","当值神明","四叠半神话大系","太白金星有点烦","克拉克森的农场","奥斯卡与玫瑰奶奶","一个人的小繁华"]
    }
]


# ============================================================
# SECTION III: Life Stratum
# ============================================================
STRATA = [
    {"year": "2020", "title": "Layer 1 / 奠基期", "label": "259天 · 338h",
"desc": "习惯形成。文学+科幻+个人成长混合探索。"},
    {"year": "2021", "title": "Layer 2 / 爆发期", "label": "349天 · 464h",
"desc": "阅读量高峰。悬疑推理爆发(+288%), 哈利波特系列集中阅读。"},
    {"year": "2022", "title": "Layer 3 / 调整期", "label": "339天 · 239h",
"desc": "时长腰斩但习惯未断。类型小说收缩, 拉美文学兴起。"},
    {"year": "2023", "title": "Layer 4 / 扩张期", "label": "360天(98.6%) · 360h",
"desc": "广度峰值。历史分类唯一进前3, 社会文化+282%。"},
    {"year": "2024", "title": "Layer 5 / 回落期", "label": "352天 · 230h(最低)",
"desc": "笔记率上升。西语原版阅读形成规模。"},
    {"year": "2025", "title": "Layer 6 / 重建期", "label": "358天 · 300h",
"desc": "文学历史最高(127h)。非虚构+传记结构性增长。"},
    {"year": "2026 H1", "title": "Layer 7 / 纪实转向", "label": "149天(半年) · 133h",
"desc": "纪实小说跃居第2。非虚构占比70%。"}
]

# ============================================================
# SECTION IV: Question Archaeology
# ============================================================
FINDS = [
    {
"question": "边界那边有什么？",
"soul": "越境者",
"emerged": "2021年",
"desc": "跨语言、跨文化的好奇。从Harry Potter西语版开始，到Proyecto Hail Mary的25小时沉浸阅读。每一次跨语言阅读都在问：用另一种语言思考的我，和原来的我是同一个人吗？这个问题没有答案，但每一次提问都拓宽了世界的边界。"
    },
    {
"question": "另一个人的生活是什么样子？",
"soul": "见证者",
"emerged": "2020年",
"desc": "对他者生命经验的好奇。从江城开始，进入一个又一个他者的世界。传记和纪实文学不是关于“后来发生了什么”，而是关于“那是怎样的感觉”。这个问题驱使读者在7年间穿越了数十种人生。"
    },
    {
"question": "谁的声音被淹没了？",
"soul": "倾听者",
"emerged": "2022年",
"desc": "对边缘和沉默的敏感。始于上野千鹤子，延伸到女性写作、边缘叙事、少数群体的声音。这不是学术兴趣，而是一种伦理上的倾斜——总是倾向于听见弱者的声音。越听越清楚，越清楚越无法转身离开。"
    },
    {
"question": "我该如何生活？",
"soul": "求道者",
"emerged": "2020年",
"desc": "对意义和价值的根本追问。走出唯一真理观、人生十二法则、当下的力量——这些书被反复阅读、密集划线，因为它们回应了一个最根本的问题。这个问题没有终极答案，但每一次追问都让生活变得更加自觉。"
    },
    {
"question": "这是怎么造出来的？",
"soul": "解构者",
"emerged": "2021年",
"desc": "对结构和系统的拆解欲。从略萨的文学结构迷宫到项飙的社会结构分析，从韩炳哲的社会诊断到制造消费者的消费系统解剖。拆解不是为了破坏，而是为了理解之后的敬畏。"
    }
]

# ============================================================
# SECTION V: Reading Turning Points
# ============================================================
TURNING_POINTS = [
    {
"book": "《走出唯一真理观》",
"meta": "2020, A级",
"before": "阅读以文学小说为主，消费性阅读",
"shift": "第一次将哲学思考引入阅读，阅读不再只是消费故事",
"after": "阅读从消费变成意义追寻",
"opened": "求道者灵魂的觉醒"
    },
    {
        "book": "Harry Potter y el cáliz de fuego",
"meta": "2021, A级",
"before": "阅读完全依赖中文翻译",
"shift": "第一次完整读完一本西语原版书",
"after": "跨语言阅读的种子",
"opened": "越境者可能性的发现"
    },
    {
"book": "《江城》",
"meta": "2021, A级",
"before": "阅读以虚构文学为主",
"shift": "第一次被非虚构作品深深打动",
"after": "纪实非虚构的进入",
"opened": "见证者灵魂的觉醒"
    },
    {
"book": "略萨系列",
"meta": "2022, A级",
"before": "阅读以类型小说为主",
"shift": "第一次系统阅读拉美文学，关注叙事结构本身",
"after": "拉美文学+结构分析的开启",
"opened": "解构者灵魂的觉醒"
    },
    {
"book": "上野千鹤子系列",
"meta": "2022, A级",
"before": "女性议题不是阅读主线",
"shift": "从私房谈话到学术著作，系统性阅读女性主义",
"after": "女性主义思想的进入",
"opened": "倾听者灵魂的觉醒"
    },
    {
        "book": "Proyecto Hail Mary",
"meta": "2024, A级",
"before": "西语阅读停留在少量练习",
"shift": "25小时沉浸阅读，跨语言阅读能力的质变",
"after": "跨语言阅读的确立",
"opened": "越境者的成熟"
    },
    {
"book": "《我灵魂里的女性》",
"meta": "2025, A级",
"before": "女性阅读偏学术和分析",
"shift": "阿连德的愤怒与爱——79条想法，全年最高互动",
"after": "女性阅读从知识到情感",
"opened": "倾听者与见证者的汇流"
    },
    {
"book": "《莉莉亚娜不可战胜的夏天》",
"meta": "2026, A级",
"before": "不同类型分散阅读",
"shift": "一部书同时激活了四个灵魂的共鸣",
"after": "四个灵魂的汇流",
"opened": "跨类型纪实的新方向"
    }
]

# ============================================================
# SECTION VII: Still Growing
# ============================================================
DIRECTIONS = [
    {
"title": "纪实与虚构的融合阅读",
"desc": "莉莉亚娜之后，跨类型纪实成为新方向。不再区分纪实与虚构，而是在交叉地带寻找新的阅读经验。纪实提供现实的重量，虚构提供想象的自由——两者的融合或许是未来阅读最富生命力的领域。"
    },
    {
"title": "西语阅读的进一步深化",
"desc": "从阅读到思考的西语化。不再满足于读懂，而是尝试用西语思考、做笔记、建立知识体系。Proyecto Hail Mary证明了跨语言阅读的可能性，下一步是让西语成为第二阅读母语。"
    },
    {
"title": "四个灵魂的协同",
"desc": "见证+倾听+解构+越境的汇流刚刚开始。莉莉亚娜之后，这四个灵魂不再轮流出场，而是开始同时工作。一本好的书将同时满足见证者的同理心、倾听者的敏感、解构者的分析欲和越境者的冒险精神。"
    },
    {
"title": "栖息者的持续存在",
"desc": "作为求道者的必要平衡。栖息者与求道者生活在同一个读者体内——在持续的追问和结构分析之后，修复性的阅读将继续存在。这不是逃避，而是让阅读可持续的生存策略。"
    }
]


# ============================================================
# HTML Generation
# ============================================================

def build_html():
    parts = []
    parts.append('<!DOCTYPE html>')
    parts.append('<html lang="zh-CN">')
    parts.append('<head>')
    parts.append('<meta charset="UTF-8">')
    parts.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    parts.append('<title>Reading Universe Archive</title>')
    parts.append(f'<style>{CSS}</style>')
    parts.append('</head>')
    parts.append('<body>')
    parts.append('<div class="wrapper">')

    # ========== SECTION I: COVER ==========
    parts.append('<section class="cover">')
    parts.append('<h1 class="cover-title">Reading Universe Archive</h1>')
    parts.append('<div class="cover-subtitle">2017–2026</div>')
    parts.append('<div class="cover-line"></div>')
    parts.append('<p class="cover-tagline">我如何在变化中保存一个连续的自己？</p>')
    parts.append('</section>')

    # ========== SECTION II: READING DOPPELGÄNGERS ==========
    parts.append('<section class="section">')
    parts.append('<div class="section-number">II</div>')
    parts.append('<h2 class="section-title">阅读分身<br><span style="font-size:14px;color:#999;font-weight:normal;letter-spacing:2px;">Reading Doppelgangers</span></h2>')

    for soul in SOULS:
        parts.append(f'<div class="card card-soul" style="border-left-color:{soul["color"]};background:{soul["bg"]};">')
        parts.append(f'<div class="soul-name" style="color:{soul["color"]};">{soul["name_cn"]}</div>')
        parts.append(f'<div class="soul-name-en">{soul["name_en"]}</div>')
        for p in soul["paragraphs"]:
            safe_p = p.replace('"', '"').replace('"', '"')
            parts.append(f'<p>{safe_p}</p>')
        parts.append(f'<div class="soul-question"><span>核心追问：</span>{soul["question"]}</div>')
        parts.append('<div class="soul-books">')
        for book in soul["books"]:
            parts.append(f'<span>{book}</span>')
        parts.append('</div>')
        parts.append('</div>')

    parts.append('</section>')

    # ========== SECTION III: LIFE STRATUM ==========
    parts.append('<section class="section">')
    parts.append('<div class="section-number">III</div>')
    parts.append('<h2 class="section-title">人生地层<br><span style="font-size:14px;color:#999;font-weight:normal;letter-spacing:2px;">Life Stratum</span></h2>')
    parts.append('<p style="text-align:center;margin-bottom:36px;font-size:14px;color:#888;font-style:italic;">阅读的七个阶段，自下而上，从沉淀到浮现</p>')

    for i, layer in enumerate(reversed(STRATA)):
        idx = len(STRATA) - 1 - i
        parts.append(f'<div class="stratum stratum-{i}">')
        parts.append(f'<div class="layer-label">{layer["year"]} — {layer["label"]}</div>')
        parts.append(f'<div class="layer-title">{layer["title"]}</div>')
        parts.append(f'<div class="layer-desc">{layer["desc"]}</div>')
        parts.append('</div>')

    parts.append('</section>')

    # ========== SECTION IV: QUESTION ARCHAEOLOGY ==========
    parts.append('<section class="section">')
    parts.append('<div class="section-number">IV</div>')
    parts.append('<h2 class="section-title">问题考古学<br><span style="font-size:14px;color:#999;font-weight:normal;letter-spacing:2px;">Question Archaeology</span></h2>')
    parts.append('<p style="text-align:center;margin-bottom:36px;font-size:14px;color:#888;font-style:italic;">驱动阅读之旅的五个长期问题，考古发掘的珍贵遗存</p>')

    for f in FINDS:
        parts.append('<div class="find">')
        parts.append(f'<div class="find-q">{f["question"]}</div>')
        parts.append(f'<div class="find-meta">所属灵魂：{f["soul"]} · 出现时间：{f["emerged"]} · 贯穿至今</div>')
        parts.append(f'<div class="find-desc">{f["desc"]}</div>')
        parts.append('</div>')

    parts.append('</section>')

    # ========== SECTION V: READING TURNING POINTS ==========
    parts.append('<section class="section">')
    parts.append('<div class="section-number">V</div>')
    parts.append('<h2 class="section-title">阅读转折点<br><span style="font-size:14px;color:#999;font-weight:normal;letter-spacing:2px;">Reading Turning Points</span></h2>')
    parts.append('<p style="text-align:center;margin-bottom:36px;font-size:14px;color:#888;font-style:italic;">八本书，八个方向改变的瞬间</p>')

    for tp in TURNING_POINTS:
        parts.append('<div class="turning">')
        parts.append(f'<h4>{tp["book"]}</h4>')
        parts.append(f'<div class="turning-meta">{tp["meta"]}</div>')
        parts.append('<div class="turning-grid">')
        parts.append(f'<div class="turning-item"><h5>Before</h5><p>{tp["before"]}</p></div>')
        parts.append(f'<div class="turning-item"><h5>The Shift</h5><p>{tp["shift"]}</p></div>')
        parts.append(f'<div class="turning-item"><h5>After</h5><p>{tp["after"]}</p></div>')
        parts.append(f'<div class="turning-item"><h5>What Was Opened</h5><p>{tp["opened"]}</p></div>')
        parts.append('</div>')
        parts.append('</div>')

    parts.append('</section>')

    # ========== SECTION VI: ROOT QUESTION ==========
    parts.append('<section class="section">')
    parts.append('<div class="section-number">VI</div>')
    parts.append('<h2 class="section-title">根本问题<br><span style="font-size:14px;color:#999;font-weight:normal;letter-spacing:2px;">The Root Question</span></h2>')
    parts.append('<div class="root-box">')
    parts.append('<div class="root-question">我如何在变化中保存一个连续的自己？</div>')
    parts.append('<div class="root-line" style="width:40px;height:1px;background:#ddd;margin:0 auto 28px;"></div>')
    parts.append('<div class="root-explanation">')
    parts.append('2020年开始阅读时，这个问题并不存在。7年之后，经过6个灵魂的轮流登场、8个转折点的偏转、89本已读书籍的累积，问题变得清晰：跨越语言、跨越类型、跨越身份——这些变化中，什么是不变的？')
    parts.append('<br><br>')
    parts.append('阅读不是寻找答案，阅读是保存问问题的那个人。')
    parts.append('</div>')
    parts.append('</div>')
    parts.append('</section>')

    # ========== SECTION VII: STILL GROWING ==========
    parts.append('<section class="section">')
    parts.append('<div class="section-number">VII</div>')
    parts.append('<h2 class="section-title">仍在生长<br><span style="font-size:14px;color:#999;font-weight:normal;letter-spacing:2px;">Still Growing</span></h2>')

    for d in DIRECTIONS:
        parts.append('<div class="dir-card">')
        parts.append(f'<h4>{d["title"]}</h4>')
        parts.append(f'<p>{d["desc"]}</p>')
        parts.append('</div>')

    parts.append('</section>')

    # ========== FOOTER ==========
    parts.append('<div class="annotation">')
    parts.append('Reading Universe Archive &middot; 2017–2026')
    parts.append('</div>')

    parts.append('</div>')
    parts.append('</body>')
    parts.append('</html>')

    return '\n'.join(parts)

if __name__ == '__main__':
    html = build_html()
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Archive written to {OUTPUT}")
    size = os.path.getsize(OUTPUT)
    print(f"File size: {size} bytes")

