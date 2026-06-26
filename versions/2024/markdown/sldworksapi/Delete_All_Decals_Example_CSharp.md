---
title: "Delete all Decals Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_All_Decals_Example_CSharp.htm"
---

# Delete all Decals Example (C#)

## Delete All Decals Example (C#)

This example shows how to delete all decals in a model.

```vb
//---------------------------------------------------------------------------
 // Preconditions: Open a part with one or more decals.
 //
 // Postconditions: Deletes all of the decals from the part.
 // --------------------------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace DeleteAllDecals_CSharp.csproj
 {
     public partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel;
             ModelDocExtension swModelDocExt;
             Boolean boolStatus;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = (ModelDocExtension)swModel.Extension;
             boolStatus = swModelDocExt.DeleteAllDecals();

         }

         public SldWorks swApp;
     }
 }
```
