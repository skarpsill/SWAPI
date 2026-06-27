---
title: "Delete all Decals Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_All_Decals_Example_VBNET.htm"
---

# Delete all Decals Example (VB.NET)

## Delete All Decals Example (VB.NET)

This example shows how to delete all decals in a model.

```vb
'----------------------------------------------------------------------------
 ' Preconditions: Open a part with one or more decals.
 '
 ' Postconditions: Deletes all of the decals from the part.
 ' ---------------------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Public Sub main()
         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim boolStatus As Boolean

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension
         boolStatus = swModelDocExt.DeleteAllDecals()

     End Sub

     Public swApp As SldWorks

 End  Class
```
