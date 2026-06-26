---
title: "Insert GTol Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_GTol_Example_VBNET.htm"
---

# Insert GTol Example (VB.NET)

This example shows how to insert a GTol with a bent leader.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the drawing exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the drawing.
' 2. Inserts a GTol.
' 3. Sets and gets the length of the bent leader.
' 4. Gets whether to display the projected tolerance zone and its height
'    in the GTol.
' 5. Examine the Immediate window and GTol.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swDrawing As DrawingDoc
        Dim swModel As ModelDoc2
        Dim swGtol As Gtol
        Dim swAnno As Annotation
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String
        Dim frameNbr As Integer
        Dim tolNbr As Integer
        Dim display As Boolean
        Dim height As String

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
        swDrawing = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swApp.ActivateDoc3("foodprocessor - Sheet1", False, swRebuildOnActivation_e.swRebuildActiveDoc, errors)
        swModel = swDrawing

        swGtol = swModel.InsertGtol()
        If Not swGtol Is Nothing Then
            swGtol.SetFrameSymbols2(1, "<IGTOL-POSI>", False, "", False, "", "", "", "")
            status = swGtol.SetFrameValues2(1, "0.2", "", "B-A-C<MOD-MMC>", "B<MOD-MMC>-C<MOD-LMC>", "C<MOD-MMC>-A")
            status = swGtol.SetPTZHeight2(1, 1, True, "50")
            swGtol.SetBetweenTwoPoints(False, "", "")
            swAnno = swGtol.GetAnnotation()
            If Not swAnno Is Nothing Then
                status = swAnno.SetPosition(0.319315975204224, 0.12666668401487, 0)
                errors = swAnno.SetLeader3(swLeaderStyle_e.swBENT, swLeaderSide_e.swLS_LEFT, True, False, False, False)
                swAnno.BentLeaderLength = 0.05
                Debug.Print("Bent leader length: " & swAnno.BentLeaderLength)
            End If
        End If

        frameNbr = 1
        tolNbr = 1
        height = ""
        status = swGtol.GetPTZHeight2(frameNbr, tolNbr, display, height)
        Debug.Print("Projected tolerance zone: ")
        Debug.Print("  Display: " & display)
        Debug.Print("  Height: " & height)

        swModel.WindowRedraw()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
