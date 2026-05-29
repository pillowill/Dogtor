"""
Dogtor - 对话数据 (扩展版, 约10000字对话素材)
每个对话节点包含导师的话和玩家的三个选项（搞怪/听话/反驳）
"""

# 选项风格
STYLE_FUNNY = "搞怪"
STYLE_OBEY = "听话"
STYLE_REBEL = "反驳"

DIALOGUES = [
    # ==================== 开场对话 (压力 0-25) ====================
    # 1
    {"id":"intro_1","advisor":"小李啊，进来坐。最近实验做得怎么样了？我上次跟你说的那个方向，你开始动手了没？","min_stress":0,"max_stress":25,"options":[
        {"text":"导师，我昨晚梦见实验成功了，醒来发现是假的，这算不算有进展？","style":STYLE_FUNNY,"stress":-5},
        {"text":"已经开始了导师，我每天都在实验室呆到很晚。","style":STYLE_OBEY,"stress":-10},
        {"text":"导师，我觉得那个方向可能不太可行，我查了一些文献...","style":STYLE_REBEL,"stress":15}]},
    # 2
    {"id":"intro_2","advisor":"我跟你说，这个方向要是做出来，发Nature绝对没问题。我认识Nature的一个副主编，到时候我帮你推荐。","min_stress":0,"max_stress":25,"options":[
        {"text":"导师太厉害了！那我是不是可以提前预订诺贝尔奖了？","style":STYLE_FUNNY,"stress":-5},
        {"text":"谢谢导师！我一定会努力不辜负您的期望。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，Nature的要求很高，我们这个方向竞争也很激烈...","style":STYLE_REBEL,"stress":10}]},
    # 3
    {"id":"intro_3","advisor":"对了，你最近论文写得怎么样了？下个月的会议投稿截止日期快到了。","min_stress":0,"max_stress":25,"options":[
        {"text":"论文正在以光速前进...大概就是蜗牛的光速。","style":STYLE_FUNNY,"stress":5},
        {"text":"我在抓紧写，每天晚上都在改。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，我觉得还需要再做一组实验才能下结论。","style":STYLE_REBEL,"stress":10}]},
    # 4
    {"id":"intro_4","advisor":"你看看隔壁实验室的王同学，人家才博二就已经发了两篇顶会了。你要加把劲啊。","min_stress":0,"max_stress":30,"options":[
        {"text":"王同学是人吗？我一直以为他是AI。","style":STYLE_FUNNY,"stress":0},
        {"text":"对不起导师，我会更加努力的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，王同学的方向和我不一样，不能这样比。","style":STYLE_REBEL,"stress":15}]},
    # 5
    {"id":"intro_5","advisor":"周末有什么安排吗？我想让你来实验室跑一组新数据，这个想法我觉得非常好。","min_stress":0,"max_stress":30,"options":[
        {"text":"本来打算去相亲的，不过实验室就是我的另一半！","style":STYLE_FUNNY,"stress":-5},
        {"text":"没问题导师，我周末都在实验室。","style":STYLE_OBEY,"stress":-10},
        {"text":"导师，我已经连续三个周末没休息了，能不能下周？","style":STYLE_REBEL,"stress":20}]},
    # 6
    {"id":"intro_6","advisor":"你知道吗，我们这个实验室在系里的地位，就靠你们的成果了。我都跟院长拍了胸脯的。","min_stress":5,"max_stress":30,"options":[
        {"text":"导师您的胸脯还好吗？要不要我帮您揉揉？","style":STYLE_FUNNY,"stress":0},
        {"text":"我一定不会给实验室丢脸的！","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，您对外承诺太多会给我们很大压力的。","style":STYLE_REBEL,"stress":15}]},
    # 7
    {"id":"intro_7","advisor":"对了，课题组经费有点紧张，你这个月的补助可能要晚点发。不过你放心，项目结题了肯定补上。","min_stress":5,"max_stress":30,"options":[
        {"text":"没事导师，我已经在考虑卖肾了，正好两个。","style":STYLE_FUNNY,"stress":5},
        {"text":"没关系的导师，我还能撑一撑。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，这已经是第三个月推迟了，我房租都快交不起了。","style":STYLE_REBEL,"stress":20}]},
    # 8
    {"id":"intro_8","advisor":"你有没有关注最近那个很火的AI方向？我觉得我们可以蹭一下热度，你去看几百篇论文，下周给我一个调研报告。","min_stress":5,"max_stress":30,"options":[
        {"text":"几百篇？导师，我的眼睛说它们想辞职。","style":STYLE_FUNNY,"stress":5},
        {"text":"好的导师，我这就开始看。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，几百篇一周看完不现实，能不能先聚焦最核心的几十篇？","style":STYLE_REBEL,"stress":10}]},
    # 9
    {"id":"intro_9","advisor":"我刚从国外开会回来，发现国外都在做这个方向。我们得加紧了，不能被别人抢了先。","min_stress":10,"max_stress":35,"options":[
        {"text":"导师，您带回来的纪念品呢？我比较关心这个。","style":STYLE_FUNNY,"stress":0},
        {"text":"明白了导师，我会加快进度的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，我们条件跟国外不一样，不能盲目追热点。","style":STYLE_REBEL,"stress":15}]},
    # 10
    {"id":"intro_10","advisor":"你说说看，你对这个课题有什么想法？随便说，不要怕说错。","min_stress":10,"max_stress":35,"options":[
        {"text":"我的想法是...能不能换个课题？","style":STYLE_FUNNY,"stress":10},
        {"text":"导师，我觉得应该严格按照您的思路来。","style":STYLE_OBEY,"stress":-5},
        {"text":"我觉得可以尝试从另一个角度切入，我整理了一些文献支持...","style":STYLE_REBEL,"stress":10}]},

    # ==================== 中期对话 (压力 25-55) ====================
    # 11
    {"id":"mid_1","advisor":"你这个实验结果为什么和预期差这么多？你是不是操作有问题？","min_stress":20,"max_stress":55,"options":[
        {"text":"可能是实验设备自己想放假了，它也需要Work-Life Balance。","style":STYLE_FUNNY,"stress":5},
        {"text":"对不起导师，我重新做一遍。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，这个实验本身的设计就有问题，我之前提过的。","style":STYLE_REBEL,"stress":20}]},
    # 12
    {"id":"mid_2","advisor":"我当年读博的时候，每天早上六点就到实验室，晚上十二点才走。现在的年轻人就是吃不了苦。","min_stress":20,"max_stress":55,"options":[
        {"text":"导师，那您那个年代有外卖吗？没有外卖确实只能早出晚归。","style":STYLE_FUNNY,"stress":10},
        {"text":"导师说得对，我会调整作息向您学习。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，时代不同了，效率比时间更重要。","style":STYLE_REBEL,"stress":15}]},
    # 13
    {"id":"mid_3","advisor":"你这个论文的Introduction写得跟本科毕业论文一样，完全没有深度。重写。","min_stress":25,"max_stress":60,"options":[
        {"text":"导师，我本科论文拿的是优秀，您这是在夸我吗？","style":STYLE_FUNNY,"stress":5},
        {"text":"好的导师，我回去重新查文献重写。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，您能给我一些具体的修改意见吗？","style":STYLE_REBEL,"stress":10}]},
    # 14
    {"id":"mid_4","advisor":"我跟你说，这个项目要是做好了，不光是Nature，Science也会来找我们的。你想想那个影响力。","min_stress":20,"max_stress":55,"options":[
        {"text":"导师，我先去把诺贝尔奖的获奖感言写好备着。","style":STYLE_FUNNY,"stress":0},
        {"text":"我一定会全力以赴的！","style":STYLE_OBEY,"stress":-10},
        {"text":"导师，我们先脚踏实地把实验做好吧。","style":STYLE_REBEL,"stress":10}]},
    # 15
    {"id":"mid_5","advisor":"你最近怎么状态这么差？是不是又熬夜打游戏了？","min_stress":25,"max_stress":60,"options":[
        {"text":"打游戏？导师您太看得起我了，我连开机的力气都没有。","style":STYLE_FUNNY,"stress":5},
        {"text":"没有导师，就是最近实验压力有点大。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，我状态不好是因为您给我的工作量太大了。","style":STYLE_REBEL,"stress":25}]},
    # 16
    {"id":"mid_6","advisor":"这个课题我已经想了很久了，你按照我说的做肯定没问题。不要有太多自己的想法。","min_stress":30,"max_stress":65,"options":[
        {"text":"好的导师，我大脑已关机，现在是您的远程机器人。","style":STYLE_FUNNY,"stress":5},
        {"text":"明白了导师，我会严格按照您的指导来做。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，我觉得博士培养的是独立思考能力，我想提出一些自己的想法。","style":STYLE_REBEL,"stress":25}]},
    # 17 - 新
    {"id":"mid_7","advisor":"对了，系里要搞一个学术沙龙，你替我去讲一下。PPT今晚做好发我。","min_stress":25,"max_stress":55,"options":[
        {"text":"没问题导师，我PPT模板都准备好几十套了，专业的代讲工具人。","style":STYLE_FUNNY,"stress":5},
        {"text":"好的导师，我会好好准备的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，这个您的报告应该是您自己讲比较合适吧？","style":STYLE_REBEL,"stress":20}]},
    # 18 - 新
    {"id":"mid_8","advisor":"你看这个审稿意见，审稿人说我们的方法没有创新性。你是不是文献综述没做好？","min_stress":30,"max_stress":60,"options":[
        {"text":"审稿人肯定没仔细看！要不我写封信夸夸他？","style":STYLE_FUNNY,"stress":5},
        {"text":"对不起导师，我重新梳理文献再改。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，文献综述是您让我按那个方向写的...","style":STYLE_REBEL,"stress":25}]},
    # 19 - 新
    {"id":"mid_9","advisor":"我最近接了一个横向项目，跟你的课题也有关系。你顺便帮忙做一下，年底给你多发点补助。","min_stress":25,"max_stress":55,"options":[
        {"text":"导师，'顺便'和'整个'是近义词吗？我中文不太好。","style":STYLE_FUNNY,"stress":10},
        {"text":"好的导师，我会协调好时间。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，横向项目跟我的课题关系不大，会严重影响我的研究进度。","style":STYLE_REBEL,"stress":20}]},
    # 20 - 新
    {"id":"mid_10","advisor":"你读博到现在也快两年了吧？有没有想过毕业以后想做什么？","min_stress":25,"max_stress":55,"options":[
        {"text":"我想做一条咸鱼，导师您看这个方向有前途吗？","style":STYLE_FUNNY,"stress":0},
        {"text":"我想继续做科研，希望能留在学术界。","style":STYLE_OBEY,"stress":-5},
        {"text":"说实话导师，我现在只想先活过这个博士阶段。","style":STYLE_REBEL,"stress":15}]},
    # 21 - 新
    {"id":"mid_11","advisor":"你那个数据集太小了，结果不可靠。想办法再去爬一些数据，越多越好。","min_stress":30,"max_stress":60,"options":[
        {"text":"导师，要不我直接爬整个互联网？可能需要几个世纪。","style":STYLE_FUNNY,"stress":5},
        {"text":"好的，我去想办找更多的数据。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，数据质量比数量更重要，现在的问题是标注不够精确。","style":STYLE_REBEL,"stress":15}]},
    # 22 - 新
    {"id":"mid_12","advisor":"下周有个学术报告，我请了个大牛来。你要不要去接待一下？顺便请教一下人家。","min_stress":30,"max_stress":55,"options":[
        {"text":"好的导师，我会举着我的论文追着他跑的。","style":STYLE_FUNNY,"stress":0},
        {"text":"谢谢导师给我这个锻炼的机会。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，接待工作不是应该由学院安排吗？","style":STYLE_REBEL,"stress":10}]},

    # ==================== 高压对话 (压力 50-80) ====================
    # 23
    {"id":"high_1","advisor":"你这个进度，我感觉四年都毕不了业。你到底还想不想读了？","min_stress":45,"max_stress":80,"options":[
        {"text":"导师，四年的博士太短了，我想读一辈子！","style":STYLE_FUNNY,"stress":10},
        {"text":"对不起导师，我会拼命赶进度的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，如果您能减少一些杂活，我的研究进度会快很多。","style":STYLE_REBEL,"stress":20}]},
    # 24
    {"id":"high_2","advisor":"我跟系里说了，你这个方向很有前途。你要是做不出来，我在系里都抬不起头。","min_stress":50,"max_stress":85,"options":[
        {"text":"导师，要不您换个学生？我推荐隔壁王同学。","style":STYLE_FUNNY,"stress":15},
        {"text":"我一定不会让您失望的，导师。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，您不应该在没有和我商量的情况下就对外承诺。","style":STYLE_REBEL,"stress":30}]},
    # 25
    {"id":"high_3","advisor":"春节你就别回家了，趁着假期没人打扰，正好冲冲实验进度。","min_stress":50,"max_stress":85,"options":[
        {"text":"好的导师，我妈说她已经不记得我长什么样了，正好视频过年。","style":STYLE_FUNNY,"stress":10},
        {"text":"好的导师，我留下来做实验。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，春节是法定假期，我需要回家看看父母。","style":STYLE_REBEL,"stress":30}]},
    # 26
    {"id":"high_4","advisor":"你的方法和别人的一样，为什么人家的结果就是比你的好？你是不是不够努力？","min_stress":55,"max_stress":90,"options":[
        {"text":"可能是因为我的实验设备比较内向，需要多一些鼓励。","style":STYLE_FUNNY,"stress":10},
        {"text":"我会多试几次，找到问题所在。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，科研不是光靠努力就有结果的，运气和方向都很重要。","style":STYLE_REBEL,"stress":20}]},
    # 27
    {"id":"high_5","advisor":"我帮你找了个实习机会，不过是在另一个城市的，每周要来回跑。但这对你简历很有帮助。","min_stress":55,"max_stress":90,"options":[
        {"text":"导师，您是不是想把我支开好清净清净？","style":STYLE_FUNNY,"stress":5},
        {"text":"谢谢导师，我会合理安排时间。","style":STYLE_OBEY,"stress":-10},
        {"text":"导师，我现在的实验已经够忙了，再加实习我怕两边都做不好。","style":STYLE_REBEL,"stress":20}]},
    # 28 - 新
    {"id":"high_6","advisor":"你知道吗，我最近在想，是不是应该把你的课题方向调整一下。之前的方向感觉没什么前途。","min_stress":50,"max_stress":80,"options":[
        {"text":"导师，我之前的半年时间是在帮您积累失败经验吗？","style":STYLE_FUNNY,"stress":15},
        {"text":"导师您说得有道理，我服从安排。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，换方向意味着之前的工作全部白费，我需要一个合理的解释。","style":STYLE_REBEL,"stress":30}]},
    # 29 - 新
    {"id":"high_7","advisor":"你们的论文我被要求挂通讯作者就够了，第一作者和后面的你自己看。对了，我有个朋友的孩子想保研，你带带他。","min_stress":55,"max_stress":85,"options":[
        {"text":"导师您真是我的再生父母啊，连师弟都帮我安排好了。","style":STYLE_FUNNY,"stress":10},
        {"text":"好的导师，我会好好带师弟的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，保研名额的事应该走正规程序吧？","style":STYLE_REBEL,"stress":25}]},
    # 30 - 新
    {"id":"high_8","advisor":"你这篇论文的英文写得太差了，我让一个本科生帮你改了一下，你看看。","min_stress":50,"max_stress":80,"options":[
        {"text":"导师，本科生都能改我的论文，那我是不是该回去重读本科？","style":STYLE_FUNNY,"stress":10},
        {"text":"谢谢导师，我会认真学习的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，我的英文水平需要提高，但这不代表本科生能比我写得好。","style":STYLE_REBEL,"stress":20}]},
    # 31 - 新
    {"id":"high_9","advisor":"今天晚上有个饭局，几个大老板都在，你过来帮我挡挡酒。这种场合对你以后发展很重要。","min_stress":50,"max_stress":80,"options":[
        {"text":"导师，我酒精过敏，但我可以表演现场写代码助兴！","style":STYLE_FUNNY,"stress":5},
        {"text":"好的导师，我会准时到的。","style":STYLE_OBEY,"stress":-10},
        {"text":"导师，我不太擅长这种场合，而且明天还有实验。","style":STYLE_REBEL,"stress":20}]},
    # 32 - 新
    {"id":"high_10","advisor":"我看了你的代码，写得一点都不规范。注释也不写，变量命名也乱。你这样以后怎么去大厂？","min_stress":55,"max_stress":85,"options":[
        {"text":"导师，我的变量名都是'劈里啪啦'和'哗啦哗啦'，很有规律啊。","style":STYLE_FUNNY,"stress":10},
        {"text":"对不起导师，我会回头好好整理的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，我一直在赶实验，没有时间重构代码。","style":STYLE_REBEL,"stress":20}]},
    # 33 - 新
    {"id":"high_11","advisor":"你知不知道，你的开题报告我帮你改了快一半才算勉强能看。你以后写东西能不能用点心？","min_stress":55,"max_stress":85,"options":[
        {"text":"导师您辛苦了！要不以后我来帮您按摩，您来帮我写论文？","style":STYLE_FUNNY,"stress":10},
        {"text":"对不起导师，我下次一定写得更好。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，开题报告本来就是需要导师指导的...","style":STYLE_REBEL,"stress":20}]},

    # ==================== 极高压力对话 (压力 70-100) ====================
    # 34
    {"id":"critical_1","advisor":"我觉得你根本不适合做科研。要不然你考虑一下转行吧。","min_stress":65,"max_stress":100,"options":[
        {"text":"导师说得对！我已经在学做煎饼果子了，您要不要来一套？","style":STYLE_FUNNY,"stress":15},
        {"text":"导师请再给我一次机会...","style":STYLE_OBEY,"stress":5},
        {"text":"导师，适不适合不是您一个人说了算的。","style":STYLE_REBEL,"stress":30}]},
    # 35
    {"id":"critical_2","advisor":"我告诉你，你要是这个月再不出结果，我就换人做这个课题。你自己看着办。","min_stress":70,"max_stress":100,"options":[
        {"text":"导师，那我这几个月是在帮您练手吗？","style":STYLE_FUNNY,"stress":20},
        {"text":"我一定会在月底之前拿出结果的！","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，您这样的管理方式对学生的心理健康影响很大。","style":STYLE_REBEL,"stress":35}]},
    # 36
    {"id":"critical_3","advisor":"你是不是觉得我太严格了？我告诉你，现在不严格，将来出了社会你会更惨。","min_stress":70,"max_stress":100,"options":[
        {"text":"导师，您这是在帮我提前适应地狱模式吗？","style":STYLE_FUNNY,"stress":10},
        {"text":"谢谢导师的栽培，严师出高徒。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，严格和PUA是有区别的。","style":STYLE_REBEL,"stress":40}]},
    # 37
    {"id":"critical_4","advisor":"你以为你在为我做实验？你是在为自己做！我这是在帮你，你懂吗？","min_stress":75,"max_stress":100,"options":[
        {"text":"我懂了导师，我是在帮Nature做实验。","style":STYLE_FUNNY,"stress":15},
        {"text":"我懂的导师，感谢您的良苦用心。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，如果您真的是在帮我，那请您也尊重一下我的时间和选择。","style":STYLE_REBEL,"stress":35}]},
    # 38
    {"id":"critical_5","advisor":"这样吧，我给你最后一次机会。下周一之前，把所有的实验数据、论文、还有那个项目的报告全部交到我桌上。","min_stress":80,"max_stress":100,"options":[
        {"text":"导师，您说的是下周一还是明年下周一？我需要确认一下时间线。","style":STYLE_FUNNY,"stress":20},
        {"text":"好的导师，我通宵也会完成的。","style":STYLE_OBEY,"stress":5},
        {"text":"导师，这根本不现实。我需要至少两周时间才能完成这些。","style":STYLE_REBEL,"stress":40}]},
    # 39 - 新
    {"id":"critical_6","advisor":"我实话跟你说吧，你这个课题当初立项的时候我就觉得悬。现在果然不出我所料。","min_stress":75,"max_stress":100,"options":[
        {"text":"导师，原来您一直在让我做一个'悬'的课题？那我是不是该去买彩票？","style":STYLE_FUNNY,"stress":20},
        {"text":"导师，我会证明这个课题是有价值的。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，如果您一开始就觉得悬，为什么不早说？浪费了我一年多的时间。","style":STYLE_REBEL,"stress":40}]},
    # 40 - 新
    {"id":"critical_7","advisor":"你博士读了这么久，paper没发几篇，实验也没出什么像样的结果。你自己说说，你对得起国家发的补助吗？","min_stress":75,"max_stress":100,"options":[
        {"text":"导师，要不我把补助退回去？不过可能要分期付款。","style":STYLE_FUNNY,"stress":15},
        {"text":"对不起导师，我愧对国家和您的培养。","style":STYLE_OBEY,"stress":5},
        {"text":"导师，科研本身就有不确定性，不能唯论文论。","style":STYLE_REBEL,"stress":30}]},
    # 41 - 新
    {"id":"critical_8","advisor":"学院最近在讨论博士生淘汰制度。你自己心里要有数。","min_stress":80,"max_stress":100,"options":[
        {"text":"淘汰了也好，我可以安心去开滴滴了，听说收入还不错。","style":STYLE_FUNNY,"stress":20},
        {"text":"导师，请您帮我跟学院说说好话。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，淘汰制度应该有明确的标准，不能凭个人好恶。","style":STYLE_REBEL,"stress":35}]},
    # 42 - 新
    {"id":"critical_9","advisor":"我帮你找了一个做行政的老师聊了聊，他说你这个情况...比较难。要不你先转硕？","min_stress":80,"max_stress":100,"options":[
        {"text":"转硕？那我之前挨的骂不是白挨了？不能这么亏！","style":STYLE_FUNNY,"stress":15},
        {"text":"导师，再给我一点时间...","style":STYLE_OBEY,"stress":5},
        {"text":"导师，转硕不是您一句话的事，我需要走正规流程了解相关政策。","style":STYLE_REBEL,"stress":30}]},
    # 43 - 新
    {"id":"critical_10","advisor":"算了，我也不想多说了。你自己好自为之吧。门在那边。","min_stress":85,"max_stress":100,"options":[
        {"text":"好的导师，门我看到了。不过我还想再挣扎一下。","style":STYLE_FUNNY,"stress":20},
        {"text":"导师，请您再给我一次机会，我什么都可以改。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，逃避问题解决不了任何事。我们需要认真谈一谈。","style":STYLE_REBEL,"stress":40}]},

    # ==================== 额外开场对话 ====================
    # 44
    {"id":"intro_11","advisor":"听说你最近在学一个新的实验技术？年轻人学东西快，学会了教教实验室其他人。","min_stress":0,"max_stress":25,"options":[
        {"text":"好的导师，我的培训班下周一开课，学费每人一杯奶茶！","style":STYLE_FUNNY,"stress":-5},
        {"text":"好的导师，我会认真教大家的。","style":STYLE_OBEY,"stress":-10},
        {"text":"导师，我自己也还不太熟练，怕误人子弟。","style":STYLE_REBEL,"stress":10}]},
    # 45
    {"id":"intro_12","advisor":"我跟你说，做科研要有大局观。不要老盯着自己那一亩三分地。","min_stress":5,"max_stress":30,"options":[
        {"text":"导师，我的大局观就是——只要导师开心，我就开心。","style":STYLE_FUNNY,"stress":-5},
        {"text":"导师说得对，我会多关注领域前沿动态的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，专注自己的方向才能做深做透。","style":STYLE_REBEL,"stress":10}]},
    # 46
    {"id":"intro_13","advisor":"对了，你的工位是不是太乱了？整理一下，给人看了也要有个搞科研的样子。","min_stress":0,"max_stress":25,"options":[
        {"text":"导师，那不叫乱，那叫'创造性混沌'，爱因斯坦的桌子也很乱。","style":STYLE_FUNNY,"stress":0},
        {"text":"好的导师，我马上就收拾。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，工位整洁度跟科研水平没有必然联系。","style":STYLE_REBEL,"stress":10}]},
    # 47
    {"id":"intro_14","advisor":"你觉得实验室的氛围怎么样？有没有什么建议？","min_stress":5,"max_stress":30,"options":[
        {"text":"建议每隔一小时播放眼保健操音乐，让大家放松一下。","style":STYLE_FUNNY,"stress":-5},
        {"text":"挺好的导师，大家都很努力。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，我觉得组会频率太高了，占用了大量实验时间。","style":STYLE_REBEL,"stress":15}]},

    # ==================== 额外中期对话 ====================
    # 48
    {"id":"mid_13","advisor":"你这组对比实验的baseline选得不对。你回去看看别人论文里怎么选的，别自己想当然。","min_stress":25,"max_stress":55,"options":[
        {"text":"导师，我就是'别人'啊，我论文里也是这么写的...哦你说的是别人。","style":STYLE_FUNNY,"stress":5},
        {"text":"好的导师，我回去重新查文献。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，我选的baseline是有文献依据的，我可以给您看。","style":STYLE_REBEL,"stress":15}]},
    # 49
    {"id":"mid_14","advisor":"实验室的服务器怎么又挂了？是不是你跑的实验把显存占满了？","min_stress":25,"max_stress":55,"options":[
        {"text":"导师，服务器可能在学我——压力太大了就想挂机。","style":STYLE_FUNNY,"stress":5},
        {"text":"对不起导师，我去检查一下。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，实验室的服务器配置本来就不够，大家都在用。","style":STYLE_REBEL,"stress":15}]},
    # 50
    {"id":"mid_15","advisor":"你下周去参加那个学术会议，顺便帮我拿一份某某教授的报告资料。记住，一定要拿到。","min_stress":30,"max_stress":60,"options":[
        {"text":"导师，我可以带上实验室的麻袋，方便'拿'资料。","style":STYLE_FUNNY,"stress":0},
        {"text":"好的导师，我会去跟那位教授沟通。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，别人的资料不一定愿意给，我只能尽力。","style":STYLE_REBEL,"stress":10}]},
    # 51
    {"id":"mid_16","advisor":"你的图做得太丑了，你看看人家顶会论文里的图，那才叫专业。","min_stress":30,"max_stress":60,"options":[
        {"text":"导师，我的图可能不好看，但它们很有'灵魂'。","style":STYLE_FUNNY,"stress":5},
        {"text":"好的导师，我去学习一下美观的作图方法。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，图的美观不是最重要的，数据的真实和准确才是核心。","style":STYLE_REBEL,"stress":15}]},
    # 52
    {"id":"mid_17","advisor":"我最近在写一个基金申请书，你帮我整理一下近五年的相关文献，做个综述。周末之前给我。","min_stress":30,"max_stress":60,"options":[
        {"text":"好的导师，我顺便帮您把诺贝尔奖提名也写了吧。","style":STYLE_FUNNY,"stress":10},
        {"text":"好的导师，我会认真整理的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，基金申请书应该是您自己写的，我最多帮您查一些文献。","style":STYLE_REBEL,"stress":25}]},
    # 53
    {"id":"mid_18","advisor":"你有没有考虑过出国做博后？我认识几个国外的教授，可以帮你推荐。","min_stress":25,"max_stress":55,"options":[
        {"text":"导师，我连中国的博士都还没读完，您已经帮我想好出国的事了？","style":STYLE_FUNNY,"stress":0},
        {"text":"谢谢导师，我会认真考虑的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，现在谈博后还太早，我应该先专注把博士阶段做好。","style":STYLE_REBEL,"stress":10}]},
    # 54
    {"id":"mid_19","advisor":"你上个月的实验记录发我看一下。我要检查一下你有没有认真记录。","min_stress":30,"max_stress":60,"options":[
        {"text":"导师，我的实验记录采用了一种新型加密技术——潦草字体。","style":STYLE_FUNNY,"stress":5},
        {"text":"好的导师，我马上发您。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，您随时检查是对我的不信任，我建议建立定期汇报机制。","style":STYLE_REBEL,"stress":20}]},
    # 55
    {"id":"mid_20","advisor":"你那个idea我仔细想过了，不太行。还是按照我之前说的方案来做。","min_stress":30,"max_stress":60,"options":[
        {"text":"导师英明！我的idea就当是为科学事业做反面教材了。","style":STYLE_FUNNY,"stress":5},
        {"text":"好的导师，我按您的方案重新来。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，您能具体说说什么地方不行吗？我花了很多时间做的方案。","style":STYLE_REBEL,"stress":20}]},
    # 56
    {"id":"mid_21","advisor":"最近学院在评选优秀博士生，我帮你报了名。你准备一下材料。","min_stress":25,"max_stress":55,"options":[
        {"text":"优秀博士生？导师，这个词跟我好像没什么关系。","style":STYLE_FUNNY,"stress":0},
        {"text":"谢谢导师！我会好好准备材料的。","style":STYLE_OBEY,"stress":-10},
        {"text":"导师，以我目前的成果，评优可能还差一些...","style":STYLE_REBEL,"stress":10}]},

    # ==================== 额外高压对话 ====================
    # 57
    {"id":"high_12","advisor":"我这段时间可能对你太温和了。从今天开始，每周一三五早上八点，到我办公室汇报进展。","min_stress":50,"max_stress":80,"options":[
        {"text":"八点？导师，我的生物钟还在西半球时间。","style":STYLE_FUNNY,"stress":10},
        {"text":"好的导师，我会按时来的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，一周三次汇报会严重影响我的实验连续性。","style":STYLE_REBEL,"stress":25}]},
    # 58
    {"id":"high_13","advisor":"你的PPT汇报我看了，漏洞百出。下周组会你要是还是这个水平，就别讲了。","min_stress":55,"max_stress":85,"options":[
        {"text":"导师，那我直接在组会上表演一段相声代替汇报？","style":STYLE_FUNNY,"stress":15},
        {"text":"对不起导师，我会彻底重做的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，您说漏洞百出，但一个具体的修改建议都没有。","style":STYLE_REBEL,"stress":25}]},
    # 59
    {"id":"high_14","advisor":"你知不知道，你延期毕业的话，对实验室的招生指标是有影响的？你自己无所谓，但不能连累师弟师妹。","min_stress":60,"max_stress":90,"options":[
        {"text":"导师，那我现在退学是不是对招生反而有利？","style":STYLE_FUNNY,"stress":15},
        {"text":"对不起导师，我会尽最大努力按时毕业。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，用招生指标来压学生是不合理的。","style":STYLE_REBEL,"stress":30}]},
    # 60
    {"id":"high_15","advisor":"我看你朋友圈了，周末还出去玩？实验结果一团糟还有心思玩？","min_stress":55,"max_stress":85,"options":[
        {"text":"导师，我去的是学校旁边的公园，可以算做田野调查。","style":STYLE_FUNNY,"stress":10},
        {"text":"对不起导师，我以后周末都不休息了。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，周末是我自己的时间，适当的休息有助于提高效率。","style":STYLE_REBEL,"stress":25}]},
    # 61
    {"id":"high_16","advisor":"我一个朋友的课题组缺人，你要不要过去交流半年？对你拓展视野有好处。","min_stress":55,"max_stress":85,"options":[
        {"text":"导师，您这是要把我'优化'出去吗？","style":STYLE_FUNNY,"stress":10},
        {"text":"谢谢导师，我会认真考虑的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，我的课题正处在关键阶段，现在离开半年不合理。","style":STYLE_REBEL,"stress":25}]},
    # 62
    {"id":"high_17","advisor":"我已经给你很多次机会了。你有没有想过，也许你真的不适合读博？","min_stress":60,"max_stress":90,"options":[
        {"text":"导师，适不适合不要紧，主要是我已经上了贼船了。","style":STYLE_FUNNY,"stress":15},
        {"text":"导师，我会证明我适合的。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，适不适合应该用客观标准来衡量，不是凭感觉。","style":STYLE_REBEL,"stress":30}]},

    # ==================== 额外极高压力对话 ====================
    # 63
    {"id":"critical_11","advisor":"你去看看心理咨询中心吧。我觉得你最近状态太差了。","min_stress":75,"max_stress":100,"options":[
        {"text":"好的导师，我会跟心理咨询师说：病因是导师。","style":STYLE_FUNNY,"stress":20},
        {"text":"谢谢导师关心，我会去的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，如果我的状态差，也许源头不止在我身上。","style":STYLE_REBEL,"stress":35}]},
    # 64
    {"id":"critical_12","advisor":"这样，你把这学期的实验全部停了，先去帮本科生带一学期的实验课。冷静冷静。","min_stress":80,"max_stress":100,"options":[
        {"text":"导师，您是让我从博士生降级成助教吗？工资涨不涨？","style":STYLE_FUNNY,"stress":20},
        {"text":"好的导师，我服从安排。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，停掉实验意味着延期更长，这对谁都没有好处。","style":STYLE_REBEL,"stress":40}]},
    # 65
    {"id":"critical_13","advisor":"你是不是觉得我针对你？我告诉你，我要针对你，你早就走人了。","min_stress":80,"max_stress":100,"options":[
        {"text":"谢谢导师不杀之恩！那我现在能回实验室了吗？","style":STYLE_FUNNY,"stress":15},
        {"text":"没有没有，我知道导师是为我好。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，您的话本身就带有威胁的意思，这不是健康的师生关系。","style":STYLE_REBEL,"stress":40}]},
    # 66
    {"id":"critical_14","advisor":"我跟你说最后一个办法：你去投一个水刊吧。虽然档次低，但至少有篇论文能毕业。","min_stress":85,"max_stress":100,"options":[
        {"text":"导师，'水刊'和'毕业'这两个词能放在一起吗？我读书少。","style":STYLE_FUNNY,"stress":15},
        {"text":"好的导师，我去试试。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，您之前不是说要发Nature吗？现在让我投水刊？","style":STYLE_REBEL,"stress":35}]},
    # 67
    {"id":"critical_15","advisor":"其实我一直没跟你说，当年收你做学生的时候我就有顾虑。现在看来我的顾虑是对的。","min_stress":85,"max_stress":100,"options":[
        {"text":"导师，那您当初为什么不相信自己的直觉呢？","style":STYLE_FUNNY,"stress":25},
        {"text":"导师，对不起让您失望了...","style":STYLE_OBEY,"stress":10},
        {"text":"导师，这种话对一个博士生来说伤害太大了。","style":STYLE_REBEL,"stress":40}]},

    # ==================== 特殊场景对话 ====================
    # 68 - 被导师在走廊偶遇
    {"id":"special_1","advisor":"哎小李！正找你呢。刚好在走廊碰到，省得我去你工位了。上次那个项目甲方在催了，你今天能搞定吧？","min_stress":10,"max_stress":50,"options":[
        {"text":"导师，走廊不是一个适合讨论deadline的地方，空气太自由了。","style":STYLE_FUNNY,"stress":5},
        {"text":"没问题导师，我今天一定搞定。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，那个项目的需求一直在变，不是我能控制的。","style":STYLE_REBEL,"stress":15}]},
    # 69 - 组会场景
    {"id":"special_2","advisor":"今天组会轮到你讲了。我希望看到你这一周的工作量，不要拿上周的东西来应付。","min_stress":20,"max_stress":60,"options":[
        {"text":"导师，我发明了时光机，把上周的工作复制到了这周——开玩笑的。","style":STYLE_FUNNY,"stress":5},
        {"text":"导师，我准备了这周的新进展汇报。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，科研不是每周都有线性进展的，这周我主要在阅读和思考。","style":STYLE_REBEL,"stress":15}]},
    # 70 - 深夜被导师电话
    {"id":"special_3","advisor":"喂？还没睡吧？我刚想到一个绝妙的idea，你现在记一下，明天就开始做。","min_stress":30,"max_stress":70,"options":[
        {"text":"导师，现在是凌晨两点，我的大脑处于'只读模式'。","style":STYLE_FUNNY,"stress":10},
        {"text":"好的导师，您说我记着。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，凌晨两点打电话讨论工作不太合适。","style":STYLE_REBEL,"stress":25}]},
    # 71 - 导师心情好
    {"id":"special_4","advisor":"今天心情不错，刚才基金中了。你跟的项目也有份，你也是功臣之一。","min_stress":5,"max_stress":40,"options":[
        {"text":"恭喜导师！请问基金里有'给学生加鸡腿'这项预算吗？","style":STYLE_FUNNY,"stress":-10},
        {"text":"恭喜导师！这都是导师领导有方。","style":STYLE_OBEY,"stress":-15},
        {"text":"恭喜导师，希望基金能切实改善实验室的研究条件。","style":STYLE_REBEL,"stress":0}]},
    # 72 - 论文署名讨论
    {"id":"special_5","advisor":"关于你那篇论文的作者排序，我想了一下。一作给你，但通讯作者必须是我。另外要把某某老师也加上，他那边有资源。","min_stress":25,"max_stress":65,"options":[
        {"text":"好的导师，要不把实验室的打印机也列为作者？它贡献也不小。","style":STYLE_FUNNY,"stress":5},
        {"text":"好的导师，按您说的来。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，某某老师对这篇论文没有实质性贡献，加上不合适。","style":STYLE_REBEL,"stress":25}]},
    # 73 - 导师画饼现场
    {"id":"special_6","advisor":"等这个项目结题了，我带你出去开个顶会，顺便旅旅游。我认识那边几个大佬，给你引荐引荐。","min_stress":15,"max_stress":50,"options":[
        {"text":"导师，您上次也是这么说的，后来我去了隔壁城市的'顶会'——学校的学术报告厅。","style":STYLE_FUNNY,"stress":10},
        {"text":"太好了导师！我会好好准备的。","style":STYLE_OBEY,"stress":-10},
        {"text":"导师，希望这次是真的，不要又只是说说而已。","style":STYLE_REBEL,"stress":15}]},
    # 74 - 导师的祝福
    {"id":"special_7","advisor":"今天是你的生日吧？生日快乐。不过生日不重要，实验数据才重要。去吧，别浪费时间。","min_stress":5,"max_stress":45,"options":[
        {"text":"谢谢导师！这是我收到过最'温暖'的生日祝福。","style":STYLE_FUNNY,"stress":5},
        {"text":"谢谢导师！我会好好做实验的。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，生日一年就一次，今天我能不能早点走？","style":STYLE_REBEL,"stress":10}]},
    # 75 - 导师的学术八卦
    {"id":"special_8","advisor":"你听说没？某某课题组的那个博士退学了。做了五年什么都没做出来。你可别步他的后尘。","min_stress":20,"max_stress":60,"options":[
        {"text":"导师，我听了这故事压力更大了，您是故意的吧？","style":STYLE_FUNNY,"stress":10},
        {"text":"我不会让这种事情发生的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，用别人的失败来吓唬学生不太合适。","style":STYLE_REBEL,"stress":20}]},

    # ==================== 生活类对话 ====================
    # 76
    {"id":"life_1","advisor":"你怎么又点外卖？天天吃外卖对身体不好。实验室有微波炉，自己做饭带过来。","min_stress":10,"max_stress":50,"options":[
        {"text":"导师，我做饭的时间都用来做实验了，这是'最优时间分配'。","style":STYLE_FUNNY,"stress":5},
        {"text":"导师说得对，我会注意饮食健康的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，如果实验时间不那么长，我确实有时间自己做饭。","style":STYLE_REBEL,"stress":15}]},
    # 77
    {"id":"life_2","advisor":"你有女朋友了吗？没有就对了，读博期间谈恋爱太分心。等毕业了再找。","min_stress":15,"max_stress":50,"options":[
        {"text":"导师，我女朋友是'科研'，她已经把我所有时间都占了。","style":STYLE_FUNNY,"stress":0},
        {"text":"导师说得对，我现在确实应该专注学业。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，个人生活是我的隐私，而且恋爱不影响科研。","style":STYLE_REBEL,"stress":15}]},
    # 78
    {"id":"life_3","advisor":"你看看你这个黑眼圈，又熬夜了吧？搞科研要有规律，别把自己身体搞垮了。","min_stress":10,"max_stress":45,"options":[
        {"text":"导师，您一边让我赶进度一边让我早睡，这道题我不会做。","style":STYLE_FUNNY,"stress":5},
        {"text":"谢谢导师关心，我会注意作息的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，我的黑眼圈跟您布置的工作量成正比。","style":STYLE_REBEL,"stress":15}]},
    # 79
    {"id":"life_4","advisor":"你头发是不是越来越少了？做科研就是这样，聪明绝顶嘛。习惯就好。","min_stress":15,"max_stress":50,"options":[
        {"text":"导师，我准备把掉下来的头发收集起来，毕业时送给您当纪念。","style":STYLE_FUNNY,"stress":0},
        {"text":"是的导师，但我觉得值得。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，掉头发不是因为聪明，是因为压力和焦虑。","style":STYLE_REBEL,"stress":20}]},
    # 80 - 导师请吃饭
    {"id":"life_5","advisor":"今天中午我请实验室吃饭。去食堂，想吃什么随便点。","min_stress":5,"max_stress":35,"options":[
        {"text":"导师，食堂的'随便点'总金额不超过30块，谢谢您！","style":STYLE_FUNNY,"stress":-5},
        {"text":"谢谢导师！","style":STYLE_OBEY,"stress":-10},
        {"text":"谢谢导师，不过食堂就不用了，您能在课题上多给些指导就好。","style":STYLE_REBEL,"stress":5}]},

    # ==================== 更极端的高压对话 ====================
    # 81
    {"id":"high_18","advisor":"我跟你说，这个月你的实验结果直接决定我明年招不招学生。你要是做不出来，后面师弟师妹都没了。","min_stress":60,"max_stress":90,"options":[
        {"text":"导师，原来我肩负着整个实验室的存亡？这压力够我写十篇Nature了。","style":STYLE_FUNNY,"stress":15},
        {"text":"我一定不会辜负大家的期望。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，招生问题不应该转嫁到学生身上。","style":STYLE_REBEL,"stress":30}]},
    # 82
    {"id":"high_19","advisor":"你最近有没有看学院的政策？博士资格考核不过的话，直接劝退。你自己去查查自己的条件够不够。","min_stress":60,"max_stress":90,"options":[
        {"text":"导师，查了之后万一发现不够，我是不是可以直接收拾行李了？","style":STYLE_FUNNY,"stress":20},
        {"text":"我会认真准备的，一定通过考核。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，考核标准应该公开透明，不是用来威胁学生的工具。","style":STYLE_REBEL,"stress":30}]},
    # 83
    {"id":"high_20","advisor":"你那篇论文我发给合作者看了，他说我们的方法不如他的好。你重新设计一下实验方案。","min_stress":60,"max_stress":90,"options":[
        {"text":"导师，合作者是不是就是审稿人？这个套路我懂的。","style":STYLE_FUNNY,"stress":10},
        {"text":"好的导师，我重新设计。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，合作者的意见应该有详细的技术理由，不能一句话就否定。","style":STYLE_REBEL,"stress":25}]},

    # ==================== 补充开场/中期 ====================
    # 84
    {"id":"intro_15","advisor":"新来的师弟你先带一带，教他做实验。他基础不太好，你多花点时间。","min_stress":10,"max_stress":40,"options":[
        {"text":"好的导师，我顺便教他如何在压力下保持微笑。","style":STYLE_FUNNY,"stress":0},
        {"text":"好的导师，我会好好带他的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，带新人会占用我大量时间，能不能算作助教工作量？","style":STYLE_REBEL,"stress":15}]},
    # 85
    {"id":"intro_16","advisor":"你有没有兴趣做实验室的安全管理员？虽然没什么报酬，但是个锻炼的机会。","min_stress":10,"max_stress":40,"options":[
        {"text":"导师，我每天在实验室的时间已经够'安全'了——24小时都在。","style":STYLE_FUNNY,"stress":5},
        {"text":"好的导师，我愿意为实验室做贡献。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，安全管理员责任重大，应该由有报酬的专职人员担任。","style":STYLE_REBEL,"stress":10}]},
    # 86
    {"id":"mid_22","advisor":"我打算申请一个大的重点项目，需要你的方向作为支撑。你把你这部分的研究计划写得漂亮一点。","min_stress":25,"max_stress":55,"options":[
        {"text":"导师，您放心，我写研究计划的能力比写论文强多了。","style":STYLE_FUNNY,"stress":0},
        {"text":"好的导师，我一定全力以赴。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，写基金申请书是您的工作，我可以提供技术支持但不能代笔。","style":STYLE_REBEL,"stress":20}]},
    # 87
    {"id":"mid_23","advisor":"你那个模型跑出来的数据怎么这么奇怪？你是不是调参的时候随便调的？","min_stress":30,"max_stress":60,"options":[
        {"text":"导师，参数不是随便调的，我是用'随机漫步'的方法调出来的。","style":STYLE_FUNNY,"stress":5},
        {"text":"我重新调整参数再跑。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，模型本身的设计有问题，不是调参能解决的。","style":STYLE_REBEL,"stress":20}]},
    # 88
    {"id":"mid_24","advisor":"下一届的助教名额我帮你要了一个。你去给本科生上几节课，锻炼一下表达能力。","min_stress":25,"max_stress":55,"options":[
        {"text":"导师，我怕本科生问我问题，我回答不出来会暴露水平。","style":STYLE_FUNNY,"stress":5},
        {"text":"谢谢导师，这对我是很好的锻炼。","style":STYLE_OBEY,"stress":-10},
        {"text":"导师，我现在的研究任务已经很重了，再加助教我怕两边都做不好。","style":STYLE_REBEL,"stress":15}]},
    # 89
    {"id":"mid_25","advisor":"你的reference格式全错了。这种低级错误都能犯，你到底认真不认真？","min_stress":30,"max_stress":60,"options":[
        {"text":"导师，参考文献格式是最难的部分，比做实验还难。","style":STYLE_FUNNY,"stress":5},
        {"text":"对不起导师，我会用EndNote重新整理的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，格式问题可以用软件自动处理，科研的核心是内容。","style":STYLE_REBEL,"stress":15}]},

    # ==================== 补充高压/极高 ====================
    # 90
    {"id":"high_21","advisor":"我跟你实话实说吧，你现在的进度，正常毕业是来不及了。你得做好心理准备。","min_stress":65,"max_stress":95,"options":[
        {"text":"导师，心理准备我早就做好了——就是没准备能正常毕业。","style":STYLE_FUNNY,"stress":15},
        {"text":"导师，我会加倍努力赶上的。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，如果延期是因为您给的方向有问题，这个责任不应该我来承担。","style":STYLE_REBEL,"stress":35}]},
    # 91
    {"id":"high_22","advisor":"学院领导对我有意见，说你作为我的学生成果太少。你能不能争点气？","min_stress":60,"max_stress":90,"options":[
        {"text":"导师，要不然我去跟领导说我不是您学生？这样就不丢您的脸了。","style":STYLE_FUNNY,"stress":15},
        {"text":"对不起导师，我会尽快出成果的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，学院领导不应该以论文数量来评判一个博士生。","style":STYLE_REBEL,"stress":25}]},
    # 92
    {"id":"critical_16","advisor":"我最后问你一次：你到底还想不想读？想读就好好做，不想读就趁早走人。别浪费彼此的时间。","min_stress":85,"max_stress":100,"options":[
        {"text":"导师，我先不说想不想读，我就想知道走人的话有没有遣散费？","style":STYLE_FUNNY,"stress":25},
        {"text":"我想读，导师请再给我一次机会。","style":STYLE_OBEY,"stress":5},
        {"text":"导师，您的问题本身就带有胁迫性质，我需要冷静地考虑。","style":STYLE_REBEL,"stress":40}]},
    # 93
    {"id":"critical_17","advisor":"行了，你出去吧。好好想想我说的话。想好了再来找我。","min_stress":85,"max_stress":100,"options":[
        {"text":"好的导师，我去走廊里站一会儿冷静一下...或者直接去天台？","style":STYLE_FUNNY,"stress":25},
        {"text":"好的导师，我会好好反省。","style":STYLE_OBEY,"stress":5},
        {"text":"导师，我需要的不只是'好好想想'，我需要具体的指导和支持。","style":STYLE_REBEL,"stress":35}]},

    # ==================== 终极对话补充 ====================
    # 94
    {"id":"misc_1","advisor":"你上次借的实验室钥匙什么时候还？一个人占着钥匙别人怎么用？","min_stress":5,"max_stress":45,"options":[
        {"text":"导师，钥匙就是我对实验室忠诚的象征，我24小时待命。","style":STYLE_FUNNY,"stress":0},
        {"text":"好的导师，我马上去配一把备用然后归还。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，我占着钥匙是因为我每天来得最早走得最晚。","style":STYLE_REBEL,"stress":10}]},
    # 95
    {"id":"misc_2","advisor":"你懂不懂什么叫'创新'？你所有的方法都是别人做过的，没有任何新意。","min_stress":35,"max_stress":65,"options":[
        {"text":"导师，创新太难了，要不我们做'创旧'——把旧方法用出新高度？","style":STYLE_FUNNY,"stress":10},
        {"text":"导师说得对，我会努力寻找创新点的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，大多数好的科研都是站在巨人的肩膀上做微小改进。","style":STYLE_REBEL,"stress":15}]},
    # 96
    {"id":"misc_3","advisor":"我跟你说，学术圈很小。你要是得罪了我，以后在这一行很难混下去。","min_stress":70,"max_stress":100,"options":[
        {"text":"导师，幸好我已经做好了转行送外卖的心理准备。","style":STYLE_FUNNY,"stress":20},
        {"text":"导师，我绝对不会得罪您的。","style":STYLE_OBEY,"stress":0},
        {"text":"导师，用职业前途来威胁学生，这本身就是学术不端行为。","style":STYLE_REBEL,"stress":40}]},
    # 97
    {"id":"misc_4","advisor":"我帮你联系了一个国外的访学机会，不过要自费一部分。你自己看看能不能承受。","min_stress":30,"max_stress":65,"options":[
        {"text":"导师，我的存款余额显示：您这是在跟我开玩笑。","style":STYLE_FUNNY,"stress":10},
        {"text":"谢谢导师，我去想办筹钱。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，自费访学对很多学生来说是不现实的。","style":STYLE_REBEL,"stress":20}]},
    # 98
    {"id":"misc_5","advisor":"你这篇论文被拒了三次了吧？你有没有认真反思过为什么？","min_stress":50,"max_stress":85,"options":[
        {"text":"导师，可能是审稿人联合起来针对我。我建议我们上诉到Nature总部。","style":STYLE_FUNNY,"stress":10},
        {"text":"我会仔细看审稿意见然后认真修改的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，论文被拒很正常，很多诺奖得主也被拒过多次。","style":STYLE_REBEL,"stress":15}]},
    # 99
    {"id":"misc_6","advisor":"你是我带过最差的一届...哦不，你是我带过最让人操心的学生。","min_stress":55,"max_stress":90,"options":[
        {"text":"导师，这个'荣誉'我会记在简历里的。","style":STYLE_FUNNY,"stress":15},
        {"text":"对不起导师，我会努力让您省心的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，每个学生都是不同的，不应该用统一标准来衡量。","style":STYLE_REBEL,"stress":25}]},
    # 100
    {"id":"misc_7","advisor":"今天就这样吧。我希望下次见到你的时候，你已经有所进步了。","min_stress":10,"max_stress":50,"options":[
        {"text":"导师，下次见面我会带一份进步报告——可能只有一行字。","style":STYLE_FUNNY,"stress":5},
        {"text":"好的导师，我不会让您失望的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，进步需要时间和正确的引导，不是一句口号。","style":STYLE_REBEL,"stress":15}]},

    # ==================== 最后一批补充 ====================
    # 101 - 论文被要求加引用
    {"id":"extra_1","advisor":"审稿人让你引用他的几篇论文。你就加上吧，反正也没什么损失，这叫审稿人友好策略。","min_stress":20,"max_stress":60,"options":[
        {"text":"好的导师，我下次投稿前先猜审稿人是谁，提前引用他的全部论文。","style":STYLE_FUNNY,"stress":5},
        {"text":"好的导师，我这就加上。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，这种强制引用是不合理的，应该向编辑反映。","style":STYLE_REBEL,"stress":20}]},
    # 102 - 导师让学生帮写推荐信
    {"id":"extra_2","advisor":"我最近在申请一个人才项目，需要推荐信。你帮我起草一封吧，以合作者的视角来写。","min_stress":25,"max_stress":60,"options":[
        {"text":"导师，我写推荐信夸您的话，算不算学术不端？","style":STYLE_FUNNY,"stress":10},
        {"text":"好的导师，您真是太优秀了，值得我好好写。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，推荐信应该由推荐人亲自写，我不能代笔。","style":STYLE_REBEL,"stress":25}]},
    # 103 - 学习压力
    {"id":"extra_3","advisor":"你是不是又在刷手机？我每次路过你工位都看到你在看屏幕，不是在写代码就是在看文献吧？...最好是这样。","min_stress":15,"max_stress":50,"options":[
        {"text":"导师，我在查文献，只不过这个文献恰好是知乎。","style":STYLE_FUNNY,"stress":10},
        {"text":"是的导师，我一直在工作。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，偶尔休息一下是正常的，您不必时刻监视我。","style":STYLE_REBEL,"stress":20}]},
    # 104 - 导师PUA升级
    {"id":"extra_4","advisor":"你真应该感谢我收了你。换成别的导师，就你这个进度，早被劝退了。","min_stress":50,"max_stress":85,"options":[
        {"text":"谢谢导师不杀之恩！您是我遇到过最好的老板，虽然我也只遇到过您一个老板。","style":STYLE_FUNNY,"stress":10},
        {"text":"谢谢导师，我非常感激您的栽培。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，导师和学生是双向选择，不是施舍关系。","style":STYLE_REBEL,"stress":30}]},
    # 105 - 导师甩锅
    {"id":"extra_5","advisor":"这个项目的deadline提前了，甲方那边的意思。没办法，只能辛苦你加加班了。","min_stress":35,"max_stress":70,"options":[
        {"text":"导师，我怀疑甲方是不是觉得我太闲了，故意整我？","style":STYLE_FUNNY,"stress":10},
        {"text":"好的导师，我加班赶。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，工期变更应该有正式的变更通知和相应的资源支持。","style":STYLE_REBEL,"stress":20}]},
    # 106 - 导师质疑能力
    {"id":"extra_6","advisor":"你是不是觉得读博就是混个学位？我告诉你，博士学位不是混出来的，是真刀真枪干出来的。","min_stress":45,"max_stress":80,"options":[
        {"text":"导师，我要是混学位就不会选您当导师了，我傻吗？","style":STYLE_FUNNY,"stress":15},
        {"text":"导师说得对，我会认真对待的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，我的态度一直很认真，请不要随便质疑。","style":STYLE_REBEL,"stress":25}]},
    # 107 - 毕业遥遥无期
    {"id":"extra_7","advisor":"我算了一下你的工作量，按照现在的速度，你可能要读六年。你自己能接受吗？","min_stress":60,"max_stress":95,"options":[
        {"text":"六年？导师，到时候我都三十了，要不直接读个博士后算了？","style":STYLE_FUNNY,"stress":15},
        {"text":"导师，我会想办法提速的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，如果您的安排合理，我本不应需要六年。","style":STYLE_REBEL,"stress":30}]},
    # 108 - 终极威胁
    {"id":"extra_8","advisor":"如果你下个学期还是没有像样的产出，我只能建议你转导师或者退学了。这不是威胁，是客观事实。","min_stress":75,"max_stress":100,"options":[
        {"text":"导师，'不是威胁'这句话本身就是一个威胁，就像'不是我吹牛'一样。","style":STYLE_FUNNY,"stress":20},
        {"text":"导师，请再给我最后一个学期。","style":STYLE_OBEY,"stress":5},
        {"text":"导师，如果您真的为我好，应该帮助我解决问题而不是下最后通牒。","style":STYLE_REBEL,"stress":40}]},
    # 109
    {"id":"extra_9","advisor":"你把最近三个月的实验数据整理一下，我要做一个综合评估。如果数据太差，我们要重新考虑整个方向了。","min_stress":40,"max_stress":75,"options":[
        {"text":"导师，三个月的实验数据...我可以帮您总结成一句话：不太妙。","style":STYLE_FUNNY,"stress":10},
        {"text":"好的导师，我会认真整理的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，综合评估应该由我们共同讨论，而不是您单方面判断。","style":STYLE_REBEL,"stress":20}]},
    # 110
    {"id":"extra_10","advisor":"明天有个企业合作方来实验室参观，你负责演示一下我们的成果。记住，要扬长避短，不好的地方别提。","min_stress":20,"max_stress":55,"options":[
        {"text":"导师，如果扬长避短，那基本上就不用演示了——没有'长'。","style":STYLE_FUNNY,"stress":10},
        {"text":"好的导师，我会好好准备的。","style":STYLE_OBEY,"stress":-5},
        {"text":"导师，科研展示应该实事求是，不能误导合作方。","style":STYLE_REBEL,"stress":20}]},
]

