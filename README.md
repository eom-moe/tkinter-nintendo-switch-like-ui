# tkinter-sample

コントローラーが外せるタイプの某ゲーム機をイメージした。

## app1.py

app1.pyの実行例

![app1.py](screenshot/app1_result.png)

以下のようにして、「4つのボタンのウィジェット」を2つ作成した。

```
    FourButtonWidget(root, directionButtonTextList, tk.LEFT)
    FourButtonWidget(root, actionButtonTextList, tk.RIGHT)
```

FourButtonWidgetはwidgetLibrary.pyで定義されている。

## app2.py

app2.pyの実行例

![app2.py](screenshot/app2_result.png)

以下のようにして、「4つのボタンのウィジェットを2つ含むウィジェット」を1つ作成した。

```
    EightButtonWidget(root)
```

EightButtonWidgetはwidgetLibrary.pyで定義されている。

## app3.py

app3.pyの実行例

![app3.py](screenshot/app3_result.png)

以下のようにして、「4つのボタンのウィジェット」を子ウィンドウとして1つずつ、合計2つ作成した。

```
    directionButtonWindow = tk.Toplevel()
    FourButtonWidget(directionButtonWindow, directionButtonTextList)

    actionButtonWindow = tk.Toplevel()
    FourButtonWidget(actionButtonWindow, actionButtonTextList)
```

app1.pyとの違いは、masterをrootではなくtk.Toplevel()にすることで、  
子ウィンドウとして表示していること。  

