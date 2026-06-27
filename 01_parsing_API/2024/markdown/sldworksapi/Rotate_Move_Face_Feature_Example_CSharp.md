---
title: "Rotate Move Face Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Move_Face_Feature_Example_CSharp.htm"
---

# Rotate Move Face Feature Example (C#)

This example shows how to rotate (draft) a Move Face feature by changing
the XYZ origin and rotation angles.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part document that kadov_tag{{</spaces>}}contains a Move Face feature kadov_tag{{</spaces>}}named Move Face1.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Rotates (drafts) the Move Face feature.
 // 2. Examine the Immediate window.
 //----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace RotateMoveFaceFeature_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Feature swFeat = default(Feature);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MoveFaceFeatureData swMoveFaceFeatData = default(MoveFaceFeatureData);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double[] varPara = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double[] newPara = new double[6];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double[] newVarPara = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double PI = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}long i = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set PI
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}PI = 4 * System.Math.Atan(1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Select, get, and access Move Face feature
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Move Face1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swMoveFaceFeatData = (MoveFaceFeatureData)swFeat.GetDefinition();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swMoveFaceFeatData.AccessSelections(swModel, null);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get current XYZ origin and rotation angles of Move Face feature
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Before rotating Move Face feature...");
             // 1 radian = 180º/p = 57.295779513º or approximately 57.3º
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" Draft angle of Move Face feature: " + swMoveFaceFeatData.Angle * 57.3 + " degrees");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" XYZ origin (first 3) and rotation angles (last 3)");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}varPara = (double[])swMoveFaceFeatData.TriadRotationParameters;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = varPara.GetLowerBound(0); i <= varPara.GetUpperBound(0); i++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" " + (varPara[i]));
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// New XYZ location and rotation angle values
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}newPara[0] = 0.0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}newPara[1] = 0.0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}newPara[2] = 0.0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}newPara[3] = 2 * PI / 180;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Convert radians to degrees
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}newPara[4] = 2 * PI / 180;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Convert radians to degrees
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}newPara[5] = 0.0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}newVarPara = newPara;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Rotate the Move Face feature
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swMoveFaceFeatData.TriadRotationParameters = newVarPara;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" ");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("After rotating Move Face feature...");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" Draft angle of Move Face feature: " + swMoveFaceFeatData.Angle * 57.3 + " degrees");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" XYZ origin (first 3) and rotation angles (last 3)");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}newVarPara = (double[])swMoveFaceFeatData.TriadRotationParameters;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = newVarPara.GetLowerBound(0); i <= newVarPara.GetUpperBound(0); i++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" " + (newVarPara[i]));
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Modify the Move Face feature
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeat.ModifyDefinition(swMoveFaceFeatData, swModel, null);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
