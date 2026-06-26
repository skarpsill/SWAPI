---
title: "Delete all Decals Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_All_Decals_Example_VB.htm"
---

# Delete all Decals Example (VBA)

## Delete All Decals Example (VBA)

This example shows how to delete all decals from a model.

```vb
'----------------------------------------------------------------------------
' Preconditions: Open a part with one or more decals.
 '
 ' Postconditions: Deletes all of the decals from the part.
 ' ---------------------------------------------------------------------------
Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim boolStatus As Boolean
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     boolStatus = swModelDocExt.DeleteAllDecals()
End Sub
```
