---
title: "Get Loft's Pick Points Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Loft's_Pick_Points_Example_VBNET.htm"
---

# Get Loft's Pick Points Example (VB.NET)

## Get and Set Loft's Pick Points Example (VB.NET)

This example shows how to get and set the pick points of a loft feature.

```vb
 '-----------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part that contains a loft.
 ' 2. Open the Immediate window.
 ' 3. Select the loft feature.
 '
 ' Postconditions:
 ' 1. New loft pick points are set.
 ' 2. Examine the part and the Immediate window to verify.
 '-----------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Diagnostics
 Imports System.Runtime.InteropServices

 Partial Class SolidWorksMacro

     Private swModel As ModelDoc2
     Private swSelMgr As SelectionMgr
     Private swFeat As Feature
     Private swFeatData As LoftFeatureData
     Private swMathPoint As MathPoint
     Private newMathPoint As MathPoint()
     Private pointArray As Double()
     Private pickPointData As [Object]()
     Private pointVar As [Object]
     Private pointData As [Object]()
     Private newChains As [Object]()
     Private selCount As Integer
     Private numberOfChains As Integer
     Private newCount As Integer

     Public Sub Main()

         swModel = DirectCast(swApp.ActiveDoc, ModelDoc2)
         swSelMgr = DirectCast(swModel.SelectionManager, SelectionMgr)
         selCount = swSelMgr.GetSelectedObjectCount()
         If selCount <> 1 Then
             System.Windows.Forms.MessageBox.Show("Select the loft feature and rerun the macro.")
             Return
         End If

         swFeat =  DirectCast(swSelMgr.GetSelectedObject6(1, -1), Feature)
         swFeatData = DirectCast(swFeat.GetDefinition(), LoftFeatureData)

         ' Get the loft's pick points
         newCount = 0
         pickPointData = DirectCast(swFeatData.PickPoints, [Object]())
         numberOfChains = pickPointData.GetUpperBound(0) + 1
         newChains = New [Object](numberOfChains - 1) {}
         Debug.Print("No. of chains = " & numberOfChains)
         Debug.Print("")

         For chainCount As Integer = pickPointData.GetLowerBound(0) To pickPointData.GetUpperBound(0)
             pointData = DirectCast(pickPointData(chainCount), [Object]())
             Dim numOfPointInEachChain As Integer = pointData.GetUpperBound(0) + 1

             Dim newPoints As MathPoint() = New MathPoint(numOfPointInEachChain - 1) {}
             Debug.Print("Chain = " & chainCount & ", Number of points = " & numOfPointInEachChain)
             For pointCount As Integer = pointData.GetLowerBound(0) To pointData.GetUpperBound(0)
                 swMathPoint = DirectCast(pointData(pointCount), MathPoint)
                 pointVar = swMathPoint.ArrayData
                 pointArray = DirectCast(pointVar, [Double]())
                 newPoints(pointCount) = swMathPoint
                 Debug.Print("X = " & CDbl(pointArray(0)) * 1000 & " Y = " & CDbl(pointArray(1)) * 1000 & " Z = " & CDbl(pointArray(2)) * 1000)

                 newCount = newCount + 1
             Next
             newChains(chainCount) = newPoints
             Debug.Print("")
             numPoints = numOfPointInEachChain
         Next

         ' Change the loft pick points, rotating them to create a twist
         Dim tmpPoints As MathPoint() = DirectCast(newChains(newChains.GetUpperBound(0)), MathPoint())
         Dim objPrev As MathPoint = tmpPoints(numPoints - 1)
         Dim chainArr As [Object]() = New [Object](newChains.GetUpperBound(0)) {}
         For chainCount As Integer = newChains.GetLowerBound(0) To newChains.GetUpperBound(0)
             Dim newPoints As MathPoint() = DirectCast(newChains(chainCount), MathPoint())
             Dim tmp As MathPoint = newPoints(numPoints - 1)
             newPoints(numPoints - 1) = objPrev
             objPrev = tmp

             Dim newPointWrapArray As DispatchWrapper() = DirectCast(ObjectArrayToDispatchWrapperArray(newPoints), DispatchWrapper())
             chainArr(chainCount) = newPointWrapArray
         Next

         ' Set the loft's new pick points
         Dim status As [Boolean] = False
         status = swFeatData.AccessSelections(swModel, Nothing)
         swFeatData.PickPoints = chainArr

         status = swFeat.ModifyDefinition(swFeatData, swModel,  Nothing)
         Debug.Print("Loft's pick points were modified: " & status)
         Debug.Print("")

         ' Get the loft's pick points
         newCount = 0
         pickPointData = DirectCast(swFeatData.PickPoints, [Object]())
         numberOfChains = pickPointData.GetUpperBound(0) + 1
         Debug.Print("No. of chains = " & numberOfChains)
         Debug.Print("")
         For chainCount As Integer = pickPointData.GetLowerBound(0) To pickPointData.GetUpperBound(0)
             pointData = DirectCast(pickPointData(chainCount), [Object]())
             Dim numOfPointInEachChain As Long = pointData.GetUpperBound(0) + 1
             Array.Resize(newMathPoint, CInt((numberOfChains * numOfPointInEachChain) - 1) + 1)
             Debug.Print("Chain = " & chainCount & ", Number of points = " & numOfPointInEachChain)
             For pointCount As Integer = pointData.GetLowerBound(0) To pointData.GetUpperBound(0)
                 swMathPoint = DirectCast(pointData(pointCount), MathPoint)
                 pointVar = swMathPoint.ArrayData
                 newMathPoint(newCount) = swMathPoint
                 newMathPoint(newCount).ArrayData = pointVar
                 pointArray = DirectCast(pointVar, [Double]())
                 Debug.Print("X = " & CDbl(pointArray(0)) * 1000 & " Y = " & CDbl(pointArray(1)) * 1000 & " Z = " & CDbl(pointArray(2)) * 1000)
                 newCount = newCount + 1
             Next
             Debug.Print("")
         Next
     End Sub

     Public Function ObjectArrayToDispatchWrapperArray(ByVal SwObjects As Object()) As DispatchWrapper()
         Dim arraySize As Integer = 0
         arraySize = SwObjects.GetUpperBound(0)
         Dim dispwrap As DispatchWrapper() = New DispatchWrapper(arraySize) {}
         Dim arrayIndex As Integer = 0
         For arrayIndex = 0 To arraySize
             dispwrap(arrayIndex) = New DispatchWrapper(SwObjects(arrayIndex))
         Next
         Return dispwrap
     End Function

     Public swApp As SldWorks
     Public numPoints As Integer

 End Class
```
