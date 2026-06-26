---
title: "Get Parabolas in Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parabolas_in_Sketch_Example_VB.htm"
---

# Get Parabolas in Sketch Example (VBA)

This example shows how to get information about all of the parabolas
in a sketch.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a part that contains one or more parabolas.
' 2. Edit the sketch that contains the parabolas.
' 3. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'------------------------------------------------
Option Explicit
```

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeatkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSketchkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vParabArrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSketch = swModel.GetActiveSketch2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeat = swSketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& swFeat.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vParabArr
= swSketch.GetParabolas2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To swSketch.GetParabolaCount- 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Parabola["
& i & "]"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Colorkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vParabArr(18 * i + 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Linetypekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vParabArr(18 * i + 1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Drawings only

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Fontkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vParabArr(18 * i + 2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Widthkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vParabArr(18 * i + 3)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LayerIDkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vParabArr(18 * i + 4)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Layer
Overridekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & vParabArr(18 * i + 5)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Start
Ptkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vParabArr(18 * i + 6) * 1000# & ", " &
vParabArr(18 * i + 7) * 1000# & ", " & vParabArr(18
* i + 8) * 1000# & ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Endkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Ptkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vParabArr(18 * i + 9) * 1000# & ", " &
vParabArr(18 * i + 10) * 1000# & ", " & vParabArr(18
* i + 11) * 1000# & ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Focus
Ptkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vParabArr(18 * i + 12) * 1000# & ", " &
vParabArr(18 * i + 13) * 1000# & ", " & vParabArr(18
* i + 14) * 1000# & ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Apexkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Ptkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vParabArr(18 * i + 15) * 1000# & ", " &
vParabArr(18 * i + 16) * 1000# & ", " & vParabArr(18
* i + 17) * 1000# & ") mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

End Sub
