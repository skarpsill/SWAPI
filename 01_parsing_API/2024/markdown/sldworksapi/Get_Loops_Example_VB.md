---
title: "Get Loops Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Loops_Example_VB.htm"
---

# Get Loops Example (VBA)

This example shows how to get loop data for the selected face.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Model document is open, and a face is selected.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swFace                  As SldWorks.Face2
     Dim swLoop                  As SldWorks.Loop2
    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFace = swSelMgr.GetSelectedObject6(1, -1)
     Set swLoop = swFace.GetFirstLoop
    Debug.Print "LoopCount = " & swFace.GetLoopCount
    While Not swLoop Is Nothing
        Debug.Print "  IsOuter      = " & swLoop.IsOuter
         Debug.Print "  IsSingular   = " & swLoop.IsSingular
         Debug.Print "  EdgeCount    = " & swLoop.GetEdgeCount
         Debug.Print "  VertexCount  = " & swLoop.GetVertexCount
         Debug.Print ""
        Set swLoop = swLoop.GetNext
     Wend
End Sub
```
