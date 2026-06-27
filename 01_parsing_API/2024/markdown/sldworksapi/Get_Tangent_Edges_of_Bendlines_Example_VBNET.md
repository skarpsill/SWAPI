---
title: "Get Tangent Edges of Bendlines Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Tangent_Edges_of_Bendlines_Example_VBNET.htm"
---

# Get Tangent Edges of Bendlines Example (VB.NET)

This example shows how to get each bendline's visible tangent edges
in a flat-pattern view in a drawing of a sheet metal part.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a SOLIDWORKS drawing of a sheet metal part
'    that has a flat-pattern view with
'    bend lines with tangent edges.
' 2. Open the Immediate window.
'
' Preconditions: Examine the Immediate window.
'---------------------------------------------------
Imports SolidWorks.Interop.sldworks
```

```vb
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDrawing As DrawingDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSheet As Sheet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swView As View
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nbrBendlines As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim BendlinesArr As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nbrRelatedTangentEdges As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim RelatedTangentEdgesArr As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSketchSegment as SketchSegment

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDrawing = swModel

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get drawing sheet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSheet = swDrawing.GetCurrentSheet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get name of drawing sheet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Name of drawing sheet: " & swSheet.GetName)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get number of views on drawing sheet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Number of drawing views on drawing sheet: " & swDrawing.GetViewCount)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' First view is the current drawing sheet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swView = swDrawing.GetFirstView
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}First drawing view is the current drawing sheet, so...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get first drawing view on drawing sheet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swView = swView.GetNextView
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}While Not swView Is Nothing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}Get next drawing view on drawing sheet...")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Get first true drawing view on current drawing sheet
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}Is this drawing view a flat-pattern view? " & swView.IsFlatPatternView)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' If this drawing view is a flat pattern view, then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' get its bendlines and their related tangent edges
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If swView.IsFlatPatternView Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' Get number of bendlines in the drawing view
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}nbrBendlines = swView.GetBendLineCount
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}Number of bendlines in this drawing view: " & nbrBendlines)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}If (nbrBendlines > 0) Then
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}BendlinesArr = swView.GetBendLines kadov_tag{{<spaces>}}                       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}For i = 0 To UBound(BendlinesArr)
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}swSketchSegment = BendlinesArr(i)
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Is bend line " & i & " really a bend line? " & swSketchSegment.IsBendLine)
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}' Get the number of tangent lines related to
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}' the bendline
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}nbrRelatedTangentEdges = swView.GetRelatedTangentEdgeCount(BendlinesArr(i))
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}Number of tangent edges for Bendline " & i & ": " & nbrRelatedTangentEdges)
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}' Get the tangent lines related to the bendline
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}If (nbrRelatedTangentEdges > 0) Then
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}RelatedTangentEdgesArr = swView.GetRelatedTangentEdges(BendlinesArr(i))
kadov_tag{{<spaces>}}                            kadov_tag{{</spaces>}}nbrRelatedTangentEdges = nbrRelatedTangentEdges - 1
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Next i
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Get next drawing view
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swView = swView.GetNextView
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End While

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
