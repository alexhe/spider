# - * - coding: UTF-8 - *
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# done
base_folder="/vagrant/12/res/"
base_arch=base_folder+'arch/'

# done
which_month='12'
chief_editor="杨赛"
chief_editor_desc="杨赛（@lazycai），InfoQ高级策划编辑。写过一点Flash和前端，现在只是个伪码农。在51CTO创办了《Linux运维趋势》电子杂志，偶尔也自己折腾系统。曾混迹于英联邦国家，学过物理，做过一些游戏汉化，练过点长拳，玩过足球、篮球、羽毛球等各类运动和若干乐器。喜欢读《失控》。"
chief_editor_image="yangsai.jpg"

# done
plant_name='雪松'
plant_desc='''
雪松，又称香柏，是松科雪松属（学名：Cedrus）植物的统称。由于球果形状相似，与杉树最为接近。原产于喜玛拉雅山脉海拔1,500－3,200米的地带和地中海沿岸1,000－2,200米的地带。
树高40－50米（也有高60米的），木材带具刺激性的树脂香味，树皮粗糙、有脊状突出，树枝扁平。幼芽分为长（形成树枝，树叶独立地以开放螺旋叶序出现）、短（树叶多长于其上，呈密集螺旋丛生状）两类。叶子常绿，呈针状，长8－60公厘，叶色由亮草绿色到蓝绿色都有，视乎防止水份蒸发的蜡质层厚度而定。球果呈桶状，长6－12厘米，像杉树弓样在成熟时释出长10－15公厘的带翅（长20－30公厘）种子。内有2－3腺体，能分泌树脂阻止松鼠侵袭。球果需一年时间成熟，每年9－10月受粉，翌年种子成熟。此树是某些鳞翅目幼虫的食物。
'''
plant_img='xuesong.jpg'

## TODO: not 
recommand_editor_name='姚琪琳'
recommand_editor_img='yaoqilin.png'
recommand_editor_desc='''还记得在InfoQ试译的第一篇新闻被笠翔改得面目全非的情形，这让我想起了8年前帮导师翻译书籍的往事。当时我的译稿也被负责该项目的师兄改得面目全非，看着文档上一片一片的红字，我的脸也一阵红一阵白。师兄几乎完全重新翻译了我的那部分，这让我更加愧疚。但正是这样鲜明的对比，让我知道了什么是好的翻译，什么是烂的翻译，以及应该如何翻译得更好。可以说，是这位师兄把我领入了翻译之门。</p>

<p>从08年开始，我跟图灵合作翻译了多本技术书籍，包括《深入理解C#（第2版）》、《精通C#（第6版）》、《C#图解教程（第4版）》、《C#与.NET 4高级程序设计（第5版）》等。然而翻译书和翻译新闻并不尽相同。一般原版书籍的语言都比较浅显，作者往往会不惜笔墨，力求表述得清晰明了。而新闻文字则惜墨如金，尽量用精炼的语言传达更多的含义。因此我在试译的时候就感到极不适应，被笠翔审批得满目疮痍并不出乎我的意料。而且，我还感受到了当年师兄指导我时的那种耐心和责任心。当我私下跟笠翔联系，表达感激之情和惭愧之意时，笠翔说没关系，当年他也被伯薇批得很惨。这让我更加切实地感受到了InfoQ团队一如既往一脉传承一丝不苟的态度。</p>

<p>在当年国内的技术翻译良莠不齐的时候，InfoQ独自扛起大旗，将一大批技术牛人招致麾下，成为InfoQ的兼职编辑。这些牛人保证了翻译质量，使得InfoQ上不计其数的英文新闻和文章也能成为广大国内程序员的精神食粮，不断地拓展着他们的视野，激励着他们前行。我就是那个时候开始关注InfoQ的，同时也梦想着有一天自己也能强大到可以成为他们的一员，通过自己的翻译特长，为广大程序员提供帮助。我曾多次在微博上看到泰稳和国清在招贤纳士，但始终无法鼓足勇气。直到去年8月的某天，我终于给国清发了私信，正式成为了一名光荣的InfoQ编辑。</p>

<p>在编辑的群里，我常常被秀涛的严谨所震撼（他常常在阅读文章时发现感觉不对的地方，就查找原文，找出错误，并在群中提出），被李彬的高产所折服，被各位编辑一起咬文嚼字反复推敲的精神所感动。我为我能找到这样一群志同道合的朋友而感到欣慰。今年的QCon北京，我有幸见到了InfoQ的水哥、赛姐、Jessie、国清等人，以及秀涛、锦龙等跟我同一批成为编辑的兄弟。非常感谢InfoQ组织这样的大会，并且给予我们免费参加的福利。</p>

<p>说了这么多，还没有自我介绍。我叫姚琪琳，现在在ThoughtWorks写代码，对翻译、OO、.NET、Java等十分感兴趣，如果你想跟我交流，可以通过以下方式与我取得联系：
Weibo：@珧麒麟，
Blog：http://kirinboy.cnblogs.com，
Email：kirinboy@gmail.com。
'''

