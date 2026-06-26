---
title: "Save as De-Featured File Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_As_Defeatured_File_Example_VB.htm"
---

# Save as De-Featured File Example (VBA)

This example shows how to de-feature an assembly and save it as a part.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
' 2. Verify that c:\temp exists.
'
' Postconditions:
' 1. Saves the assembly as a de-featured part.
' 2. Open c:\temp\ball_valve.sldprt to verify.
'------------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    boolstatus = swModel.Extension.SaveDeFeaturedFile("c:\temp\ball_valve.sldprt")
```

```
End Sub
```
