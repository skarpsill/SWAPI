---
title: "Get Fixed Face of Flatten-Bends Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Fixed_Face_of_Flatten-Bends_Feature_Example_VBNET.htm"
---

# Get Fixed Face of Flatten-Bends Feature Example (VB.NET)

This example shows how to get the fixed face of a flatten-bends feature.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open a sheet metal part.
' 2. Select a Process-Bends feature in the FeatureManager design
'    tree.
'
' Postconditions:
' 1. Rolls the FeatureManager design tree back to the feature
'    that contains the fixed face of the Process-Bends feature.
' 2. Selects the fixed face of the Process-Bends feature.
' 3. Examine the FeatureManager design tree and graphics area,
'    then press F5.
' 4. Rolls the FeatureManager design tree forward.
'------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

Sub main()

	Dim swModel As ModelDoc2
	Dim swSelMgr As SelectionMgr
	Dim swFeat As Feature
	Dim swBends As BendsFeatureData
	Dim swFace As Face2
	Dim swEntity As Entity
	Dim bRet As Boolean

	swModel = swApp.ActiveDoc
	swSelMgr = swModel.SelectionManager
	swFeat = swSelMgr.GetSelectedObject6(1, -1)
	swBends = swFeat.GetDefinition

	' Roll back to access the Process-Bends feature data
	bRet = swBends.AccessSelections(swModel, Nothing)
	swFace = swBends.GetFixedFace
	swEntity = swFace
	bRet = swEntity.Select4(False, Nothing)

	Stop
	' Press F5

	' Cancel any changes made
	swBends.ReleaseSelectionAccess()

End Sub
```

```
	Public swApp As SldWorks

End Class
```
