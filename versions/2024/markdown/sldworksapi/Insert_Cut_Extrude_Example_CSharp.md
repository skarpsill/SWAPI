---
title: "Insert Cut Extrude Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cut_Extrude_Example_CSharp.htm"
---

# Insert Cut Extrude Example (C#)

This example shows how to insert a cut extrude feature.

```vb
//----------------------------------------------------------
 // Preconditions: Verify that specified part to open exists.
 //
 // Postconditions:
 // 1. Inserts a cut extrude feature is in the model.
 // 2. Examine the graphics area.
 //
 // NOTE: Because the part document is used elsewhere, do not save
 // changes.
 //----------------------------------------------
using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
namespace FeatureCut3FeatureManagerCSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SketchManager swSketchManager = default(SketchManager);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SketchSegment swSketchSegment = default(SketchSegment);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}FeatureManager swFeatureManager = default(FeatureManager);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Feature swFeature = default(Feature);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int fileerror = 0;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int filewarning = 0;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Open part document
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\plate.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref fileerror, ref filewarning);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = (ModelDocExtension)swModel.Extension;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Select the face where to sketch a circle
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.02031412853728, 0.006977746007294, -0.008053400767039, false, 0, null, 0);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchManager = (SketchManager)swModel.SketchManager;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchManager.InsertSketch(true);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Sketch a circle
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(0.0, 0.0, 0.0, 0.01708, -0.030458, 0.0);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Insert a cut-extrude feature using the circle
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeatureManager = (FeatureManager)swModel.FeatureManager;
 swFeature = (Feature)swFeatureManager.FeatureCut3(true, false, false, (int)swEndConditions_e.swEndCondThroughAll,
 kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}(int)swEndConditions_e.swEndCondBlind, 0.01, 0.01, false, false, false,
 kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}false, 0.01745329251994, 0.01745329251994, false, false, false, false, false, true, true,
 kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}false, false, false, (int)swStartConditions_e.swStartSketchPlane, 0, false);
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
