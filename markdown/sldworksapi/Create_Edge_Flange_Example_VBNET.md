---
title: "Create Edge Flange Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Edge_Flange_Example_VBNET.htm"
---

# Create Edge Flange Example (VB.NET)

This example shows how to create a sheet metal edge flange.

```vb
  '-----------------------------------------------------
 ' Preconditions: Open install_dir\samples\tutorial\sheetmetal\formtools\cover.sldprt.
 '
 ' Postconditions: Creates Edge-Flange1 in the FeatureManager design tree.
  '------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial   Class   SolidWorksMacro
       Public  Sub main()

           Dim swModel  As  ModelDoc2
           Dim bValue  As  Boolean
           Dim swEdge  As  Edge
           Dim dAngle  As  Double
           Dim dLength  As  Double
           Dim swFeature   As   Feature
           Dim swEntity  As  Entity
           Dim swSketch  As  Sketch
           Dim vSketchSegments(0)   As   Object
           Dim swSketchLine   As   SketchLine
           Dim swStartPoint   As   SketchPoint
           Dim swEndPoint   As   SketchPoint
           Dim dSize  As  Double
           Dim dFactor1  As  Double
           Dim dFactor2  As  Double
           Dim aFlangeEdges(0)   As   Edge
           Dim vFlangeEdges(0)   As   Object
           Dim aSketchFeats(0)   As   Sketch
           Dim vSketchFeats(0)   As   Object
           Dim FeatData  As  EdgeFlangeFeatureData
           Dim edgeFlangeFeat   As   Feature
           Dim PBendData   As   CustomBendAllowance

          swModel = swApp.ActiveDoc

           ' Flange angle
          dAngle = (90.0# / 180.0#) * 3.1415926535897

           ' Flange length
          dLength = 0.02

          swModel.ShowNamedView2("*Back", -1)
          swModel.ViewZoomtofit2

           ' Select edge for which to create the edge flange
          bValue = swModel.Extension.SelectByRay(0.0353852695288734, 0.0527495553160953, 0.0485267999999905, 0, 0, 1, 0.000283299018635423, 1,   False, 0, 0)
          swEdge = swModel.SelectionManager.GetSelectedObject6(1, -1)

           ' Insert a sketch of the edge flange profile
          swFeature = swModel.InsertSketchForEdgeFlange(swEdge, dAngle,   False)
          bValue = swFeature.Select2(False, 0)

          swModel.EditSketch
          swSketch = swModel.GetActiveSketch2

          swEntity = swEdge

           ' Select edge
          bValue = swEntity.Select4(False,   Nothing)

           ' Use the edge in the sketch
          bValue = swModel.SketchManager.SketchUseEdge(False)

           ' Get the created sketch line
          vSketchSegments = swSketch.GetSketchSegments
          swSketchLine = vSketchSegments(0)

           ' Get start and end point
          swStartPoint = swSketchLine.GetStartPoint2
          swEndPoint = swSketchLine.GetEndPoint2

           ' Create additional lines to define sketch

           ' Set parameters defining the sketch geometry
          dSize = swEndPoint.X - swStartPoint.X
          dFactor1 = 0.1
          dFactor2 = 1.25

           ' Add directly and do not display to speed things up
          swModel.SetAddToDB(True)
          swModel.SetDisplayWhenAdded(False)

          swModel.CreateLine2(swStartPoint.X, swStartPoint.Y, 0#, swStartPoint.X, swStartPoint.Y + dLength, 0#)
          swModel.CreateLine2(swStartPoint.X, swStartPoint.Y + dLength, 0#, swStartPoint.X + dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0#)
          swModel.CreateLine2(swStartPoint.X + dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0#, swEndPoint.X - dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0#)
          swModel.CreateLine2(swEndPoint.X - dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0#, swEndPoint.X, swEndPoint.Y + dLength, 0#)
          swModel.CreateLine2(swEndPoint.X, swEndPoint.Y, 0#, swEndPoint.X, swEndPoint.Y + dLength, 0#)

          swModel.SetDisplayWhenAdded(True)
          swModel.SetAddToDB(False)

           ' Commit changes made to the sketch
          swModel.InsertSketch2(True)

           ' Insert the edge flange

          aFlangeEdges(0) = swEdge
          aSketchFeats(0) = swSketch

          vFlangeEdges = aFlangeEdges
          vSketchFeats = aSketchFeats

          FeatData = swModel.FeatureManager.CreateDefinition(swFeatureNameID_e.swFmEdgeFlange)

           Call FeatData.AddEdges(vFlangeEdges, vSketchFeats)

          FeatData.UseDefaultBendRadius =   False
          FeatData.BendRadius = 0.0007366
          FeatData.GapDistance = 0.001
          FeatData.BendAngle = dAngle
          FeatData.LockAngle =   True
          FeatData.OffsetType =   swFlangeOffsetTypes_e.swFlangeOffsetBlind
          FeatData.OffsetDistance = dLength
          FeatData.OffsetDimType =   swFlangeDimTypes_e.swFlangeDimTypeInnerVirtualSharp
          FeatData.PositionType =   swFlangePositionTypes_e.swFlangePositionTypeMaterialInside
          FeatData.UsePositionOffset =   True
          FeatData.PositionOffsetType =   swFlangeOffsetTypes_e.swFlangeOffsetBlind
          FeatData.PositionOffsetDistance = 0.01
          FeatData.UseDefaultBendAllowance =   False
          PBendData = FeatData.GetCustomBendAllowance
          PBendData.KFactor = 0.5
          PBendData.Type =   swBendAllowanceTypes_e.swBendAllowanceDeduction
          FeatData.SetCustomBendAllowance(PBendData)
          FeatData.UseDefaultBendRelief =   False
          FeatData.UseReliefRatio =   True
          FeatData.ReliefRatio = 0.5
          FeatData.AutoReliefType =   swSheetMetalReliefTypes_e.swSheetMetalReliefTear
          FeatData.ReliefTearType =   swReliefTearTypes_e.swReliefTearTypeRip

          edgeFlangeFeat = swModel.FeatureManager.CreateFeature(FeatData)

       End  Sub
       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```
