---
title: "Get Weld Bead Symbol Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VB.htm"
---

# Get Weld Bead Symbol Data Example (VBA)

This example shows how to get weld bead symbol data in a drawing.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing that contains at least one view with a weld bead
 '    annotation.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swDraw                  As SldWorks.DrawingDoc
     Dim swSheet                 As SldWorks.Sheet
     Dim swView                  As SldWorks.View
     Dim swWBead                 As SldWorks.WeldBead
     Dim swDispData              As SldWorks.DisplayData
     Dim strFilled As String
     Dim lineCount As Long
     Dim vLine As Variant
     Dim lineColor As Long, lineLineType As Long, lineStyle As Long, lineWeight As Long
     Dim lineX As Double, lineY As Double, lineZ As Double
     Dim polygonCount As Long
     Dim vPolygon As Variant
     Dim polyColor As Long, polyLineType As Long, polyNumPts As Long
     Dim polyX As Double, polyY As Double, polyZ As Double
     Dim index As Long, index2 As Long, arrayIndex As Long
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swDraw = swModel
     Set swSheet = swDraw.GetCurrentSheet
     Set swView = swDraw.GetFirstView
    While Not swView Is Nothing
        Debug.Print swView.Name
         Set swWBead = swView.GetFirstWeldBead()
        While Not swWBead Is Nothing
            Debug.Print "  Weld Bead..."
             If (swWBead.SolidFill = False) Then
                 strFilled = "open"
             Else
                 strFilled = "solid filled"
             End If
            Set swDispData = swWBead.GetAnnotation().GetDisplayData()
             lineCount = swDispData.GetLineCount
             Debug.Print "    Line count = " & lineCount
            For index = 0 To lineCount - 1
                 vLine = swDispData.GetLineAtIndex3(index)
                 If Not IsEmpty(vLine) Then
                     lineColor = vLine(0)
                     lineLineType = vLine(1)
                     lineStyle = vLine(2)
                     lineWeight = vLine(3)
                     Debug.Print "      Color = " & lineColor & ", line type = " & lineLineType & ", line style = " & lineStyle & ", line weight = " & lineWeight
                     arrayIndex = 4
                     For index2 = 0 To 1
                         lineX = vLine(arrayIndex)
                         lineY = vLine(arrayIndex + 1)
                         lineZ = vLine(arrayIndex + 2)
                         Debug.Print "       " & index2 & " (" & lineX & ", " & lineY & ", " & lineZ & ")"
                         arrayIndex = arrayIndex + 3
                     Next index2
                 End If
             Next index
            Debug.Print "    Polyline count = " & swDispData.GetPolyLineCount
             Debug.Print "    Arc count = " & swDispData.GetArcCount
             polygonCount = swDispData.GetPolygonCount
             Debug.Print "    Polygon count = " & polygonCount
            For index = 0 To polygonCount - 1
                 vPolygon = swDispData.GetPolygonAtIndex(index)
                 If Not IsEmpty(vPolygon) Then
                     polyColor = vPolygon(0)
                     polyLineType = vPolygon(1)
                     polyNumPts = vPolygon(4)
                     Debug.Print "      Color = " & polyColor & ", line type = " & polyLineType & ", point count = " & polyNumPts & ", " & strFilled
                     arrayIndex = 5
                    For index2 = 0 To polyNumPts - 1
                         polyX = vPolygon(arrayIndex)
                         polyY = vPolygon(arrayIndex + 1)
                         polyZ = vPolygon(arrayIndex + 2)
                         Debug.Print "       " & index2 & " (" & polyX & ", " & polyY & ", " & polyZ & ")"
                         arrayIndex = arrayIndex + 3
                     Next index2
                 End If
             Next index
             Set swWBead = swWBead.GetNext()
         Wend
         Set swView = swView.GetNextView
     Wend
End Sub
```
