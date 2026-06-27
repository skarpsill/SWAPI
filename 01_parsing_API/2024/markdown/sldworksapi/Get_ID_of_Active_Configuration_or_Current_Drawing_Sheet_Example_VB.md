---
title: "Get ID of Active Configuration or Current Drawing Sheet Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_VB.htm"
---

# Get ID of Active Configuration or Current Drawing Sheet Example (VBA)

This example shows how to get the name and ID of the active configuration of
a part or assembly or the current sheet of a drawing.

**NOTE**: A unique ID is assigned to each configuration and drawing. This ID does
not change when the name of the configuration or drawing sheet is changed.

'---------------------------------------------------------------------------- ' Preconditions: ' 1. Open a part, assembly, or drawing document. ' 2. Open the Immediate window. ' ' Postconditions: ' 1. Changes either the active configuration's name or ' the current sheet's name to Test . However, the ' document's ID is unchanged. ' 2. Examine the Immediate window. '---------------------------------------------------------------------------

```vb
Option Explicit

Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swConfig As SldWorks.Configuration
 Dim swDrawingDoc As SldWorks.DrawingDoc
 Dim swSheet As SldWorks.Sheet
 Dim nDocType As Long
Sub main()
```

```vb
Set swApp = Application.SldWorks
 Set swModel = swApp.ActiveDoc

' Get type of model document
 If swModel.GetType = 1 Then
    kadov_tag{{</spaces>}}nDocType = swDocPART
 ElseIf swModel.GetType = 2 Then
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}nDocType = swDocASSEMBLY
 ElseIf swModel.GetType = 3 Then
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}nDocType = swDocDRAWING
 Else
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Not a SOLIDWORKS model document,
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' so exit macro
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Exit Sub
 End If
 kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
' If a part or assembly document,
 ' then get the name of it and its ID
 If nDocType <> swDocDRAWING Then
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swConfig = swModel.GetActiveConfiguration
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If Not swConfig Is Nothing Then
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Active configuration's name = " & swConfig.Name & ", ID = " & swConfig.GetID
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Change the active configuration's name
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swConfig.Name = "Test"
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Test to see if the ID remains the same
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' after changing the name of the configuration
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Active configuration's new name = " & swConfig.Name & ", ID = " & swConfig.GetID
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Exit Sub
 End If

 ' A drawing sheet must be active,
 ' so get its name and ID
 Set swDrawingDoc = swModel
 Set swSheet = swDrawingDoc.GetCurrentSheet
 If Not swSheet Is Nothing Then
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Current sheet's name = " & swSheet.GetName & ", ID = " & swSheet.GetID
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Change current sheet's name
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swSheet.SetName "Test"
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Test to see if the ID remains the same
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' after changing the name of the sheet
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Current sheet's new name = " & swSheet.GetName & ", ID = " & swSheet.GetID
 End If
```

```vb
End Sub
```
