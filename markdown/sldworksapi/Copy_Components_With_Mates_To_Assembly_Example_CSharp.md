---
title: "Copy Components With Mates to Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_Components_With_Mates_To_Assembly_Example_CSharp.htm"
---

# Copy Components With Mates to Assembly Example (C#)

This example shows how to copy components with mates in an assembly.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\driveworksxpress\mobile gantry.SLDASM.
 // 2. Inspect Leg<1> and Leg<2> in the assembly.
 //
 // Postconditions:
 // 1. Replaces Leg<1> with a copy of Leg<2>.
 // 2. Inspect Leg<2> and leg<3> in the assembly.
 //
 // NOTE: Because this assembly is used elsewhere, do not save any changes.
 //---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using System.Runtime.InteropServices;
namespace CopyComponentsWithMatesToAssembly_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool[] blRepeat = new bool[3];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool[] blFlip = new bool[3];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object SelectedComps = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object RepeatOptions = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] MateRefs = new object[3];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object InpValues = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object FlipValues = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AssemblyDoc swAssy = default(AssemblyDoc);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Component2 swItem = default(Component2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Feature swFeature = default(Feature);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}RefPlane refPlane = default(RefPlane);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] arrMateEntities = new object[3];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] arrCompsToCopy = new object[1];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}double[] dValues = new double[3];

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssy = (AssemblyDoc)swModel;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Leg-1@mobile gantry", "COMPONENT", 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.EditDelete();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Leg-2@mobile gantry", "COMPONENT", 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swItem = (Component2)swSelMgr.GetSelectedObject6(1, -1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}arrCompsToCopy[0] = swItem;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}arrMateEntities[0] = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}arrMateEntities[1] = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Left End@Universal Beam-1@mobile gantry", "PLANE", 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}refPlane = (RefPlane)swFeature.GetSpecificFeature2();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}arrMateEntities[2] = refPlane;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}blRepeat[0] = true;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}blRepeat[1] = true;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}blRepeat[2] = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectedComps = arrCompsToCopy;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}RepeatOptions = blRepeat;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MateRefs = arrMateEntities;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dValues[0] = 0.0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dValues[1] = 0.0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dValues[2] = 0.0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}InpValues = dValues;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}blFlip[0] = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}blFlip[1] = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}blFlip[2] = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}FlipValues = blFlip;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DispatchWrapper[] disparrCompsToCopy = new DispatchWrapper[1];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}disparrCompsToCopy[0] = new DispatchWrapper(arrCompsToCopy[0]);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DispatchWrapper[] dispMateRefs = new DispatchWrapper[3];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dispMateRefs[0] = new DispatchWrapper(MateRefs[0]);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dispMateRefs[1] = new DispatchWrapper(MateRefs[1]);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}dispMateRefs[2] = new DispatchWrapper(MateRefs[2]);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Repeat all mates except the coincident mate with "Right End@Universal Beam-1"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssy.CopyWithMates((disparrCompsToCopy), RepeatOptions, (dispMateRefs), InpValues, FlipValues);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssy.EditRebuild();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
