---
title: "Flip Dowel Pin Symbol Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Flip_Dowel_Pin_Symbol_Example_VB.htm"
---

# Flip Dowel Pin Symbol Example (VBA)

This example shows how to insert and flip a dowel pin symbol in a drawing.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing document
'    to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing document.
' 2. Selects a circular edge in a drawing view.
' 3. Inserts a dowel pin symbol.
' 4. Selects the dowel pin symbol and flips it.
' 5. Examine the drawing and the Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'---------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawingDoc As SldWorks.DrawingDoc
Dim swDowelSymbol As SldWorks.DowelSymbol
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swAnnotation As SldWorks.Annotation
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open drawing document and insert a dowel pin symbol
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem20.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("", "EDGE", 0.128048002364532, 0.165546371003625, -1499.96487716824, False, 0, Nothing, 0)
    Set swDrawingDoc = swModel
    Set swDowelSymbol = swDrawingDoc.InsertDowelSymbol()
    swModel.ClearSelection2 True
```

```
    'Flip the dowel pin symbol
    status = swModelDocExt.SelectByID2("DetailItem354@Drawing View1", "DOWELSYM", 0.121630029714286, 0.180965058285714, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swDowelSymbol = swSelectionMgr.GetSelectedObject6(1, -1)
    swDowelSymbol.Flipped = True
    swModel.EditRebuild3
    Debug.Print "Dowel pin symbol flipped? " & swDowelSymbol.Flipped
    Set swAnnotation = swDowelSymbol.GetAnnotation
    Debug.Print "Name of dowel pin symbol annotation: " & swAnnotation.GetName

End Sub
```
