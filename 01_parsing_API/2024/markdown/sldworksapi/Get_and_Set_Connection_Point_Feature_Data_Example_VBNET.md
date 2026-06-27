---
title: "Get and Set Connection Point Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Connection_Point_Feature_Data_Example_VBNET.htm"
---

# Get and Set Connection Point Feature Data Example (VB.NET)

This example shows how to get and set data for connection point features.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Ensure that the latest SOLIDWORKS Design Library is loaded.
 ' 2.   Drag and drop design library > routing > electrical > db9 male.sldprt
 '      into the main view.
 ' 3.   Observe CPoint1 in the FeatureManager design tree.
 ' 4. Run (F5) this macro.
 '
 ' Postconditions:
 '  1. Inspect the Immediate Window.
 '  2.   CPoint1 is now MyCPoint in the FeatureManager design tree.
 '
 ' NOTE:  Because this is a Design Library part, close it without saving changes.
 '---------------------------------------------------------------------------
```

```vb
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim Part As ModelDoc2
         Dim selMgr As SelectionMgr
         Dim selCount As Long
         Dim selType As Long
         Dim selObj As Object
         Dim selFeat As Feature = Nothing
         Dim vLocation As Object
         Dim xLoc As Double, yLoc As Double, zLoc As Double
         Dim vDirection As Object
         Dim xDir As Double, yDir As Double, zDir As Double
         Dim boolstatus As Boolean

         Part = swApp.ActiveDoc
         selMgr = Part.SelectionManager

         boolstatus = Part.Extension.SelectByID2("CPoint1", "CONNECTIONPOINT", 0, 0, 0, False, 0, Nothing, 0)

         selCount = selMgr.GetSelectedObjectCount2(-1)
         If (selCount > 0) Then
             selType = selMgr.GetSelectedObjectType3(1, -1)
             selObj = selMgr.GetSelectedObject6(1, -1)
             If (selType = swSelectType_e.swSelCONNECTIONPOINTS)  Then
                 selFeat = selObj
             End If
         End If

         Part.ClearSelection2(True)

         Dim featData As Object = Nothing
         If Not IsNothing(selFeat) Then
             featData = selFeat.GetDefinition()
         End If
         Dim cPointData As IConnectionPointFeatureData
         cPointData = featData

         If Not cPointData Is Nothing Then
             Debug.Print("Get stublength = " & cPointData.StubLength)
             cPointData.StubLength = 0.009
             Debug.Print("Set stublength = " & cPointData.StubLength)

             Debug.Print("Get diameter = " & cPointData.RouteDiameter)
             cPointData.RouteDiameter = 0.011
             Debug.Print("Set diameter = " & cPointData.RouteDiameter)

             Debug.Print("Get route type = " & cPointData.RouteType)
             cPointData.RouteType = 2
             Debug.Print("Set route type = " & cPointData.RouteType)

             Debug.Print("Get route sub type = " & cPointData.RouteSubType)
             cPointData.RouteSubType = 3
             Debug.Print("Set route sub type = " & cPointData.RouteSubType)

             Debug.Print("Get electrical Pin ID = " & cPointData.ElectricalPinID)
             cPointData.ElectricalPinID =  "zxc"
             Debug.Print("Set electrical Pin ID = " & cPointData.ElectricalPinID)

             Debug.Print("Get port ID = " & cPointData.PortID)
             cPointData.PortID = "newPortID"
             Debug.Print("Set port ID = " & cPointData.PortID)

             Debug.Print("Get CPoint name = " & cPointData.Name2)
             cPointData.Name2 = "myCPoint"
             Debug.Print("Set CPoint name = " & cPointData.Name2)

             vLocation = cPointData.Location
             xLoc = vLocation(0)
             yLoc = vLocation(1)
             zLoc = vLocation(2)
             Debug.Print("Get location: " & xLoc & " " & yLoc & " " & zLoc)

             vDirection = cPointData.Direction
             xDir = vDirection(0)
             yDir = vDirection(1)
             zDir = vDirection(2)
             Debug.Print("Get direction vector: " & xDir & " " & yDir & " " & zDir)

         End If
         Part.ForceRebuild3(false)
         cPointData =  Nothing
         featData =  Nothing
     End Sub

     Public swApp As SldWorks

 End  Class
```
