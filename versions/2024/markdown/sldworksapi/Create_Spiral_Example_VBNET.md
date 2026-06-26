---
title: "Create Spiral Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Spiral_Example_VBNET.htm"
---

# Create Spiral Example (VB.NET)

This example shows how to create a spiral.

```
'----------------------------------------------------------
' Preconditions: Specified part template exists.
'
' Postconditions:
' 1. Opens a new part.
' 2. Selects Front Plane on which to create a circle.
' 3. Creates a circle.
' 4. Creates a spiral using the circle.
'----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchMgr As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim status As Boolean

        swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
        'Select Front Plane, create circle, and create
        'spiral using circle
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", -0.0517981810568133, 0.0505753331558577, 0.0012310671470727, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swSketchMgr = swModel.SketchManager
        swSketchSegment = swSketchMgr.CreateCircle(0.0#, 0.0#, 0.0#, 0.021866, 0.001156, 0.0#)
        swModel.InsertHelix(False, True, False, False, swHelixDefinedBy_e.swHelixDefinedBySpiral, 0, 0.04, 2, 0, 4.712388980385)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
