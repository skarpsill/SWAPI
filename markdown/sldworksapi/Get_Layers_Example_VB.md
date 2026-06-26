---
title: "Get Layers Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Layers_Example_VB.htm"
---

# Get Layers Example (VBA)

This example shows how to get the layers in a drawing document.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing document.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                       As SldWorks.SldWorks
     Dim swModel                     As SldWorks.ModelDoc2
     Dim swLayerMgr                  As SldWorks.LayerMgr
     Dim vLayerArr                   As Variant
     Dim vLayer                      As Variant
     Dim swLayer                     As SldWorks.Layer
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swLayerMgr = swModel.GetLayerManager
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  Current Layer = " & swLayerMgr.GetCurrentLayer
     Debug.Print ""
    vLayerArr = swLayerMgr.GetLayerList
     For Each vLayer In vLayerArr
         Set swLayer = swLayerMgr.GetLayer(vLayer)
        Debug.Print "    Layer          = " & swLayer.Name
         Debug.Print "    Color          = " & swLayer.Color
         Debug.Print "    Description    = " & swLayer.Description
         Debug.Print "    ID             = " & swLayer.GetID
         Debug.Print "    Style          = " & swLayer.Style
         Debug.Print "    Visible        = " & swLayer.Visible
         Debug.Print "    Width          = " & swLayer.Width
         Debug.Print "    Printable      = " & swLayer.Printable
     Next
End Sub
```
