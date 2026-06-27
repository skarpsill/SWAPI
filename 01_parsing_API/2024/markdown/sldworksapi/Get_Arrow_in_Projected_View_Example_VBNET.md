---
title: "Get Arrow in Projected View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Arrow_in_Projected_View_Example_VBNET.htm"
---

# Get Arrow in Projected View Example (VB.NET)

This example shows how to get the arrow in a projected view.

```
'---------------------------------------------------------
' Preconditions:
' 1. Open a drawing that has a projected view that contains
'    an arrow with a label.
' 2. Select that projected view.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets information about the projected view's arrow.
' 2. Examine the Immediate window.
'--------------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Sub ProcessTextFormat(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swTextFormat As TextFormat)
        Debug.Print("    BackWards                    = " & swTextFormat.BackWards)
        Debug.Print("    Bold                         = " & swTextFormat.Bold)
        Debug.Print("    CharHeight                   = " & swTextFormat.CharHeight)
        Debug.Print("    CharHeightInPts              = " & swTextFormat.CharHeightInPts)
        Debug.Print("    CharSpacingFactor            = " & swTextFormat.CharSpacingFactor)
        Debug.Print("    Escapement                   = " & swTextFormat.Escapement)
        Debug.Print("    IsHeightSpecifiedInPts       = " & swTextFormat.IsHeightSpecifiedInPts)
        Debug.Print("    Italic                       = " & swTextFormat.Italic)
        Debug.Print("    LineLength                   = " & swTextFormat.LineLength)
        Debug.Print("    LineSpacing                  = " & swTextFormat.LineSpacing)
        Debug.Print("    ObliqueAngle                 = " & swTextFormat.ObliqueAngle)
        Debug.Print("    Strikeout                    = " & swTextFormat.Strikeout)
        Debug.Print("    TypeFaceName                 = " & swTextFormat.TypeFaceName)
        Debug.Print("    Underline                    = " & swTextFormat.Underline)
        Debug.Print("    UpsideDown                   = " & swTextFormat.UpsideDown)
        Debug.Print("    Vertical                     = " & swTextFormat.Vertical)
        Debug.Print("    WidthFactor                  = " & swTextFormat.WidthFactor)
        Debug.Print("")
    End Sub

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swDraw As DrawingDoc
        Dim swView As View
        Dim swProjArr As ProjectionArrow
        Dim swBaseView As View
        Dim vCoord As Object
        Dim swTextFormat As TextFormat
        Dim bRet As Boolean

        swModel = swApp.ActiveDoc
        swDraw = swModel
        swSelMgr = swModel.SelectionManager
        swView = swSelMgr.GetSelectedObject6(1, -1)
        swProjArr = swView.GetProjectionArrow
        swBaseView = swProjArr.GetView
        swTextFormat = swProjArr.GetTextFormat
        vCoord = swProjArr.GetCoordinates
        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print("  " & swView.Name & " --> " & swBaseView.Name)
        Debug.Print("  Coordinates              = (" & vCoord(0) * 1000.0# & ", " & vCoord(1) * 1000.0# & ", " & vCoord(2) * 1000.0# & ") mm")
        Debug.Print("  Label                    = " & swProjArr.GetLabel)
        Debug.Print("  Use document text format = " & swProjArr.GetUseDocTextFormat)

        ProcessTextFormat(swApp, swModel, swTextFormat)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
