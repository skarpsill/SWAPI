---
title: "Translate Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Translate_Sketch_Example_VB.htm"
---

# Translate Sketch Example (VBA)

This example shows how to move a sketch.

```
'----------------------------------------------------------------------------
' Preconditions: Verify that the specified template exists.
'
' Postconditions:
' 1. Creates a sketch.
' 2. Creates a parabola.
' 3. While observing the graphics area, press F5 at Stop
'    to move the sketch.
'----------------------------------------------------------------------------

Option Explicit
```

```vb
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2

    Set swApp = Application.SldWorks
     Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)

    If swModel Is Nothing Then
         swApp.SendMsgToUser2 "A part document must be active.", swMbWarning, swMbOk
         Exit Sub
     End If
    Dim modelType As Long
     modelType = swModel.GetType

    If modelType <> SwConst.swDocPART Then
         swApp.SendMsgToUser2 "A part document must be active.", swMbWarning, swMbOk
         Exit Sub
     End If

    'Select a plane on which to sketch
     If SelectPlane(swModel) = False Then
         MsgBox "Could not select plane."
         Exit Sub
     End If

    'Get point data
     Dim pFocal      As SldWorks.SketchPoint
     Dim pApex       As SldWorks.SketchPoint
     Dim pStart      As SldWorks.SketchPoint
     Dim pEnd        As SldWorks.SketchPoint
     Dim swSkMgr As SldWorks.SketchManager
     Set swSkMgr = swModel.SketchManager

    Dim swSelMgr As SldWorks.SelectionMgr
     Set swSelMgr = swModel.SelectionManager

    Dim swSketch As Sketch
     swSkMgr.InsertSketch True
     Set swSketch = swSkMgr.ActiveSketch

    ' Focal point
     Set pFocal = swSkMgr.CreatePoint(0, -0.025930732990048, 0)
     ' Apex point
     Set pApex = swSkMgr.CreatePoint(1.10754938634727E-02, -4.85199777778575E-02, 0)
     ' Start point
     Set pStart = swSkMgr.CreatePoint(0.057136404168939, 8.69770346454566E-02, 0)
     ' End point
     Set pEnd = swSkMgr.CreatePoint(-0.120690397734139, -4.65528735997846E-03, 0)

    Dim vPoint As Variant

    ' Make sure a sketch is active
     If swSketch Is Nothing Then
         MsgBox "Please sketch a focal point, apex point, start point, and end point."
         Exit Sub
     End If

    vPoint = swSketch.GetSketchPoints2

    Dim SkParabola As SldWorks.SketchParabola
     Set SkParabola = swModel.SketchManager.CreateParabola(pFocal.X, pFocal.Y, 0, pApex.X, pApex.Y, 0, pStart.X, pStart.Y, 0, pEnd.X, pEnd.Y, 0)

    swModel.ViewZoomtofit2
     swSkMgr.InsertSketch True

    Stop
    swModel.SketchModifyTranslate pApex.X, pApex.Y, 0.06, -0.01

End Sub
Public Function SelectPlane(Plane As SldWorks.ModelDoc2) As Boolean
    Dim featureTemp As Feature
     Set featureTemp = Plane.FirstFeature

    While Not featureTemp Is Nothing
         Dim sFeatureName As String
         sFeatureName = featureTemp.GetTypeName2

        If sFeatureName = "RefPlane" Then
             featureTemp.Select2 True, 0
             SelectPlane = True
             Exit Function
         End If

        Set featureTemp = featureTemp.GetNextFeature
    Wend
End Function
```
