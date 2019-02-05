Sub Stocks()
    
    
Dim ws As Worksheet

    
For Each ws In Worksheets

'column names
    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Yearly Change"
    ws.Cells(1, 11).Value = "Percent Change"
    ws.Cells(1, 12).Value = "Total Stock Volume"

    'tick
        Dim tickername As String

    'grab and hold total
        Dim Vol_total As Double
        Vol_total = 0

    'location
        Dim rowsc As Long
        rowsc = 2

    'opening price
        Dim open1 As Double
        open1 = 0

    'closing price
        Dim closing As Double
        closing = 0
        
    'price changes
        Dim change As Double
        change = 0

    'percentage
        Dim percent As Double
        percent = 0

    'all the way down
        Dim lastrow As Long
        lastrow = ws.Cells(rows.Count, 1).End(xlUp).row

    'for loop
        For i = 2 To lastrow
            
        'set the condition
        If ws.Cells(i, 1).Value <> ws.Cells(i - 1, 1).Value Then

            open1 = ws.Cells(i, 3).Value

        End If

      'volume total
        Vol_total = Vol_total + ws.Cells(i, 7)

       'is the ticker different
             If ws.Cells(i, 1).Value <> ws.Cells(i + 1, 1).Value Then

           'print ticker
               ws.Cells(rowsc, 9).Value = ws.Cells(i, 1).Value
               
        'print volume
              ws.Cells(rowsc, 12).Value = Vol_total

        'find the closing price
                closing = ws.Cells(i, 6).Value

        'formula and print for change
                change = closing - open1
                ws.Cells(rowsc, 10).Value = change

            'format negative and positive
            
        If change >= 0 Then
                   ws.Cells(rowsc, 10).Interior.ColorIndex = 4
                Else
                  ws.Cells(rowsc, 10).Interior.ColorIndex = 3
                End If

       'formula percentage change and print
            
             If open1 = 0 And closing = 0 Then
                    
                    
                    
     'resolve divide by zero error or else boom! resolve for new stocks
            percent = 0
           ws.Cells(rowsc, 11).Value = percent
            ws.Cells(rowsc, 11).NumberFormat = "0.00%"
                ElseIf open1 = 0 Then
    
                    Dim newstock As String
                    newstock = "New"
                    ws.Cells(rowsc, 11).Value = percent
                Else
                    percent = change / open1
                    ws.Cells(rowsc, 11).Value = percent
                    ws.Cells(rowsc, 11).NumberFormat = "0.00%"
                End If

    
                rowsc = rowsc + 1

        'Reset counters
                Vol_total = 0
                open1 = 0
                closing = 0
                change = 0
                percent = 0
                
            End If
        Next i

        'summary table
        ws.Cells(2, 15).Value = "Greatest % Increase"
        ws.Cells(3, 15).Value = "Greatest % Decrease"
        ws.Cells(4, 15).Value = "Greatest Total Volume"
        ws.Cells(1, 16).Value = "Ticker"
        ws.Cells(1, 17).Value = "Value"

        'lastrow
        lastrow = ws.Cells(rows.Count, 9).End(xlUp).row

        'highs and lows for summary
        Dim hightick As String
        Dim hvalue As Double

        
        hvalue = ws.Cells(2, 11).Value

        Dim ltick As String
        Dim lvalue As Double

        
        lvalue = ws.Cells(2, 11).Value

        Dim hvoltick2 As String
        Dim hvoltick As Double

        
        hvoltick = ws.Cells(2, 12).Value

        'for loop 2
        For j = 2 To lastrow

            
            If ws.Cells(j, 11).Value > hvalue Then
                hvalue = ws.Cells(j, 11).Value
                hightick = ws.Cells(j, 9).Value
            End If

            
            If ws.Cells(j, 11).Value < lvalue Then
                lvalue = ws.Cells(j, 11).Value
                ltick = ws.Cells(j, 9).Value
            End If

            
            If ws.Cells(j, 12).Value > hvoltick Then
                hvoltick = ws.Cells(j, 12).Value
                hvoltick2 = ws.Cells(j, 9).Value
            End If

        Next j

        'print
        ws.Cells(2, 16).Value = hightick
        ws.Cells(2, 17).Value = hvalue
        ws.Cells(2, 17).NumberFormat = "0.00%"
        ws.Cells(3, 16).Value = ltick
        ws.Cells(3, 17).Value = lvalue
        ws.Cells(3, 17).NumberFormat = "0.00%"
        ws.Cells(4, 16).Value = hvoltick2
        ws.Cells(4, 17).Value = hvoltick

        'fomatting
        ws.Columns("I:L").EntireColumn.AutoFit
        ws.Columns("O:Q").EntireColumn.AutoFit

    Next ws

End Sub

