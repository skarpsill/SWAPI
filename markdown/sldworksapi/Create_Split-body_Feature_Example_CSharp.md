---
title: "Create Split Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Split-body_Feature_Example_CSharp.htm"
---

# Create Split Feature Example (C#)

This example shows how to create a Split feature.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open a part document that contains a body that is bisected by the
//    Top Plane.
// 2. Verify that c:\temp exists.
// 3. Open an Immediate window.
//
// Postconditions:
// 1. Creates Split1.
// 2. Saves a split body to c:\temp\Body1.sldprt.
// 3. Inspect the Immediate window, FeatureManager design tree, graphics area,
//    and c:\temp.
//---------------------------------------------------------------------------
using Microsoft.VisualBasic;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;

namespace CreateSplitBody2_CSharp.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 swModel;
        SelectionMgr swSelMgr;
        ModelDocExtension swModelDocExt;
        Feature swFeat;
        FeatureManager swFeatMgr;
        SplitBodyFeatureData swSplitBodyFeat;

        bool boolstatus;

        public void Main()
        {
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swFeatMgr = swModel.FeatureManager;

            //Select the cutting tool
            boolstatus = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, true, 0, null, 0);

            object vBodyNames = null;
            object[] bodiesToMark = new Body2[2];
            string[] bodyNames = new string[2];
            object[] bodyOrigins = new Vertex[2];

            //Get bodies that will result from the split operation
            object[] vResultingBodies = null;
            vResultingBodies = (object[])swFeatMgr.PreSplitBody2();

            swModel.ClearSelection2(true);

            //Set up the arrays for the post-split operation

            //If you do not want to assign body origin, set it to nothing so that the default origin is used
            bodyOrigins[0] = null;
            bodyOrigins[1] = null;

            bodiesToMark[0] = vResultingBodies[0];
            bodiesToMark[1] = vResultingBodies[1];

            //Save the first body to a separate part document
            //Substitute the name of the actual folder where to save the body
            bodyNames[0] = "c:\\temp\\Body1.sldprt";
            //Do not save the second body
            bodyNames[1] = "";

            DispatchWrapper[] preSplitBodies = null;
            preSplitBodies = (DispatchWrapper[])ObjectArrayToDispatchWrapperArray((bodiesToMark));
            vBodyNames = bodyNames;
            DispatchWrapper[] originsToUse = null;
            originsToUse = (DispatchWrapper[])ObjectArrayToDispatchWrapperArray((bodyOrigins));

            //Create the Split feature, consuming all split bodies
            swFeat = swFeatMgr.PostSplitBody2((preSplitBodies), true, (originsToUse), (vBodyNames), "");

            if (((swFeat != null)))
            {
                Debug.Print("Split feature: " + swFeat.Name);
                swSplitBodyFeat = (SplitBodyFeatureData)swFeat.GetDefinition();
                Debug.Print("Bodies consumed? " + swSplitBodyFeat.Consume);
                Debug.Print(" ");
            }
        }

        public DispatchWrapper[] ObjectArrayToDispatchWrapperArray(object[] Objects)
        {
            int ArraySize = 0;
            ArraySize = Objects.GetUpperBound(0);
            DispatchWrapper[] d = new DispatchWrapper[ArraySize + 1];
            int ArrayIndex = 0;
            for (ArrayIndex = 0; ArrayIndex <= ArraySize; ArrayIndex++)
            {
                d[ArrayIndex] = new DispatchWrapper(Objects[ArrayIndex]);
            }
            return d;
        }

        public SldWorks swApp;
    }
}
```
