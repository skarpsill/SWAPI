---
title: "Insert Sheet Metal Hem Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Sheet_Metal_Hem_Example_VBNET.htm"
---

# Insert Sheet Metal Hem Example (VB.NET)

This example shows how to insert a hem into a sheet metal part.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a sheet metal part.
' 2. Select the edge to which you can add a hem.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Adds an open hem with a custom relief of type Obround and
'    a relief ratio of 1.0.
' 2. Gets the hem type.
' 3. Examine the Immediate window and graphics area.
' ---------------------------------------------------------------------------

		Imports SolidWorks.Interop.sldworks

		Imports SolidWorks.Interop.swconst

		Imports System.Runtime.InteropServices

		Imports System

		Imports System.Diagnostics

		Partial Class SolidWorksMacro

		    Dim Part As ModelDoc2

		    Dim CBAObject As CustomBendAllowance

		    Dim myFeature As Feature

		    Dim myHem As HemFeatureData

		    Sub main()

		        Part = swApp.ActiveDoc

		        CBAObject = Part.FeatureManager.CreateCustomBendAllowance()

		        CBAObject.Type = 2

		        CBAObject.KFactor = 0.5

		        ' Insert an open hem of custom
		relief type Obround and relief ratio 1.0

		        myFeature =
		Part.FeatureManager.InsertSheetMetalHem2(swHemTypes_e.swHemTypeOpen, swHemPositionTypes_e.swHemPositionTypeOutside, False, 0.01,
		0.01, 0, 0.005, 0.0011, CBAObject, False, swSheetMetalReliefTypes_e.swSheetMetalReliefObround, 0, True, 1.0#, 0,
		0)

		        Part.ClearSelection2(True)

		        myHem = myFeature.GetDefinition

		        Debug.Print("Hem type as
		defined in swHemTypes_e: " & myHem.Type)

		    End Sub

		    Public swApp As SldWorks

		End Class
```
