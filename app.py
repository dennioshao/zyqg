#app.py
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# 完整的64卦数据
gua_data = [
    {"name": "乾卦", "symbol": "111111", "gua_ci": "元亨利贞", "wu_xing": "金"},
    {"name": "坤卦", "symbol": "000000", "gua_ci": "利牝马之贞", "wu_xing": "土"},
    {"name": "屯卦", "symbol": "010001", "gua_ci": "元亨利贞，勿用有攸往", "wu_xing": "水"},
    {"name": "蒙卦", "symbol": "100010", "gua_ci": "亨，匪我求童蒙", "wu_xing": "水"},
    {"name": "需卦", "symbol": "010111", "gua_ci": "有孚，光亨，贞吉", "wu_xing": "水"},
    {"name": "讼卦", "symbol": "111010", "gua_ci": "有孚窒，惕中吉", "wu_xing": "金"},
    {"name": "师卦", "symbol": "000010", "gua_ci": "贞，丈人吉", "wu_xing": "土"},
    {"name": "比卦", "symbol": "010000", "gua_ci": "吉，原筮元永贞", "wu_xing": "水"},
    {"name": "小畜卦", "symbol": "110111", "gua_ci": "亨，密云不雨", "wu_xing": "木"},
    {"name": "履卦", "symbol": "111011", "gua_ci": "履虎尾，不咥人，亨", "wu_xing": "金"},
    {"name": "泰卦", "symbol": "000111", "gua_ci": "小往大来，吉亨", "wu_xing": "土"},
    {"name": "否卦", "symbol": "111000", "gua_ci": "否之匪人，不利君子贞", "wu_xing": "金"},
    {"name": "同人卦", "symbol": "111101", "gua_ci": "同人于野，亨", "wu_xing": "金"},
    {"name": "大有卦", "symbol": "101111", "gua_ci": "元亨", "wu_xing": "火"},
    {"name": "谦卦", "symbol": "000100", "gua_ci": "亨，君子有终", "wu_xing": "土"},
    {"name": "豫卦", "symbol": "001000", "gua_ci": "利建侯行师", "wu_xing": "土"},
    {"name": "随卦", "symbol": "011001", "gua_ci": "元亨利贞，无咎", "wu_xing": "木"},
    {"name": "蛊卦", "symbol": "100110", "gua_ci": "元亨，利涉大川", "wu_xing": "木"},
    {"name": "临卦", "symbol": "000011", "gua_ci": "元亨利贞，至于八月有凶", "wu_xing": "土"},
    {"name": "观卦", "symbol": "110000", "gua_ci": "盥而不荐，有孚颙若", "wu_xing": "木"},
    {"name": "噬嗑卦", "symbol": "101001", "gua_ci": "亨，利用狱", "wu_xing": "火"},
    {"name": "贲卦", "symbol": "100101", "gua_ci": "亨，小利有攸往", "wu_xing": "火"},
    {"name": "剥卦", "symbol": "100000", "gua_ci": "不利有攸往", "wu_xing": "土"},
    {"name": "复卦", "symbol": "000001", "gua_ci": "亨，出入无疾", "wu_xing": "土"},
    {"name": "无妄卦", "symbol": "111001", "gua_ci": "元亨利贞", "wu_xing": "金"},
    {"name": "大畜卦", "symbol": "100111", "gua_ci": "利贞，不家食吉", "wu_xing": "木"},
    {"name": "颐卦", "symbol": "100001", "gua_ci": "贞吉，观颐", "wu_xing": "木"},
    {"name": "大过卦", "symbol": "011110", "gua_ci": "栋桡，利有攸往", "wu_xing": "木"},
    {"name": "坎卦", "symbol": "010010", "gua_ci": "有孚维心，亨", "wu_xing": "水"},
    {"name": "离卦", "symbol": "101101", "gua_ci": "利贞，亨", "wu_xing": "火"},
    {"name": "咸卦", "symbol": "011100", "gua_ci": "亨，利贞", "wu_xing": "木"},
    {"name": "恒卦", "symbol": "001110", "gua_ci": "亨，无咎，利贞", "wu_xing": "木"},
    {"name": "遁卦", "symbol": "111100", "gua_ci": "亨，小利贞", "wu_xing": "金"},
    {"name": "大壮卦", "symbol": "001111", "gua_ci": "利贞", "wu_xing": "土"},
    {"name": "晋卦", "symbol": "101000", "gua_ci": "康侯用锡马蕃庶", "wu_xing": "火"},
    {"name": "明夷卦", "symbol": "000101", "gua_ci": "利艰贞", "wu_xing": "土"},
    {"name": "家人卦", "symbol": "110101", "gua_ci": "利女贞", "wu_xing": "木"},
    {"name": "睽卦", "symbol": "101110", "gua_ci": "小事吉", "wu_xing": "火"},
    {"name": "蹇卦", "symbol": "010100", "gua_ci": "利西南，不利东北", "wu_xing": "水"},
    {"name": "解卦", "symbol": "001010", "gua_ci": "利西南，无所往", "wu_xing": "水"},
    {"name": "损卦", "symbol": "100011", "gua_ci": "有孚，元吉", "wu_xing": "木"},
    {"name": "益卦", "symbol": "110010", "gua_ci": "利有攸往，利涉大川", "wu_xing": "木"},
    {"name": "夬卦", "symbol": "111110", "gua_ci": "扬于王庭，孚号", "wu_xing": "金"},
    {"name": "姤卦", "symbol": "011111", "gua_ci": "女壮，勿用取女", "wu_xing": "木"},
    {"name": "萃卦", "symbol": "011000", "gua_ci": "亨，王假有庙", "wu_xing": "土"},
    {"name": "升卦", "symbol": "000110", "gua_ci": "元亨，用见大人", "wu_xing": "土"},
    {"name": "困卦", "symbol": "011010", "gua_ci": "亨，贞大人吉", "wu_xing": "水"},
    {"name": "井卦", "symbol": "010110", "gua_ci": "改邑不改井", "wu_xing": "水"},
    {"name": "革卦", "symbol": "011101", "gua_ci": "己日乃孚，元亨", "wu_xing": "火"},
    {"name": "鼎卦", "symbol": "101011", "gua_ci": "元吉，亨", "wu_xing": "火"},
    {"name": "震卦", "symbol": "001001", "gua_ci": "亨，震来虩虩", "wu_xing": "木"},
    {"name": "艮卦", "symbol": "100100", "gua_ci": "艮其背，不获其身", "wu_xing": "土"},
    {"name": "渐卦", "symbol": "110100", "gua_ci": "女归吉，利贞", "wu_xing": "木"},
    {"name": "归妹卦", "symbol": "001110", "gua_ci": "征凶，无攸利", "wu_xing": "木"},
    {"name": "丰卦", "symbol": "001101", "gua_ci": "亨，王假之", "wu_xing": "火"},
    {"name": "旅卦", "symbol": "101100", "gua_ci": "小亨，旅贞吉", "wu_xing": "火"},
    {"name": "巽卦", "symbol": "110110", "gua_ci": "小亨，利有攸往", "wu_xing": "木"},
    {"name": "兑卦", "symbol": "011011", "gua_ci": "亨，利贞", "wu_xing": "金"},
    {"name": "涣卦", "symbol": "110010", "gua_ci": "亨，王假有庙", "wu_xing": "水"},
    {"name": "节卦", "symbol": "010011", "gua_ci": "亨，苦节不可贞", "wu_xing": "水"},
    {"name": "中孚卦", "symbol": "011110", "gua_ci": "豚鱼吉，利涉大川", "wu_xing": "木"},
    {"name": "小过卦", "symbol": "001100", "gua_ci": "亨，利贞", "wu_xing": "木"},
    {"name": "既济卦", "symbol": "010101", "gua_ci": "亨小，利贞", "wu_xing": "水"},
    {"name": "未济卦", "symbol": "101010", "gua_ci": "亨，小狐汔济", "wu_xing": "火"}
]

