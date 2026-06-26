---
title: "Create a Sketch Point Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Sketch_Point_Example_VB.htm"
---

# Create a Sketch Point Example (VBA)

This example shows how to create a sketch point.

```
'---------------------------------------------------------------------------
' Preconditions: Verify that the specified part template exists.
'
' Postconditions:
' 1. Opens a new part document and creates a sketch.
' 2. Creates a sketch point in the sketch.
' 3. Examine the graphics area.
'---------------------------------------------------------------------------
```

```vb
Option Explicit

Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim swSkMgr As SldWorks.SketchManager
     Dim longstatus As Long
     Dim boolstatus As Boolean

    Set swApp = Application.SldWorks
     swApp.ResetUntitledCount 0, 0, 0
     Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)
     swApp.ActivateDoc2 "Part1", False, longstatus
     Set swModel = swApp.ActiveDoc

    Set swSkMgr = swModel.SketchManager
     swSkMgr.InsertSketch True
     boolstatus = swModel.Extension.SelectByID2("Top Plane", "PLANE", -5.53489443349025E-02, 3.30468607538553E-03, 2.69617286188933E-02, False, 0, Nothing, 0)
     swModel.ClearSelection2 True

    ' Check whether document is active
     If swModel Is Nothing Then
         swApp.SendMsgToUser2 "A part document must be active.", swMbWarning, swMbOk
         Exit Sub
     End If

    ' Check whether document is a part
     Dim modelType As Long
     modelType = swModel.GetType

    If modelType <> SwConst.swDocPART Then
         swApp.SendMsgToUser2 "A part document must be active.", swMbWarning, swMbOk
         Exit Sub
     End If

    Dim skPoint As SldWorks.SketchPoint
     Set skPoint = swSkMgr.CreatePoint(-0.127443, 0.042892, 0#)
     swSkMgr.InsertSketch True

End Sub
```
