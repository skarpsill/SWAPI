---
title: "Delete Decal Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Decal_Example_CSharp.htm"
---

# Delete Decal Example (C#)

This example shows how to delete a decal from a model.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a model document that has at least one
 //    decal applied to it.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Deletes all of the decals.
 // 2. Examine the Immediate window.
 //----------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace DeleteDecal_CSharp.csproj
 {
     public partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel;
             ModelDocExtension swModelDocExt;
             Object[] arrDecals;
             Decal swDecal;
             Boolean boolstatus;
             int iDecalCnt;
             int iDecalID;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = (ModelDocExtension)swModel.Extension;

             iDecalCnt = swModelDocExt.GetDecalsCount();
             Debug.Print("Decal Count : " + iDecalCnt);

             arrDecals = (Object[])swModelDocExt.GetDecals();

             for (int i = 0; i <= arrDecals.Length - 1; i++ )
             {
                 swDecal = (Decal)arrDecals[i];
                 iDecalID = swDecal.DecalID;
                 Debug.Print("Decal ID: " + iDecalID);
                 boolstatus = swModelDocExt.DeleteDecal(iDecalID, true);
             }

         }

         public SldWorks swApp;
     }
 }
```
