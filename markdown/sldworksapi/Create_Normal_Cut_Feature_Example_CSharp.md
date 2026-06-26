---
title: "Create Normal Cut Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Normal_Cut_Feature_Example_CSharp.htm"
---

# Create Normal Cut Feature Example (C#)

This example shows how to create a normal cut feature.

```vb
  //------------------------------------------------------------------------------
 // Preconditions:
 // 1. Open:
 //    c:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\whatsnew\sheet metal\normal_cut.sldprt.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Creates Normal Cut1 in the FeatureManager design tree.
  // 2. Edits the feature by specifying a normal cut direction entity.
 // 3. Inspect the Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save any changes to it.
  //------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace CreateNormalCut_CSharp
 {
     partial class SolidWorksMacro
     {

         private ModelDoc2 swModel;
         private ModelDocExtension swModelDocExt;
         private FeatureManager swFeatMgr;
         private Feature swFeat;
         private SMNormalCutFeatureData2 swNormalCutFeatData;
         private SMNormalCutGroupData grpData;
         private SelectionMgr swSelMgr;
         private Face2 swCutDirectionFace;
         private int errCode;
         private bool boolstatus;
         private object[] varGrpNames;
         private int i;
         private int j;
         private string Name;
         private Face2 Face;

         public void Main()
         {

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;
             swFeatMgr = swModel.FeatureManager;
             swNormalCutFeatData = (SMNormalCutFeatureData2)swFeatMgr.CreateDefinition((int)swFeatureNameID_e.swFmNormalCut);
             swNormalCutFeatData.AutoPropagation = true;
             swNormalCutFeatData.OptimizeGeometry = true;
             swNormalCutFeatData.NormalCutParameters = (int)swNormalCutParameters_e.swNormalCutExtent;

             // Select the face(s) to make normal

             boolstatus = swModel.Extension.SelectByRay(0.0471296104838217, 0.0142054003862171, -0.00668923799798904, -0.13322686545804, 0.182153484913837, 0.974202602261958, 0.000619874904830013, 2, true, 1, 0);

             grpData = (SMNormalCutGroupData)swNormalCutFeatData.CreateGroup(out errCode);

             // Create the normal cut feature

             swFeat = swFeatMgr.CreateFeature(swNormalCutFeatData);

             // Modify the normal cut feature

             swNormalCutFeatData = (SMNormalCutFeatureData2)swFeat.GetDefinition();
             swNormalCutFeatData.AccessSelections(swModel, null);
             varGrpNames = (object[])swNormalCutFeatData.GetGroupNames();

             for (i = 0; i <= varGrpNames.GetUpperBound(0); i++)
             {
                 Name = (string)varGrpNames[i];
                 Debug.Print("GroupName: " + Name);
                 grpData = (SMNormalCutGroupData)swNormalCutFeatData.GetGroupByName(Name);
                 object[] varFaces = (object[])grpData.Faces;
                 for (j = 0; j <= varFaces.GetUpperBound(0); j++)
                 {
                     Face = (Face2)varFaces[j];
                     Debug.Print("Face " + j + " area: " + Face.GetArea());
                 }
                 Debug.Print("--------------------");
             }

             //Specify the cut direction

             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             boolstatus = swModel.Extension.SelectByRay(-0.149999999999892, 0.0258556514245498, -0.00463505465353364, 0.393242668518252, 0.12460738379391, -0.910951811876282, 0.00122626958447854, 2, false, 0, 0);
             swCutDirectionFace = null;
             swCutDirectionFace = (Face2)swSelMgr.GetSelectedObject6(1, -1);

             Entity swSelectEnt = (Entity)swCutDirectionFace;
             boolstatus = swSelectEnt.Select4(false, null);
             swNormalCutFeatData.CutDirection = swCutDirectionFace;

             bool isModified = swFeat.ModifyDefinition(swNormalCutFeatData, swModel, null);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```
