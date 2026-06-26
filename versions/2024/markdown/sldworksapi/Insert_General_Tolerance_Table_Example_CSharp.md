---
title: "Insert General Tolerance Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_General_Tolerance_Table_Example_CSharp.htm"
---

# Insert General Tolerance Table Example (C#)

This example shows how to create a general tolerance table annotation.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part.
  // 2. Ensure that the specified table template exists.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Creates a general tolerance table annotation.
  // 2. Inspect the Immediate window, the graphics area, and the Tables folder
 //    of the FeatureManager design tree.
  //----------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using System.Diagnostics;

 namespace InsertTable_CSharp
 {
     public partial class SolidWorksMacro
     {
         public void Main()
         {

             ModelDoc2 Part = default(ModelDoc2);
             GeneralToleranceTableAnnotation gttAnno = default(GeneralToleranceTableAnnotation);
             GeneralToleranceTableFeature gttFeat = default(GeneralToleranceTableFeature);
             Feature feat = default(Feature);
             ModelDocExtension mde = default(ModelDocExtension);
             bool boolstatus = false;

             Part = (ModelDoc2)swApp.ActiveDoc;
             mde = Part.Extension;
             gttAnno = mde.InsertGeneralToleranceTableAnnotation("c:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\bom-standard.sldbomtbt", 481, 163);
             gttFeat = gttAnno.GeneralToleranceTableFeature;
             feat = gttFeat.GetFeature();
             Debug.Print("Created " + feat.Name);
             boolstatus = Part.EditRebuild3();
         }

         // The SldWorks swApp variable is pre-assigned for you.
         public SldWorks swApp;

     }
 }
```
