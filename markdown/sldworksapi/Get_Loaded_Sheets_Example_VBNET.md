---
title: "Get Loaded Sheets Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Loaded_Sheets_Example_VBNET.htm"
---

# Get Loaded Sheets Example (VB.NET)

This example shows how to determine if the sheets in a drawing are loaded.

```
'----------------------------------------------
' Preconditions:
' 1. Click File > Open.
' 2. Browse to public_documents\samples\tutorial\advdrawings.
' 3. Select foodprocessor.slddrw.
' 4. Click Select sheets to open > Selected > Sheet1* (Load) > OK > Open.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Loads Sheet1 only.
' 2. Mouse over the Sheet2, Sheet3, and Sheet4 tabs and
'    examine the Immediate window to verify step 1.
'
' NOTE: Because this drawing is used elsewhere, do not save
' changes.
'----------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDraw As DrawingDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vSheetName As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim bRet As Boolean

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDraw = swModel

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the sheets in the drawing document
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vSheetName = swDraw.GetSheetNames

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Traverse the drawing sheets and determine whether
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' they're loaded
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To UBound(vSheetName)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bRet = swDraw.ActivateSheet(vSheetName(i))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim swSheet As Sheet
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSheet = swDraw.GetCurrentSheet
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If (swSheet.IsLoaded) Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(vSheetName(i) & " is loaded.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(vSheetName(i) & " is not loaded.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next i
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
