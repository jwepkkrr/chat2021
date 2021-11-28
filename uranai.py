import time
import random
import IPython
from google.colab import output


n = 0 
def chat(text, **kw):  #チャット用の関数（ここを書き換える）
  global n
  n += 1
  return 'ほ' * n

# アイコンの指定
BOT_ICON = 'https://2.bp.blogspot.com/-ZLhOf_T1yNw/U9zBtKvfYbI/AAAAAAAAjl8/twAFdgLth2c/s800/eto_hitsuji_aisatsu.png'
YOUR_ICON = 'https://4.bp.blogspot.com/-jDG-EHpiWDQ/Ur1HdybdzMI/AAAAAAAAcg8/KwaSvHiDAdw/s800/dog_rottweiler.png'

def run_chat(chat = chat, start='おすすめスイーツを占うよ。準備はいい？', **kw):

  def display_bot(bot_text):
    with output.redirect_to_element('#output'):
      bot_name = kw.get('bot_name', 'ボット')
      bot_icon = kw.get('bot_icon', BOT_ICON)
      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-left">
            <img src="{bot_icon}" width="60px">
        </div><!-- /.icon-img icon-img-left -->
        <div class="icon-name icon-name-left">{bot_name}</div>
        <div class="sb-side sb-side-left">
            <div class="sb-txt sb-txt-left">
              {bot_text}
            </div><!-- /.sb-txt sb-txt-left -->
        </div><!-- /.sb-side sb-side-left -->
    </div><!-- /.sb-box -->
      '''))

  def display_you(your_text):
    with output.redirect_to_element('#output'):
      your_name = kw.get('your_name', 'あなた')
      your_icon = kw.get('your_icon', YOUR_ICON)

      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-right">
            <img src="{your_icon}" width="60px">
        </div><!-- /.icon-img icon-img-right -->
        <div class="icon-name icon-name-right">{your_name}</div>
        <div class="sb-side sb-side-right">
            <div class="sb-txt sb-txt-right">
              {your_text}
            </div><!-- /.sb-txt sb-txt-right -->
        </div><!-- /.sb-side sb-side-right -->
      </div><!-- /.sb-box -->
      '''))

  display(IPython.display.HTML('''
      <style>
        /* 全体 */
        .sb-box {
            position: relative;
            overflow: hidden;
        }
        /* アイコン画像 */
        .icon-img {
            position: absolute;
            overflow: hidden;
            top: 0;
            width: 80px;
            height: 80px;
        }
        /* アイコン画像（左） */
        .icon-img-left {
            left: 0;
        }
        /* アイコン画像（右） */
        .icon-img-right {
            right: 0;
        }
        /* アイコン画像 */
        .icon-img img {
            border-radius: 50%;
            border: 2px solid #eee;
        }
        /* アイコンネーム */
        .icon-name {
            position: absolute;
            width: 80px;
            text-align: center;
            top: 83px;
            color: #fff;
            font-size: 10px;
        }
        /* アイコンネーム（左） */
        .icon-name-left {
            left: 0;
        }
        /* アイコンネーム（右） */
        .icon-name-right {
            right: 0;
        }
        /* 吹き出し */
        .sb-side {
            position: relative;
            float: left;
            margin: 0 105px 40px 105px;
        }
        .sb-side-right {
            float: right;
        }
        /* 吹き出し内のテキスト */
        .sb-txt {
            position: relative;
            border: 2px solid #eee;
            border-radius: 6px;
            background: #eee;
            color: #333;
            font-size: 15px;
            line-height: 1.7;
            padding: 18px;
        }
        .sb-txt>p:last-of-type {
            padding-bottom: 0;
            margin-bottom: 0;
        }
        /* 吹き出しの三角 */
        .sb-txt:before {
            content: "";
            position: absolute;
            border-style: solid;
            top: 16px;
            z-index: 3;
        }
        .sb-txt:after {
            content: "";
            position: absolute;
            border-style: solid;
            top: 15px;
            z-index: 2;
        }
        /* 吹き出しの三角（左） */
        .sb-txt-left:before {
            left: -7px;
            border-width: 7px 10px 7px 0;
            border-color: transparent #eee transparent transparent;
        }
        .sb-txt-left:after {
            left: -10px;
            border-width: 8px 10px 8px 0;
            border-color: transparent #eee transparent transparent;
        }
        /* 吹き出しの三角（右） */
        .sb-txt-right:before {
            right: -7px;
            border-width: 7px 0 7px 10px;
            border-color: transparent transparent transparent #eee;
        }
        .sb-txt-right:after {
            right: -10px;
            border-width: 8px 0 8px 10px;
            border-color: transparent transparent transparent #eee;
        }
        /* 767px（iPad）以下 */
        @media (max-width: 767px) {
            .icon-img {
                width: 60px;
                height: 60px;
            }
            /* アイコンネーム */
            .icon-name {
                width: 60px;
                top: 62px;
                font-size: 9px;
            }
            /* 吹き出し（左） */
            .sb-side-left {
                margin: 0 0 30px 78px;
                /* 吹き出し（左）の上下左右の余白を狭く */
            }
            /* 吹き出し（右） */
            .sb-side-right {
                margin: 0 78px 30px 0;
                /* 吹き出し（右）の上下左右の余白を狭く */
            }
            /* 吹き出し内のテキスト */
            .sb-txt {
                padding: 12px;
                /* 吹き出し内の上下左右の余白を-6px */
            }
        }
    </style>
      <script>
        var inputPane = document.getElementById('input');
        inputPane.addEventListener('keydown', (e) => {
          if(e.keyCode == 13) {
            google.colab.kernel.invokeFunction('notebook.Convert', [inputPane.value], {});
            inputPane.value=''
          }
        });
      </script>
    <div id='output' style='background: #66d;'></div>
    <div style='text-align: right'><textarea id='input' style='width: 100%; background: #eee;'></textarea></div>
      '''))

  def convert(your_text):
    display_you(your_text)
    bot_text = chat(your_text, **kw)
    time.sleep(random.randint(0,4))
    display_bot(bot_text)

  output.register_callback('notebook.Convert', convert)
  if start is not None:
    display_bot(start)

