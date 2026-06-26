---
title: "Get Drawing Template Size Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Drawing_Template_Size_Example_VB.htm"
---

# Get Drawing Template Size Example (VBA)

This example shows how to get the size of the specified drawing template.

'-------------------------------------

Option Explicit

Public Enum swDwgPaperSizes_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperAsize
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperAsizeVertical
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperBsize
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperCsize
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperDsize
= 4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperEsize
= 5

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperA4size
= 6

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperA4sizeVertical
= 7

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperA3size
= 8

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperA2size
= 9

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperA1size
= 10

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperA0size
= 11

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPapersUserDefined
= 12

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Const
sTemplateName As String = "c:Program Files\SOLIDWORKS\data\templates\drawing.drwdot"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vTemplateSizeskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vTemplateSizes
= swApp.GetTemplateSizes(sTemplateName)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Template = " & sTemplateName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Paper
Sizekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vTemplateSizes(0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Widthkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vTemplateSizes(1) * 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Heightkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vTemplateSizes(2) * 1000# & " mm"

End Sub

'-------------------------------------
