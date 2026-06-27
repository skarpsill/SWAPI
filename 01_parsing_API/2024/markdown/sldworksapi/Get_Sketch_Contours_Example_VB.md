---
title: "Get Sketch Contours Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Contours_Example_VB.htm"
---

# Get Sketch Contours Example (VBA)

This example shows how to get the sketch contours in a model document.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a part that contains a Sketch1 feature.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the number of sketch contours in Sketch1 and whether
'    they are open or closed.
' 2. Gets the number of sketch segments in Sketch1 and their type.
' 3. Gets the number of edges Sketch1.
' 4. Examine the Immediate window.
'----------------------------------------------------------------------------
Option Explicit
```

```vb
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim myModel As SldWorks.ModelDoc2
     Dim myPart As SldWorks.PartDoc
     Dim SelMgr As SldWorks.SelectionMgr
     Dim mySelectData As SldWorks.SelectData
     Dim myFeature As SldWorks.Feature
     Dim mySketch As SldWorks.Sketch
     Dim contourCount As Integer
     Dim vSkContours As Variant
     Dim skContour As SketchContour
     Dim vEdges As Variant, myEdge As SldWorks.Edge
     Dim skSegCount As Long
     Dim vSkSegments As Variant
     Dim skSegment As SldWorks.SketchSegment
     Dim skSegType As Long, skSegTypesString As String
     Dim closed As Boolean, closedString As String
     Dim i As Integer, j As Integer, k As Integer
     Dim boolstatus As Boolean
    Set swApp = Application.SldWorks
     Set myModel = swApp.ActiveDoc
     Set SelMgr = myModel.SelectionManager
     Set mySelectData = SelMgr.CreateSelectData
     Set myPart = myModel
     Set myFeature = myPart.FeatureByName("Sketch1")
     Set mySketch = myFeature.GetSpecificFeature2()
 '             or
 '    Set mySketch = myModel.GetActiveSketch2()
 '    Set myFeature = mySketch
    If Not mySketch Is Nothing Then
         vSkContours = mySketch.GetSketchContours()
         contourCount = UBound(vSkContours) - LBound(vSkContours) + 1
        Debug.Print ""
         Debug.Print contourCount & " Contours in sketch " & myFeature.Name
        For i = LBound(vSkContours) To UBound(vSkContours)
             Set skContour = vSkContours(i)
            If Not skContour Is Nothing Then
                 closed = skContour.IsClosed()
                If (closed = 0) Then
                     closedString = "Open"
                 Else
                     closedString = "Closed"
                 End If
                Debug.Print "  Contour " & i & ": " & closedString
                 vSkSegments = skContour.GetSketchSegments()
                 skSegCount = UBound(vSkSegments) - LBound(vSkSegments) + 1
                For j = LBound(vSkSegments) To UBound(vSkSegments)
                     If j = LBound(vSkSegments) Then
                         skSegTypesString = "("
                     End If
                    Set skSegment = vSkSegments(j)
                    If Not skSegment Is Nothing Then
                         skSegType = skSegment.GetType()
                         Select Case skSegType

                        Case SwConst.swSketchSegments_e.swSketchLINE
                             skSegTypesString = skSegTypesString & "line"
                        Case SwConst.swSketchSegments_e.swSketchARC
                             skSegTypesString = skSegTypesString & "arc"
                        Case SwConst.swSketchSegments_e.swSketchELLIPSE
                             skSegTypesString = skSegTypesString & "ellipse"
                        Case SwConst.swSketchSegments_e.swSketchPARABOLA
                             skSegTypesString = skSegTypesString & "parabola"
                        Case SwConst.swSketchSegments_e.swSketchSPLINE
                             skSegTypesString = skSegTypesString & "spline"
                        Case SwConst.swSketchSegments_e.swSketchTEXT
                             skSegTypesString = skSegTypesString & "text"
                        Case Default
                             skSegTypesString = skSegTypesString & "unknown"
                        End Select
                    End If
                    If j = UBound(vSkSegments) Then
                         skSegTypesString = skSegTypesString & ")"
                     Else
                         skSegTypesString = skSegTypesString & ","
                     End If
                 Next j
                Debug.Print "    Sketch segment count = " & skSegCount & " " & skSegTypesString
                vEdges = skContour.GetEdges()
                If IsEmpty(vEdges) Then
                     Debug.Print "    No edges."
                 Else
                     For k = LBound(vEdges) To UBound(vEdges)
                         Set myEdge = vEdges(k)
                        If Not myEdge Is Nothing Then
                             Debug.Print "    Edge " & k & ": "
                         End If
                     Next k
                End If
                boolstatus = skContour.Select2(False, mySelectData)
                 If boolstatus = 0 Then
                     Debug.Print "    Selection of contour failed."
                 End If
                Stop
            End If
        Next i
    End If
End Sub
```
