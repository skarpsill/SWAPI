---
title: "Get Fixed Face of Flat-Pattern Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Fixed_Face_of_Flat-Pattern_Feature_Example_VBNET.htm"
---

# Get Fixed Face of Flat-Pattern Feature Example (VB.NET)

This example shows how to get the fixed face of a Flat-Pattern feature.

```
'----------------------------------------------------------------------------
' Preconditions: Open a sheet metal part and select a Flat-Pattern feature.
'
' Postconditions:
' 1. Inspect the graphics area to see that the fixed face
'    of the Flat-Pattern feature is selected.
' 2. Press F5 to run the macro to completion.
'----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

	Sub main()

	   Dim swModel As ModelDoc2
	   Dim swSelMgr As SelectionMgr
	   Dim swFeat As Feature
	   Dim swFlatPatt As FlatPatternFeatureData
	   Dim swFixedFace As Face2
	   Dim swFixedFaceEntity As Entity
	   Dim bRet As Boolean

	   swModel = swApp.ActiveDoc
	   swSelMgr = swModel.SelectionManager
	   swFeat = swSelMgr.GetSelectedObject6(1, -1)

	   swFlatPatt = swFeat.GetDefinition
	   bRet = swFlatPatt.AccessSelections(swModel, Nothing)

	   swFixedFace = swFlatPatt.FixedFace2
	   swFixedFaceEntity = swFixedFace
	   bRet = swFixedFaceEntity.Select4(True, Nothing)

	   Stop
           ' Press F5

	   swFlatPatt.ReleaseSelectionAccess()

	End Sub

	Public swApp As SldWorks

End Class
```
