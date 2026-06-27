---
title: "Get Layers Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Layers_Example_VBNET.htm"
---

# Get Layers Example (VB.NET)

This example shows how to get the layers in a drawing document.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing document.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swLayerMgr As LayerMgr
         Dim vLayerArr As Object
         Dim vLayer As Object
         Dim swLayer As Layer

         swModel = swApp.ActiveDoc
         swLayerMgr = swModel.GetLayerManager

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  Current Layer = " & swLayerMgr.GetCurrentLayer)
         Debug.Print("")

         vLayerArr = swLayerMgr.GetLayerList
         For Each vLayer In vLayerArr
             swLayer = swLayerMgr.GetLayer(vLayer)

             Debug.Print("    Layer          = " & swLayer.Name)
             Debug.Print("    Color          = " & swLayer.Color)
             Debug.Print("    Description    = " & swLayer.Description)
             Debug.Print("    ID             = " & swLayer.GetID)
             Debug.Print("    Style          = " & swLayer.Style)
             Debug.Print("    Visible        = " & swLayer.Visible)
             Debug.Print("    Width          = " & swLayer.Width)
             Debug.Print("    Printable      = " & swLayer.Printable)
         Next

     End Sub

     Public swApp As SldWorks

 End  Class
```
