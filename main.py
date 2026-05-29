"""
Dogtor - 像素风博士生与导师对话游戏
主游戏引擎 - v3.0
场景系统 + 故事线 + 时间压力 + 像素艺术 + 人格选择 + 知识问答
"""
import pygame
import random
import sys
import math
import time
import os
from config import *
from story_data import *

# ==================== Pygame 初始化 ====================
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dogtor - 博士生生存模拟器")
clock = pygame.time.Clock()

# ==================== 字体加载 ====================
import traceback

def _try_load_font(path, size):
    """Try to load a font file, return pygame Font or None."""
    try:
        # Normalize path for Windows
        path = os.path.normpath(path)
        if os.path.exists(path):
            return pygame.font.Font(path, size)
    except Exception:
        pass
    return None

def _resolve_font_path(font_name="simhei.ttf"):
    """Find font file with exhaustive fallback paths."""
    candidates = []
    
    # 1. PyInstaller bundle path
    if getattr(sys, 'frozen', False):
        try:
            candidates.append(os.path.join(sys._MEIPASS, font_name))
        except Exception:
            pass
    
    # 2. Same directory as the exe (for portable deployment)
    try:
        exe_dir = os.path.dirname(sys.executable)
        candidates.append(os.path.join(exe_dir, font_name))
    except Exception:
        pass
    
    # 3. Same directory as this script
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        candidates.append(os.path.join(script_dir, font_name))
    except Exception:
        pass
    
    # 4. Current working directory
    candidates.append(os.path.join(os.getcwd(), font_name))
    
    # 5. Windows Fonts directory with multiple Chinese fonts
    windir = os.environ.get('WINDIR', 'C:\\Windows')
    chinese_fonts = [
        'simhei.ttf', 'SimHei.ttf', 'SIMHEI.TTF',
        'msyh.ttc', 'msyhbd.ttc',       # Microsoft YaHei
        'simsun.ttc', 'SimSun.ttc',      # SimSun
        'simkai.ttf', 'SimKai.ttf',      # KaiTi
        'FZSTK.TTF',                     # FangSong
    ]
    for cf in chinese_fonts:
        candidates.append(os.path.join(windir, 'Fonts', cf))
        candidates.append('C:\\Windows\\Fonts\\' + cf)
    
    # 6. Try all candidates and return first found
    for p in candidates:
        if os.path.exists(p):
            return os.path.normpath(p)
    
    return None

# Load fonts with multiple strategies
FONT_PATH = _resolve_font_path()
FONT_LOADED = False

if FONT_PATH is None:
    # Last resort: try pygame's built-in SysFont
    try:
        test_font = pygame.font.SysFont("simhei", 20, bold=False)
        if test_font:
            # SysFont can't be used with custom path; use as fallback
            _sysfont_name = "simhei"
            FONT_LOADED = True
    except Exception:
        _sysfont_name = None
else:
    _sysfont_name = None

try:
    if FONT_PATH:
        font_title = pygame.font.Font(FONT_PATH, FONT_SIZE_TITLE)
        font_large = pygame.font.Font(FONT_PATH, FONT_SIZE_LARGE)
        font_normal = pygame.font.Font(FONT_PATH, FONT_SIZE_NORMAL)
        font_small = pygame.font.Font(FONT_PATH, FONT_SIZE_SMALL)
        font_huge = pygame.font.Font(FONT_PATH, FONT_SIZE_HUGE)
        FONT_LOADED = True
    elif _sysfont_name:
        font_title = pygame.font.SysFont(_sysfont_name, FONT_SIZE_TITLE)
        font_large = pygame.font.SysFont(_sysfont_name, FONT_SIZE_LARGE)
        font_normal = pygame.font.SysFont(_sysfont_name, FONT_SIZE_NORMAL)
        font_small = pygame.font.SysFont(_sysfont_name, FONT_SIZE_SMALL)
        font_huge = pygame.font.SysFont(_sysfont_name, FONT_SIZE_HUGE)
        FONT_PATH = _sysfont_name  # Mark as using sysfont
    else:
        raise FileNotFoundError("No Chinese font available")
except Exception as e:
    # Silent fallback - in windowed mode print goes nowhere
    # Write error to temp file for debugging
    try:
        with open(os.path.join(os.environ.get('TEMP', '.'), 'dogtor_font_error.log'), 'w', encoding='utf-8') as f:
            f.write(f"Font loading failed: {e}\n")
            f.write(f"FONT_PATH: {FONT_PATH}\n")
            f.write(f"sys.frozen: {getattr(sys, 'frozen', False)}\n")
            f.write(f"sys._MEIPASS: {getattr(sys, '_MEIPASS', 'N/A')}\n")
            traceback.print_exc(file=f)
    except:
        pass
    
    # Last resort: try to find ANY Chinese-capable system font
    _fallback_font = None
    _fallback_paths = [
        'C:\\Windows\\Fonts\\msyh.ttc',
        'C:\\Windows\\Fonts\\simhei.ttf',
        'C:\\Windows\\Fonts\\simsun.ttc',
        'C:\\Windows\\Fonts\\simkai.ttf',
    ]
    for _fp in _fallback_paths:
        if os.path.exists(_fp):
            try:
                _fallback_font = _fp
                break
            except:
                pass
    
    if _fallback_font:
        font_title = pygame.font.Font(_fallback_font, FONT_SIZE_TITLE)
        font_large = pygame.font.Font(_fallback_font, FONT_SIZE_LARGE)
        font_normal = pygame.font.Font(_fallback_font, FONT_SIZE_NORMAL)
        font_small = pygame.font.Font(_fallback_font, FONT_SIZE_SMALL)
        font_huge = pygame.font.Font(_fallback_font, FONT_SIZE_HUGE)
        FONT_PATH = _fallback_font
        FONT_LOADED = True
    else:
        font_title = pygame.font.Font(None, FONT_SIZE_TITLE)
        font_large = pygame.font.Font(None, FONT_SIZE_LARGE)
        font_normal = pygame.font.Font(None, FONT_SIZE_NORMAL)
        font_small = pygame.font.Font(None, FONT_SIZE_SMALL)
        font_huge = pygame.font.Font(None, FONT_SIZE_HUGE)
        FONT_LOADED = False

# ==================== 字体自检 ====================
def _font_self_check():
        """Verify font rendering works at startup. Writes log if issues found."""
        font_path = _resolve_font_path()
        if font_path:
            try:
                test_font = pygame.font.Font(font_path, 20)
                test_surf = test_font.render("测试中文 Test", True, (255, 255, 255))
                return True
            except Exception as e:
                try:
                    with open(os.path.join(os.environ.get('TEMP', '.'), 'dogtor_font_error.log'), 'w', encoding='utf-8') as f:
                        f.write(f"Font self-check failed\npath={font_path}\nerror={e}\n")
                        traceback.print_exc(file=f)
                except:
                    pass
        else:
            try:
                with open(os.path.join(os.environ.get('TEMP', '.'), 'dogtor_font_error.log'), 'w', encoding='utf-8') as f:
                    f.write("Font self-check: no font path resolved\n")
                    f.write(f"sys.frozen: {getattr(sys, 'frozen', False)}\n")
                    f.write(f"sys._MEIPASS: {getattr(sys, '_MEIPASS', 'N/A')}\n")
                    f.write(f"cwd: {os.getcwd()}\n")
                    f.write(f"exe_dir: {os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else 'N/A'}\n")
                    # List bundled files
                    try:
                        for fn in os.listdir(getattr(sys, '_MEIPASS', '.')):
                            f.write(f"  bundled: {fn}\n")
                    except:
                        pass
            except:
                pass
        return False

_font_check_ok = _font_self_check()

def get_font(size):
    """Return a pygame Font with the requested size."""
    global FONT_PATH
    if FONT_PATH is None:
        FONT_PATH = _resolve_font_path()
    if FONT_PATH and not isinstance(FONT_PATH, str):
        FONT_PATH = _resolve_font_path()
    if FONT_PATH and FONT_PATH != "simhei":
        try:
            return pygame.font.Font(FONT_PATH, size)
        except Exception:
            pass
    # Fallback: try system Chinese fonts
    for sysfont in ['C:\\Windows\\Fonts\\msyh.ttc', 'C:\\Windows\\Fonts\\simhei.ttf',
                     'C:\\Windows\\Fonts\\simsun.ttc', 'C:\\Windows\\Fonts\\simkai.ttf']:
        if os.path.exists(sysfont):
            try:
                return pygame.font.Font(sysfont, size)
            except:
                pass
    # Absolute last resort
    return pygame.font.Font(None, size)