## 
foreword_title='创业和预测未来'
forword_content='''

<blockquote><p>“历史和社会不是缓慢爬行的，而是在一步步地跳跃。它们从一个断层跃上另一个断层，其间极少有波折。而我们（以及历史学家）喜欢相信那些我们能够预测的小的逐步演变。我们只是一台巨大的回头看的机器。”</p></blockquote>

<p>——《黑天鹅：如何应对不可预知的未来》</p>

<p>今天我们所见到的世界，有多少是你在2010年就预见到了的？有多少是你在2008年就预见到了的？有多少是你在2006年就能预见到的？</p>

<p>出来创业的人，在创业过程中大概总有某一个阶段会在心里描绘一幅三年之后、五年之后或者七年之后的市场画面。他们试图找到这个“想象中的世界”与现实世界之间的差距，并作出假设：如果能够填补这个差距，就能到达那个“想象中的世界”。那个世界中也许有一整个今天还不存在的市场，也可能只不过是一些细微的技术改进或模式改进。不管“想象中的世界”和今天的差别是大是小，它总归是一个新的世界。</p>

<p>这是一个预测未来的过程。</p>

<p>未来是一个概率事件。历史告诉我们，什么事都有可能发生，只是概率不同。作为一位预测者，如果你收集到尽可能多的、相关的可靠情报，你对“这件事可能会发生的几率”的判断会比其他人更准确；如果你这时去赌博（比如投资），就有更大的胜率。</p>

<p>但是，预测未来只是创业过程中很小的一部分。创业者跟大部分预测者的不同在于：</p>

<p>1、创业者有必要进入大部分人认为“不太可能发生的未来”</p>

<p>2、创业者的大部分工作是为了增加“这件事可能发生的几率”，或者“提前这件事真实到来的时间”</p>

<p>比如，IBM创始人曾预测人类只需要几台计算机。但是当计算机足够便宜、易用之后，市场自己解决了“计算机能做什么”这个问题。</p>

<p>比如在站长自己架站的时代，大部分人想不通一个普通人或者店铺做一个网站有什么用；但是当建立一个自己的页面变得足够简单之后，市场自己解决了这个问题。</p>

<p>比如我自己在2012年之前，一直坚持认为我需要一个全键盘的、待机时间长的手机，直到我入手了我的第一台Android手机之后，我才发现一个真正智能的系统完全可以“一美遮百丑”。</p>

<p>众所周知，创业的成功率很低，因为你不仅需要在正确的时间站在正确的地方，还需要找到推动事件前进的“杠杆”才能增加事情发生的几率。但是在事情真正发生前，你很难猜到这个“杠杆”是什么。所以市场的规则是，创业者们前仆后继的涌入，各自拿出各自猜测的可行道路，最后有极少数的道路走通了，于是我们进入了新时代。</p>

<p>（当然，极少数的道路成为了未来，并不意味着其他道路无法走通。这一切只因为大部分可能发生的未来都是小概率事件。）</p>

<p>在往新世界前进的道路上，大家心里那个“想象中的世界”不会一成不变，往往会进行一些修订。</p>

<p>有些修订出于对现实的妥协，这并不是理想的，因为妥协可能意味着一系列目标下滑的一个开端，结果是你折回到了旧世界当中，沦为平庸。</p>

<p>有些修订出于早期对时间和地点的预判偏离，这是应该的，这会有助于你减少浪费。</p>

<p>有些修订出于你看到了以前没看到的一些东西，这是必要的，因为未来往往来自意外。比如，发现宇宙背景微波辐射的两位科学家本来只是在找天线上的鸟粪。</p>

<p>我觉得旅途当中最重要的是，绝对不要忘记你的“新世界”将带来哪些新的价值。你在行走的路上会遇到各种各样的干扰：我要去学习谁的模式？我要去抢谁的生意？我要去打造什么样的差异化？</p>

<p>不要因此而分心。</p>

<p>我们学习历史，为的是学习他“为什么会发生”，而不是学习他“如何发生的”。没有发生的未来并非不可能发生，我们只不过在赌一个几率。你要做的是专心寻找那只杠杆。</p>

<p>记住你的愿景，反复在脑海中描绘你的新世界，你有更大的可能性会到达那里。</p>

<p>还有，我所说的，很可能是错的。</p>

<blockquote><p>“如果你是石器时代的哲学家，你的部落首席计划官要求你在一份综合报告中预测未来，你必须预测到车轮的发明，否则你就会错过大部分人类进展。……预测要求我们知道将在未来发现的技术。但认识到这一点几乎会自动地让我们立即开始开发这些技术。因此，我们不知道我们将知道什么。”</p></blockquote>

<p>最后给大家赠送一句摘抄：</p>

<blockquote><p>“我们制造玩具，有些玩具改变了世界。”</p></blockquote>'''

