---
title: "Delete Decal Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Decal_Example_VBNET.htm"
---

# Delete Decal Example (VB.NET)

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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim arrDecals As Object
         Dim swDecal As Decal
         Dim boolstatus As Boolean
         Dim iDecalCnt As Integer
         Dim iDecalID As Integer
         Dim i As  Integer

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension

         iDecalCnt = swModelDocExt.GetDecalsCount
         Debug.Print("Decal Count : " & iDecalCnt)

         arrDecals = swModelDocExt.GetDecals()

         For i = LBound(arrDecals) To UBound(arrDecals)
             swDecal = arrDecals(i)
             iDecalID = swDecal.DecalID
             Debug.Print("Decal ID : " & iDecalID)
             boolstatus = swModelDocExt.DeleteDecal(iDecalID,  True)
         Next
     End Sub

     Public swApp As SldWorks

 End  Class
```
