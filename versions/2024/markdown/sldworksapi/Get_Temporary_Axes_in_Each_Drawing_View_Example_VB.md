---
title: "Get Temporary Axes in Each Drawing View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Temporary_Axes_in_Each_Drawing_View_Example_VB.htm"
---

# Get Temporary Axes in Each Drawing View Example (VBA)

This example shows how to get the temporary axes in each drawing view
and convert them to lines.

```
'----------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\block.sldprt.
' 2. Click File > Make Drawing from Part and
'    add one or more views to the drawing.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Converts all temporary axes to lines.
' 2. Examine the Immediate window and graphics area.
'----------------------------------------------------
Option Explicit
```

Dim swApp As SldWorks.SldWorks

Dim swDrawDoc As SldWorks.DrawingDoc

Dim swSelMgr As SldWorks.SelectionMgr

Dim swView As SldWorks.View

Dim pline As SldWorks.SketchSegment

Dim itr As Long

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDrawDoc = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swDrawDoc.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Iterate through the views

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swDrawDoc.GetFirstView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}While
Not swView Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not swView.Type= swDrawingSheet
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
swView.GetName2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDrawDoc.ActivateViewswView.GetName2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nCount As Long, vTempAxesPoints As Variant, nJump As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get number of temporary axes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nCount
= swView.GetTemporaryAxesCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
" Number of temporary axes = " & nCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nJump
= 6

'
Get temporary axes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vTempAxesPoints
= swView.GetTemporaryAxes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
itr = 0 To nCount - 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
startPt(2) As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
endPt(2) As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}startPt(0)
= vTempAxesPoints(nJump * itr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}startPt(1)
= vTempAxesPoints(nJump * itr + 1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}startPt(2)
= vTempAxesPoints(nJump * itr + 2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}endPt(0)
= vTempAxesPoints(nJump * itr + 3)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}endPt(1)
= vTempAxesPoints(nJump * itr + 4)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}endPt(2)
= vTempAxesPoints(nJump * itr + 5)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Temporary
axis " & itr; " data :"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}start
: x = " & startPt(0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}y
= " & startPt(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}z
= " & startPt(2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}endkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}:
x = " & endPt(0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}y
= " & endPt(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}z
= " & endPt(2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

' Convert temporary axes to line

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pline = swDrawDoc.CreateLine2(startPt(0),
startPt(1), startPt(2), endPt(0), endPt(1), endPt(2))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not pline Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Color

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
clr As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}clr
= swApp.GetUserPreferenceIntegerValue(swSystemColorsConstructionGeometry)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pline.Color= clr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Width

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pline.Width= swLW_NORMAL

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Style ( only an approximation )

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}pline.Style= swLineCHAIN

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
itr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get next view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swView.GetNextView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Wend

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDrawDoc.**ClearSelection2**True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub
