---
title: "Modify Move/Copy Body Using Vertex Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_and_Copy_Body_Using_Vertex_Example_CSharp.htm"
---

# Modify Move/Copy Body Using Vertex Example (C#)

This example shows how to modify a move/copy body feature using a vertex.

```
//---------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Selects a solid body and two vertices.
// 3. Inserts a move/copy body feature and gets and sets some of its feature data.
// 4. Examine the FeatureManager design tree, the graphics area, and
//    the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//---------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace MoveCopyBodyFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureManager = default(FeatureManager);
            Feature swFeature = default(Feature);
            MoveCopyBodyFeatureData swMoveCopyBodyFeatureData = default(MoveCopyBodyFeatureData);
            Vertex swVertexFrom = default(Vertex);
            Vertex swVertexTo = default(Vertex);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            //Open part document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_inter.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swFeatureManager = (FeatureManager)swModel.FeatureManager;

            //Select solid body and vertices for move/copy body feature
            status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, 0, 0.065, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, -0.09, 0.065, true, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Extrude-Thin1", "SOLIDBODY", 0, 0, 0, false, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, 0, 0.065, true, 4, null, 0);
            status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, -0.09, 0.065, true, 8, null, 0);

            //Insert move/copy body feature
            swFeature = (Feature)swFeatureManager.InsertMoveCopyBody2(0, 0, 0, 0, -0.085, 0, 0.065, 0, 0, 0,
            true, 1);

            //Roll forward the feature and get and set move/copy body feature data
            swMoveCopyBodyFeatureData = (MoveCopyBodyFeatureData)swFeature.GetDefinition();
            status = swMoveCopyBodyFeatureData.AccessSelections(swModel, null);
            Debug.Print("Move/copy body feature data:");
            Debug.Print("  Number of bodies to move or rotate and copy: " + swMoveCopyBodyFeatureData.GetBodiesCount());
            Debug.Print("  Number of copies: " + swMoveCopyBodyFeatureData.NumberOfCopies);
            Debug.Print("  Transform type (0 = None, 1 = Translation, 2 = Rotation): " + swMoveCopyBodyFeatureData.TransformType);

            //Change translation vertex
            status = swModelDocExt.SelectByID2("", "VERTEX", -0.085, -0.09, 0.065, true, 8, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swVertexFrom = (Vertex)swSelectionMgr.GetSelectedObject6(1, -1);
            swMoveCopyBodyFeatureData.TransformReferenceEntity = swVertexFrom;
            swMoveCopyBodyFeatureData.TranslateToVertex = swVertexFrom;
            status = swModelDocExt.SelectByID2("", "VERTEX", 0, -0.065, 0, false, 0, null, 0);
            swVertexTo = (Vertex)swSelectionMgr.GetSelectedObject6(1, -1);
            swMoveCopyBodyFeatureData.TranslateToVertex = swVertexTo;
            swMoveCopyBodyFeatureData.TransformX = 0.05;

            //Apply the changes and roll back the feature
            swFeature.ModifyDefinition(swMoveCopyBodyFeatureData, swModel, null);

            swModel.ViewZoomtofit2();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
