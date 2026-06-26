---
title: "Select Assembly Components by Size Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Assembly_Components_by_Size_Example_VB.htm"
---

# Select Assembly Components by Size Example (VBA)

This example shows how to select components by percent of assembly size.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open an assembly.
 '
 ' Postconditions: Selects components that are 30% of the size of the
 ' assembly or smaller.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim assem As SldWorks.AssemblyDoc
 Dim bool As Boolean
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
     Set assem = Part
     bool = assem.SelectComponentsBySize(30#)

End Sub
```
