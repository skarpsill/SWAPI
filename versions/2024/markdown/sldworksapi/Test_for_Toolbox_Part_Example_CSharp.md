---
title: "Test for Toolbox Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Test_for_Toolbox_Part_Example_CSharp.htm"
---

# Test for Toolbox Part Example (C#)

This example shows how to test whether a part is a Toolbox part.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\bagel.sldprt.
 //
 // Postconditions: Inspect the Immediate window for the Toolbox part type.
 //
 // NOTE: Because the model is used elsewhere,
 // do not save changes when closing it.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace ToolboxPartType_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 part;
         ModelDocExtension modelDocExt;

         int ret;

         public void Main()
         {
             part = (ModelDoc2)swApp.ActiveDoc;
             modelDocExt = part.Extension;
             ret = modelDocExt.ToolboxPartType;

             Debug.Print("Toolbox part type as defined in swToolBoxPartType_e? " + ret);

         }

         public SldWorks swApp;

     }
 }
```
