---
title: "Get Loops Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Loops_Example_VBNET.htm"
---

# Get Loops Example (VB.NET)

This example shows how to get loop data for the selected face.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Model document is open, and a face is selected.
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
         Dim swSelMgr As SelectionMgr
         Dim swFace As Face2
         Dim swLoop As Loop2

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFace = swSelMgr.GetSelectedObject6(1, -1)
         swLoop = swFace.GetFirstLoop

         Debug.Print("LoopCount = " & swFace.GetLoopCount)

         While Not swLoop Is  Nothing

             Debug.Print("  IsOuter      = " & swLoop.IsOuter)
             Debug.Print("  IsSingular   = " & swLoop.IsSingular)
             Debug.Print("  EdgeCount    = " & swLoop.GetEdgeCount)
             Debug.Print("  VertexCount  = " & swLoop.GetVertexCount)
             Debug.Print("")

             swLoop = swLoop.GetNext
         End While

     End Sub

     Public swApp As SldWorks

 End  Class
```
