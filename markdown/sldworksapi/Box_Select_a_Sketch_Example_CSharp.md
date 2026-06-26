---
title: "Box Select a Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Box_Select_a_Sketch_Example_CSharp.htm"
---

# Box Select a Sketch Example (C#)

This example shows how to box select all of the entities in a sketch
block.

//----------------------------------------------------------------------------- // Preconditions: Open public_documents \samples\tutorial\blocks\piston_mechanism.sldblk . // // Postconditions: // 1. Opens and box selects Sketch1 . // 2. Examine the list of selected entities // in the PropertyManager page. // 3. Interactively quit editing the sketch without // saving any changes. // 4. Close the document. //--------------------------------------

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
namespace SketchBoxSelect_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Select the sketch and open it
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.EditSketch();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ViewZoomtofit2();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Box select the sketch
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SketchBoxSelect("-0.663893", "1.322001", "0.000000", "-0.395073", "0.698568", "0.000000");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
