---
title: "Insert GTol Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_GTol_Example_VB.htm"
---

# Insert GTol Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swDrawing As SldWorks.DrawingDoc
Dim swModel As SldWorks.ModelDoc2
Dim swGtol As SldWorks.Gtol
Dim swAnno As SldWorks.Annotation
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim frameNbr As Long
Dim tolNbr As Long
Dim display As Boolean
Dim height As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
    Set swDrawing = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    swApp.ActivateDoc3 "foodprocessor - Sheet1", False, swRebuildOnActivation_e.swRebuildActiveDoc, errors
    Set swModel = swDrawing
```

```
    Set swGtol = swModel.InsertGtol()
    If Not swGtol Is Nothing Then
        swGtol.SetFrameSymbols2 1, "<IGTOL-POSI>", False, "", False, "", "", "", ""
        status = swGtol.SetFrameValues2(1, "0.4", "", "B-A-C<MOD-MMC>", "B<MOD-MMC>-C<MOD-LMC>", "C<MOD-MMC>-A")
        status = swGtol.SetPTZHeight2(1, 1, True, "50")
        swGtol.SetBetweenTwoPoints False, "", ""
        Set swAnno = swGtol.GetAnnotation()
        If Not swAnno Is Nothing Then
            status = swAnno.SetPosition(0.319315975204224, 0.12666668401487, 0)
            errors = swAnno.SetLeader3(swLeaderStyle_e.swBENT, swLeaderSide_e.swLS_LEFT, True, False, False, False)
            swAnno.BentLeaderLength = 0.05
            Debug.Print "Bent leader length: " & swAnno.BentLeaderLength
        End If
    End If

    frameNbr = 1
    tolNbr = 1
    height = ""
    status = swGtol.GetPTZHeight2(frameNbr, tolNbr, display, height)
    Debug.Print "Projected tolerance zone: "
    Debug.Print "  Display: " & display
    Debug.Print "  Height: " & height

    swModel.WindowRedraw
```

```
End Sub
```
