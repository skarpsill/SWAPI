---
title: "Insert Coordinate System Feature at Center of Mass Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Coordinate_System_Feature_at_Center_of_Mass_Example_VB.htm"
---

# Insert Coordinate System Feature at Center of Mass Example (VBA)

This example shows how to insert a coordinate system feature on the
center of mass.

'------------------------------------------------------- ' Preconditions: ' 1. Open a part or assembly. ' 2. Open the Immediate window. ' ' Postconditions: ' 1. Inserts a 3D sketch at the center of mass. ' 2. Inserts a coordinate system at center of mass. ' 3. Examine the graphics area and the Immediate window. '------------------------------------------------------- Option Explicit Sub main()

```vb
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swApp kadov_tag{{</spaces>}}As SldWorks.SldWorks
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModel kadov_tag{{</spaces>}}As SldWorks.ModelDoc2
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swFeatMgr kadov_tag{{</spaces>}}As SldWorks.FeatureManager
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModDocExt kadov_tag{{</spaces>}}As SldWorks.ModelDocExtension
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swMass kadov_tag{{</spaces>}}As SldWorks.MassProperty
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vCofG kadov_tag{{</spaces>}}As Variant
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vXaxis kadov_tag{{</spaces>}}As Variant
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vYAxis kadov_tag{{</spaces>}}As Variant
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vZAxis kadov_tag{{</spaces>}}As Variant
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSkCofG kadov_tag{{</spaces>}}As SldWorks.SketchPoint
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSkXaxis kadov_tag{{</spaces>}}As SldWorks.SketchLine
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSkYaxis kadov_tag{{</spaces>}}As SldWorks.SketchLine
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSkSegXaxis kadov_tag{{</spaces>}}As SldWorks.SketchSegment
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSkSegYaxis kadov_tag{{</spaces>}}As SldWorks.SketchSegment
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSelMgr kadov_tag{{</spaces>}}As SldWorks.SelectionMgr
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSelData kadov_tag{{</spaces>}}As SldWorks.SelectData
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swFeat kadov_tag{{</spaces>}}As SldWorks.Feature
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swCoordSys kadov_tag{{</spaces>}}As SldWorks.CoordinateSystemFeatureData
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swComp kadov_tag{{</spaces>}}As SldWorks.Component2
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim bRet kadov_tag{{</spaces>}}As Booleankadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swApp = Application.SldWorks
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = swApp.ActiveDoc
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSelMgr = swModel.SelectionManager
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSelData = swSelMgr.CreateSelectData
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModDocExt = swModel.Extension

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swMass = swModDocExt.CreateMassProperty
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vCofG = swMass.CenterOfMass
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vXaxis = swMass.PrincipleAxesOfInertia(0)
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vYAxis = swMass.PrincipleAxesOfInertia(1)
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vZAxis = swMass.PrincipleAxesOfInertia(2)
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swModel.Insert3DSketch2 False
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swModel.SetAddToDB True
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSkCofG = swModel.CreatePoint2(vCofG(0), vCofG(1), vCofG(2))
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSkXaxis = swModel.CreateLine2(kadov_tag{{</spaces>}}vCofG(0), vCofG(1), vCofG(2),  kadov_tag{{</spaces>}}vCofG(0) + vXaxis(0), vCofG(1) + vXaxis(1), vCofG(2) + vXaxis(2))
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSkYaxis = swModel.CreateLine2( kadov_tag{{</spaces>}} vCofG(0), vCofG(1), vCofG(2), kadov_tag{{</spaces>}}vCofG(0) + vYAxis(0), vCofG(1) + vYAxis(1), vCofG(2) + vYAxis(2))
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSkSegXaxis = swSkXaxis
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSkSegYaxis = swSkYaxis
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swModel.SetAddToDB False
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swModel.Insert3DSketch2 True
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swModel.ClearSelection2 True
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swSelData.Mark = 1
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}bRet = swSkCofG.Select4(True, swSelData): Debug.Assert bRet
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swSelData.Mark = 2
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}bRet = swSkSegXaxis.Select4(True, swSelData): Debug.Assert bRet
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swSelData.Mark = 4
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}bRet = swSkSegYaxis.Select4(True, swSelData): Debug.Assert bRet
 kadov_tag{{<spaces>}}
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Insert the coordinate system feature, get the feature, and modify it, using the feature data
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swFeatMgr = swModel.FeatureManager
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swFeat = swFeatMgr.InsertCoordinateSystem(False, False, False)
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If swFeat Is Nothing Then
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Did not get coordinate system feature."
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Else
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swCoordSys = swFeat.GetDefinition
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bRet = swCoordSys.AccessSelections(swModel, swComp)kadov_tag{{<spaces>}}
 kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "XFlipped? " & swCoordSys.XFlipped
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swCoordSys.XFlipped = Truekadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the origin entity
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim gvx As Variant
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vxCount As Long
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Long
       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the origin entity
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim entType As Long
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim geo kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}As Object
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim oent As SldWorks.Entity
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim skpnt As SldWorks.SketchPoint
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set geo = swCoordSys.OriginEntity

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Is it an entity?
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If TypeOf geo Is Entity Then
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set oent = geo
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}entType = geo.GetType
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print "Entity type: " & entType
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print "Is sketch point."
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set skpnt = geo
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If Not skpnt Is Nothing Then
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print "Got sketch point."
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim xEnt As Object
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vxCount = swCoordSys.GetXAxisEntitiesCount
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}gvx = swCoordSys.XAxisEntities
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Find out about the x axis entities
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim skent As SldWorks.SketchSegment
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To UBound(gvx)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set xEnt = gvx(i)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If TypeOf xEnt Is SketchSegment Then
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Set skent = xEnt
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}entType = skent.GetType
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print "Entity type: " & entType
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next ikadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bRet = swFeat.ModifyDefinition(swCoordSys, swModel, Nothing)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swCoordSys.ReleaseSelectionAccess

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Ifkadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
```
