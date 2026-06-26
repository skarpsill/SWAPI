---
title: "Get Surface Trim Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Surface_Trim_Feature_Data_Example_VBNET.htm"
---

# Get Surface Trim Feature Data Example (VB.NET)

```vb
This example shows how to get surface trim feature data.
```

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a part document with a surface trim feature.
' 2. Select the surface trim feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the type of surface trim feature.
' 2. Examine the Immediate window.
'---------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Dim swModel As ModelDoc2

	    Dim swSelMgr As SelectionMgr

	    Dim swFeat As Feature

	    Dim swSurfTrimFeat As SurfaceTrimFeatureData

	    Dim surftrimtype As Integer

	    Sub main()

	        swModel = swApp.ActiveDoc

	        swSelMgr = swModel.SelectionManager

	        swFeat = swSelMgr.GetSelectedObject6(1, -1)

	        swSurfTrimFeat = swFeat.GetDefinition

	        surftrimtype = swSurfTrimFeat.GetType

	        Debug.Print("Surface trim type (swSurfaceTrimType_e):
	" & surftrimtype)

	    End Sub

	    Public swApp As SldWorks

	End Class
```
