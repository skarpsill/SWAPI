---
title: "Get Detail Circle Information Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Detail_Circle_Information_Example_VB.htm"
---

# Get Detail Circle Information Example (VBA)

This example shows how to get information about detail circles.

'-----------------------------

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Drawing document is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
Drawing view to which you added at

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}least
one detail circle is selected.

'

' Postconditions: None

'

'-----------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDrawkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DrawingDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAssykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.AssemblyDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swViewkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.View

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vDetCirckadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nSizekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nNumDetCirckadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
jkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
indexkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nNumArrowkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDraw = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swSelMgr.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'View::GetDetailCircleInfo2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}[
numDetailCircles,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}[
layer, centerPt[3], startPt[3], endPt[3], lineType, textPt[3], textHeight,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}numArrows,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}[
arrowTip[3], arrowComponent[3], arrowWidth, arrowHeight, arrowStyle ]

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}]

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}]

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vDetCirc
= swView.GetDetailCircleInfo2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nNumDetCirc
= swView.GetDetailCircleCount2(nSize)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Assert
nNumDetCirc = vDetCirc(0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Assert
nSize = UBound(vDetCirc) + 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}View
= " & swView.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}index
= 1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set index to start of first detail circle

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To nNumDetCirc - 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Circle("
& i & ")"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Layerkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vDetCirc(index + 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Center
ptkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vDetCirc(index + 1) * 1000# & ", " & vDetCirc(index
+ 2) * 1000# & ", " & vDetCirc(index + 3) * 1000# &
") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Startkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ptkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vDetCirc(index + 4) * 1000# & ", " & vDetCirc(index
+ 5) * 1000# & ", " & vDetCirc(index + 6) * 1000# &
") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Endkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ptkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vDetCirc(index + 7) * 1000# & ", " & vDetCirc(index
+ 8) * 1000# & ", " & vDetCirc(index + 9) * 1000# &
") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Line
typekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vDetCirc(index + 10)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Textkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ptkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vDetCirc(index + 11) * 1000# & ", " &
vDetCirc(index + 12) * 1000# & ", " & vDetCirc(index
+ 13) * 1000# & ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Textkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}htkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vDetCirc(index + 14) * 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nNumArrow
= vDetCirc(index + 15)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}index
= index + 16kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set index to start of first arrow

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
j = 0 To nNumArrow - 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Arrow("
& j & ")"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Tipkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ptkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vDetCirc(index + 0) * 1000# & ", " & vDetCirc(index
+ 1) * 1000# & ", " & vDetCirc(index + 2) * 1000# &
") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Comp
ptkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vDetCirc(index + 3) * 1000# & ", " & vDetCirc(index
+ 4) * 1000# & ", " & vDetCirc(index + 5) * 1000# &
") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Widthkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vDetCirc(index + 6) * 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Heightkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vDetCirc(index + 7) * 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Stylekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vDetCirc(index + 8)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}index
= index + 9kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set index to start of next arrow

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
j

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Index should now be at start of next detail circle

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

End Sub

'-----------------------------
