---
title: "Create New Part from Existing Part Using Temporary Body Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_New_Part_from_Existing_Part_Using_Temporary_Body_Example_CSharp.htm"
---

# Create New Part from Existing Part Using Temporary Body Example (C#)

This example shows how to delete faces from a temporary body and how
to create a new part using that temporary body.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\toolbox\braceright.sldprt.
// 2. Verify that the specified part template exists..
//
// Postconditions:
// 1. Creates a new part; the new part has same body as original part
//    but with selected faces deleted.
// 2. Close the new part without saving it.
// 3. Close braceright.sldprt without saving it.
//----------------------------------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace DeleteFaces5Body2_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public object GetFacesWithAttribute(SldWorks swApp, Body2 swBody, AttributeDef swAttDef)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Face2 swFace = default(Face2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Entity swEnt = default(Entity);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidWorks.Interop.sldworks.Attribute swAttCopy = default(SolidWorks.Interop.sldworks.Attribute);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Search for faces on temporary body based on copied attributes
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Face2[] swFaceArr = new Face2[1];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFace = (Face2)swBody.GetFirstFace();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}while ((null != swFace))
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swEnt = (Entity)swFace;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swAttCopy = null;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}// Only one instance of attribute on a face should exist
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swAttCopy = (SolidWorks.Interop.sldworks.Attribute)swEnt.FindAttribute(swAttDef, 0);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if ((swAttCopy != null))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}swFaceArr[swFaceArr.GetUpperBound(0)] = swFace;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Array.Resize(ref swFaceArr, swFaceArr.GetUpperBound(0) + 2);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swFace = (Face2)swFace.GetNextFace();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Array.Resize(ref swFaceArr, swFaceArr.GetUpperBound(0));
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return swFaceArr;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}const int CreateVisible = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}const string sAttDefName = "temp_attrib";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}const string sAttRootName = "root_attrib";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttributeDef swAttDef = default(AttributeDef);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}PartDoc swPart = default(PartDoc);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Body2 swBody = default(Body2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Body2 swCopyBody = default(Body2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}long nSelCount = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Face2 swFace = default(Face2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Entity swEnt = default(Entity);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidWorks.Interop.sldworks.Attribute[] swAtt = new SolidWorks.Interop.sldworks.Attribute[6];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] vFaceArr = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}PartDoc swNewPart = default(PartDoc);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swNewModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Feature swFeat = default(Feature);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] vBodies = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int i = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool bLocChk = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool bRet = false;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAttDef = (AttributeDef)swApp.DefineAttribute(sAttDefName);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart = (PartDoc)swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bRet = swAttDef.Register();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Debug.Assert(bRet);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.02203398034251, 0.2107859236428, 0.005471558832284, true, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.03651723484872, 0.1911276369938, 0.007226351471076, true, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.01524, 0.1384548315647, 0.004444480215071, true, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1306826750488, 0.0172129316129, 0.006448917397336, true, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1068570742154, 0.01524000000001, 0.00670683128584, true, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.01652926606039, 0.01775444632528, 0.004157527166058, true, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Add attribute to selected faces
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}nSelCount = swSelMgr.GetSelectedObjectCount2(-1);
kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = 1; i <= nSelCount; i++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swFace = (Face2)swSelMgr.GetSelectedObject6(i, -1);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swEnt = (Entity)swFace;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swAtt[i - 1] = swAttDef.CreateInstance5(swModel, swEnt, sAttRootName + i, CreateVisible, (int)swInConfigurationOpts_e.swAllConfiguration);
kadov_tag{{<spaces>}}             kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Object varBodies;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vBodies = (Object[])swPart.GetBodies2((int)swBodyType_e.swAllBodies, true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}varBodies = vBodies;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swBody = (Body2)vBodies[0];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swCopyBody = (Body2)swBody.Copy();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Remove attribute from faces
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = 1; i <= nSelCount; i++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}bRet = swAtt[i - 1].Delete(true);
kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}vFaceArr = (Object[])GetFacesWithAttribute(swApp, swCopyBody, swAttDef);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Object varFaceArr = vFaceArr;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bRet = swCopyBody.DeleteFaces5(varFaceArr, (int)swHealActionType_e.swHealAction_Shrink, (int)swLoopProcessOption_e.swLoopProcess_Auto, true, out varBodies, out bLocChk);
kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swNewPart = (PartDoc)swApp.NewDocument("C:\\Documents and Settings\\All Users\\Application Data\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\part.prtdot", 0, 0, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swNewModel = (ModelDoc2)swNewPart;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeat = (Feature)swNewPart.CreateFeatureFromBody3(swCopyBody, false, (int)swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
