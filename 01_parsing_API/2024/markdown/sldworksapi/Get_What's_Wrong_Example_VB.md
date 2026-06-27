---
title: "Get What's Wrong Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_What's_Wrong_Example_VB.htm"
---

# Get What's Wrong Example (VBA)

This example shows how to get the What's Wrong information for a document.

```vb
'-----------------------------------
' Preconditions: Model document is active. Examine the Immediate
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}window after running this macro to see the What's Wrong
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}items in the model document.
'
' Postconditions: None
'------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim vFeatures As Variant
Dim vErrorCodes As Variant
Dim vWarnings As Variant
Dim boolstatus As Boolean
Dim i As Long
Dim nbrWhatsWrong As Long
Dim swFeature As SldWorks.Feature

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swModelDocExt = swModel.Extension
nbrWhatsWrong = swModelDocExt.GetWhatsWrongCount
Debug.Print "Number of What's Wrong items: " & nbrWhatsWrong
Debug.Print ""
If nbrWhatsWrong > 0 Then
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swModelDocExt.GetWhatsWrong(vFeatures, vErrorCodes, vWarnings)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For i = 0 To UBound(vFeatures)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swFeature = vFeatures(i)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Name of feature: " & swFeature.GetTypeName2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Error: " & vErrorCodes(i)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Did SOLIDWORKS flag this item as a warning ? " & vWarnings(i)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print ""
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next i
Else
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "No What's Wrong items."
End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
```
