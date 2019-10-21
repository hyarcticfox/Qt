import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from MainWin import *
from Script import *

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        """
       
        self.Note()



"""
    def Note(self):
        self.textBrowser.append("宏仅供参考，避风塘团内使用，暂勿传播，暂时没找到好用的蓬莱宏、莫问宏")

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

    def JYScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast [tnobuff: 穿心 | tbufftime: 穿心 < 3] 穿心弩")
        self.textEditScript1.append("/fcast 暴雨梨花针")
        self.textEditScript1.append("/cast 夺魄箭")
        self.textEditScript1.append("/cast 心无旁骛")
        self.textEditScript1.append("/cast [energy<41] 百里追魂")
        self.textEditScript1.append("/cast 追命箭")

        self.textEditScript2.clear()
        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()

    def GBScript(self):
        self.show()
        self.textEditScript1.clear()
        self.textEditScript1.append("/cast 酒中仙")
        self.textEditScript1.append("/cast 潜龙勿用")
        self.textEditScript1.append("/cast [mana>0.35] 龙战于野")
        self.textEditScript1.append("/cast [mana>0.42] 龙跃于渊")
        self.textEditScript1.append("/cast 拨狗朝天")
        self.textEditScript1.append("/cast 棒打狗头")

        self.textEditScript2.clear()
        self.textEditScript3.clear()
        self.textEditInstruct1.clear()
        self.textEditInstruct1.append("一掌宏，拨狗会心回蓝秘籍不要点，酒中仙3CD1读条")
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()

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
        self.textEditInstruct2.clear()
        self.textEditInstruct3.clear()

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
    mainWin.pushButtonYJ.clicked.connect(scriptWin.YJScript)
    mainWin.pushButtonHST.clicked.connect(scriptWin.HSTScript)
    mainWin.pushButtonBX.clicked.connect(scriptWin.BXScript)
    mainWin.pushButtonHJ.clicked.connect(scriptWin.HJScript)
    mainWin.pushButtonFY.clicked.connect(scriptWin.FYScript)
    mainWin.pushButtonMJT.clicked.connect(scriptWin.MJTScript)
    mainWin.pushButtonDJ.clicked.connect(scriptWin.DJScript)
    mainWin.pushButtonQC.clicked.connect(scriptWin.QCScript)
    mainWin.pushButtonTL.clicked.connect(scriptWin.TLScript)

    sys.exit(app.exec_())