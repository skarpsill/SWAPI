---
title: "Create a Thread Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_a_Thread_Feature_Example_CSharp.htm"
---

# Create a Thread Feature Example (C#)

This example shows how to create and edit a thread feature.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open:
 //    public_documents\samples\tutorial\api\holecube.sldprt
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates Thread1.
 // 2. Modifies the start angle and overrides the pitch of Thread1.
 // 3. Inspect the Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;

 namespace ThreadFeature_CSharp
 {
     public partial class SolidWorksMacro
     {
         public void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);
             Feature swFeat = default(Feature);
             FeatureManager FeatMgr = default(FeatureManager);
             ThreadFeatureData swThreadFeatData = default(ThreadFeatureData);
             Edge pEdge = default(Edge);

             bool boolstatus = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             FeatMgr = swModel.FeatureManager;

            //Create and initialize a thread feature data object
             swThreadFeatData = (ThreadFeatureData)FeatMgr.CreateDefinition((int)swFeatureNameID_e.swFmSweepThread);
             swThreadFeatData.InitializeThreadData();

            //Specify the thread method type as extrude
             swThreadFeatData.ThreadMethod = 1;

            //Specify the up-to-selection end conditon
             swThreadFeatData.EndCondition = (int)swThreadEndCondition_e.swThreadEndCondition_UpToSelection;

            //Select the thread's starting edge
             boolstatus = swModel.Extension.SelectByRay(0.011047195612548, -0.0190800402080527, -0.000365739009737354, 0.164466301431523, -0.479983539625146, -0.861723063044243, 0.00160036844432164, 1, false, 1,
             0);
             pEdge = (Edge)((SelectionMgr)(swModel.SelectionManager)).GetSelectedObject6(1, -1);
             swThreadFeatData.Edge = pEdge;
             swModel.ClearSelection2(true);

            //Select the thread's up-to reference
             boolstatus = swModel.Extension.SelectByRay(0.00850469161018452, -0.0212858011305457, -0.0254798703094821, 0.164466301431523, -0.479983539625146, -0.861723063044243, 0.00160036844432164, 1, true, 1,
             0);
             pEdge = (Edge)((SelectionMgr)(swModel.SelectionManager)).GetSelectedObject6(1, -1);
             swThreadFeatData.SetEndConditionReference(pEdge);
             swModel.ClearSelection2(true);

            //Create the thread feature
             swFeat = FeatMgr.CreateFeature(swThreadFeatData);
             Debug.Print("File = " + swModel.GetPathName());

            //Access the thread feature data and print its properties
             swThreadFeatData = (ThreadFeatureData)swFeat.GetDefinition();

             swThreadFeatData.AccessSelections((ModelDoc)swModel, null);
             Debug.Print("Offset the starting location of the helix? " + swThreadFeatData.Offset);
             Debug.Print("Reverse direction of offset? " + swThreadFeatData.ReverseOffset);
             Debug.Print("Offset distance: " + swThreadFeatData.OffsetDistance);
             Debug.Print("Thread starting angle: " + swThreadFeatData.ThreadStartAngle);
             Debug.Print("End condition as defined in swThreadEndCondition_e: " + swThreadFeatData.EndCondition);
             Debug.Print("End condition offset: " + swThreadFeatData.EndConditionOffset);
             Debug.Print("Reverse end condition offset? " + swThreadFeatData.EndConditionOffsetReverse);
             Debug.Print("End condition offset distance: " + swThreadFeatData.EndConditionOffsetDistance);
             Debug.Print("Keep thread length constant? " + swThreadFeatData.MaintainThreadLength);
             Debug.Print("Thread profile type: " + swThreadFeatData.Type);
             Debug.Print("Size: " + swThreadFeatData.Size);
             Debug.Print("Diameter overridden? " + swThreadFeatData.DiameterOverride);
             Debug.Print("Diameter: " + swThreadFeatData.Diameter);
             Debug.Print("Pitch overridden? " + swThreadFeatData.PitchOverride);
             Debug.Print("Pitch: " + swThreadFeatData.Pitch);
             Debug.Print("Thread method as defined in swThreadMethod_e: " + swThreadFeatData.ThreadMethod);
             Debug.Print("Flip the profile of the helix about an axis? " + swThreadFeatData.MirrorProfile);
             Debug.Print("How to flip the profile of the helix as defined in swThreadMirrorType_e: " + swThreadFeatData.MirrorType);
             Debug.Print("Helix rotation angle: " + swThreadFeatData.RotationAngle);
             Debug.Print("Thread wind direction (true = clockwise, false = counterclockwise): " + swThreadFeatData.RightHanded);
             Debug.Print("Multiple thread starts? " + swThreadFeatData.MultipleStart);
             if (swThreadFeatData.MultipleStart == true)
             {
                 Debug.Print("  Number of starts? " + swThreadFeatData.NumberOfStarts);
             }
             Debug.Print("Trim with the end face? " + swThreadFeatData.TrimEndFace);
             Debug.Print("Trim with the start face? " + swThreadFeatData.TrimStartFace);

            //Change the thread start angle and pitch
             swThreadFeatData.ThreadStartAngle = 0.04;
            swThreadFeatData.PitchOverride = true;
            swThreadFeatData.Pitch = 0.01
            //Modify the feature definition
             swFeat.ModifyDefinition(swThreadFeatData, swModel, null);
         }

         // The SldWorks swApp variable is pre-assigned for you.
         public SldWorks swApp;

     }
 }
```