#专栏语
column_image = 'column.jpg'
column_title='敏捷与结构性模块化'
column_desc='''
敏捷开发方法论日益流行，然而大多数“敏捷”专家和分析师都在孤立地讨论敏捷，也就是说忽视了系统“结构”（Kirk Knoernschild是一个例外，他编写了一本名为《Java Application Architecture》的图书阐述这一理念）。考虑到“敏捷”是基础实体的一个重要特性或属性，那么，这种疏忽令人感到很惊讶。一个实体要具有“敏捷”的特性，它必须具有高度的结构性模块化（structural modularity）特征（参见Scott Page的《Diversity & Complexity》）。

也许正因为这种疏忽，许多组织在敏捷开发流程方面进行投入但忽略了应用程序的结构。除了“如何实现一个敏捷的系统？”这个问题以外, 有人肯定还会问, “如何构建一个在结构上具备高度模块化的系统？”
</p><p>
这个系列的文章将从探讨结构性模块化和敏捷之间的关系开始。
'''

## x=done,专题语
topic_image='topic.jpeg'
topic_title='内核那些事'

topic_desc='''
现在互联网的兴盛离不开操作系统的发展，但是对于大部分的互联网从业人员来说，内核一般都是不需要涉及的，但是当应用达到一定的量级之后，
开发人员将会面临系统性能的问题，此时优化的层面只能从底层入手，这也就是本期专栏的主题：内核那些事。这次的内容不仅讲到在处理大数据时如何断点不丢数据，还通过采访
UNIX环境高级编程的作者Stephen Rago，听他谈一谈这本程序员手边书一些背后的故事。
'''

gen_list=[
'arch/cover','arch/foreword','ads/InfoQ','arch/toc',
'ads/qclub',
'ads/qconbeijing',
'arch/0',
'arch/1','arch/2',
'arch/topic',
'arch/3','arch/4','arch/5',
'arch/6','arch/7',
'ads/ag1',
'arch/column','arch/8','arch/9','arch/10',
'ads/tuling',
'arch/11','arch/12','arch/13',
'ads/book',
'ads/history',
'ads/ag2',
'arch/plant',
'ads/1kg',
'arch/right']
org_urls={
    "人物 | People": # done
    [
        "http://www.infoq.com/cn/articles/codenvy-interview"
    ],
    
    "观点 | View": # done
    [
        "http://www.infoq.com/cn/news/2013/11/mongodb-things",
        "http://www.infoq.com/cn/news/2013/11/2014-trend"
    ],

    "本期专题：内核那些事 | Topic": #done
    [
        "http://www.infoq.com/cn/articles/large-data-processing-ensuring-data-not-lost-when-power-off",
        "http://www.infoq.com/cn/articles/apue_interview",
        "http://www.infoq.com/cn/articles/wjl-linux-pluggable-authentication-module"
    ],

    "推荐文章 | Article": #done
    [
        "http://www.infoq.com/cn/articles/HadoopSecurityModel",
        "http://www.infoq.com/cn/articles/make-imdg-enterprise-ready"
    ], 

    "特别专栏 | Column":#done
    [
        "http://www.infoq.com/cn/articles/agile-and-structural-modularity-part1",
        "http://www.infoq.com/cn/articles/agile-and-structural-modularity-part2",
        "http://www.infoq.com/cn/articles/agile-and-structural-modularity-part3",
    ],

    "避开那些坑 | Void":#done
    [
        "http://www.infoq.com/cn/news/2013/11/spring-web-flaw",
        "http://www.infoq.com/cn/news/2013/11/six-java-features-to-avoid"
    ],

    "新品推荐 | Product":# done
    [ 
        "http://www.infoq.com/cn/news/2013/11/netty4-twitter",
        "http://www.infoq.com/cn/news/2013/11/android-4-4-kitkat",
        "http://www.infoq.com/cn/news/2013/11/dart-10",
        "http://www.infoq.com/cn/news/2013/11/spring-data-neo4j-intro",
        "http://www.infoq.com/cn/news/2013/11/TypeScript-0-9-1",
        "http://www.infoq.com/cn/news/2013/11/apigee-nodejs-volos"
    ]

}


gen_list2=['ads\\InfoQ','arch\\toc',
'ads\\QClub','arch\\0','arch\\1','arch\\2',
'arch\\topic',
'arch\\3',
'arch\\4',
'arch\\5',
'arch\\6',
'arch\\7',
'arch\\8',
'arch\\9',
'arch\\column',
'arch\\10',
'arch\\11',
'arch\\12',
'arch\\13',
'ads\\book',
'ads\\history',
'arch\\plant',
'ads\\1kg']

