---
title: "Get Chamfer Dimension Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Chamfer_Dimension_Example_VBNET.htm"
---

# Get Chamfer Dimension Example (VB.NET)

This example shows how to the values of a chamfer dimension.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing that contains a chamfered part.
' 2. Click Tools > Dimension > Chamfer.
' 3. Select a chamfered edge, select one of the lead-in edges, and click
'    the drawing to display and select the chamfer dimension.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Gets the chamfer dimensions.
' 2. Examine the Immediate window.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swDisplayDimension As DisplayDimension
        Dim swDimension As Dimension
        Dim status As Boolean
        Dim length As Double
        Dim angle As Double

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swSelMgr = swModel.SelectionManager

        'Get chamfer dimensions
        swDisplayDimension = swSelMgr.GetSelectedObject6(1, -1)
        swDimension = swDisplayDimension.GetDimension
        status = swDimension.GetSystemChamferValues(length, angle)
        Debug.Print("Is selected dimension a chamfer dimension? " & status)
        '1 radian = 180º/p = 57.295779513º or approximately 57.3º
        Debug.Print("Angle = " & (angle * 57.3) & " degrees")
        Debug.Print("Length = " & length)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
