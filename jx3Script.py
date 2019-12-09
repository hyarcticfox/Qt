import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QIcon
from MainWin import *
from Script import *

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initUi()
        self.Note()

    def Note(self):
        self.textBrowser.append("宏仅供参考，避风塘团内使用，暂勿传播，某些职业奇穴可能有问题，及时反馈")

    def initUi(self):
        self.setWindowIcon(QIcon("./hy.ico"))


class ScriptWindow(QDialog, Ui_Script):
    def __init__(self):
        super(ScriptWindow, self).__init__()
        self.setupUi(self)
        self.pushButtonCopy_1.clicked.connect(self.ScriptCopy1)
        self.pushButtonCopy_2.clicked.connect(self.ScriptCopy2)
        self.pushButtonCopy_3.clicked.connect(self.ScriptCopy3)

    def AXScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast [nobuff:激雷] 撼如雷")
        self.textEditScript1.append("/cast [rage<3|bufftime:破楼兰<1.5] 灭")
        self.textEditScript1.append("/cast [rage<4|tnobuff:流血|tbufftime:流血<3] 龙吟")
        self.textEditScript1.append("/cast [rage=5] 龙牙")
        self.textEditScript1.append("/cast 穿云")

        self.textEditScript2.clear()
        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("手动突，风")
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()

        self.textTalent.clear()
        self.textTalent.append("[扬戈],[神勇],[徐如林],[击水],[劲风],[风虎],[破楼兰],[战心],[牧云],[激雷],[龙血],[虎贲]")
    def JCScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast 人剑合一")
        self.textEditScript1.append("/cast [qidian>8] 无我无剑")
        self.textEditScript1.append("/cast [bufftime:玄门>32] 碎星辰")
        self.textEditScript1.append("/cast [bufftime:玄门<32] 吞日月")
        self.textEditScript1.append("/cast 生太极")
        self.textEditScript1.append("/cast 八荒归元")
        self.textEditScript1.append("/cast 吞日月")
        self.textEditScript1.append("/cast 三环套月")

        self.textEditScript2.clear()
        self.textEditScript2.append("/cast [bufftime:玄门<3] 人剑合一")
        self.textEditScript2.append("/cast [nobuff:碎星辰] 碎星辰")
        self.textEditScript2.append("/cast [qidian<10] 八荒归元")
        self.textEditScript2.append("/cast [nobuff:紫气东来&qidian<8] 三环套月")
        self.textEditScript2.append("/cast 无我无剑")
        self.textEditScript2.append("/cast 八荒归元")


        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("云中剑理论上没有宏，仅供懒人使用")
        self.textEditInstruct2.clear()
        self.textEditInstruct2.append("无意混子一键宏")
        self.textEditInstruct3.clear()

        self.textTalent.clear()
        self.textTalent.append("云中剑：[心固],[深埋],[昆吾],[云中剑],[风逝],[叠刃],[长生],[负阴],[和光],[期声],[无欲],[玄门]")
        self.textTalent.append("无意流：[心固],[深埋],[昆吾],[无意],[风逝],[叠刃],[切玉],[负阴],[和光],[期声],[无欲],[玄门]")
        self.textTalent.append("第三个奇穴如果缺蓝洗化三清，群攻洗白虹")
    def CJScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast [buff:夜雨] 云飞玉皇")
        self.textEditScript1.append("/cast [buff:夜雨&rage>50|rage<45] 松舍问霞")
        self.textEditScript1.append("/cast [buff:夜雨&rage<10|rage>6] 听雷")
        self.textEditScript1.append("/cast 夕照雷峰")
        self.textEditScript1.append("/cast 听雷")
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("懒人造化宏，进阶请删掉所有带听雷语句")

        self.textEditScript2.clear()
        self.textEditScript2.append("/cast [buff:凤鸣] 松舍问霞")
        self.textEditScript2.append("/cast [buff:夜雨] 云飞玉皇")
        self.textEditScript2.append("/cast [nobuff:凤鸣&rage<97] 听雷")
        self.textEditScript2.append("/cast 夕照雷峰")

        self.textEditScript3.clear()
        self.textEditInstruct2.clear()
        self.textEditInstruct2.append("映波宏")
        self.textEditInstruct3.clear()
        self.textTalent.clear()
        self.textTalent.append("[淘尽]-[清风]-[夜雨]-[夜风]-[造化/映波锁澜]-[怜光]-[层云]-[厌高]-[山重水复]-[碧归]-[如风]-[松舍问霞]")
        self.textTalent.append("香鸡厌高洗梅隐香，群攻松舍改孤鸾，大战十人本碧归可以换残雪")
    def BDScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast 雷走风切")
        self.textEditScript1.append("/cast 上将军印")
        self.textEditScript1.append("/cast [bufftime:尘身<1] 停止释放")
        self.textEditScript1.append("/cast [nobuff:疏狂] 西楚悲歌")
        self.textEditScript1.append("/cast [rage<40] 龙骧虎步")
        self.textEditScript1.append("/cast [rage>30] 破釜沉舟")
        self.textEditScript1.append("/cast 雪絮金屏")
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("大刀宏，洗疏狂，不洗疏狂删去第四行，手动破釜删去第五行")

        self.textEditScript2.clear()
        self.textEditScript2.append("/cast 坚壁清野")
        self.textEditScript2.append("/cast [nobuff:上将军印|bufftime:上将军印<1.1] 秀明尘身")
        self.textEditScript2.append("/cast 刀啸风吟")
        self.textEditScript2.append("/cast [sun<10] 松烟竹雾")
        self.textEditInstruct2.clear()
        self.textEditInstruct2.append("鞘刀宏")

        self.textEditScript3.clear()
        self.textEditScript3.append("/cast 雷走风切")
        self.textEditScript3.append("/cast [tnobuff:闹须弥] 闹须弥")
        self.textEditScript3.append("/cast [rage>20&sun>20] 雪絮金屏")
        self.textEditScript3.append("/cast 擒龙六斩")
        self.textEditScript3.append("/cast 逐鹰式")
        self.textEditScript3.append("/cast 控鹤式")
        self.textEditScript3.append("/cast 雪絮金屏")
        self.textEditInstruct3.clear()
        self.textEditInstruct3.append("双刀宏")

        self.textTalent.clear()
        self.textTalent.append("[孤漠]-[归酣]-[阳关]-[霜天]-[啸吒]-[砺锋]-[分疆]-[星火]-[楚歌]-[绝期]-[重烟]-[心境]")
        self.textTalent.append("洗脚阳关换疏狂")
    def FSScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast [nobuff:血怒] 血怒")
        self.textEditScript1.append("/cast [rage>30&tbuff:流血] 盾猛")
        self.textEditScript1.append("/cast 盾压")
        self.textEditScript1.append("/cast 盾刀")
        self.textEditScript1.append("/cast [rage>60] 盾飞")
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("盾宏")

        self.textEditScript2.clear()
        self.textEditScript2.append("/cast [nobuff:血怒] 血怒")
        self.textEditScript2.append("/cast [bufftime:盾飞<3|tbufftime:流血<3|tnobuff:流血|rage<45] 斩刀")
        self.textEditScript2.append("/cast [tbufftime:流血>17] 闪刀")
        self.textEditScript2.append("/cast 劫刀")
        self.textEditInstruct2.clear()
        self.textEditInstruct2.append("刀宏")


        self.textEditScript3.clear()
        self.textEditInstruct3.clear()
        self.textTalent.clear()
        self.textTalent.append("[刀魂]-[炼狱]-[飞瀑]-[劫生]-[锋鸣]-[割裂]-[活脉]-[恋战]-[从容]-[愤恨]-[蔑视]-[骇日]")
        self.textTalent.append("盾飞持续秘籍不点")

    def CYTScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast [tnobuff:流血&buff:寒甲&rage>15] 盾飞")
        self.textEditScript1.append("/cast [rage>99&nobuff:盾档] 盾挡")
        self.textEditScript1.append("/cast [life<0.8] 血怒")
        self.textEditScript1.append("/cast 盾压")
        self.textEditScript1.append("/cast 盾刀")
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("单刷宏，盾宏")

        self.textEditScript2.clear()
        self.textEditScript2.append("/cast [rage<15] 血怒")
        self.textEditScript2.append("/cast 斩刀")
        self.textEditScript2.append("/cast [tbuff:流血|tbufftime:盾威<13] 盾回")
        self.textEditInstruct2.clear()
        self.textEditInstruct2.append("单刷宏，刀宏")

        self.textEditScript3.clear()
        self.textEditInstruct3.clear()

        self.textTalent.clear()
        self.textTalent.append("[盾威]-[炼狱]-[铿锵]-[坚铁]-[千山]-[割裂]-[活血]-[雄峦]-[从容]-[寒甲]-[叱威]-[澄生]")

    def JYScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("[tnobuff:穿心|tbufftime:穿心<3] 穿心弩")
        self.textEditScript1.append("/cast 暴雨梨花针")
        self.textEditScript1.append("/cast [buff:追命无声] 追命箭")
        self.textEditScript1.append("/cast 夺魄箭")
        self.textEditScript1.append("/cast 逐星箭")
        self.textEditScript1.append("/cast 裂石弩")

        self.textEditScript2.clear()
        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("手动开心无，且开心无的时机为：暴雨追命均未CD，且身上至少有一层无声buff。")
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()

        self.textTalent.clear()
        self.textTalent.append("[迅电流光][千里无痕][狂风暴雨][摧心][穿林打叶][浴血沁骨][声若惊雷][梨花带雨][秋风散影][回肠荡气][妙手连环][奥妙无穷]")


    def GBScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast 酒中仙")
        self.textEditScript1.append("/cast 潜龙勿用")
        self.textEditScript1.append("/cast [mana>0.35] 龙战于野")
        self.textEditScript1.append("/cast [mana>0.42] 龙跃于渊")
        self.textEditScript1.append("/cast 亢龙有悔")
        self.textEditScript1.append("/cast 拨狗朝天")
        self.textEditScript1.append("/cast 棒打狗头")

        self.textEditScript2.clear()
        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("一掌宏，拨狗会心回蓝秘籍不要点，酒中仙3CD1读条")
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()

        self.textTalent.clear()
        self.textTalent.append("[玄黄]-[御龙]-[自强]-[无疆]-[益元]-[越渊]-[满盈]-[驯至]-[贞固]-[复礼]-[饮江]-[潜龙勿用]")

    def TCTScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast [life<0.2] 啸如虎")
        self.textEditScript1.append("/cast [tnobuff:破风] 龙吟")
        self.textEditScript1.append("/cast [rage=5] 龙牙")
        self.textEditScript1.append("/cast 灭")
        self.textEditScript1.append("/cast 龙吟")
        self.textEditScript1.append("/cast 穿云")

        self.textEditScript2.clear()
        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("手动沧月，山，风")
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()

        self.textTalent.clear()
        self.textTalent.append("[定军]-[龙痕]-[大漠]-[望西京]-[劲风]-[掠如火]-[踏北邙]-[战心]-[长征/渊]-[昂如岳/坚城]-[载戎/戟胜]-[号令三军]")
        self.textTalent.append("后面几个奇穴主要根据BOSS调整")
    def PLScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/fcast 翼绝云天")
        self.textEditScript1.append("/cast 振翅图南")
        self.textEditScript1.append("/cast [buff:梦悠&skill_energy:物化天行>0] 浮游天地")
        self.textEditScript1.append("/cast 木落雁归")
        self.textEditScript1.append("/cast 跃潮斩波")
        self.textEditScript1.append("/cast 击水三千")

        self.textEditScript2.clear()
        self.textEditScript2.append("/fcast 翼绝云天")
        self.textEditScript2.append("/cast 振翅图南")
        self.textEditScript2.append("/cast 物化天行")
        self.textEditScript2.append("/cast 海运南冥")
        self.textEditScript2.append("/cast 溟海御波")
        self.textEditScript2.append("/cast 逐波灵游")
        self.textEditScript2.append("/cast [skill_energy:物化天行<2] 木落雁归")

        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("地宏")
        self.textEditInstruct2.clear()
        self.textEditInstruct2.append("天宏")
        self.textEditInstruct3.clear()
        self.textEditInstruct3.append("起手定波砥澜蓄力，后面当定波CD好了且物化层数大于等于1层时手动定波蓄力，在天上无技能时手动跃潮或者落地")

        self.textTalent.clear()
        self.textTalent.append("[海隅]-[扶桑]-[羽彰]-[清源]-[太息]-[伞意]-[罔象]-[怅归]-[藏锋]-[驰行]-[梦悠]-[濯流]")

    def YJScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast [qidian>2] 罗汉金身")
        self.textEditScript1.append("/cast [qidian>2] 拿云式")
        self.textEditScript1.append("/cast [qidian>2] 韦陀献杵")
        self.textEditScript1.append("/cast [tbufftime:普渡>7&buff:擒龙诀|tbufftime:普渡>2] 守缺式")
        self.textEditScript1.append("/cast 普渡四方")

        self.textEditScript2.clear()
        self.textEditScript2.append("/cast [qidian>2] 拿云式")
        self.textEditScript2.append("/cast [qidian>2] 韦陀献杵")
        self.textEditScript2.append("/cast 守缺式")
        self.textEditScript2.append("/cast 普渡四方")

        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("洗脚宏，DOT结束且小于3豆时手动横扫")
        self.textEditInstruct2.clear()
        self.textEditInstruct2.append("明澈宏，DOT结束且小于3豆时手动横扫，蓝下百分之10，一豆的时候用金身回蓝")
        self.textEditInstruct3.clear()

        self.textTalent.clear()
        self.textTalent.append("[涅果][幻身][明法][缩地][降魔渡厄][金刚怒目][净果][三生][众嗔][华香][佛果/明澈][二业依缘]")

    def HSTScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast 擒龙诀")
        self.textEditScript1.append("/cast [qidian>2] 韦陀献杵")
        self.textEditScript1.append("/cast [qidian>2] 罗汉金身")
        self.textEditScript1.append("/cast [qidian>2] 立地成佛")
        self.textEditScript1.append("/cast 普渡四方")

        self.textEditScript2.clear()

        self.textEditScript3.clear()
        self.textEditInstruct1.clear()

        self.textEditInstruct2.clear()

        self.textEditInstruct3.clear()
        self.textTalent.clear()
        self.textTalent.append("[不垢][取法][执迷不返][归去来棍][生缘][立地成佛][天龙音][明王身][无量][轮回决][独觉][舍身弘法]")


    def BXScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast [buff:枕上=5] 繁音急节")
        self.textEditScript1.append("/fcast [tbufftime:急曲<2|tbuff:急曲<3|tnobuff:急曲] 剑破虚空")
        self.textEditScript1.append("/cast 玳弦急曲")

        self.textEditScript2.clear()
        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()

        self.textTalent.clear()
        self.textTalent.append("洗脚：[明妃]-[千里冰封]-[新妆]-[青梅]-[枕上]-[生莲]-[望舒]-[元君]-[霜风]-[朝露]-[焕颜]-[清娟]")
        self.textTalent.append("不洗脚：[青梅嗅]-[千里冰封]-[新妆]-[青梅]-[枕上]-[生莲]-[望舒]-[元君]-[霜风]-[朝露]-[焕颜]-[霜降]")
        self.textTalent.append("理性打团，和谐第一")

    def HJScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast [tnobuff:兰摧玉折] 兰摧玉折")
        self.textEditScript1.append("/cast [tnobuff:钟林毓秀&tbufftime:商阳指>16.6] 钟林毓秀")
        self.textEditScript1.append("/cast [tnobuff:商阳指] 商阳指")
        self.textEditScript1.append("/cast 玉石俱焚")
        self.textEditScript1.append("/cast 快雪时晴")

        self.textEditScript2.clear()
        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("延迟过高或网速不佳的情况下会挂双钟林，请根据网速或延迟情况自行修改16.6的数值，延迟越高数值越小。手动点掉流离buff")
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()

        self.textTalent.clear()
        self.textTalent.append("[弹指]-[雪中行]-[倚天]-[焚玉]-[青歌]-[青冠]-[清流]-[雪弃]-[流离]-[梦歌]-[踏歌]-[涓流]")

    def FYScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast 净世破魔击")
        self.textEditScript1.append("/cast [sun<22&moon<35] 银月斩")
        self.textEditScript1.append("/cast [moon<80] 驱夜断愁")
        self.textEditScript1.append("/cast [sun<60] 烈日斩")
        self.textEditScript1.append("/cast [sun<80] 赤日轮")
        self.textEditScript1.append("/cast [sun<100&moon<100] 幽月轮")

        self.textEditScript2.clear()
        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()

        self.textTalent.clear()
        self.textTalent.append("[腾焰飞芒][净身明礼][洞若观火][无明业火][明光恒照][辉耀红尘][用晦而明][日月同辉][天地诛戮][寂灭劫灰][万念俱灰][驱夷逐法]")

    def MJTScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast 心火叹")
        self.textEditScript1.append("/cast 生死劫")
        self.textEditScript1.append("/cast [tnobuff:戒火|tbufftime:戒火<3] 戒火斩")
        self.textEditScript1.append("/cast [moon>sun] 银月斩")
        self.textEditScript1.append("/cast [moon>sun] 幽月轮")
        self.textEditScript1.append("/cast 烈日斩")
        self.textEditScript1.append("/cast 赤日轮")

        self.textEditScript2.clear()
        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("生死劫宏")
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()

        self.textTalent.clear()
        self.textTalent.append("[圣光明][慈悲心][寂灭][月尽天明][超凡入圣][极乐引][纵遇善缘][妙镜惊寂][渡厄力][日月同辉][无量妙镜][心火叹]")
        self.textTalent.append("最后一个奇穴根据BOSS调整")
    def DJScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast [tnobuff:蛇影|tbufftime:蛇影<=2] 蛇影")
        self.textEditScript1.append("/cast 蛊虫献祭")
        self.textEditScript1.append("/cast 灵蛇引")
        self.textEditScript1.append("/cast 攻击")
        self.textEditScript1.append("/fcast 幻击")
        self.textEditScript1.append("/cast 百足")
        self.textEditScript1.append("/cast 蟾啸")
        self.textEditScript1.append("/cast 蝎心")

        self.textEditScript2.clear()
        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("手动灵蛊")
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()
        self.textTalent.clear()
        self.textTalent.append("[尻尾]-[无常]-[黯影]-[虫兽]-[蝉啸]-[不鸣]-[尾后针]-[祭礼]-[蛇悉]-[蛊虫狂暴]-[啖灵]-[封丘]")
        self.textTalent.append("洗脚蛇悉换分澜，回蓝蝉啸换桃僵，理性打团，和谐第一")

    def QCScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/fcast [nobuff:破苍穹] 破苍穹")
        self.textEditScript1.append("/cast [nobuff:气剑|bufftime:气剑<1.7] 万世不竭")
        self.textEditScript1.append("/fcast [qidian>7] 两仪化形")
        self.textEditScript1.append("/fcast 四象轮回")

        self.textEditScript2.clear()
        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("手动剑出、六合、紫气")
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()
        self.textTalent.clear()
        self.textTalent.append("[白虹]-[心固]-[同尘]-[无形]-[天地根]-[跬步]-[万物]-[抱阳]-[浮生]-[期声]-[重光]-[剑出鸿蒙]")
        self.textTalent.append("回蓝无形换化三清，大无敌期声换心眼，无敌战斗重置剑出换规焉，理性打团，和谐第一")

    def TLScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast 暗藏杀机")
        self.textEditScript1.append("/cast [tnobuff:化血|tbufftime:化血<6] 天女散花")
        self.textEditScript1.append("/cast [buff:鬼斧神工] 心无旁骛")
        self.textEditScript1.append("/cast [tbufftime:化血>6] 暴雨梨花针")
        self.textEditScript1.append("/cast 天绝地灭")
        self.textEditScript1.append("/cast 蚀肌弹")

        self.textEditScript2.clear()
        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("手动千机变连弩攻击，图穷匕见")
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()

        self.textTalent.clear()
        self.textTalent.append("[毒手尊拳][劫数难逃][弩击急骤][千机之威][千机巨擘][聚精凝神][化血迷心][蚀肌化血][[秋风散影][回肠荡气][曙色催寒][雷甲三铉]")

    def MWScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast 高山流水")
        self.textEditScript1.append("/cast [skill_energy:疏影横斜>1|buff:孤影化双] 疏影横斜")
        self.textEditScript1.append("/cast 变宫")
        self.textEditScript1.append("/fcast 剑·宫")

        self.textEditScript2.clear()
        self.textEditScript2.append("/fcast 阳春白雪")
        self.textEditScript2.append("/cast 疏影横斜")
        self.textEditScript2.append("/cast [nobuff:清绝影歌] 清绝影歌")

        self.textEditScript3.clear()
        self.textEditScript3.append("/cast 疏影横斜")
        self.textEditScript3.append("/cast 高山流水")
        self.textEditScript3.append("/cast [tnobuff:商] 商")
        self.textEditScript3.append("/cast [tnobuff:角] 角")
        self.textEditScript3.append("/cast [bufftime:青霄飞羽<1.38] 羽")
        self.textEditScript3.append("/cast 变宫")
        self.textEditScript3.append("/cast 羽")

        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("高山一键宏")
        self.textEditInstruct2.clear()
        self.textEditInstruct2.append("高山一键宏，切剑阳春，清绝影歌好了就用")
        self.textEditInstruct3.clear()
        self.textEditInstruct3.append("鹿鸣流一键宏，建议加速1269")

        self.textTalent.clear()
        self.textTalent.append("高山宏：[音朗]-[飞帆]-[洞天]-[照月]-[浮影]-[师襄]-[别鹤]-[弄影]-[徊影]-[云汉]-[凝眉]-[鹿鸣]")
        self.textTalent.append("鹿鸣宏：[音朗]-[风入松]-[洞天]-[殊曲]-[气略]-[师襄]-[别鹤]-[刻梦]-[相仿]-[云汉]-[凝眉]-[鹿鸣]")

    def ScriptCopy1(self):
        self.textEditScript1.selectAll()
        self.textEditScript1.copy()

    def ScriptCopy2(self):
        self.textEditScript2.selectAll()
        self.textEditScript2.copy()

    def ScriptCopy3(self):
        self.textEditScript3.selectAll()
        self.textEditScript3.copy()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    scriptWin = ScriptWindow()
    mainWin.show()

    mainWin.pushButtonAX.clicked.connect(scriptWin.AXScript)
    mainWin.pushButtonCJ.clicked.connect(scriptWin.CJScript)
    mainWin.pushButtonJC.clicked.connect(scriptWin.JCScript)
    mainWin.pushButtonBD.clicked.connect(scriptWin.BDScript)
    mainWin.pushButtonFS.clicked.connect(scriptWin.FSScript)
    mainWin.pushButtonCYT.clicked.connect(scriptWin.CYTScript)
    mainWin.pushButtonJY.clicked.connect(scriptWin.JYScript)
    mainWin.pushButtonGB.clicked.connect(scriptWin.GBScript)
    mainWin.pushButtonTCT.clicked.connect(scriptWin.TCTScript)
    mainWin.pushButtonPL.clicked.connect(scriptWin.PLScript)
    mainWin.pushButtonYJ.clicked.connect(scriptWin.YJScript)
    mainWin.pushButtonHST.clicked.connect(scriptWin.HSTScript)
    mainWin.pushButtonBX.clicked.connect(scriptWin.BXScript)
    mainWin.pushButtonHJ.clicked.connect(scriptWin.HJScript)
    mainWin.pushButtonFY.clicked.connect(scriptWin.FYScript)
    mainWin.pushButtonMJT.clicked.connect(scriptWin.MJTScript)
    mainWin.pushButtonDJ.clicked.connect(scriptWin.DJScript)
    mainWin.pushButtonQC.clicked.connect(scriptWin.QCScript)
    mainWin.pushButtonTL.clicked.connect(scriptWin.TLScript)
    mainWin.pushButtonMW.clicked.connect(scriptWin.MWScript)

    sys.exit(app.exec_())