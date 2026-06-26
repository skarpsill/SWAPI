---
title: "Get Ruled-Surface Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Ruled_Surface_Feature_Data_Example_VBNET.htm"
---

# Get Ruled-Surface Feature Data Example (VB.NET)

This example shows how to get ruled-surface feature data.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open a part document that contains a ruled-surface feature.
' 2. Select the ruled-surface feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the type of ruled-surface feature.
' 2. Examine the Immediate window.
'------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Dim swModel As ModelDoc2

	    Dim swFeat As Feature

	    Dim swSelMgr As SelectionMgr

	    Dim swRuledSurfFeat As RuledSurfaceFeatureData

	    Sub main()

	        swModel = swApp.ActiveDoc

	        swSelMgr = swModel.SelectionManager

	        swFeat = swSelMgr.GetSelectedObject6(1, -1)

	        swRuledSurfFeat = swFeat.GetDefinition

	        ' Ruled-surface feature type as
	defined in swRuledSurfaceType_e

	        Debug.Print("Ruled-surface
	feature type: " & swRuledSurfFeat.Type)

	    End Sub

	    Public swApp As SldWorks

	End Class
```
