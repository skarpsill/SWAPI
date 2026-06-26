---
title: "Flip Dowel Pin Symbol Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Flip_Dowel_Pin_Symbol_Example_VBNET.htm"
---

# Flip Dowel Pin Symbol Example (VB.NET)

This example shows how to insert and flip a dowel pin symbol in a drawing.

```
'--------------------------------------------------------------
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
'--------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swDrawingDoc As DrawingDoc
        Dim swDowelSymbol As DowelSymbol
        Dim swSelectionMgr As SelectionMgr
        Dim swAnnotation As Annotation
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        'Open drawing document and insert a dowel pin symbol
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem20.slddrw"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("", "EDGE", 0.128048002364532, 0.165546371003625, -1499.96487716824, False, 0, Nothing, 0)
        swDrawingDoc = swModel
        swDowelSymbol = swDrawingDoc.InsertDowelSymbol()
        swModel.ClearSelection2(True)

        'Flip the dowel pin symbol
        status = swModelDocExt.SelectByID2("DetailItem354@Drawing View1", "DOWELSYM", 0.121630029714286, 0.180965058285714, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swDowelSymbol = swSelectionMgr.GetSelectedObject6(1, -1)
        swDowelSymbol.Flipped = True
        swModel.EditRebuild3()
        Debug.Print("Dowel pin symbol flipped? " & swDowelSymbol.Flipped)
        swAnnotation = swDowelSymbol.GetAnnotation
        Debug.Print("Name of dowel pin symbol annotation: " & swAnnotation.GetName)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
