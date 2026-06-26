---
title: "Insert Thin Cut Extrude Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Thin_Cut_Extrude_Example_CSharp.htm"
---

# Insert Thin Cut Extrude Example (C#)

This example shows how to insert a thin cut extrude feature.

```
//------------------------------------------------------
// Preconditions: Verify that the specified part exists.
//
// Postconditions:
// 1. Opens the part.
// 2. Inserts a thin cut extrude feature in the part.
// 3. Examine the FeatureManager design tree and
//    graphics area.
//
// NOTE: Because this part document is used elsewhere,
// do not save changes.
//-----------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;

namespace FeatureCutThin2FeatureManagerCSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial
 class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public
 void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SketchManager swSketchManager = default(SketchManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SketchSegment swSketchSegment = default(SketchSegment);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}FeatureManager swFeatureManager = default(FeatureManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Feature swFeature = default(Feature);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errorstatus = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int warnings = 0;
```

```vb
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Open part
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\water.sldprt", 1, 0, "",
 ref errorstatus, ref warnings);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Select face on which to sketch a circle
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = (ModelDocExtension)swModel.Extension;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.0001655362220845, -0.0477671348753, 0.072, false, 0, null, 0)

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ShowNamedView2("*Normal To", (int)swStandardViews_e.swBackView);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Sketch a circle
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchManager = (SketchManager)swModel.SketchManager;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(0.0, 0.0, 0.0, 0.030255, -0.042492, 0.0);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Create the thin cut extrude
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeatureManager = (FeatureManager)swModel.FeatureManager;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeature = (Feature)swFeatureManager.FeatureCutThin2(true, false, false, (int)swEndConditions_e.swEndCondBlind,
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}(int)swEndConditions_e.swEndCondBlind, 0.01, 0.01, false, false, false,
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}false, 0.01745329251994, 0.01745329251994, false, false, false, false, 0.01, 0.01, 0.01,
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}0, 0, false, 0.005, true, true, (int)swStartConditions_e.swStartSketchPlane, 0, false);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ShowNamedView2("*Isometric", (int)swStandardViews_e.swIsometricView);

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
 }
```
