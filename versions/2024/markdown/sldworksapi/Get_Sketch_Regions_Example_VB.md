---
title: "Get Sketch Regions Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Regions_Example_VB.htm"
---

# Get Sketch Regions Example (VBA)

This example shows how to get the sketch regions in a sketch.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document that contains a Sketch1 feature with
 '    one or more sketch regions.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Gets each sketch region.
 ' 2. Press F5 at each Stop statement.
 ' 3. Examine the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim myModel As SldWorks.ModelDoc2
     Dim myPart As SldWorks.PartDoc
     Dim SelMgr As SldWorks.SelectionMgr
     Dim mySelectData As SldWorks.SelectData
     Dim myFeature As SldWorks.Feature
     Dim mySketch As SldWorks.Sketch
     Dim regionCount As Long
     Dim vSkRegions As Variant
     Dim skRegion As SketchRegion
     Dim myLoop As Loop2
     Dim edgeCount As Long, vertexCount As Long
     Dim vEdges As Variant, myEdge As SldWorks.Edge
     Dim vVertices As Variant, myVertex As SldWorks.Vertex
     Dim vPoint As Variant, X As Double, Y As Double, Z As Double
     Dim outer As Boolean, strOuter As String
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
         regionCount = mySketch.GetSketchRegionCount()
         Debug.Print ""
         Debug.Print regionCount & " regions in sketch " & myFeature.Name
        vSkRegions = mySketch.GetSketchRegions()
        For i = LBound(vSkRegions) To UBound(vSkRegions)
             Set skRegion = vSkRegions(i)
            If Not skRegion Is Nothing Then
                 Debug.Print "  Region " & i & ":"
                 j = 0
                 Set myLoop = skRegion.GetFirstLoop()
                 While Not myLoop Is Nothing
                     edgeCount = myLoop.GetEdgeCount()
                     vertexCount = myLoop.GetVertexCount()
                     outer = myLoop.IsOuter()
                    If outer = 0 Then
                         strOuter = "Inner loop"
                     Else
                         strOuter = "Outer loop"
                     End If
                    Debug.Print "    Loop " & j & ": " & edgeCount & " edges, " & vertexCount & " vertices, " & strOuter
                    vEdges = myLoop.GetEdges()
                    For k = LBound(vEdges) To UBound(vEdges)
                         Set myEdge = vEdges(k)
                         If Not myEdge Is Nothing Then
                             Debug.Print "      Edge " & k & ": "
                         End If
                    Next k
                    vVertices = myLoop.GetVertices()
                    For k = LBound(vVertices) To UBound(vVertices)
                         Set myVertex = vVertices(k)
                         If Not myVertex Is Nothing Then
                             vPoint = myVertex.GetPoint()
                             X = vPoint(0)
                             Y = vPoint(1)
                             Z = vPoint(2)

                            Debug.Print "      Vertex " & k & ": " & "(" & X & ", " & Y & ", " & Z & ")"
                         End If
                     Next k
                    Set myLoop = myLoop.GetNext()
                     j = j + 1
                 Wend
                boolstatus = skRegion.Select2(False, mySelectData)
                 If boolstatus = 0 Then
                     Debug.Print "    Selection of region failed."
                 End If
                Stop
            End If
        Next i
    End If
End Sub
```
