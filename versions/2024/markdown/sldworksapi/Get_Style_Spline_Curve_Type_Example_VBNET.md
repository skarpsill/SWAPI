---
title: "Get Style Spline Curve Type Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Style_Spline_Curve_Type_Example_VBNET.htm"
---

# Get Style Spline Curve Type Example (VB.NET)

This example shows how to create a style spline and get its type of curve.

```
'---------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates a style spline.
' 3. Selects the style spline.
' 4. Gets whether the selection is a style spline
'    and, if so, gets its curve type.
' 5. Examine the Immediate window.
'---------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchManager As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swSketchSpline As SketchSpline
        Dim swSelectionMgr As SelectionMgr
        Dim pointArray As Object
        Dim points() As Double
        Dim status As Boolean

        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\part.prtdot", 0, 0, 0)

        ' Create style spline
        ReDim points(0 To 32)
        points(0) = -0.068952134919552
        points(1) = 0.00871923799128056
        points(2) = 0
        points(3) = -0.0563242730011457
        points(4) = 0.0185409083722633
        points(5) = 0
        points(6) = -0.0418924308086813
        points(7) = 0.00871923799128056
        points(8) = 0
        points(9) = -0.0204451097726579
        points(10) = 0.0243537336997836
        points(11) = 0
        points(12) = 0.00621370983286659
        points(13) = -0.0125276407920698
        points(14) = 0
        points(15) = 0.0244539548261202
        points(16) = -0.00450995068514512
        points(17) = 0
        points(18) = 0.0330729716910642
        points(19) = 0.00631393095920317
        points(20) = 0
        points(21) = 0.048306582894221
        points(22) = 0.0117258717813773
        points(23) = 0
        points(24) = 0.05852913778055
        points(25) = -0.00611348870653004
        points(26) = 0
        points(27) = 0.0653441743714359
        points(28) = -0.0107236605180117
        points(29) = 0
        points(30) = -999999999
        points(31) = -999999999
        points(32) = -999999969
        pointArray = points
        swSketchManager = swModel.SketchManager
        swSketchSegment = swSketchManager.CreateSpline2((pointArray), True)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

        ' Get whether selection is style spline and, if so, get its curve type
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Spline1@Sketch1", "EXTSKETCHSEGMENT", -0.0311890911939585, 0.0122942518144824, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swSketchSpline = swSelectionMgr.GetSelectedObject6(1, -1)
        status = swSketchSpline.IsStyleSpline
        Debug.Print("Is the selection a style spline? " & status)
        If status Then
            Debug.Print("Style spline curve type (3 = swStyleSplineCurveType_e.BSpline_Degree7): " & swSketchSpline.CurveType)
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
