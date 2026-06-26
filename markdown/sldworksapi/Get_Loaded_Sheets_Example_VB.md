---
title: "Get Loaded Sheets Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Loaded_Sheets_Example_VB.htm"
---

# Get Loaded Sheets Example (VBA)

This example shows how to determine which sheets in a drawing document
are loaded.

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
Sub main()

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swApp kadov_tag{{<spaces>}}                      kadov_tag{{</spaces>}}As SldWorks.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModel kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}As SldWorks.ModelDoc2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swDraw kadov_tag{{<spaces>}}                     kadov_tag{{</spaces>}}As SldWorks.DrawingDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vSheetName kadov_tag{{<spaces>}}                 kadov_tag{{</spaces>}}As Variant
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim nRetval kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim i kadov_tag{{<spaces>}}                          kadov_tag{{</spaces>}}As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim bRet kadov_tag{{<spaces>}}                       kadov_tag{{</spaces>}}As Boolean

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swApp = Application.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swDraw = swModel
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get the sheets in the drawing document
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vSheetName = swDraw.GetSheetNames
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Traverse the drawing sheets and determine whether
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' they're loaded
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For i = 0 To UBound(vSheetName)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bRet = swDraw.ActivateSheet(vSheetName(i))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSheet As Sheet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swSheet = swDraw.GetCurrentSheet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If (swSheet.IsLoaded) Then
kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}Debug.Print vSheetName(i) & " is loaded."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}Debug.Print vSheetName(i) & " is not loaded."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next i
End Sub
```
