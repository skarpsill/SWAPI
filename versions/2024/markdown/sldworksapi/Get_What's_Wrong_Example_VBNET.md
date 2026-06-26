---
title: "Get What's Wrong Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_What's_Wrong_Example_VBNET.htm"
---

# Get What's Wrong Example (VB.NET)

This example shows how to get the What's Wrong information for a document.

```vb
'-----------------------------------
' Preconditions: Model document is active. Examine the Immediate
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}window after running this macro to see the What's Wrong
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}items in the model document.
'
' Postconditions: None
'------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()
```

```vb
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vFeatures As Object = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vErrorCodes As Object = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vWarnings As Object = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nbrWhatsWrong As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeature As Feature

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}nbrWhatsWrong = swModelDocExt.GetWhatsWrongCount
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Number of What's Wrong items: " & nbrWhatsWrong)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If nbrWhatsWrong > 0 Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.GetWhatsWrong(vFeatures, vErrorCodes, vWarnings)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}For i = 0 To UBound(vFeatures)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swFeature = vFeatures(i)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Name of feature: " & swFeature.GetTypeName2)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Error: " & vErrorCodes(i))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Did SOLIDWORKS flag this item as a warning ? " & vWarnings(i))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Next i
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("No What's Wrong items.")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
