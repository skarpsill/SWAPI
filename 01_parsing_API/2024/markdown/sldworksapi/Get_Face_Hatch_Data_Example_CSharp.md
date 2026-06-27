---
title: "Get Face Hatch Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Face_Hatch_Data_Example_CSharp.htm"
---

# Get Face Hatch Data Example (C#)

This example shows how to get the number of face hatches in a standard
or derived (detail, section, projected, broken, etc.) drawing view and
their data.

```vb
//------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\introsw\bolt-assembly.slddrw.
 // 2. Select Section View A-A in the FeatureManager design tree.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Gets face hatch data.
 // 2. Examine the Immediate window.
 //--------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace UseMaterialHatchFaceHatchCSharp.csproj
 {
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}View swView = default(View);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] vFaceHatch = null;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}FaceHatch swFaceHatch = default(FaceHatch);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int i = 0;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swView = (View)swSelMgr.GetSelectedObject6(1, -1);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("View = " + swView.Name);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" Type = " + swView.Type);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vFaceHatch = (object[])swView.GetFaceHatches();
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((vFaceHatch == null))
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" No face hatches in selected view.");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" Number of face hatches in this view = " + (vFaceHatch.Length));
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((vFaceHatch != null))
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" Face hatches =");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}for (i = 0; i <= vFaceHatch.Length - 1; i++)
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}swFaceHatch = (FaceHatch)vFaceHatch[i];
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}// Get face hatch data
                     // 1 radian = 180º/p = 57.295779513º or approximately 57.3º
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Angle kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}= " + swFaceHatch.Angle * 57.3 + " degrees");
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Color kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}= " + swFaceHatch.Color);
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Definition kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}= " + swFaceHatch.Definition);
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Layer kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}= " + swFaceHatch.Layer);
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Pattern kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}= " + swFaceHatch.Pattern);
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Scale kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}= " + swFaceHatch.Scale2);
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}SolidFill kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}= " + swFaceHatch.SolidFill);
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Material crosshatch = " + swFaceHatch.UseMaterialHatch);
 kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}-----------------------");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
 }
```