# ==================== 场景渲染函数 ====================

def draw_pixel_character(surf, x, y, skin_color, shirt_color, hair_color, 
                         suit_color=None, tie_color=None, glasses_color=None,
                         scale=1.0, head_tilt=0):
    """绘制像素风角色"""
    s = int(4 * scale)
    hx = x
    hy = y
    
    # 头部 (带倾斜)
    head_offset = int(head_tilt * 2)
    pygame.draw.rect(surf, skin_color, (hx - s + head_offset, hy - s * 3, s * 2, s * 2))
    
    # 头发
    if hair_color:
        pygame.draw.rect(surf, hair_color, (hx - s + head_offset, hy - s * 3, s * 2, s))
    
    # 眼镜
    if glasses_color:
        glass_y = hy - s * 2
        pygame.draw.rect(surf, glasses_color, (hx - s + 1 + head_offset, glass_y, s - 1, s - 1), 1)
        pygame.draw.rect(surf, glasses_color, (hx + 1 + head_offset, glass_y, s - 1, s - 1), 1)
    
    # 身体
    body_top = hy - s
    if suit_color:
        pygame.draw.rect(surf, suit_color, (hx - s, body_top, s * 2, s * 3))
        # 领带
        if tie_color:
            tie_w = max(1, s // 2)
            pygame.draw.rect(surf, tie_color, (hx - tie_w // 2, body_top + s, tie_w, s * 2))
    elif shirt_color:
        pygame.draw.rect(surf, shirt_color, (hx - s, body_top, s * 2, s * 3))
    
    # 手臂
    arm_color = skin_color
    pygame.draw.rect(surf, arm_color, (hx - s - s // 2, body_top + s // 2, s // 2, s * 2))
    pygame.draw.rect(surf, arm_color, (hx + s, body_top + s // 2, s // 2, s * 2))


def draw_office_scene(surf, is_night=False):
    """绘制办公室场景"""
    w, h = SCREEN_WIDTH, SCENE_HEIGHT
    
    if is_night:
        # 深夜：暗色调
        bg_color = Colors.DARKER_BG
        wall_color = (30, 28, 38)
        floor_color = (50, 42, 35)
        window_light = (40, 50, 80)
        lamp_glow = True
    else:
        bg_color = Colors.DARK_BG
        wall_color = Colors.WALL
        floor_color = Colors.FLOOR
        window_light = Colors.WINDOW_LIGHT
        lamp_glow = False
    
    # 背景
    surf.fill(bg_color)
    
    # 墙壁
    wall_h = int(h * 0.65)
    pygame.draw.rect(surf, wall_color, (0, 0, w, wall_h))
    
    # 地板
    pygame.draw.rect(surf, floor_color, (0, wall_h, w, h - wall_h))
    
    # 地板纹理线
    for i in range(6):
        lx = i * (w // 5)
        pygame.draw.line(surf, (80, 68, 55), (lx, wall_h), (lx + 40, h), 2)
        pygame.draw.line(surf, (80, 68, 55), (lx + w // 5 // 2, wall_h), (lx + w // 5 // 2 + 40, h), 1)
    
    # 窗户 (左侧)
    win_x, win_y, win_w, win_h_rect = 60, 25, 220, 250
    pygame.draw.rect(surf, (40, 40, 50), (win_x, win_y, win_w, win_h_rect))
    pygame.draw.rect(surf, window_light, (win_x + 8, win_y + 8, win_w - 16, win_h_rect - 16))
    # 窗格
    pygame.draw.line(surf, (40, 40, 50), (win_x + win_w // 2, win_y + 8), (win_x + win_w // 2, win_y + win_h_rect - 8), 3)
    pygame.draw.line(surf, (40, 40, 50), (win_x + 8, win_y + win_h_rect // 2), (win_x + win_w - 8, win_y + win_h_rect // 2), 3)
    
    if is_night:
        # 夜空中星星
        for _ in range(12):
            sx = win_x + 20 + random.randint(0, win_w - 40)
            sy = win_y + 15 + random.randint(0, win_h_rect // 3)
            pygame.draw.circle(surf, (200, 200, 220), (sx, sy), 1)
        # 月亮
        pygame.draw.circle(surf, (220, 220, 200), (win_x + 120, win_y + 40), 15)
    
    # 书架 (右侧墙)
    shelf_x, shelf_y = w - 160, 15
    pygame.draw.rect(surf, (80, 55, 30), (shelf_x, shelf_y, 140, 260))
    for i in range(5):
        sy2 = shelf_y + 25 + i * 50
        pygame.draw.rect(surf, (100, 70, 40), (shelf_x + 8, sy2, 124, 7))
        # 书本
        for j in range(7):
            book_x = shelf_x + 12 + j * 18
            book_h = random.randint(30, 45)
            book_colors = [(180, 40, 40), (40, 80, 180), (40, 150, 60), (180, 140, 30), (120, 50, 120)]
            bc = random.choice(book_colors)
            pygame.draw.rect(surf, bc, (book_x, sy2 - book_h, 15, book_h))
    
    # 大办公桌 (中心偏右)
    desk_x = w // 2 - 80
    desk_y = int(h * 0.52)
    desk_w = 460
    desk_h = 24
    pygame.draw.rect(surf, Colors.DESK, (desk_x, desk_y, desk_w, desk_h))
    # 桌面高光
    pygame.draw.rect(surf, (130, 95, 60), (desk_x, desk_y, desk_w, 7))
    # 桌腿
    for lx in [desk_x + 40, desk_x + desk_w - 40]:
        pygame.draw.rect(surf, (70, 50, 35), (lx - 6, desk_y + desk_h, 12, h - desk_y - desk_h))
    
    # 桌上的物品
    if lamp_glow:
        lamp_x = desk_x + 350
        lamp_y = desk_y - 50
        pygame.draw.rect(surf, (80, 80, 80), (lamp_x, lamp_y, 33, 50))
        pygame.draw.polygon(surf, (60, 60, 60), [(lamp_x - 6, lamp_y), (lamp_x + 39, lamp_y), (lamp_x + 27, lamp_y - 20)])
        # 灯光光晕
        glow_surf = pygame.Surface((120, 100), pygame.SRCALPHA)
        for r in range(60, 10, -10):
            alpha = max(5, 30 - r // 3)
            pygame.draw.circle(glow_surf, (255, 230, 150, alpha), (60, 50), r)
        surf.blit(glow_surf, (lamp_x - 55, lamp_y - 75))
    
    # 文件/纸张
    pygame.draw.rect(surf, (220, 220, 210), (desk_x + 60, desk_y - 4, 55, 4))
    pygame.draw.rect(surf, (240, 240, 225), (desk_x + 130, desk_y - 5, 48, 4))
    # 咖啡杯
    pygame.draw.rect(surf, (180, 180, 180), (desk_x + 230, desk_y - 16, 18, 16))
    pygame.draw.ellipse(surf, (100, 60, 20), (desk_x + 233, desk_y - 16, 13, 6))
    
    # 导师椅子 (桌后)
    chair_x = desk_x + desk_w // 2
    chair_y = desk_y - 10
    pygame.draw.rect(surf, Colors.CHAIR, (chair_x - 38, chair_y - 92, 76, 100))
    pygame.draw.rect(surf, (80, 60, 45), (chair_x - 38, chair_y - 6, 76, 17))
    
    # 导师 (坐在椅子上)
    advisor_x = chair_x
    advisor_y = chair_y - 135
    draw_pixel_character(surf, advisor_x, advisor_y,
                        Colors.ADVISOR_SKIN, None, (80, 75, 90),
                        suit_color=Colors.ADVISOR_SUIT, 
                        tie_color=Colors.ADVISOR_TIE,
                        glasses_color=Colors.ADVISOR_GLASSES,
                        scale=5.5, head_tilt=0)
    
    # 学生 (站在桌前)
    student_x = desk_x + 120
    student_y = desk_y + 55
    draw_pixel_character(surf, student_x, student_y,
                        Colors.PLAYER_SKIN, Colors.PLAYER_SHIRT, Colors.PLAYER_HAIR,
                        scale=5.0, head_tilt=-3)
    
    # 地毯
    carpet_points = [(desk_x - 30, h), (desk_x + desk_w + 30, h), 
                     (desk_x + desk_w + 65, h - 25), (desk_x - 65, h - 25)]
    pygame.draw.polygon(surf, (80, 30, 30), carpet_points)
    
    return surf


def draw_lab_scene(surf):
    """绘制实验室场景"""
    w, h = SCREEN_WIDTH, SCENE_HEIGHT
    
    surf.fill(Colors.DARK_BG)
    
    # 墙壁
    wall_h = int(h * 0.7)
    pygame.draw.rect(surf, (55, 55, 70), (0, 0, w, wall_h))
    # 地板
    pygame.draw.rect(surf, (90, 90, 100), (0, wall_h, w, h - wall_h))
    # 地板网格线
    for i in range(0, w, 60):
        pygame.draw.line(surf, (75, 75, 85), (i, wall_h), (i, h), 1)
    for j in range(wall_h, h, 40):
        pygame.draw.line(surf, (75, 75, 85), (0, j), (w, j), 1)
    
    # 天花板灯
    for lx in [w // 4, w // 2, 3 * w // 4]:
        pygame.draw.rect(surf, (200, 200, 210), (lx - 30, 5, 60, 8))
        glow = pygame.Surface((80, 60), pygame.SRCALPHA)
        pygame.draw.ellipse(glow, (255, 255, 200, 30), (10, 8, 60, 45))
        surf.blit(glow, (lx - 40, 13))
    
    # 工作台
    bench_x, bench_y = 50, int(h * 0.5)
    bench_w, bench_h = 450, 22
    pygame.draw.rect(surf, (100, 100, 110), (bench_x, bench_y, bench_w, bench_h))
    pygame.draw.rect(surf, (80, 80, 90), (bench_x - 6, bench_y - 4, bench_w + 12, 8))
    
    # 工作台上的设备
    # 显示器1
    monitor_colors = [(40, 40, 45), (35, 38, 42)]
    for mi, mx in enumerate([bench_x + 40, bench_x + 200]):
        pygame.draw.rect(surf, monitor_colors[mi], (mx, bench_y - 75, 110, 55))
        pygame.draw.rect(surf, (20, 30, 50), (mx + 10, bench_y - 65, 90, 38))
        pygame.draw.rect(surf, (60, 60, 65), (mx - 3, bench_y - 80, 116, 10))
        # 屏幕内容 - 代码/图表
        for sl in range(4):
            line_y = bench_y - 58 + sl * 9
            line_w = random.randint(25, 70)
            pygame.draw.rect(surf, (80, 200, 100), (mx + 16, line_y, line_w, 4))
    
    # 键盘
    pygame.draw.rect(surf, (50, 50, 55), (bench_x + 130, bench_y + 3, 160, 11))
    
    # 实验室设备柜 (右侧)
    cabinet_x = w - 230
    pygame.draw.rect(surf, (60, 65, 75), (cabinet_x, 30, 200, 260))
    for row in range(4):
        ry = 42 + row * 62
        pygame.draw.rect(surf, (80, 85, 95), (cabinet_x + 12, ry, 176, 50))
        pygame.draw.rect(surf, (40, 42, 46), (cabinet_x + 18, ry + 6, 164, 38))
        # 设备指示灯
        for led in range(3):
            led_color = random.choice([(255, 50, 50), (50, 255, 50), (50, 50, 255)])
            pygame.draw.circle(surf, led_color, (cabinet_x + 30 + led * 18, ry + 25), 4)
    
    # 白板 (左侧墙)
    wb_x, wb_y = 180, 45
    pygame.draw.rect(surf, (230, 230, 225), (wb_x, wb_y, 230, 165))
    pygame.draw.rect(surf, (180, 180, 180), (wb_x, wb_y, 230, 165), 4)
    # 白板上的涂鸦
    for _ in range(8):
        sx = wb_x + 20 + random.randint(0, 180)
        sy = wb_y + 18 + random.randint(0, 130)
        sw = random.randint(25, 75)
        pygame.draw.rect(surf, (50, 50, 200), (sx, sy, sw, 4))
        # 公式乱码
        fx = sx + sw + 6
        if fx < wb_x + 210:
            pygame.draw.rect(surf, (200, 50, 50), (fx, sy, 18, 4))
    
    # 学生 (在工作台前)
    student_x = bench_x + 220
    student_y = bench_y + 80
    draw_pixel_character(surf, student_x, student_y,
                        Colors.PLAYER_SKIN, Colors.PLAYER_SHIRT, Colors.PLAYER_HAIR,
                        scale=4.5, head_tilt=-2)
    
    # 椅子
    pygame.draw.rect(surf, (50, 55, 60), (student_x - 30, student_y + 25, 60, 80))
    
    return surf


def draw_hallway_scene(surf):
    """绘制走廊场景 (透视)"""
    w, h = SCREEN_WIDTH, SCENE_HEIGHT
    
    surf.fill((30, 30, 42))
    
    # 透视走廊 - 天花板
    vp_x = w // 2
    vp_y = int(h * 0.35)
    
    # 后墙
    pygame.draw.rect(surf, (60, 58, 72), (vp_x - 80, vp_y, 160, h - vp_y))
    
    # 地板透视
    floor_points = [
        (0, h), (w, h),
        (vp_x + 120, vp_y + 120), (vp_x - 120, vp_y + 120)
    ]
    pygame.draw.polygon(surf, (70, 65, 55), floor_points)
    # 地板线
    for i in range(1, 8):
        t = i / 8.0
        ly = h - t * (h - vp_y - 120)
        lw_left = int((1 - t) * (vp_x - 120))
        lw_right = int((1 - t) * (vp_x - 120))
        alpha_line = max(15, int(80 * (1 - t)))
        color = (alpha_line + 50, alpha_line + 45, alpha_line + 35)
        pygame.draw.line(surf, color, (lw_left, int(ly)), (w - lw_right, int(ly)), 1)
    
    # 天花板透视
    ceil_points = [
        (0, 0), (w, 0),
        (vp_x + 120, vp_y + 80), (vp_x - 120, vp_y + 80)
    ]
    pygame.draw.polygon(surf, (50, 48, 60), ceil_points)
    
    # 左侧墙
    left_wall = [(0, 0), (vp_x - 120, vp_y + 80), (vp_x - 120, vp_y + 120), (0, h)]
    pygame.draw.polygon(surf, (70, 68, 82), left_wall)
    
    # 右侧墙
    right_wall = [(w, 0), (vp_x + 120, vp_y + 80), (vp_x + 120, vp_y + 120), (w, h)]
    pygame.draw.polygon(surf, (65, 63, 77), right_wall)
    
    # 荧光灯 (天花板)
    for i in range(3):
        t = 0.2 + i * 0.25
        lx = int(vp_x - 120 + t * 240)
        ly = int(vp_y + 80 + t * 40)
        lw = int(60 * (1 - t * 0.5))
        pygame.draw.rect(surf, (220, 220, 230), (lx - lw // 2, ly, lw, 6))
        # 光晕
        glow_s = pygame.Surface((lw + 40, 30), pygame.SRCALPHA)
        pygame.draw.ellipse(glow_s, (255, 255, 200, 20), (10, 10, lw + 20, 15))
        surf.blit(glow_s, (lx - lw // 2 - 20, ly - 5))
    
    # 门 (左侧墙)
    door_x = 60
    door_y = int(h * 0.30)
    door_w = 168
    door_h = int(h * 0.52)
    pygame.draw.rect(surf, (90, 70, 50), (door_x, door_y, door_w, door_h))
    pygame.draw.rect(surf, (110, 85, 60), (door_x + 7, door_y + 7, door_w - 14, door_h - 14))
    # 门牌
    pygame.draw.rect(surf, (200, 180, 80), (door_x + door_w // 2 - 35, door_y + 20, 70, 25))
    pygame.draw.rect(surf, (160, 140, 50), (door_x + door_w // 2 - 35, door_y + 20, 70, 25), 1)
    # 门把手
    pygame.draw.circle(surf, (180, 160, 40), (door_x + door_w - 20, door_y + door_h // 2), 7)
    
    # 公告板 (右侧墙)
    board_x = w - 210
    board_y = int(h * 0.18)
    pygame.draw.rect(surf, (140, 120, 80), (board_x, board_y, 195, 240))
    pygame.draw.rect(surf, (180, 160, 120), (board_x + 10, board_y + 10, 175, 220))
    # 公告板上的纸张
    for _ in range(6):
        px = board_x + 18 + random.randint(0, 135)
        py = board_y + 18 + random.randint(0, 185)
        pw = random.randint(35, 95)
        ph = random.randint(25, 60)
        paper_color = random.choice([(240, 240, 220), (220, 240, 220), (255, 240, 200)])
        pygame.draw.rect(surf, paper_color, (px, py, pw, ph))
        pygame.draw.rect(surf, (160, 160, 160), (px, py, pw, ph), 1)
        # 文字线
        for tl in range(3):
            pygame.draw.rect(surf, (100, 100, 100), (px + 6, py + 10 + tl * 12, pw - 12, 2))
    
    # 饮水机 (底部)
    disp_x = w // 2 - 110
    disp_y = h - 110
    pygame.draw.rect(surf, (180, 180, 190), (disp_x, disp_y, 65, 105))
    pygame.draw.rect(surf, (200, 200, 210), (disp_x + 6, disp_y + 6, 53, 40))
    # 水桶 (蓝色)
    pygame.draw.rect(surf, (120, 170, 220), (disp_x + 11, disp_y - 7, 43, 15))
    # 水龙头
    pygame.draw.circle(surf, (100, 100, 100), (disp_x + 33, disp_y + 60), 5)
    
    return surf


def draw_meeting_scene(surf):
    """绘制组会/会议室场景"""
    w, h = SCREEN_WIDTH, SCENE_HEIGHT
    
    surf.fill(Colors.DARK_BG)
    
    # 墙壁
    wall_h = int(h * 0.6)
    pygame.draw.rect(surf, (55, 58, 72), (0, 0, w, wall_h))
    pygame.draw.rect(surf, (95, 85, 70), (0, wall_h, w, h - wall_h))
    
    # 投影屏幕 (中央墙上)
    screen_x = w // 2 - 140
    screen_y = 30
    pygame.draw.rect(surf, (40, 40, 45), (screen_x, screen_y, 280, 180))
    pygame.draw.rect(surf, (220, 220, 225), (screen_x + 8, screen_y + 8, 264, 164))
    # 投影内容 - 图表
    for i in range(5):
        bar_x = screen_x + 40 + i * 50
        bar_h = random.randint(40, 120)
        bar_color = random.choice([(60, 120, 220), (220, 80, 60), (60, 180, 100)])
        pygame.draw.rect(surf, bar_color, (bar_x, screen_y + 160 - bar_h, 35, bar_h))
    
    # 投影仪光柱
    proj_surf = pygame.Surface((280, 200), pygame.SRCALPHA)
    for a in range(5, 25, 3):
        pygame.draw.rect(proj_surf, (255, 255, 255, a), (100, 20, 80, 180))
    surf.blit(proj_surf, (screen_x, screen_y))
    
    # 长会议桌
    table_x = 60
    table_y = int(h * 0.45)
    table_w = w - 120
    table_h = 22
    pygame.draw.rect(surf, (140, 100, 60), (table_x, table_y, table_w, table_h))
    pygame.draw.rect(surf, (170, 125, 75), (table_x, table_y, table_w, 7))
    
    # 桌腿
    for lx in [table_x + 50, table_x + table_w - 100]:
        pygame.draw.rect(surf, (100, 70, 40), (lx - 4, table_y + table_h, 8, h - table_y - table_h))
    
    # 椅子围绕桌子
    chair_positions = [
        (table_x + 40, table_y - 35, False),   # 左侧
        (table_x + 170, table_y - 35, False),  # 左侧
        (w // 2 - 20, table_y - 42, True),     # 导师位 (中央上)
        (table_x + table_w - 210, table_y - 35, False),  # 右侧
        (table_x + table_w - 100, table_y - 35, False),   # 右侧
        (table_x + 100, table_y + 28, False),   # 面对屏幕
        (table_x + table_w - 150, table_y + 28, False),
    ]
    
    for ci, (cx, cy, is_advisor) in enumerate(chair_positions):
        chair_w, chair_h_rect = 42, 45
        pygame.draw.rect(surf, Colors.CHAIR, (cx - chair_w // 2, cy, chair_w, chair_h_rect))
        
        if is_advisor:
            # 导师
            draw_pixel_character(surf, cx, cy - 35,
                               Colors.ADVISOR_SKIN, None, (80, 75, 90),
                               suit_color=Colors.ADVISOR_SUIT,
                               tie_color=Colors.ADVISOR_TIE,
                               glasses_color=Colors.ADVISOR_GLASSES,
                               scale=4.5)
        else:
            # 其他参会者
            skin_variants = [(220, 185, 155), (230, 200, 170), (210, 175, 145)]
            shirt_variants = [(70, 70, 150), (150, 70, 70), (60, 120, 60)]
            hair_variants = [(30, 25, 20), (60, 50, 40), (40, 30, 25)]
            sk = skin_variants[ci % 3]
            sh = shirt_variants[ci % 3]
            ha = hair_variants[ci % 3]
            draw_pixel_character(surf, cx, cy - 35, sk, sh, ha, scale=3.5)
    
    # 白板 (右侧墙)
    wb_x = w - 140
    pygame.draw.rect(surf, (230, 230, 225), (wb_x, 60, 115, 180))
    pygame.draw.rect(surf, (160, 160, 160), (wb_x, 60, 115, 180), 3)
    for _ in range(5):
        sx = wb_x + 8 + random.randint(0, 90)
        sy = 72 + random.randint(0, 155)
        pygame.draw.rect(surf, (50, 50, 180), (sx, sy, random.randint(18, 60), 4))
    
    return surf


def draw_night_scene(surf):
    """绘制深夜办公室场景 (暗色调)"""
    return draw_office_scene(surf, is_night=True)


def render_scene(surf, scene_name):
    """根据场景名渲染对应场景"""
    if scene_name == SCENE_OFFICE:
        return draw_office_scene(surf)
    elif scene_name == SCENE_LAB:
        return draw_lab_scene(surf)
    elif scene_name == SCENE_HALLWAY:
        return draw_hallway_scene(surf)
    elif scene_name == SCENE_MEETING:
        return draw_meeting_scene(surf)
    elif scene_name == SCENE_NIGHT:
        return draw_night_scene(surf)
    else:
        return draw_office_scene(surf)


# ==================== 辅助绘制函数 ====================

def draw_text_with_wrap(surf, text, font, color, x, y, max_width, line_spacing=4):
    """绘制自动换行文本，返回总高度"""
    words = list(text)
    lines = []
    current_line = ""
    for char in words:
        test_line = current_line + char
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = char
    if current_line:
        lines.append(current_line)
    
    total_h = 0
    for line in lines:
        text_surf = font.render(line, True, color)
        surf.blit(text_surf, (x, y + total_h))
        total_h += font.get_height() + line_spacing
    return total_h


def draw_scanlines(surf):
    """在屏幕上绘制扫描线覆盖"""
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    for y in range(0, SCREEN_HEIGHT, 3):
        pygame.draw.line(overlay, (0, 0, 0, 25), (0, y), (SCREEN_WIDTH, y))
    surf.blit(overlay, (0, 0))


# ==================== 游戏类 ====================


class Game:
    def __init__(self):
        self.state = STATE_TITLE
        self.stress = INITIAL_STRESS
        self.current_arc = None
        self.current_arc_id = None
        self.current_dialogue_index = 0
        self.current_dialogue = None
        self.completed_arcs = []
        self.text_display = ""
        self.text_index = 0
        self.text_timer = 0
        self.text_speed = 1
        self.show_options = False
        self.shuffled_options = []
        self.shuffled_stress_changes = []
        self.shake_timer = 0
        self.shake_intensity = 0
        self.transition_alpha = 255
        self.transition_state = "none"
        self.intro_index = 0
        self.intro_timer = 0
        self.game_over_text = ""
        self.game_over_timer = 0
        self.floating_texts = []
        self.bg_offset = 0
        self.title_glitch = 0
        self.choice_start_time = 0
        self.time_pressure_accumulator = 0
        self.timer_pulse = 0
        self.glitch_offset = 0
        self.fade_alpha = 0
        self.personality = None
        self.peer_text = ""
        self.peer_timer = 0
        self.personality_desc_index = 0
        self.quiz_result_text = ""
        self.quiz_result_timer = 0
        self.is_quiz_node = False
        self.correct_quiz_index = -1
        self.arc_transition_timer = 0
        self.arc_transition_text = ""

    def reset(self):
        self.state = STATE_PLAYING
        self.stress = INITIAL_STRESS
        self.current_arc = None
        self.current_arc_id = None
        self.current_dialogue_index = 0
        self.current_dialogue = None
        self.completed_arcs = []
        self.text_display = ""
        self.text_index = 0
        self.text_timer = 0
        self.show_options = False
        self.shuffled_options = []
        self.shuffled_stress_changes = []
        self.shake_timer = 0
        self.shake_intensity = 0
        self.floating_texts = []
        self.choice_start_time = 0
        self.time_pressure_accumulator = 0
        self.timer_pulse = 0
        self.glitch_offset = 0
        self.fade_alpha = 0
        self.arc_transition_timer = 0
        self.arc_transition_text = ""
        self.personality = "obedient"  # Default, will be set during personality selection
        self.peer_text = ""
        self.peer_timer = 0
        self.quiz_result_text = ""
        self.quiz_result_timer = 0
        self.is_quiz_node = False
        self.correct_quiz_index = -1

    def start_arc(self, arc_id):
        if arc_id in STORY_ARCS and arc_id not in self.completed_arcs:
            self.state = STATE_PLAYING
            self.current_arc_id = arc_id
            self.current_arc = STORY_ARCS[arc_id]
            self.current_dialogue_index = 0
            self.current_dialogue = None
            self.text_display = ""
            self.text_index = 0
            self.text_timer = 0
            self.show_options = False
            self.choice_start_time = 0
            self.time_pressure_accumulator = 0
            self._start_dialogue()
            return True
        return False

    def _start_dialogue(self):
        if not self.current_arc or self.current_dialogue_index >= len(self.current_arc["dialogues"]):
            self.current_dialogue = None
            self.show_options = False
            return
        
        raw_dialogue = self.current_arc["dialogues"][self.current_dialogue_index]
        self.current_dialogue = {
            "id": raw_dialogue["id"],
            "advisor": raw_dialogue["advisor"],
            "options": list(raw_dialogue["options"]),
            "stress_changes": list(raw_dialogue.get("stress_changes", [0, 0, 0])),
        }
        
        # Check quiz type
        self.is_quiz_node = raw_dialogue.get("type") == "quiz"
        self.correct_quiz_index = raw_dialogue.get("correct_index", -1) if self.is_quiz_node else -1
        
        # Personality variant override
        pid = raw_dialogue["id"]
        if self.personality and self.personality in PERSONALITY_VARIANTS:
            variant = PERSONALITY_VARIANTS[self.personality].get(pid, {})
            if "advisor" in variant:
                self.current_dialogue["advisor"] = variant["advisor"]
            if "options" in variant:
                self.current_dialogue["options"] = variant["options"]
            if "stress_changes" in variant:
                self.current_dialogue["stress_changes"] = variant["stress_changes"]
        
        # Shuffle: map original indices to shuffled positions
        num_opts = len(self.current_dialogue["options"])
        self._shuffle_map = list(range(num_opts))
        random.shuffle(self._shuffle_map)
        
        self.shuffled_options = [self.current_dialogue["options"][i] for i in self._shuffle_map]
        self.shuffled_stress_changes = [self.current_dialogue["stress_changes"][i] for i in self._shuffle_map]
        
        if self.is_quiz_node:
            # Find where correct answer moved to
            self.shuffled_correct_index = self._shuffle_map.index(self.correct_quiz_index)
        
        self.text_display = ""
        self.text_index = 0
        self.text_timer = 0
        self.show_options = False
        self.choice_start_time = 0
        self.time_pressure_accumulator = 0
        self.peer_text = ""
        self.peer_timer = 0

    def select_choice(self, option_index):
        if not self.show_options or not self.current_dialogue:
            return
        if option_index < 0 or option_index >= len(self.shuffled_stress_changes):
            return
        
        stress_change = self.shuffled_stress_changes[option_index]
        
        # Apply personality multiplier to stress change
        if self.personality and self.personality in PERSONALITY_TYPES:
            stress_change = int(stress_change * PERSONALITY_TYPES[self.personality]["stress_mult"])
        
        # Quiz handling: check if answer is correct
        if self.is_quiz_node:
            if option_index == self.shuffled_correct_index:
                stress_change = QUIZ_STRESS_CORRECT
                self.quiz_result_text = "✓ 回答正确！导师微微点头。"
            else:
                stress_change = QUIZ_STRESS_WRONG
                self.quiz_result_text = "✗ 回答错误！导师的脸色更难看了..."
            self.quiz_result_timer = 90
        
        self.stress += stress_change
        self.stress = max(0, min(MAX_STRESS, self.stress))
        
        # Peer feedback
        raw_dialogue = self.current_arc["dialogues"][self.current_dialogue_index]
        peer_reaction_key = raw_dialogue.get("peer_reaction")
        if peer_reaction_key and peer_reaction_key in PEER_REACTIONS:
            self.peer_text = random.choice(PEER_REACTIONS[peer_reaction_key])
            self.peer_timer = 120
        
        if self.stress >= MAX_STRESS:
            self.state = STATE_GAME_OVER
            self.game_over_text = random.choice(GAME_OVER_MESSAGES)
            self.game_over_timer = 0
            self.shake_timer = 40
            self.shake_intensity = 15
            return
        
        self.current_dialogue_index += 1
        self.show_options = False
        self.choice_start_time = 0
        self.time_pressure_accumulator = 0
        
        if self.current_dialogue_index >= len(self.current_arc["dialogues"]):
            self.completed_arcs.append(self.current_arc_id)
            self._transition_to_next_arc()
        else:
            self._start_dialogue()

    def _transition_to_next_arc(self):
        possible = ARC_TRANSITIONS.get(self.current_arc_id, [])
        available = [a for a in possible if a not in self.completed_arcs]
        if not available:
            all_arcs = [k for k in STORY_ARCS.keys() if k not in self.completed_arcs]
            if all_arcs:
                available = all_arcs
        if available:
            next_arc = random.choice(available)
            arc_name = ARC_NAMES.get(next_arc, next_arc)
            self.arc_transition_text = arc_name
            self.arc_transition_timer = 120
            self.state = STATE_ARC_TRANSITION
            self.current_arc = None
            self.current_arc_id = next_arc
            self.current_dialogue_index = 0
            self.current_dialogue = None
            self.text_display = ""
            self.text_index = 0
            self.show_options = False
        else:
            self.state = STATE_GAME_OVER
            self.game_over_text = random.choice(GAME_OVER_MESSAGES)
            self.game_over_timer = 0
            self.shake_timer = 40
            self.shake_intensity = 15

    def update(self, dt):
        self.timer_pulse += dt
        if self.current_dialogue and self.text_index < len(self.current_dialogue["advisor"]):
            self.text_timer += dt * 60
            chars_to_add = int(self.text_timer * self.text_speed)
            if chars_to_add > 0:
                self.text_timer = 0
                full_text = self.current_dialogue["advisor"]
                self.text_index = min(len(full_text), self.text_index + chars_to_add)
                self.text_display = full_text[:self.text_index]
                if self.text_index >= len(full_text):
                    self.show_options = True
                    self.choice_start_time = time.time()
                    self.time_pressure_accumulator = 0
        if self.state == STATE_ARC_TRANSITION:
            self.arc_transition_timer -= dt * 60
            if self.arc_transition_timer <= 0:
                self.start_arc(self.current_arc_id)
        if self.shake_timer > 0:
            self.shake_timer -= dt * 60
        if self.state == STATE_GAME_OVER:
            self.game_over_timer += dt * 60
        if self.show_options and self.choice_start_time > 0:
            elapsed = time.time() - self.choice_start_time
            if elapsed > MAX_CHOICE_TIME:
                if self.shuffled_stress_changes:
                    idx = random.randrange(len(self.shuffled_stress_changes))
                    self.select_choice(idx)
            elif elapsed > 0:
                self.time_pressure_accumulator += dt * 60
                if self.time_pressure_accumulator >= TIME_PRESSURE_INTERVAL * 60:
                    self.time_pressure_accumulator -= TIME_PRESSURE_INTERVAL * 60
                    stress_increase = TIME_PRESSURE_BASE * (elapsed ** TIME_PRESSURE_EXPONENT) / TIME_PRESSURE_DIVISOR
                    if self.personality and self.personality in PERSONALITY_TYPES:
                        stress_increase = int(stress_increase * PERSONALITY_TYPES[self.personality]["stress_mult"])
                    self.stress = min(MAX_STRESS, self.stress + stress_increase)
                    if self.stress >= MAX_STRESS:
                        self.state = STATE_GAME_OVER
                        self.game_over_text = random.choice(GAME_OVER_MESSAGES)
                        self.game_over_timer = 0
                        self.shake_timer = 40
                        self.shake_intensity = 15
        
        if self.peer_timer > 0:
            self.peer_timer -= 1
        if self.quiz_result_timer > 0:
            self.quiz_result_timer -= 1

    def get_scene_name(self):
        if self.current_arc:
            return self.current_arc.get("scene", SCENE_OFFICE)
        return SCENE_OFFICE

    def skip_typewriter(self):
        if self.current_dialogue and self.text_index < len(self.current_dialogue["advisor"]):
            self.text_index = len(self.current_dialogue["advisor"])
            self.text_display = self.current_dialogue["advisor"]
            self.show_options = True
            self.choice_start_time = time.time()
            self.time_pressure_accumulator = 0


def _draw_glitch_rect(surf, color, rect, offset_range=3):
    ox = random.randint(-offset_range, offset_range)
    oy = random.randint(-offset_range, offset_range)
    r = pygame.Rect(rect.x + ox, rect.y + oy, rect.width, rect.height)
    pygame.draw.rect(surf, color, r)


def draw_choice_buttons(surf, game):
    if not game.show_options or not game.current_dialogue:
        return
    mouse_pos = pygame.mouse.get_pos()
    elapsed = time.time() - game.choice_start_time if game.choice_start_time > 0 else 0
    time_ratio = min(1.0, elapsed / MAX_CHOICE_TIME)
    high_pressure = time_ratio > 0.6
    
    for i in range(3):
        bx = CHOICE_START_X + i * (CHOICE_BUTTON_WIDTH + CHOICE_BUTTON_GAP)
        by = CHOICE_START_Y
        btn_rect = pygame.Rect(bx, by, CHOICE_BUTTON_WIDTH, CHOICE_BUTTON_HEIGHT)
        hovered = btn_rect.collidepoint(mouse_pos)
        
        if high_pressure:
            glitch_offset = int((time_ratio - 0.6) * 15)
            ox = random.randint(-glitch_offset, glitch_offset)
            oy = random.randint(-glitch_offset // 2, glitch_offset // 2)
            draw_rect = pygame.Rect(bx + ox, by + oy, CHOICE_BUTTON_WIDTH, CHOICE_BUTTON_HEIGHT)
        else:
            draw_rect = btn_rect
        
        color = Colors.BTN_HOVER if hovered else Colors.BTN_IDLE
        pygame.draw.rect(surf, color, draw_rect, border_radius=3)
        border_color = Colors.BORDER_LIGHT if hovered else Colors.BORDER
        if high_pressure and random.random() < time_ratio * 0.3:
            border_color = Colors.GLITCH_GREEN
        pygame.draw.rect(surf, border_color, draw_rect, 2, border_radius=3)
        
        if i < len(game.shuffled_options):
            text = game.shuffled_options[i]
            text_color = Colors.BTN_HOVER_TEXT if hovered else Colors.BTN_TEXT
            text_surf = font_small.render(text, True, text_color)
            
            if high_pressure and random.random() < time_ratio * 0.2:
                gx = random.randint(-2, 2)
                gy = random.randint(-1, 1)
            else:
                gx, gy = 0, 0
            
            text_x = bx + (CHOICE_BUTTON_WIDTH - text_surf.get_width()) // 2 + gx
            text_y = by + (CHOICE_BUTTON_HEIGHT - text_surf.get_height()) // 2 + gy
            surf.blit(text_surf, (text_x, text_y))
            
            if hovered:
                indicator = font_small.render(">", True, Colors.TEXT_YELLOW)
                surf.blit(indicator, (bx + 8, text_y))


def draw_stress_bar(surf, stress):
    bar_x, bar_y = STRESS_BAR_X, STRESS_BAR_Y
    bar_w, bar_h = STRESS_BAR_WIDTH, STRESS_BAR_HEIGHT
    
    label = font_small.render("压力", True, Colors.TEXT_WHITE)
    surf.blit(label, (bar_x, bar_y - 22))
    
    pygame.draw.rect(surf, Colors.STRESS_BG, (bar_x, bar_y, bar_w, bar_h))
    pygame.draw.rect(surf, Colors.STRESS_BORDER, (bar_x, bar_y, bar_w, bar_h), 1)
    
    fill_w = int(bar_w * stress / MAX_STRESS)
    if stress <= 30:
        fill_color = Colors.STRESS_LOW
    elif stress <= 55:
        fill_color = Colors.STRESS_MED
    elif stress <= 75:
        fill_color = Colors.STRESS_HIGH
    else:
        fill_color = Colors.STRESS_CRIT
    
    if stress > 75:
        pulse = abs(math.sin(pygame.time.get_ticks() * 0.005)) * 0.3 + 0.7
        fill_color = tuple(min(255, int(c * pulse)) for c in fill_color)
    
    pygame.draw.rect(surf, fill_color, (bar_x, bar_y, fill_w, bar_h))
    
    stress_text = font_small.render(f"{int(stress)}/{MAX_STRESS}", True, Colors.TEXT_WHITE)
    surf.blit(stress_text, (bar_x + bar_w + 10, bar_y - 2))
    
    if stress > 75:
        for _ in range(2):
            sx = bar_x + random.randint(0, fill_w)
            sy = bar_y + random.randint(0, bar_h)
            pygame.draw.rect(surf, (255, 80, 80), (sx, sy, 2, 2))


def draw_timer_indicator(surf, game):
    if not game.show_options or game.choice_start_time <= 0:
        return
    elapsed = time.time() - game.choice_start_time
    time_ratio = min(1.0, elapsed / MAX_CHOICE_TIME)
    
    tx = SCREEN_WIDTH - 80
    ty = DIALOG_BOX_Y + 5
    radius = 12
    
    if time_ratio < 0.5:
        ring_color = Colors.STRESS_LOW
    elif time_ratio < 0.75:
        ring_color = Colors.STRESS_MED
    else:
        ring_color = Colors.STRESS_CRIT
    
    pulse = abs(math.sin(pygame.time.get_ticks() * (0.003 + time_ratio * 0.015)))
    if time_ratio > 0.5:
        ring_color = tuple(min(255, int(c * (0.7 + pulse * 0.5))) for c in ring_color)
    
    pygame.draw.circle(surf, Colors.STRESS_BG, (tx, ty), radius + 2)
    pygame.draw.circle(surf, ring_color, (tx, ty), radius, 2)
    
    angle = -math.pi / 2 + time_ratio * 2 * math.pi
    end_x = tx + int(math.cos(angle) * (radius - 3))
    end_y = ty + int(math.sin(angle) * (radius - 3))
    pygame.draw.line(surf, ring_color, (tx, ty), (end_x, end_y), 3)
    
    if time_ratio > 0.8:
        warn_alpha = int((time_ratio - 0.8) * 5 * 128)
        for _ in range(2):
            wx = tx + random.randint(-3, 3)
            wy = ty + random.randint(-3, 3)
            pygame.draw.circle(surf, (255, 40, 40), (wx, wy), radius + 1, 1)


def draw_dialog_box(surf, game):
    if not game.current_dialogue:
        return
    
    bx, by = DIALOG_BOX_X, DIALOG_BOX_Y
    bw, bh = DIALOG_BOX_WIDTH, DIALOG_BOX_HEIGHT
    
    pygame.draw.rect(surf, Colors.PANEL_BG, (bx, by, bw, bh), border_radius=4)
    
    elapsed = 0
    if game.show_options and game.choice_start_time > 0:
        elapsed = time.time() - game.choice_start_time
    time_ratio = min(1.0, elapsed / MAX_CHOICE_TIME)
    
    if time_ratio > 0.3:
        flicker = abs(math.sin(pygame.time.get_ticks() * (0.005 + time_ratio * 0.03)))
        border_r = min(255, int(70 + flicker * (255 - 70)))
        border_g = min(255, int(70 + flicker * 40))
        border_b = min(255, int(100 + flicker * 20))
        border_color = (border_r, border_g, border_b)
    else:
        border_color = Colors.BORDER
    
    pygame.draw.rect(surf, border_color, (bx, by, bw, bh), 2, border_radius=4)
    
    name_label = font_small.render("导师", True, Colors.TEXT_YELLOW)
    surf.blit(name_label, (bx + 15, by + 10))
    pygame.draw.line(surf, Colors.BORDER, (bx + 50, by + 20), (bx + bw - 30, by + 20), 1)
    
    text = game.text_display
    draw_text_with_wrap(surf, text, font_normal, Colors.TEXT_WHITE,
                       bx + 18, by + 30, bw - 36, line_spacing=6)
    
    if game.text_index < len(game.current_dialogue["advisor"]):
        if (pygame.time.get_ticks() // 400) % 2:
            full = game.text_display
            cursor_x = bx + 18
            if full:
                last_line = full.split("\n")[-1] if "\n" in full else full
                cursor_x += font_normal.size(last_line)[0]
            cursor_y = by + bh - 30
            pygame.draw.rect(surf, Colors.TEXT_WHITE, (cursor_x, cursor_y, 8, font_normal.get_height()))


def draw_personality_screen(surf, game):
    """Draw personality selection screen"""
    # Dark overlay
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(Colors.DARK_BG)
    surf.blit(overlay, (0, 0))
    
    font_title = get_font(32)
    font_desc = get_font(16)
    font_name = get_font(22)
    font_bonus = get_font(14)
    
    title_text = "=== 选择你的研究风格 ==="
    title_surf = font_title.render(title_text, True, Colors.TEXT_WHITE)
    surf.blit(title_surf, (SCREEN_WIDTH // 2 - title_surf.get_width() // 2, 40))
    
    personalities = list(PERSONALITY_TYPES.items())
    box_width = 280
    box_gap = 30
    total_width = len(personalities) * box_width + (len(personalities) - 1) * box_gap
    start_x = (SCREEN_WIDTH - total_width) // 2
    box_y_start = 130
    box_height = 420
    
    mouse_pos = pygame.mouse.get_pos()
    
    for i, (pid, pdata) in enumerate(personalities):
        bx = start_x + i * (box_width + box_gap)
        by = box_y_start
        hovered = pygame.Rect(bx, by, box_width, box_height).collidepoint(mouse_pos)
        
        # Card background
        card_color = pdata["color"]
        card_surf = pygame.Surface((box_width, box_height))
        card_surf.set_alpha(200)
        card_surf.fill((30, 30, 40))
        surf.blit(card_surf, (bx, by))
        
        # Border
        border_color = card_color if hovered else Colors.BORDER
        border_width = 3 if hovered else 1
        pygame.draw.rect(surf, border_color, (bx, by, box_width, box_height), border_width)
        
        # Name
        name_surf = font_name.render(pdata["name"], True, card_color)
        surf.blit(name_surf, (bx + box_width // 2 - name_surf.get_width() // 2, by + 20))
        
        # Description (multiline)
        desc_lines = pdata["desc"].split("\n")
        for j, line in enumerate(desc_lines):
            line_surf = font_desc.render(line, True, Colors.TEXT_GRAY)
            surf.blit(line_surf, (bx + 15, by + 70 + j * 22))
        
        # Bonus text
        bonus_surf = font_bonus.render(pdata["bonus_text"], True, card_color)
        surf.blit(bonus_surf, (bx + 15, by + box_height - 60))
        
        # Key hint
        key_hint = font_desc.render(f"按 {i+1} 选择", True, Colors.TEXT_GRAY if not hovered else Colors.TEXT_WHITE)
        surf.blit(key_hint, (bx + box_width // 2 - key_hint.get_width() // 2, by + box_height - 30))
    
    # Bottom hint
    hint = font_desc.render("选择不同的研究风格会影响整个游戏体验", True, Colors.TEXT_GRAY)
    surf.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, SCREEN_HEIGHT - 50))


def draw_title_screen(surf, game):
    surf.fill(Colors.DARKER_BG)
    cx = SCREEN_WIDTH // 2
    cy = SCREEN_HEIGHT // 2
    
    for y in range(0, SCREEN_HEIGHT, 4):
        alpha = random.randint(10, 20)
        pygame.draw.line(surf, (0, 0, 0), (0, y), (SCREEN_WIDTH, y))
    
    title_surf = font_huge.render("Dogtor", True, Colors.TEXT_YELLOW)
    tx = cx - title_surf.get_width() // 2
    ty = cy - 120
    title_glitch = 0
    if (pygame.time.get_ticks() // 2000) % 3 == 0:
        title_glitch = random.randint(-3, 3)
    surf.blit(title_surf, (tx + title_glitch, ty + title_glitch // 2))
    
    subtitle = font_large.render("博士生生存模拟器", True, Colors.TEXT_WHITE)
    surf.blit(subtitle, (cx - subtitle.get_width() // 2, ty + 70))
    
    for i in range(5):
        dot_x = cx - 120 + i * 60
        dot_size = 6 + int(abs(math.sin(pygame.time.get_ticks() * 0.003 + i)) * 4)
        pygame.draw.rect(surf, Colors.TEXT_YELLOW, (dot_x, ty + 120, dot_size, dot_size))
    
    arc_count = len(STORY_ARCS)
    info = font_small.render(f"共 {arc_count} 个故事篇章 · 像素风对话冒险", True, Colors.TEXT_GRAY)
    surf.blit(info, (cx - info.get_width() // 2, ty + 160))
    
    if (pygame.time.get_ticks() // 600) % 2:
        start_text = font_large.render("按 SPACE 开始游戏", True, Colors.TEXT_WHITE)
        surf.blit(start_text, (cx - start_text.get_width() // 2, SCREEN_HEIGHT - 80))


def draw_intro_screen(surf, game):
    surf.fill(Colors.DARKER_BG)
    cx = SCREEN_WIDTH // 2
    cy = SCREEN_HEIGHT // 2
    
    if game.intro_index < len(INTRO_TEXT):
        text = INTRO_TEXT[game.intro_index]
        alpha = min(255, int(game.intro_timer * 2))
        color = (min(255, Colors.TEXT_WHITE[0]),
                 min(255, Colors.TEXT_WHITE[1]),
                 min(255, Colors.TEXT_WHITE[2]))
        text_surf = font_large.render(text, True, color)
        surf.blit(text_surf, (cx - text_surf.get_width() // 2, cy - 20))
    
    hint = font_small.render("按 SPACE 继续", True, Colors.TEXT_GRAY)
    surf.blit(hint, (cx - hint.get_width() // 2, SCREEN_HEIGHT - 60))


def draw_game_over_screen(surf, game):
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    surf.blit(overlay, (0, 0))
    
    cx = SCREEN_WIDTH // 2
    cy = SCREEN_HEIGHT // 2
    
    go_text = font_huge.render("游戏结束", True, Colors.TEXT_RED)
    surf.blit(go_text, (cx - go_text.get_width() // 2, cy - 100))
    
    msg = font_normal.render(game.game_over_text, True, Colors.TEXT_WHITE)
    surf.blit(msg, (cx - msg.get_width() // 2, cy - 30))
    
    bar_w, bar_h = 400, 25
    bar_x = cx - bar_w // 2
    bar_y = cy + 20
    pygame.draw.rect(surf, Colors.STRESS_BG, (bar_x, bar_y, bar_w, bar_h))
    pygame.draw.rect(surf, Colors.STRESS_CRIT, (bar_x, bar_y, bar_w, bar_h))
    pygame.draw.rect(surf, Colors.STRESS_BORDER, (bar_x, bar_y, bar_w, bar_h), 1)
    stress_label = font_small.render("压力: 100/100", True, Colors.TEXT_RED)
    surf.blit(stress_label, (bar_x + bar_w + 10, bar_y))
    
    if (pygame.time.get_ticks() // 600) % 2:
        restart = font_large.render("按 R 重新开始", True, Colors.TEXT_WHITE)
        surf.blit(restart, (cx - restart.get_width() // 2, cy + 80))


def draw_arc_transition(surf, game):
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    alpha = min(200, abs(math.sin(game.arc_transition_timer * 0.02)) * 200 + 30)
    overlay.fill((0, 0, 0, int(alpha)))
    surf.blit(overlay, (0, 0))
    
    cx = SCREEN_WIDTH // 2
    cy = SCREEN_HEIGHT // 2
    
    chapter_text = font_large.render("下一章", True, Colors.TEXT_GRAY)
    surf.blit(chapter_text, (cx - chapter_text.get_width() // 2, cy - 40))
    
    name_text = font_title.render(game.arc_transition_text, True, Colors.TEXT_YELLOW)
    surf.blit(name_text, (cx - name_text.get_width() // 2, cy + 10))
    
    completed = len(game.completed_arcs)
    total = len(STORY_ARCS)
    prog = font_small.render(f"已完成 {completed} 个章节", True, Colors.TEXT_GRAY)
    surf.blit(prog, (cx - prog.get_width() // 2, cy + 60))


def draw_playing_scene(surf, game):
    shake_x, shake_y = 0, 0
    if game.shake_timer > 0:
        shake_x = random.randint(-game.shake_intensity, game.shake_intensity)
        shake_y = random.randint(-game.shake_intensity, game.shake_intensity)
    
    # 场景区域
    scene_surf = pygame.Surface((SCREEN_WIDTH, SCENE_HEIGHT))
    scene_name = game.get_scene_name()
    render_scene(scene_surf, scene_name)
    surf.blit(scene_surf, (shake_x, shake_y))
    
    # 场景分隔线
    pygame.draw.line(surf, Colors.BORDER, (0, SCENE_HEIGHT), (SCREEN_WIDTH, SCENE_HEIGHT), 2)
    
    # 对话框
    draw_dialog_box(surf, game)
    
    # 计时器指示器
    draw_timer_indicator(surf, game)
    
    # 选项按钮
    draw_choice_buttons(surf, game)
    
    # 压力条
    draw_stress_bar(surf, game.stress)
    
    # Draw peer feedback
    if game.peer_timer > 0 and game.peer_text:
        peer_font = get_font(14)
        peer_color = Colors.TEXT_GRAY
        # Fade out effect
        alpha = min(255, game.peer_timer * 5)
        peer_surf = peer_font.render(game.peer_text, True, peer_color)
        peer_surf.set_alpha(alpha)
        surf.blit(peer_surf, (DIALOG_BOX_X + 20, DIALOG_BOX_Y + DIALOG_BOX_HEIGHT + 8))
    
    # Draw quiz result
    if game.quiz_result_timer > 0 and game.quiz_result_text:
        quiz_font = get_font(18)
        if "正确" in game.quiz_result_text:
            quiz_color = (80, 230, 80)
        else:
            quiz_color = (230, 60, 60)
        alpha = min(255, game.quiz_result_timer * 5)
        quiz_surf = quiz_font.render(game.quiz_result_text, True, quiz_color)
        quiz_surf.set_alpha(alpha)
        surf.blit(quiz_surf, (SCREEN_WIDTH // 2 - quiz_surf.get_width() // 2, CHOICE_START_Y + 120))


# ==================== 主循环 ====================

def handle_events(game):
    global running
    mouse_clicked = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_clicked = True
        if event.type == pygame.KEYDOWN:
            if game.state == STATE_TITLE:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    game.state = STATE_PERSONALITY
            elif game.state == STATE_PERSONALITY:
                pers_keys = list(PERSONALITY_TYPES.keys())
                if event.key == pygame.K_1 and len(pers_keys) >= 1:
                    game.personality = pers_keys[0]
                    game.state = STATE_INTRO
                    game.intro_index = 0
                    game.intro_timer = 0
                elif event.key == pygame.K_2 and len(pers_keys) >= 2:
                    game.personality = pers_keys[1]
                    game.state = STATE_INTRO
                    game.intro_index = 0
                    game.intro_timer = 0
                elif event.key == pygame.K_3 and len(pers_keys) >= 3:
                    game.personality = pers_keys[2]
                    game.state = STATE_INTRO
                    game.intro_index = 0
                    game.intro_timer = 0
            elif game.state == STATE_INTRO:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    game.intro_index += 1
                    game.intro_timer = 0
                    if game.intro_index >= len(INTRO_TEXT):
                        game.state = STATE_PLAYING
                        game.start_arc("first_meeting")
            elif game.state == STATE_PLAYING:
                if game.current_dialogue:
                    if game.show_options:
                        if event.key == pygame.K_1:
                            game.select_choice(0)
                        elif event.key == pygame.K_2:
                            game.select_choice(1)
                        elif event.key == pygame.K_3:
                            game.select_choice(2)
                    else:
                        if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                            game.skip_typewriter()
                if event.key == pygame.K_ESCAPE:
                    game.state = STATE_TITLE
            elif game.state == STATE_GAME_OVER:
                if event.key == pygame.K_r:
                    game.reset()
                    game.start_arc("first_meeting")
                elif event.key == pygame.K_ESCAPE:
                    game.state = STATE_TITLE
            elif game.state == STATE_ARC_TRANSITION:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    game.arc_transition_timer = 0
                    game.start_arc(game.current_arc_id)
    
    # Mouse click handling
    if mouse_clicked:
        mouse_pos = pygame.mouse.get_pos()
        if game.state == STATE_TITLE:
            game.state = STATE_PERSONALITY
        elif game.state == STATE_PERSONALITY:
            personalities = list(PERSONALITY_TYPES.items())
            box_width = 280
            box_gap = 30
            total_width = len(personalities) * box_width + (len(personalities) - 1) * box_gap
            start_x = (SCREEN_WIDTH - total_width) // 2
            box_y_start = 130
            box_height = 420
            for i, (pid, pdata) in enumerate(personalities):
                bx = start_x + i * (box_width + box_gap)
                if pygame.Rect(bx, box_y_start, box_width, box_height).collidepoint(mouse_pos):
                    game.personality = pid
                    game.state = STATE_INTRO
                    game.intro_index = 0
                    game.intro_timer = 0
                    break
        elif game.state == STATE_PLAYING and game.show_options:
            for i in range(3):
                bx = CHOICE_START_X + i * (CHOICE_BUTTON_WIDTH + CHOICE_BUTTON_GAP)
                by = CHOICE_START_Y
                if pygame.Rect(bx, by, CHOICE_BUTTON_WIDTH, CHOICE_BUTTON_HEIGHT).collidepoint(mouse_pos):
                    game.select_choice(i)
                    break
        elif game.state == STATE_GAME_OVER:
            game.reset()
            game.start_arc("first_meeting")
    
    return True, mouse_clicked


running = True

def main():
    global running
    game = Game()
    dt = 1.0 / FPS
    
    while running:
        continue_running, _ = handle_events(game)
        if not continue_running:
            break
        
        game.update(dt)
        
        screen.fill(Colors.DARK_BG)
        
        if game.state == STATE_TITLE:
            draw_title_screen(screen, game)
        elif game.state == STATE_PERSONALITY:
            draw_personality_screen(screen, game)
        elif game.state == STATE_INTRO:
            draw_intro_screen(screen, game)
        elif game.state == STATE_PLAYING:
            draw_playing_scene(screen, game)
        elif game.state == STATE_GAME_OVER:
            scene_name = game.get_scene_name()
            scene_surf = pygame.Surface((SCREEN_WIDTH, SCENE_HEIGHT))
            render_scene(scene_surf, scene_name)
            shake_x, shake_y = 0, 0
            if game.shake_timer > 0:
                shake_x = random.randint(-game.shake_intensity, game.shake_intensity)
                shake_y = random.randint(-game.shake_intensity, game.shake_intensity)
            screen.blit(scene_surf, (shake_x, shake_y))
            pygame.draw.line(screen, Colors.BORDER, (0, SCENE_HEIGHT), (SCREEN_WIDTH, SCENE_HEIGHT), 2)
            draw_dialog_box(screen, game)
            draw_stress_bar(screen, game.stress)
            draw_game_over_screen(screen, game)
        elif game.state == STATE_ARC_TRANSITION:
            scene_name = game.get_scene_name()
            scene_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            render_scene(scene_surf, scene_name)
            screen.blit(scene_surf, (0, 0))
            pygame.draw.line(screen, Colors.BORDER, (0, SCENE_HEIGHT), (SCREEN_WIDTH, SCENE_HEIGHT), 2)
            draw_arc_transition(screen, game)
        
        draw_scanlines(screen)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
