---
title: "Autodimension All Sketches Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Autodimension_All_Sketches_Example_CSharp.htm"
---

# Autodimension All Sketches Example (C#)

This example shows how to autodimension all under-constrained sketches in a part.

```
//------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Inserts two sketches.
// 3. Autodimensions the sketches.
// 4. Examine the Immediate window.
//-----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace AutoDimension2AllCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        const string swTnProfileFeature = "ProfileFeature";
        const double nTolerance = 1E-08;

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            PartDoc swPart = default(PartDoc);
            object[] sketchLines = null;
            string[] sSketchNameArr = null;
            string sSketchName = null;
            Feature swFeat = default(Feature);
            Sketch swSketch = default(Sketch);
            SketchSegment sketchSegment = default(SketchSegment);
            SketchManager swSketchMgr = default(SketchManager);
            int nRetVal = 0;
            bool bRet = false;

            // Create new part document and insert sketches
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2015\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            bRet = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            bRet = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            sketchLines = (object[])swSketchMgr.CreateCornerRectangle(0, 0, 0, 0.0711560575730914, -0.0480714437538268, 0);
            swModel.ClearSelection2(true);
            bRet = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            bRet = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
            sketchLines = (object[])swSketchMgr.CreateCornerRectangle(-0.100496797175254, 0.0481170506199078, 0, -0.0506046179404507, 0.0100165849869995, 0);
            swModel.ClearSelection2(true);
            sketchSegment = (SketchSegment)swSketchMgr.CreateCircle(-0.06189, -0.041869, 0.0, -0.066641, -0.077213, 0.0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);
            sketchSegment = (SketchSegment)swSketchMgr.CreateCircle(-0.032637, 0.106589, 0, -0.021539, 0.095387, 0);
            swModel.ClearSelection2(true);
            sketchSegment = (SketchSegment)swSketchMgr.CreateCircle(0, 0.083617, 0, 0.01255, 0.067729, 0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);
            swModel.ClearSelection2(true);

            // Find all under-constrained sketches
            swPart = (PartDoc)swModel;
            sSketchNameArr = new string[1];
            swFeat = (Feature)swPart.FirstFeature();
            while ((swFeat != null)) {
               if (swTnProfileFeature == swFeat.GetTypeName2()) {
                  swSketch = (Sketch)swFeat.GetSpecificFeature2();
                  if ((int)swConstrainedStatus_e.swUnderConstrained == swSketch.GetConstrainedStatus()) {
                     sSketchNameArr[sSketchNameArr.GetUpperBound(0)] = (string)swFeat.Name;
                     Array.Resize(ref sSketchNameArr, sSketchNameArr.GetUpperBound(0) + 2);
                  }
               }
               swFeat = (Feature)swFeat.GetNextFeature();
           }

           // Autodimension all under-constrained sketches
           Array.Resize(ref sSketchNameArr, sSketchNameArr.GetUpperBound(0));
           foreach (string sSketchName_loopVariable in sSketchNameArr)
           {
                sSketchName = sSketchName_loopVariable;
                swFeat = (Feature)swPart.FeatureByName(sSketchName);
                swSketch = (Sketch)swFeat.GetSpecificFeature2();
                nRetVal = AutoDimensionSketch(swApp, swModel, swSketch);
                Debug.Print(sSketchName + " autodimensioned (0 = success): " + nRetVal);
           }

        }

        public void FindAllUnderConstrainedSketches(SldWorks swApp, ModelDoc2 swModel, string[] sSketchNameArr)
        {
            PartDoc swPart = default(PartDoc);
            Feature swFeat = default(Feature);
            Sketch swSketch = default(Sketch);

            swPart = (PartDoc)swModel;
            swFeat = (Feature)swPart.FirstFeature();
            while ((swFeat != null))
            {
                if (swTnProfileFeature == swFeat.GetTypeName2())
                {
                    swSketch = (Sketch)swFeat.GetSpecificFeature2();
                    if ((int)swConstrainedStatus_e.swUnderConstrained == swSketch.GetConstrainedStatus())
                    {
                        sSketchNameArr[sSketchNameArr.GetUpperBound(0)] = (string)swFeat.Name;
                        Array.Resize(ref sSketchNameArr, sSketchNameArr.GetUpperBound(0) + 2);
                   }
                }
                swFeat = (Feature)swFeat.GetNextFeature();
            }
            // Remove last empty sketch name
            Array.Resize(ref sSketchNameArr, sSketchNameArr.GetUpperBound(0));
        }
        public object GetAllSketchLines(SldWorks swApp, ModelDoc2 swModel, Sketch swSketch)
        {
            object functionReturnValue = null;
            object[] vSketchSegArr = null;
            SketchSegment vSketchSeg = null;
            SketchSegment swSketchSeg = default(SketchSegment);
            SketchLine swSketchCurrLine = default(SketchLine);
            SketchLine[] swSketchLineArr = null;

            swSketchLineArr = new SketchLine[1];
            vSketchSegArr = (object[])swSketch.GetSketchSegments();
            if ((vSketchSegArr != null))
            {
                foreach (SketchSegment vSketchSeg_loopVariable in vSketchSegArr)
                {
                    vSketchSeg = (SketchSegment)vSketchSeg_loopVariable;
                    swSketchSeg = (SketchSegment)vSketchSeg;
                    if ((int)swSketchSegments_e.swSketchLINE == swSketchSeg.GetType())
                    {
                        swSketchCurrLine = (SketchLine)swSketchSeg;
                        swSketchLineArr[swSketchLineArr.GetUpperBound(0)] = (SketchLine)swSketchCurrLine;
                        Array.Resize(ref swSketchLineArr, swSketchLineArr.GetUpperBound(0) + 2);
                    }
                }
            }
            if (0 == swSketchLineArr.GetUpperBound(0))
            {
                // No straight lines in this sketch
                functionReturnValue = null;
                return functionReturnValue;
            }
            // Remove last empty sketch line
            Array.Resize(ref swSketchLineArr, swSketchLineArr.GetUpperBound(0));
            functionReturnValue = (object[])swSketchLineArr;
            return functionReturnValue;
        }

        public bool GetSketchPoint(SldWorks swApp, ModelDoc2 swModel, Sketch swSketch, SketchPoint swSketchPt)
        {
            bool functionReturnValue = false;
            object[] vSketchPtArr = null;

            vSketchPtArr = (object[])swSketch.GetSketchPoints2();
            if ((vSketchPtArr != null))
            {
                // Use first point
                swSketchPt = (SketchPoint)vSketchPtArr[0];
                functionReturnValue = true;
                return functionReturnValue;
            }
            functionReturnValue = false;
            return functionReturnValue;
        }

        public bool FindVerticalOrigin(SldWorks swApp, ModelDoc2 swModel, Sketch swSketch, SketchSegment swSketchSegVert, SketchPoint swSketchPtVert)
        {
            bool functionReturnValue = false;
            SketchLine[] vSketchLineArr = null;
            SketchLine vSketchLine = null;
            SketchLine swSketchCurrLine = default(SketchLine);
            SketchPoint swStartPt = default(SketchPoint);
            SketchPoint swEndPt = default(SketchPoint);

            // Try to get first vertical line
            vSketchLineArr = (SketchLine[])GetAllSketchLines(swApp, swModel, swSketch);
            if ((vSketchLineArr != null))
            {
                foreach (SketchLine vSketchLine_loopVariable in vSketchLineArr)
                {
                    vSketchLine = (SketchLine)vSketchLine_loopVariable;
                    swSketchCurrLine = (SketchLine)vSketchLine;
                    swStartPt = (SketchPoint)swSketchCurrLine.GetStartPoint2();
                    swEndPt = (SketchPoint)swSketchCurrLine.GetEndPoint2();
                    if (Math.Abs(swStartPt.X - swEndPt.X) < nTolerance)
                    {
                        swSketchSegVert = (SketchSegment)swSketchCurrLine;
                        functionReturnValue = true;
                        return functionReturnValue;
                    }
                }
            }
            // Try to get the first point
            functionReturnValue = GetSketchPoint(swApp, swModel, swSketch, swSketchPtVert);
            return functionReturnValue;
        }

        public bool FindHorizontalOrigin(SldWorks swApp, ModelDoc2 swModel, Sketch swSketch, SketchSegment swSketchSegHoriz, SketchPoint swSketchPtHoriz)
        {
            bool functionReturnValue = false;
            SketchLine[] vSketchLineArr = null;
            SketchLine vSketchLine = null;
            SketchLine swSketchCurrLine = default(SketchLine);
            SketchPoint swStartPt = default(SketchPoint);
            SketchPoint swEndPt = default(SketchPoint);

            // Try to get first horizontal line
            vSketchLineArr = (SketchLine[])GetAllSketchLines(swApp, swModel, swSketch);
            if ((vSketchLineArr != null))
            {
                foreach (SketchLine vSketchLine_loopVariable in vSketchLineArr)
                {
                    vSketchLine = (SketchLine)vSketchLine_loopVariable;
                    swSketchCurrLine = (SketchLine)vSketchLine;
                    swStartPt = (SketchPoint)swSketchCurrLine.GetStartPoint2();
                    swEndPt = (SketchPoint)swSketchCurrLine.GetEndPoint2();
                    if (Math.Abs(swStartPt.Y - swEndPt.Y) < nTolerance)
                    {
                        swSketchSegHoriz = (SketchSegment)swSketchCurrLine;
                        functionReturnValue = true;
                        return functionReturnValue;
                    }
                }
            }
            // Try to get the first point
            functionReturnValue = GetSketchPoint(swApp, swModel, swSketch, swSketchPtHoriz);
            return functionReturnValue;
        }

        public int AutoDimensionSketch(SldWorks swApp, ModelDoc2 swModel, Sketch swSketch)
        {
            int functionReturnValue = 0;
            Feature swFeat = default(Feature);
            SketchSegment swSketchSegHoriz = null;
            SketchPoint swSketchPtHoriz = null;
            SketchSegment swSketchSegVert = null;
            SketchPoint swSketchPtVert = null;
            SketchManager swSketchMgr = null;
            bool bRet = false;

            if (false == FindHorizontalOrigin(swApp, swModel, swSketch, swSketchSegHoriz, swSketchPtHoriz))
            {
                functionReturnValue = (int)swAutodimStatus_e.swAutodimStatusDatumLineNotHorizontal;
                return functionReturnValue;
            }
            if (false == FindVerticalOrigin(swApp, swModel, swSketch, swSketchSegVert, swSketchPtVert))
            {
                functionReturnValue = (int)swAutodimStatus_e.swAutodimStatusDatumLineNotVertical;
                return functionReturnValue;
            }
            swFeat = (Feature)swSketch;
            bRet = swFeat.Select2(false, 0);
            // Editing sketch clears selections
            swModel.EditSketch();
            // Reselect sketch segments for autodimensioning
            if ((swSketchSegVert != null))
            {
                // Vertical line is for horizontal datum
                bRet = swSketchSegVert.Select4(true, null);
            }
            else if ((swSketchPtHoriz != null))
            {
                bRet = swSketchPtHoriz.Select4(true, null);
            }
            else if ((swSketchPtVert != null))
            {
                // Use any sketch point for horizontal datum
                bRet = swSketchPtVert.Select4(true, null);
            }
            if ((swSketchSegHoriz != null))
            {
                // Horizontal line is for vertical datum
                bRet = swSketchSegHoriz.Select4(true, null);
            }
            else if ((swSketchPtVert != null))
            {
                bRet = swSketchPtVert.Select4(true, null);
            }
            else if ((swSketchPtHoriz != null))
            {
                // Use any sketch point for vertical datum
                bRet = swSketchPtHoriz.Select4(true, null);
            }
            // No straight lines, probably contains circles,
            // so use sketch points for datums
            if ((GetAllSketchLines(swApp, swModel, swSketch) == null))
            {
                if ((swSketchPtHoriz != null))
                {
                    bRet = swSketchPtHoriz.Select4(false, null);
                }
                else if ((swSketchPtVert != null))
                {
                    bRet = swSketchPtVert.Select4(false, null);
                }
            }
            functionReturnValue = swSketch.AutoDimension2((int)swAutodimEntities_e.swAutodimEntitiesAll, (int)swAutodimScheme_e.swAutodimSchemeBaseline, (int)swAutodimHorizontalPlacement_e.swAutodimHorizontalPlacementBelow, (int)swAutodimScheme_e.swAutodimSchemeBaseline, (int)swAutodimVerticalPlacement_e.swAutodimVerticalPlacementLeft);
            // Redraw so dimensions are displayed
            swModel.GraphicsRedraw2();
            // Exit sketch mode
	    swSketchMgr = swModel.SketchManager;
            swSketchMgr.InsertSketch(false);
            return functionReturnValue;

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
