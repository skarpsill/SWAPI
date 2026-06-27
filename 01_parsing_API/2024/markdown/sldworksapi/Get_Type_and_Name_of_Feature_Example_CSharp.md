---
title: "Get Feature Type and Name Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Type_and_Name_of_Feature_Example_CSharp.htm"
---

# Get Feature Type and Name Example (C#)

This example shows how to get the feature type and name of the selected feature for use with IModelDocExtension::SelectByID2.

```vb
//-------------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\floxpress\ball valve\ball_valve.sldasm.
 // 2. Expand any component in the FeatureManager design tree
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}and select one of its features.
 //
// Postconditions:
 // 1. Gets the selected feature's type and name.
 // 2. Examine the Immediate window.
 //
 // NOTE: Because this assembly document is used elsewhere, do not save changes.
 //-------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace GetNameForSelectionFeatureCSharp.csproj
 {
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Feature swFeat = default(Feature);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string featName = null;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string featType = null;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = (ModelDocExtension)swModel.Extension;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the selected feature
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get the feature's type and name
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}featName = swFeat.GetNameForSelection(out featType);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt.SelectByID2(featName, featType, 0, 0, 0, true, 0, null, 0);

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Print the feature's type and name
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// to the Immediate window
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Feature type: " + featType);
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Feature name: " + featName);
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
 }
```