# 五行相生相克关系
wu_xing_relations = {
    "金": {"生": "水", "克": "木"},
    "木": {"生": "火", "克": "土"},
    "水": {"生": "木", "克": "火"},
    "火": {"生": "土", "克": "金"},
    "土": {"生": "金", "克": "水"}
}

# 随机起卦函数
def generate_gua():
    gua_binary = ''.join([str(random.randint(0, 1)) for _ in range(6)])
    for gua in gua_data:
        if gua["symbol"] == gua_binary:
            return gua
    return gua_data[0]  # 默认返回乾卦

# 五行分析函数
def analyze_wu_xing(gua):
    wu_xing = gua["wu_xing"]
    sheng = wu_xing_relations[wu_xing]["生"]
    ke = wu_xing_relations[wu_xing]["克"]
    return f"此卦五行属{wu_xing}，利于{sheng}，受制于{ke}。"

# 统一路由处理输入和结果
# 统一路由处理输入和结果
@app.route('/', methods=['GET'])
def index():
    user_input = request.args.get('input', None)
    if user_input:  # 如果有输入，渲染结果页面
        gua = generate_gua()
        wu_xing_analysis = analyze_wu_xing(gua)
        luck_words = ["大吉", "吉", "中平", "小吉", "凶", "大凶"]
        luck = random.choice(luck_words)
        return render_template('result.html', gua=gua, analysis=wu_xing_analysis, user_input=user_input, luck=luck)
    else:  # 无输入，渲染输入页面
        return render_template('index.html')