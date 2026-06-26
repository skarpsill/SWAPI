---
title: "Get OLE Object Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_OLE_Object_Data_Example_VBNET.htm"
---

# Get OLE Object Data Example (VB.NET)

This example shows how to get OLE object data from a model document.

```vb
  '----------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document.
 ' 2. Click Insert > Object.
 ' 3. Click Paintbrush Picture > OK.
 ' 4. Click File > Close.
 ' 5. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '-----------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swModelDocExt As ModelDocExtension
     Dim swSelMgr As SelectionMgr
     Dim swOleObj As SwOLEObject
     Dim boolstatus As Boolean

     Sub main()

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension
         swSelMgr = swModel.SelectionManager

         swOleObj = swSelMgr.GetSelectedObject6(1, 0)

         Debug.Print("OLE Object")
         Debug.Print("  Class ID: " & swOleObj.Clsid)
         Debug.Print("  Is linked? " & swOleObj.IsLinked)
         Debug.Print("    Filename: " & swOleObj.FileName)
         Debug.Print("  Buffer size: " & swOleObj.BufferSize)
         Debug.Print("  Viewing aspect (1=Content, 2=Thumbnail, 4=Icon, 8=DocPrint): " & swOleObj.Aspect)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
