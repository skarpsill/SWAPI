---
title: "Get Sense for Each Coedge in a Loop (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sense_for_Each_Coedge_in_a_Loop_Example_VB.htm"
---

# Get Sense for Each Coedge in a Loop (VBA)

This example gets the coedges in a loop and their senses.

```vb
'--------------------------------------
 ' Preconditions:
 ' 1. Open a model document.
 ' 2. Select a face on the model.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Traverses the loops on the selected face.
 ' 2. Gets the number of coedges on the selected face
 '    and the sense (i.e., true if the coedge has the same
 '    direction as the underlying edge, false if not)
 '    for each coedge.
 ' 3. Examine the Immediate window.
 '--------------------------------------
 Option Explicit

 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim myEdge As SldWorks.CoEdge
 Dim myLoop As SldWorks.Loop2
 Dim myFace As SldWorks.Face2
 Dim myEdges As Variant
 Dim index As Long
 Dim count As Long

 Sub main()
```

```vb
Set swApp = Application.SldWorks
 Set swModel = swApp.ActiveDoc
 Set swSelMgr = swModel.SelectionManager
 Set myFace = swSelMgr.GetSelectedObject6(1, -1)

 ' Get the first loop on the selected face
 Set myLoop = myFace.GetFirstLoop
 ' Get the number of coedges in the loop
 count = myLoop.GetCoEdgeCount
 Debug.Print count

 ' Get the coedges in the loop
 myEdges = myLoop.GetCoEdges
 ' For each coedge, get its sense
```

```vb
For index = LBound(myEdges) To UBound(myEdges)
 Set myEdge = myEdges(index)
 Debug.Print myEdge.GetSense
```

```vb
Next index
```

```vb
End Sub
```
