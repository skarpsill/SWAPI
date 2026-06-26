---
title: "Get and Set Loft's Pick Points Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Loft's_Pick_Points_Example_CSharp.htm"
---

# Get and Set Loft's Pick Points Example (C#)

This example shows how to get and set the pick points of a loft feature.

```vb
 //----------------------------------------------------------
 // Preconditions:
 // 1. Open a part that contains a loft.
 // 2. Open the Immediate window.
 // 3. Select the loft feature.
 //
 // Postconditions:
 // 1. New loft pick points are set.
 // 2. Examine the part and Immediate window to verify.
 //
 //----------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 using System.Runtime.InteropServices;

 namespace GetPickPointsLoft_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SelectionMgr swSelMgr;
         Feature swFeat;
         LoftFeatureData swFeatData;
         MathPoint swMathPoint;
         MathPoint[] newMathPoint;
         double[] pointArray;
         Object[] pickPointData;
         Object pointVar;
         Object[] pointData;
         Object[] newChains;
         int selCount;
         int numberOfChains;
         int newCount;

         public void Main()
         {

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             selCount = swSelMgr.GetSelectedObjectCount();
             if (selCount != 1)
             {
                 System.Windows.Forms.MessageBox.Show("Select the loft feature and rerun the macro.");
                 return;
             }

             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swFeatData = (LoftFeatureData)swFeat.GetDefinition();

             // Get the loft's pick points
             newCount = 0;
             pickPointData = (Object[])swFeatData.PickPoints;
             numberOfChains = pickPointData.GetUpperBound(0) + 1;
             newChains = new Object[numberOfChains];
             Debug.Print("No. of chains = " + numberOfChains);
             Debug.Print("");

             for (int chainCount = pickPointData.GetLowerBound(0); chainCount <= pickPointData.GetUpperBound(0); chainCount++)
             {
                 pointData = (Object[])pickPointData[chainCount];
                 int numOfPointInEachChain = pointData.GetUpperBound(0) + 1;

                 MathPoint[] newPoints = new MathPoint[numOfPointInEachChain];
                 Debug.Print("Chain = " + chainCount +  ", Number of points = " + numOfPointInEachChain);
                 for (int pointCount = pointData.GetLowerBound(0); pointCount <= pointData.GetUpperBound(0); pointCount++)
                 {
                     swMathPoint = (MathPoint)pointData[pointCount];
                     pointVar = swMathPoint.ArrayData;
                     pointArray = (Double[])pointVar;
                     newPoints[pointCount] = swMathPoint;
                     Debug.Print("X = " + (double)pointArray[0] * 1000 + " Y = " + (double)pointArray[1] * 1000 + " Z = " + (double)pointArray[2] * 1000);

                     newCount = newCount + 1;
                 }
                 newChains[chainCount] = newPoints;
                 Debug.Print("");
                 numPoints = numOfPointInEachChain;
             }

             // Change the loft pick points, rotating them to create a twist
             MathPoint[] tmpPoints = (MathPoint[])newChains[newChains.GetUpperBound(0)];
             MathPoint objPrev = tmpPoints[numPoints - 1];
             Object[] chainArr = new Object[newChains.GetUpperBound(0) + 1];
             for (int chainCount = newChains.GetLowerBound(0); chainCount <= newChains.GetUpperBound(0); chainCount++)
             {
                 MathPoint[] newPoints = (MathPoint[])newChains[chainCount];
                 MathPoint tmp = newPoints[numPoints - 1];
                 newPoints[numPoints - 1] = objPrev;
                 objPrev = tmp;

                 DispatchWrapper[] newPointWrapArray = (DispatchWrapper[])ObjectArrayToDispatchWrapperArray(newPoints);
                 chainArr[chainCount] = newPointWrapArray;
             }

             // Set the loft's new pick points
             Boolean status = false;
             status = swFeatData.AccessSelections(swModel,  null);
             swFeatData.PickPoints = chainArr;

             status = swFeat.ModifyDefinition(swFeatData, swModel, null);
             Debug.Print("Loft's pick points were modified: " + status);
             Debug.Print("");

             // Get the loft's pick points
             newCount = 0;
             pickPointData = (Object[])swFeatData.PickPoints;
             numberOfChains = pickPointData.GetUpperBound(0) + 1;
             Debug.Print("No. of chains = " + numberOfChains);
             Debug.Print("");
             for (int chainCount = pickPointData.GetLowerBound(0); chainCount <= pickPointData.GetUpperBound(0); chainCount++)
             {
                 pointData = (Object[])pickPointData[chainCount];
                 long numOfPointInEachChain = pointData.GetUpperBound(0) + 1;
                 Array.Resize(ref newMathPoint, (int)((numberOfChains * numOfPointInEachChain) - 1) + 1);
                 Debug.Print("Chain = " + chainCount +  ", Number of points = " + numOfPointInEachChain);
                 for (int pointCount = pointData.GetLowerBound(0); pointCount <= pointData.GetUpperBound(0); pointCount++)
                 {
                     swMathPoint = (MathPoint)pointData[pointCount];
                     pointVar = swMathPoint.ArrayData;
                     newMathPoint[newCount] = swMathPoint;
                     newMathPoint[newCount].ArrayData = pointVar;
                     pointArray = (Double[])pointVar;
                     Debug.Print("X = " + (double)pointArray[0] * 1000 + " Y = " + (double)pointArray[1] * 1000 + " Z = " + (double)pointArray[2] * 1000);
                     newCount = newCount + 1;
                 }
                 Debug.Print("");
             }
         }

         public DispatchWrapper[] ObjectArrayToDispatchWrapperArray(object[] SwObjects)
         {
             int arraySize = 0;
             arraySize = SwObjects.GetUpperBound(0);
             DispatchWrapper[] dispwrap = new DispatchWrapper[arraySize + 1];
             int arrayIndex = 0;
             for (arrayIndex = 0; arrayIndex <= arraySize; arrayIndex++)
             {
                 dispwrap[arrayIndex] = new DispatchWrapper(SwObjects[arrayIndex]);
             }
             return dispwrap;
         }

         public SldWorks swApp;
         public int numPoints;

     }
 }
```
