---
title: "Create, Unlink, and Purge Display States in Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create,_Unlink,_and_Purge_Display_States_in_Part_Example_VBNET.htm"
---

# Create, Unlink, and Purge Display States in Part Example (VB.NET)

This example shows how to create, unlink, and purge display states in
a part document.

```
'---------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\multibody\multi-inter.sldprt,
'    whose Default configuration has two display states:
'    * PhotoWorks Display
'    * Display State 1
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates and unlinks Display State 2.
' 2. Attempts to purge any display states identical to
'    Display State 2.
' 3. Closes the part document without saving any changes.
' 4. Examine the Immediate window.
'-----------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```vb
 Partial Class SolidWorksMacro

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swConfig As Configuration
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim modelName As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get Default configuration and create a display state
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swConfig = (swModel.GetConfigurationByName("Default"))
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swConfig.CreateDisplayState("Display State 2")
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If boolstatus Then Debug.Print("Display State 2 created.")
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ForceRebuild3(True)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If display is linked, unlink it
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Is Display State 2 linked? " & swModelDocExt.LinkedDisplayState)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt.LinkedDisplayState = False
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Is Display State 2 still linked? " & swModelDocExt.LinkedDisplayState)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Purge any display states identical to Display State 2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.PurgeDisplayState
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Identical display states to Display State 2 purged? " & boolstatus)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ForceRebuild3(True)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Close the part without saving changes
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}modelName = swModel.GetTitle
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.QuitDoc(modelName)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
```
