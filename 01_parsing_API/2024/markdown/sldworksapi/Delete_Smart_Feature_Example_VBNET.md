---
title: "Delete a Smart Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Smart_Feature_Example_VBNET.htm"
---

# Delete a Smart Feature Example (VB.NET)

This example shows how to delete a feature from a Smart Component.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\holecube.sldprt.
' 2. Expand the Smart Feature and Features folders to verify that
'    Features contains two extrusion features.
'
' Postconditions:
' 1. Deletes one extrusion feature from the Features folder.
' 2. Expand the Smart Feature and Features folders to verify that
'    Features contains one extrusion feature.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'---------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Dim featMgr As FeatureManager

	    Dim myFeature As Feature

	    Dim swTrainAss As ModelDoc2

	    Dim swSmartPart As ModelDoc2

	    Dim swSCFD As SmartComponentFeatureData

	    Dim selMgr As SelectionMgr

	    Dim feat As Feature

	    Dim feats As Object

	    Dim obj As Object

	    Dim i As Long

	    Dim count As Long

	    Dim boolstatus As Boolean

	    Sub main()

	        swSmartPart = swApp.ActiveDoc

	        featMgr = swSmartPart.FeatureManager

	        feats = featMgr.GetFeatures(True)

	        count = featMgr.GetFeatureCount(True)

	        For i = 0 To count - 1

	            myFeature = feats(i)

	            If myFeature.Name = "Smart Feature" Then

	                Debug.Print(myFeature.Name)

	                swSCFD = myFeature.GetDefinition

	                ' Open the training
	assembly of the Smart Component

	                '
	Open the SmartComponent PropertyManager page to access its selection lists

	                boolstatus = swSCFD.AccessSelections(True)

	                swTrainAss = swApp.ActiveDoc

	                selMgr = swTrainAss.SelectionManager

	                Debug.Print("Number of
	features: " & selMgr.GetSelectedObjectCount2(swSmartComponentSelectionTypes_e.swSmartComponentFeatures))

	                Debug.Print("Number of
	components: " & selMgr.GetSelectedObjectCount2(swSmartComponentSelectionTypes_e.swSmartComponentComponents))

	                ' Get the first extrusion
	from the features selection list

	                obj = selMgr.GetSelectedObject6(1, swSmartComponentSelectionTypes_e.swSmartComponentFeatures)

	                feat = obj

	                ' To delete an extrusion
	feature from a Smart Component,

	                '
	re-select it in the Smart Features selection list

	                boolstatus = feat.Select2(True, swSmartComponentSelectionTypes_e.swSmartComponentFeatures)

	                ' Modify the definition of
	the Smart Feature,

	                '
	close the training assembly, and rebuild the Smart Component

	                boolstatus = myFeature.ModifyDefinition(swSCFD, swSmartPart, Nothing)

	            End If

	        Next

	    End Sub

	    Public swApp As SldWorks

	End Class
```
