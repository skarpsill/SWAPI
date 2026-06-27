---
title: "Insert Explode Line Sketch and Route Line Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Exploded_Line_Sketch_and_Route_Line_Example_VBNET.htm"
---

# Insert Explode Line Sketch and Route Line Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swAssembly As AssemblyDoc
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swSketch As Sketch
        Dim swSketchMgr As SketchManager
        Dim swFace As Face2
        Dim itemsToConnect(1) As Object
        Dim itemsReverse(1) As Object
        Dim itemsPath(1) As Object
        Dim alongXYZ(1) As Object
        Dim boolstatus As Boolean

        swModel = swApp.ActiveDoc
        swAssembly = swModel
        swSelMgr = swModel.SelectionManager
        swModelDocExt = swModel.Extension
        swSketchMgr = swModel.SketchManager

        ' Explode the assembly
        swAssembly.AutoExplode()
        swModel.EditRebuild3()
        swModel.ViewZoomtofit2()

        ' Insert an explode line sketch
        swSketchMgr.InsertExplodeLineSketch()

        ' Select two faces for the route line
        boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.00555234504082591, 0.0271707519863185, 0.00337956573349629, False, 0, Nothing, 0)
        swFace = swSelMgr.GetSelectedObject6(1, -1)
        itemsToConnect(0) = swFace
        boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00581777224675761, 0.0211322449790146, 0.127676153954326, True, 0, Nothing, 0)
        swFace = swSelMgr.GetSelectedObject6(1, -1)
        itemsToConnect(1) = swFace

        itemsReverse(0) = False
        itemsReverse(1) = False
        itemsPath(0) = False
        itemsPath(1) = False
        alongXYZ(0) = False
        alongXYZ(1) = False

        ' Insert the route line in the explode line sketch
        swSketch = swModel.GetActiveSketch2
        boolstatus = swSketch.InsertRouteLine((itemsToConnect), itemsReverse, itemsPath, alongXYZ)
        Debug.Print("Route line inserted in explode line sketch? " & boolstatus)

        ' Close the explode line sketch
        swSketchMgr.InsertExplodeLineSketch()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
