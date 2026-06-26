---
title: "Get Shut-Off Surface Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Shut-Off_Surface_Data_Example_VBNET.htm"
---

# Get Shut-Off Surface Data Example (VB.NET)

This example shows how to get a shut-off surface feature's data.

```
'----------------------------------------------------------------------------
' Preconditions: Open a model that contains a Shut-Off Surface1 feature with
' the patch type of swShutOffSurfacePatchType_e.swPatchTypeTangent = 2.
'
' Postconditions:
' 1. Gets Shut-Off Surface1 data.
' 2. Gets the tangent faces for the specified loops where to create the patches.
' 3. Creates the patches on the opposite tangent faces.
' 4. Examine the graphic area and Immediate window.
'----------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Dim swModel As ModelDoc2

	    Dim swModelDocExt As ModelDocExtension

	    Dim swSelMgr As SelectionMgr

	    Dim swFeat As Feature

	    Dim swFeatData As ShutOffSurfaceFeatureData

	    Dim swEnt As Entity

	    Dim params As Object

	    Dim boolstatus As Boolean

	    Dim i As Integer

	    Dim j As Integer

	    Sub main()

	        swModel = swApp.ActiveDoc

	        swModelDocExt = swModel.Extension

	        swSelMgr = swModel.SelectionManager

	        boolstatus = swModelDocExt.SelectByID2("Shut-Off
	Surface1", "REFSURFACE",
	0, 0, 0, False,
	0, Nothing, swSelectOption_e.swSelectOptionDefault)

	        swFeat = swSelMgr.GetSelectedObject6(1, -1)

	        swFeatData = swFeat.GetDefinition

	        boolstatus = swFeatData.AccessSelections(swModel, Nothing)

	        Debug.Print("Status = " + CStr(swFeatData.Status))

	        Debug.Print("Knit flag = " + CStr(swFeatData.Knit))

	        Debug.Print("Edge count = " + CStr(swFeatData.GetEdgeCount))

	        Debug.Print("Loop count = " + CStr(swFeatData.GetLoopCount))

	        For i = 0 To swFeatData.GetLoopCount - 1

	            Debug.Print("Loop(" + CStr(i) + ")")

	            Debug.Print("    Edge count =
	" + CStr(swFeatData.GetLoopEdgeCount(i)))

	            Debug.Print("    Patch type =
	" + CStr(swFeatData.LoopPatchType(i)))

	            params = swFeatData.LoopEdges(i)

	            For j = 0 To UBound(params)

	                swEnt = params(j)

	                boolstatus = swEnt.Select4(False, Nothing)

	            Next j

	        Next i

	        params = swFeatData.Edges

	        For i = 0 To UBound(params)

	            swEnt = params(i)

	            boolstatus = swEnt.Select4(False, Nothing)

	            swEnt = swFeatData.GetFaceTangentTo(i)

	            If Not swEnt Is Nothing Then

	                boolstatus = swEnt.Select4(True, Nothing)

	            End If

	            swFeatData.FlipFaceTangentTo(i)

	            swEnt = swFeatData.GetFaceTangentTo(i)

	            If Not swEnt Is Nothing Then

	                boolstatus = swEnt.Select4(True, Nothing)

	            End If

	            swFeatData.FlipFaceTangentTo(i)

	        Next i

	        boolstatus = swFeat.ModifyDefinition(swFeatData, swModel, Nothing)

	    End Sub

	    Public swApp As SldWorks

	End Class
```
