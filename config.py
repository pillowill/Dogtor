"""
Dogtor v3.0 - 像素风博士生与导师对话游戏
重构版：场景系统 + 故事线 + 时间压力 + 人格选择 + 知识问答
"""
import random
import math

# 窗口设置
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FPS = 60

TILE_SIZE = 16

# ==================== 颜色方案 ====================
class Colors:
    DARK_BG = (22, 22, 34)
    DARKER_BG = (14, 14, 24)
    PANEL_BG = (30, 30, 46)
    BORDER = (70, 70, 100)
    BORDER_LIGHT = (110, 110, 150)
    
    TEXT_WHITE = (220, 220, 240)
    TEXT_GRAY = (140, 140, 160)
    TEXT_DARK = (100, 100, 120)
    TEXT_YELLOW = (255, 220, 80)
    TEXT_RED = (255, 70, 70)
    
    BTN_IDLE = (40, 40, 60)
    BTN_HOVER = (55, 55, 80)
    BTN_SELECTED = (70, 70, 100)
    BTN_TEXT = (200, 200, 220)
    BTN_HOVER_TEXT = (255, 255, 255)
    
    STRESS_BG = (35, 35, 55)
    STRESS_LOW = (80, 200, 80)
    STRESS_MED = (220, 200, 40)
    STRESS_HIGH = (240, 120, 40)
    STRESS_CRIT = (240, 40, 40)
    STRESS_BORDER = (90, 90, 130)
    
    ADVISOR_SKIN = (230, 200, 170)
    ADVISOR_SUIT = (60, 55, 80)
    ADVISOR_TIE = (140, 40, 40)
    ADVISOR_GLASSES = (50, 50, 50)
    
    PLAYER_SKIN = (220, 190, 160)
    PLAYER_SHIRT = (70, 100, 160)
    PLAYER_HAIR = (40, 35, 30)
    
    DESK = (100, 70, 50)
    CHAIR = (60, 45, 35)
    WALL = (60, 55, 75)
    FLOOR = (100, 85, 70)
    WINDOW_LIGHT = (180, 200, 230)
    
    GLITCH_GREEN = (80, 255, 80)

# ==================== 字体 ====================
FONT_SIZE_SMALL = 15
FONT_SIZE_NORMAL = 19
FONT_SIZE_LARGE = 26
FONT_SIZE_TITLE = 44
FONT_SIZE_HUGE = 60

# ==================== 压力与时间系统 ====================
MAX_STRESS = 100
INITIAL_STRESS = 15
# 时间压力：压力增量 = base * (秒数^EXPONENT) / DIVISOR
TIME_PRESSURE_BASE = 0.3       # 基础倍率
TIME_PRESSURE_EXPONENT = 2.0   # 指数（平方增长）
TIME_PRESSURE_DIVISOR = 1.0    # 除数
TIME_PRESSURE_INTERVAL = 0.5   # 每0.5秒检查一次
MAX_CHOICE_TIME = 15.0         # 15秒后自动随机选择

# ==================== UI布局 ====================
# 场景区域 (上半部分)
SCENE_X = 0
SCENE_Y = 0
SCENE_WIDTH = SCREEN_WIDTH
SCENE_HEIGHT = 420

# 对话框区域 (下半部分)
DIALOG_BOX_X = 40
DIALOG_BOX_Y = 430
DIALOG_BOX_WIDTH = 944
DIALOG_BOX_HEIGHT = 140

# 选项区域
CHOICE_START_Y = 585
CHOICE_BUTTON_WIDTH = 290
CHOICE_BUTTON_HEIGHT = 70
CHOICE_BUTTON_GAP = 18
CHOICE_START_X = 40

# 压力条
STRESS_BAR_X = 40
STRESS_BAR_Y = 670
STRESS_BAR_WIDTH = 400
STRESS_BAR_HEIGHT = 20

# 计时器
TIMER_X = SCREEN_WIDTH - 200
TIMER_Y = DIALOG_BOX_Y + 10

# ==================== 场景定义 ====================
SCENE_OFFICE = "office"         # 导师办公室
SCENE_LAB = "lab"               # 实验室
SCENE_HALLWAY = "hallway"       # 走廊
SCENE_MEETING = "meeting"       # 组会
SCENE_NIGHT = "night"           # 深夜办公室

# ==================== 游戏状态 ====================
STATE_TITLE = "title"
STATE_PLAYING = "playing"
STATE_GAME_OVER = "game_over"
STATE_INTRO = "intro"
STATE_ARC_TRANSITION = "arc_transition"

# ==================== 故事弧名称 ====================
ARC_NAMES = {
    "first_meeting": "初次交锋",
    "empty_promises": "画饼充饥",
    "paper_hell": "论文生死线",
    "direction_conflict": "方向之争",
    "final_ultimatum": "最终通牒",
}

# ==================== 人格系统 (v3) ====================
STATE_PERSONALITY = "personality"

PERSONALITY_TYPES = {
    "obedient": {
        "name": "听话型",
        "desc": "导师说什么就做什么，\n信奉「听话出活」的生存哲学。\n压力增长慢，但容易被安排杂活。",
        "stress_mult": 0.8,     # 压力增长系数
        "bonus_text": "导师对你的信任度 +10%",
        "color": (80, 200, 120),
    },
    "innovative": {
        "name": "创新型",
        "desc": "有自己的想法和主见，\n敢在组会上提出不同方案。\n平衡型，中庸之道。",
        "stress_mult": 1.0,
        "bonus_text": "研究方向自主权 +20%",
        "color": (100, 180, 220),
    },
    "rebellious": {
        "name": "反叛型",
        "desc": "看不惯导师画饼就怼回去，\n不信权威只信实验结果。\n压力增长快，但可能触发隐藏剧情。",
        "stress_mult": 1.3,
        "bonus_text": "隐藏剧情触发率 +30%",
        "color": (220, 120, 80),
    },
}

# ==================== 知识问答系统 (v3) ====================
QUIZ_STRESS_CORRECT = -8     # 答对减压
QUIZ_STRESS_WRONG = 25       # 答错大幅增压
QUIZ_TIME_PENALTY = 15       # 超时额外惩罚

# ==================== 同门反馈 (v3) ====================
PEER_REACTIONS = {
    "praise": [
        "同门们纷纷点头，窃窃私语：'说得有道理啊...'",
        "旁边的师弟悄悄给了你一个大拇指。",
        "师姐投来赞许的目光，嘴角微微上扬。",
    ],
    "silence": [
        "会议室里寂静无声，所有人都低着头不敢说话。",
        "同门们面面相觑，空气仿佛凝固了。",
        "一阵尴尬的沉默笼罩了整间办公室。",
    ],
    "murmur": [
        "后排传来低语：'导师今天火气好大...'",
        "师弟偷偷在手机上打字，屏幕一闪：'挺住兄弟'",
        "几个同门用教科书挡住脸，肩膀微微发抖。",
    ],
    "shock": [
        "全场倒吸一口冷气，有人手里的笔都掉在了地上。",
        "一个同门嘴里的水差点喷出来，赶紧假装咳嗽。",
        "对面的博士生张大了嘴巴，眼镜从鼻梁上滑了下来。",
    ],
}

# ==================== 辅助函数 ====================
def shuffle_options(options):
    """打乱选项顺序"""
    shuffled = options[:]
    random.shuffle(shuffled)
    return shuffled
