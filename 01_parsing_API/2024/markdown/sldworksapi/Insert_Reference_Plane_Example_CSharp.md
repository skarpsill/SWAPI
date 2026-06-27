---
title: "Insert Reference Plane Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Reference_Plane_Example_CSharp.htm"
---

# Insert Reference Plane Example (C#)

This example shows how to create a constraint-based angle reference
plane.

```
//-----------------------------------------------------------
// 1. Verify that the specified part exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a constraint-based reference plane.
// 2. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not
// save changes.
//-----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
```

```vb
namespace InsertRefPlaneFeatureManagerCSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}FeatureManager swFeatureManager = default(FeatureManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Feature swFeature = default(Feature);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}RefPlane swRefPlane = default(RefPlane);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}RefPlaneFeatureData swRefPlaneFeatureData = default(RefPlaneFeatureData);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int fileerror = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int filewarning = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int planeType = 0;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\plate.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref fileerror, ref filewarning);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = (ModelDocExtension)swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeatureManager = (FeatureManager)swModel.FeatureManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Create a constraint-based reference plane
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.028424218552, 0.07057725774359, 0, true, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "EDGE", 0.05976462601598, 0.0718389621656, 0.0001242036435087, true, 1, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swRefPlane = (RefPlane)swFeatureManager.InsertRefPlane(16, 0.7853981633975, 4, 0, 0, 0);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get type of the just-created reference plane
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swRefPlaneFeatureData = (RefPlaneFeatureData)swFeature.GetDefinition();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}planeType = swRefPlaneFeatureData.Type2;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Type of reference plane using IRefPlaneFeatureData::Type2: ");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}switch (planeType)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 0:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Invalid");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 1:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Undefined");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 2:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Line Point");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 3:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Three Points");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 4:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Line Line");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 5:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Distance");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 6:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Parallel");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 7:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Angle");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 8:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Normal");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 9:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" On Surface");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 10:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Standard");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 11:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Constraint-based");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}planeType = swRefPlaneFeatureData.Type;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Type of reference plane using IRefPlaneFeatureData::Type: ");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}switch (planeType)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 0:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Invalid");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 1:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Undefined");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 2:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Line Point");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 3:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Three Points");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 4:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Line Line");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 5:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Distance");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 6:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Parallel");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 7:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Angle");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 8:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Normal");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 9:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" On Surface");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 10:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Standard");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}case 11:
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Debug.Print(" Constraint-based");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}break;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
