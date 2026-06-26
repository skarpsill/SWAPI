---
title: "Rebuild an Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rebuild_an_Assembly_Example_CSharp.htm"
---

# Rebuild an Assembly Example (C#)

This example shows how to rebuild an assembly.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\wrench.sldasm.
 //
 // Postconditions:
 // 1. Rebuilds the assembly.
 // 2. Inspect the Immediate window for the result code.
 //
 // NOTE: Because the model is used elsewhere,
 // do not save changes when closing it.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace Rebuild_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 part;
         ModelDocExtension modelDocExt;

         bool ret;

         public void Main()
         {
             part = (ModelDoc2)swApp.ActiveDoc;
             modelDocExt = part.Extension;
             ret = modelDocExt.Rebuild((int)swRebuildOptions_e.swRebuildAll);

             Debug.Print("Successfully rebuilt? " + ret);

         }

         public SldWorks swApp;

     }

 }
```
