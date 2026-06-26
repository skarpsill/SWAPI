---
title: "Insert and Change DeleteFace Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Change_DeleteFace_Feature_Example_CSharp.htm"
---

# Insert and Change DeleteFace Feature Example (C#)

This example shows how to insert a DeleteFace feature and how to modify that feature.

```vb
// ---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\fillets\knob.sldprt.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Creates and modifies a DeleteFace feature.
 // 2. Examine the Immediate window.
 //
 // NOTE: Because this part document is used elsewhere, kadov_tag{{</spaces>}}do not save changes.
 // ---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace DeleteFaceFeatureDataCSharp.csproj
 {
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Feature swFeature = default(Feature);
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}DeleteFaceFeatureData swDeleteFaceFeature = default(DeleteFaceFeatureData);
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string featureName = null;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int opt = 0;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = (ModelDocExtension)swModel.Extension;

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Select a face for the
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// DeleteFace feature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModel.Extension.SelectByID2("", "FACE", 0.002251015125069, -0.001872569429423, 0.02015405789763, false, 0, null, 0);
    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Create a DeleteFace feature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.InsertDeleteFace((int)swFaceDeleteOption_e.swFaceDelete_Default); kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Get the DeleteFace feature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeature = (Feature)swModel.FirstFeature();
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}while ((swFeature != null)) {
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}featureName = swFeature.Name; kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}while (featureName != "DeleteFace1") {
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swFeature = (Feature)swFeature.GetNextFeature();
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}featureName = swFeature.Name;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Feature name: " + featureName);
             kadov_tag{{</spaces>}}swDeleteFaceFeature = (DeleteFaceFeatureData)swFeature.GetDefinition();
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swDeleteFaceFeature.AccessSelections(swModel, null);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" Number of deleted faces: " + swDeleteFaceFeature.GetDeletedFacesCount());
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the DeleteFace feature's option
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}opt = swDeleteFaceFeature.Options;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" Before changing the option...");
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DeleteFaceOptions(opt);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Change the DeleteFace feature's option
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDeleteFaceFeature.Options = (int)swFaceDeleteOption_e.swFaceDelete_Patch;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}opt = swDeleteFaceFeature.Options;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" After changing the option...");
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DeleteFaceOptions(opt);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Save modification made to DeleteFace feature
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swFeature.ModifyDefinition(swDeleteFaceFeature, swModel, null);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get next feature until no more features
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeature = (Feature)swFeature.GetNextFeature();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}} kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public void DeleteFaceOptions(long options)
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}switch (options) {
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case 0:
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Option = swFaceDelete_Default");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case 1:
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Option = swFaceDelete_Patch");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case 2:
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Option = swFaceDelete_Fill");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}case 3:
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Option = swFaceDelete_FillWithTangent");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}break;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>kadov_tag{{<spaces>}}
         kadov_tag{{</spaces>}}/// kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
