---
title: "Insert Explode Line Sketch and Route Line Example(VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Exploded_Line_Sketch_and_Route_Line_Example_VB.htm"
---

# Insert Explode Line Sketch and Route Line Example(VBA)

## Insert Explode Line Sketch and Route Line Example (VBA)

This example shows how to insert a route line in an explode line sketch.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates an exploded view of the assembly.
' 2. Adds a route line, which is a type of explode line.
' 3. Examine the Immediate window and graphics area.
' 4. Locate and click 3DExplode1, the explode line sketch, on the
'    ConfigurationManager tab (click the ConfigurationManager
'    tab and expand default and ExplView1).
'
' NOTE: Because this assembly is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssembly As SldWorks.AssemblyDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swSketch As SldWorks.Sketch
Dim swSketchMgr As SldWorks.SketchManager
Dim swFace As SldWorks.Face2
Dim itemsToConnect(1) As Variant
Dim itemsReverse(1) As Variant
Dim itemsPath(1) As Variant
Dim alongXYZ(1) As Variant
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssembly = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
    Set swSketchMgr = swModel.SketchManager
```

```
    ' Explode the assembly
    swAssembly.AutoExplode
```

```
    swModel.EditRebuild3
```

```
    swModel.ViewZoomtofit2
```

```
    ' Insert an explode line sketch
    swSketchMgr.InsertExplodeLineSketch
```

```
    ' Select two faces for the route line
    boolstatus = swModelDocExt.SelectByID2("", "FACE", -5.55234504082591E-03, 2.71707519863185E-02, 3.37956573349629E-03, False, 0, Nothing, 0)
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
    Set itemsToConnect(0) = swFace
```

```
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 5.81777224675761E-03, 2.11322449790146E-02, 0.127676153954326, True, 0, Nothing, 0)
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
    Set itemsToConnect(1) = swFace
```

```
    itemsReverse(0) = False
    itemsReverse(1) = False
    itemsPath(0) = False
    itemsPath(1) = False
    alongXYZ(0) = False
    alongXYZ(1) = False
```

```
    ' Insert the route line in the explode line sketch
    Set swSketch = swModel.GetActiveSketch2
    boolstatus = swSketch.InsertRouteLine((itemsToConnect), itemsReverse, itemsPath, alongXYZ)
    Debug.Print "Route line inserted in explode line sketch? " & boolstatus
```

```
    ' Close the explode line sketch
    swSketchMgr.InsertExplodeLineSketch
```

```
End Sub
```
