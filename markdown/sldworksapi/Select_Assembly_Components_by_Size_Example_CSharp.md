---
title: "Select Assembly Components by Size Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Assembly_Components_by_Size_Example_CSharp.htm"
---

# Select Assembly Components by Size Example (C#)

This example shows how to select components by percent of assembly size.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open an assembly.
 //
 // Postconditions: Selects components that are 30% of the size of the
 // assembly or smaller.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace SelectComponentsBySize_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         AssemblyDoc assem;
          bool  result;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             assem = (AssemblyDoc)Part;
             result = assem.SelectComponentsBySize(30.0);

         }

         public SldWorks swApp;

     }
 }
```
