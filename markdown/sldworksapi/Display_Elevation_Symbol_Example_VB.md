---
title: "Display Elevation Symbol Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Elevation_Symbol_Example_VB.htm"
---

# Display Elevation Symbol Example (VBA)

This example shows how to display an elevation symbol at the end of
each ordinate dimension extension line in a part.

'-----------------------------------------------------

'

' Preconditions: Part document called Block.SLDPRT is

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}open
and contains the selected dimensions.

'

' Postconditions: An elevation symbol and the word "Dowel"
are displayed

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}at
the end of each extension line of each selected dimension.

'

'------------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModelDoc As SldWorks.ModelDoc2

Dim swModelDocExt As SldWorks.ModelDocExtension

Dim swSelMgr As SldWorks.SelectionMgr

Dim swDisplayDim As SldWorks.DisplayDimension

Dim boolstatus As Boolean

Dim longstatus As Long

Dim longwarnings As Long

Dim selType As Long

Dim i As Long

Sub SelectDimensions()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("D1@Sketch1@Block.SLDPRT",
"DIMENSION", -0.1000132239804, 0.1006163020026, 0.015, True,
0, Nothing, swSelectOptionDefault)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("D2@Sketch1@Block.SLDPRT",
"DIMENSION", -0.06157715941924, 0.1015772036167, 0.015, True,
0, Nothing, swSelectOptionDefault)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("D3@Sketch1@Block.SLDPRT",
"DIMENSION", -0.02362154566506, 0.1054208100728, 0.015, True,
0, Nothing, swSelectOptionDefault)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("D4@Sketch1@Block.SLDPRT",
"DIMENSION", 0.01481451889614, 0.1063817116868, 0.015, True,
0, Nothing, swSelectOptionDefault)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("D5@Sketch1@Block.SLDPRT",
"DIMENSION", 0.04940697700122, 0.1063817116868, 0.015, True,
0, Nothing, swSelectOptionDefault)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("D6@Sketch1@Block.SLDPRT",
"DIMENSION", 0.08592123833436, 0.1068621624938, 0.015, True,
0, Nothing, swSelectOptionDefault)

End Sub

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDoc = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocExt = swModelDoc.Extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModelDoc.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModelDoc.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
SelectDimensions

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
selCount As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}selCount
= swSelMgr.GetSelectedObjectCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 1 To selCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}selType
= swSelMgr.GetSelectedObjectType2(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
selType = swSelDIMENSIONS Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDisplayDim = swSelMgr.GetSelectedObject5(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDisplayDim.SetTextswDimensionTextAll, "Dowel"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDisplayDim.EndSymbol= swOrdDimEndSymbol_Dowel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDisplayDim.Elevation= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModelDoc.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub
