---
title: "Create Derived or Underived Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Derived_or_Underived_Sketch_Example_CSharp.htm"
---

# Create Derived or Underived Sketch Example (C#)

This example shows how to create a derived or underived sketch.

```vb
 //--------------------------------------------------------------
 // Preconditions:
 // 1. Open a part that contains at least one sketch.
 // 2. Select a sketch.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. If the selected sketch is not derived, then a
 //    derived sketch is created.
 //    - or -
 //    If the selected sketch is derived, then the
 //    sketch is changed to underived.
 // 2. Examine the FeatureManager design tree and Immediate
 //    window.
 //--------------------------------------------------------------
using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace DeriveSketch_CSharp.csproj
 {
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Feature swFeat = default(Feature);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Sketch swSketch = default(Sketch);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Interactively select a sketch
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketch = (Sketch)swFeat.GetSpecificFeature2();

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Is the selected sketch derived?
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Is the selected sketch derived? " + swSketch.IsDerived());
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// If the selected sketch is a derived sketch,
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// then create a derived sketch; else, underive the
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// selected sketch
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swSketch.IsDerived())
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swModel.UnderiveSketch();
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Selected sketch was derived; sketch is now underived.");
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swModel.DeriveSketch();
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Selected sketch was not derived; a derived sketch has been created.");
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ForceRebuild3(false);
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
 }
```