# 游戏结束嘲讽语句
GAME_OVER_MESSAGES = [
    "你还得再沉淀沉淀。",
    "科研这条路不适合所有人。",
    "要不考虑一下转行？送外卖也挺好的。",
    "你的压力值已经爆表了，回去休息吧。",
    "导师表示：这届学生不行啊。",
    "Nature编辑部发来贺电：感谢你没有投稿。",
    "你的博士学位正在以肉眼可见的速度远离你。",
    "连导师的画饼都消化不了，怎么消化科研的苦？",
    "游戏结束。现实比这更残酷哦~",
    "你已解锁成就：【被导师劝退的博士生】",
    "压力山大！建议去操场跑十圈冷静一下。",
    "恭喜你，荣获本届'最崩溃博士生'称号！",
    "导师已经把门打开了，请开始你的表演。",
    "你的博士生涯进度条：▰▰▰▰▰▰▰▰▰▰ 100% ...哦不，是压力条满了。",
]

# 导师表达满意时的过渡语
ADVISOR_COMPLIMENTS = [
    "嗯，这还差不多。",
    "行吧，这次就这样。",
    "算你有点悟性。",
    "知道努力就好。",
    "继续加油吧。",
]

# 开场白
INTRO_TEXT = [
    "又是一个普通的周一早晨...",
    "你推开导师办公室的门...",
    "导师正坐在他那张看起来比你年龄还大的办公桌后面...",
    "他抬起头，镜片后面的眼睛闪烁着诡异的光芒...",
    "你知道，一场'愉快'的对话即将开始...",
]

# 标题
TITLE_TEXT = "Dogtor"
SUBTITLE_TEXT = "博士生生存模拟器"
