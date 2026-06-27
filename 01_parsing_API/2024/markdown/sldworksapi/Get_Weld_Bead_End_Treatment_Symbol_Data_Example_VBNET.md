---
title: "Get Weld Bead Symbol Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VBNET.htm"
---

# Get Weld Bead Symbol Data Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swDraw As DrawingDoc
         Dim swSheet As Sheet
         Dim swView As View
         Dim swWBead As WeldBead
         Dim swDispData As DisplayData
         Dim strFilled As String
         Dim lineCount As Integer
         Dim vLine As Object
         Dim lineColor As Integer, lineLineType As Integer, lineStyle As Integer, lineWeight As Integer
         Dim lineX As Double, lineY As Double, lineZ As Double
         Dim polygonCount As Integer
         Dim vPolygon As Object
         Dim polyColor As Integer, polyLineType As Integer, polyNumPts As Integer
         Dim polyX As Double, polyY As Double, polyZ As Double
         Dim index As Integer, index2 As Integer, arrayIndex As Integer

         swModel = swApp.ActiveDoc
         swDraw = swModel
         swSheet = swDraw.GetCurrentSheet
         swView = swDraw.GetFirstView

         While Not swView Is Nothing

             Debug.Print(swView.Name)
             swWBead = swView.GetFirstWeldBead()

             While Not swWBead Is Nothing

                 Debug.Print("  Weld Bead...")
                 If (swWBead.SolidFill = False) Then
                     strFilled = "open"
                 Else
                     strFilled = "solid filled"
                 End If

                 swDispData = swWBead.GetAnnotation().GetDisplayData()
                 lineCount = swDispData.GetLineCount
                 Debug.Print("    Line count = " & lineCount)

                 For index = 0 To lineCount - 1
                     vLine = swDispData.GetLineAtIndex3(index)
                     If Not IsNothing(vLine) Then
                         lineColor = vLine(0)
                         lineLineType = vLine(1)
                         lineStyle = vLine(2)
                         lineWeight = vLine(3)
                         Debug.Print("      Color = " & lineColor & ", line type = " & lineLineType & ", line style = " & lineStyle & ", line weight = " & lineWeight)
                         arrayIndex = 4
                         For index2 = 0 To 1
                             lineX = vLine(arrayIndex)
                             lineY = vLine(arrayIndex + 1)
                             lineZ = vLine(arrayIndex + 2)
                             Debug.Print("       " & index2 & " (" & lineX & ", " & lineY & ", " & lineZ & ")")
                             arrayIndex = arrayIndex + 3
                         Next index2
                     End If
                 Next index

                 Debug.Print("    Polyline count = " & swDispData.GetPolyLineCount)
                 Debug.Print("    Arc count = " & swDispData.GetArcCount)
                 polygonCount = swDispData.GetPolygonCount
                 Debug.Print("    Polygon count = " & polygonCount)

                 For index = 0 To polygonCount - 1
                     vPolygon = swDispData.GetPolygonAtIndex(index)
                     If Not IsNothing(vPolygon) Then
                         polyColor = vPolygon(0)
                         polyLineType = vPolygon(1)
                         polyNumPts = vPolygon(4)
                         Debug.Print("      Color = " & polyColor & ", line type = " & polyLineType & ", point count = " & polyNumPts & ", " & strFilled)
                         arrayIndex = 5

                         For index2 = 0 To polyNumPts - 1
                             polyX = vPolygon(arrayIndex)
                             polyY = vPolygon(arrayIndex + 1)
                             polyZ = vPolygon(arrayIndex + 2)
                             Debug.Print("       " & index2 & " (" & polyX & ", " & polyY & ", " & polyZ & ")")
                             arrayIndex = arrayIndex + 3
                         Next index2
                     End If
                 Next index
                 swWBead = swWBead.GetNext()
             End While
             swView = swView.GetNextView
         End While

     End Sub

     Public swApp As SldWorks

 End Class
```
