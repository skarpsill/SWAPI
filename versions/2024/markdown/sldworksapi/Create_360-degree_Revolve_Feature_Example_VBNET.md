---
title: "Create 360-degree Revolve Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_360-degree_Revolve_Feature_Example_VBNET.htm"
---

# Create 360-degree Revolve Feature Example (VB.NET)

## Create 360 ° Revolve Feature Example (VB.NET)

This example shows how to create a 360° revolve feature.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a part document that contains Axis1
'    and Sketch1 features; Sketch1 must be a rectangle and Axis1
'    must have been created using an edge on the rectangle.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a 360° revolve feature.
' 2. Examine the Immediate window, graphics area, and FeatureManager
'    design tree.
'---------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Dim swModel As ModelDoc2

	    Dim swModelDocExt As ModelDocExtension

	    Dim swFeatMgr As FeatureManager

	    Dim swFeat As Feature

	    Dim swRevolveFeat As RevolveFeatureData2

	    Dim boolstatus As Boolean

	    Sub main()

	        swModel = swApp.ActiveDoc

	        swModelDocExt = swModel.Extension

	        boolstatus = swModelDocExt.SelectByID2("Axis1", "AXIS", 0, 0, 0, False,
	16, Nothing,
	0)

	        boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH",
	0, 0, 0, True,
	0, Nothing,
	0)

	        swFeatMgr = swModel.FeatureManager

	        swFeat = swFeatMgr.FeatureRevolve2(True, True, False, False, False, False, 0,
	0, 6.2831853071796, 0, False, False,
	0.01, 0.01, 0, 0, 0, True, True, True)

	        swModel.ViewZoomtofit2()

	        swRevolveFeat = swFeat.GetDefinition

	        ' Set the type of revolve as
	defined in swRevolveType_e

	        Debug.Print("Revolve feature type
	before setting to 5: " & swRevolveFeat.Type)

	        swRevolveFeat.Type = 5

	        boolstatus = swFeat.ModifyDefinition(swRevolveFeat, swModel, Nothing)

	        Debug.Print("Revolve feature type after setting to 5: " & swRevolveFeat.Type)

	    End Sub

	    Public swApp As SldWorks

	End Class
```
