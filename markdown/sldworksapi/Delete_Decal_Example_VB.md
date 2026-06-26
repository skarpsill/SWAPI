---
title: "Delete Decal Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Decal_Example_VB.htm"
---

# Delete Decal Example (VBA)

This example shows how to delete a decal from a model.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document that has at least one
 '    decal applied to it.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Deletes all of the decals.
 ' 2. Examine the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim arrDecals As Variant
 Dim swDecal As SldWorks.Decal
 Dim boolstatus As Boolean
 Dim iDecalCnt As Integer
 Dim iDecalID As Integer
 Dim i As Integer
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension

    iDecalCnt = swModelDocExt.GetDecalsCount
     Debug.Print "Decal Count : " & iDecalCnt

    arrDecals = swModelDocExt.GetDecals()

    For i = LBound(arrDecals) To UBound(arrDecals)
         Set swDecal = arrDecals(i)
         iDecalID = swDecal.DecalID
         Debug.Print "Decal ID : " & iDecalID
         boolstatus = swModelDocExt.DeleteDecal(iDecalID, True)
     Next
End Sub
```
