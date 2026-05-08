Imports System.Windows.Forms
Imports System.Drawing

Module Program
    Sub Main()
        ' 1. メインの窓（Form）を作成
        Dim mainForm As New Form()
        mainForm.Text = "VB 魔法のウィンドウ"
        mainForm.Size = New Size(400, 250)
        mainForm.StartPosition = FormStartPosition.CenterScreen
        mainForm.BackColor = Color.LightSkyBlue

        Dim myTxt As New TextBox()
        myTxt.Location = New Point(130, 40)
        mainForm.Controls.Add(myTxt)

        ' 2. ボタンを作成
        Dim myButton As New Button()
        myButton.Text = "ここを押してね！"
        myButton.Location = New Point(130, 80)
        myButton.Size = New Size(120, 40)
        myButton.Font = New Font("Meryo UI", 10, FontStyle.Bold)

        ' 3. ボタンが押された時の「魔法（処理）」を登録
        AddHandler myButton.Click, Sub(sender, e)
                                       MessageBox.Show("こんにちは！VBのコードから画面を作れましたね！", "大成功")
                                   End Sub

        ' 4. 窓にボタンを載せる
        mainForm.Controls.Add(myButton)

        ' 5. 窓を起動！
        Application.Run(mainForm)
    End Sub
End Module