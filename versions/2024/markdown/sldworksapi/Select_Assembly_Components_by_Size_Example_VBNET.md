---
title: "Select Assembly Components by Size Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Assembly_Components_by_Size_Example_VBNET.htm"
---

# Select Assembly Components by Size Example (VB.NET)

This example shows how to select components by percent of assembly size.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open an assembly.
 '
 ' Postconditions: Selects components that are 30% of the size of the
 ' assembly or smaller.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim assem As AssemblyDoc
     Dim bool As Boolean

     Sub main()

         Part = swApp.ActiveDoc
         assem = Part
         bool = assem.SelectComponentsBySize(30.0#)

     End Sub

     Public swApp As SldWorks

 End  Class
```
