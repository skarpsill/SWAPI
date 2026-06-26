---
title: "Insert Body-Delete/Keep Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Delete_Body_Feature_Example_CSharp.htm"
---

# Insert Body-Delete/Keep Feature Example (C#)

This example shows how to insert a Body-Delete/Keep feature into a multibody part.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\multibody\multi_local.sldprt.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates Body-Delete/Keep 1 in the FeatureManager design tree.
 // 2. Inspect the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 // ---------------------------------------------------------------------------
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace InsertDeleteBody_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         Feature myFeature;
         DeleteBodyFeatureData insDelBody;

         bool boolstatus;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             // Select body to delete
             boolstatus = Part.Extension.SelectByID2("Fillet5", "SOLIDBODY", 0.0592851881957586, 0.0409115950836281, -0.0197275812591329,  true, 0,  null, 0);
             // Create a Body-Delete/Keep feature
             myFeature = Part.FeatureManager.InsertDeleteBody2(false);

             insDelBody = (DeleteBodyFeatureData)myFeature.GetDefinition();
             Debug.Print("Number of bodies in this Body-Delete/Keep feature: " + insDelBody.GetBodiesCount());
             Debug.Print("Keep bodies: " + insDelBody.KeepBodies);

         }

         public SldWorks swApp;

     }
 }
```