l = []
def uranai(input_text):
  if l == []:
    l.append(1)
    return '質問：「フルーティー系」か「エキゾチック系」の香りなら「フルーティー系」が好きですか？(YesかNoで答えてください)'

  if l == [1] and input_text == 'Yes':
    l.append(2)
    return '質問：表情を変えずに梅干を食べることができますか？(YesかNoで答えてください)'
  
  if l == [1] and input_text == 'No':
    l.append(7)

  if l == [1,2] and input_text == 'Yes':
    l.append('x')
    return 'おすすめスイーツは🍊柑橘系スイーツ🍋\n・元気で活発。好奇心旺盛\n・価値観が「楽しいか楽しくないか」\n・都合の悪いことは忘れる\nという特徴があります。'

  if l == [1,2] and input_text == 'No':
    l.append(4)
    return '質問：ショートケーキを食べるときにイチゴを最後に食べますか?(YesかNoで答えてください)'

  if l == [1,2,4] and input_text == 'Yes':
    l.append('x')
    return 'おすすめスイーツは🍓ベリースイーツ🍓\n・かわいいものが大好き\n・寂しがり屋でたまにすねる\n・打ち解けるまでは少し時間がかかる\nという特徴があります。'
  
  
  if l == [1,2,4] and input_text == 'No':
    l.append('x')
    return 'おすすめスイーツは🌰栗のスイーツ🌰\n・他の人よりも疲れを感じにくい\n・自分の感情に素直になれない\n・古くからの友人をとても大切にする\nという特徴があります。'

  
  
  if l == [1,7]:
    l.append(8)
    return '質問：今日の気分は色にすると a:水色、b:茶色、c:黄緑色の中だとどれに近いですか？(aかbかcで答えてください)' 

  if l == [1,7,8] and input_text == 'a':
    l.append('x')
    return  'おすすめスイーツは【ミントのスイーツ(^^)/】・人の世話面倒をよくみている\n・太陽のような人でリーダー格\n・おおざっぱ\nという特徴があります。'
  
  if l == [1,7,8] and input_text == 'b':
    l.append('x')
    return 'おすすめスイーツは🎂チョコスイーツ🍫☆\n・目標や夢を持って生きている\n・サービス精神が旺盛\n・影の努力家\nという特徴があります。'

  if l == [1,7,8] and input_text == 'c':
    l.append('x')
    return 'おすすめスイーツは🍵抹茶スイーツ🍃\n・大器晩成\n・器用ではない\n・他人の感情に向き合うプロ\nという特徴を持っています。'

  if input_text != ('Yes' and 'No' and 'a' and 'b' and 'c') and 'x'  not in l:
    return '正しく入力してください'

  if 'x' in l:
    return '占いは終わりです。おつかれさまでした。'
    
    return output_text

run_chat(chat=uranai)   
