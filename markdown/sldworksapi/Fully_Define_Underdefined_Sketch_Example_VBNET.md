---
title: "Fully Define Under Defined Sketch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fully_Define_Underdefined_Sketch_Example_VBNET.htm"
---

# Fully Define Under Defined Sketch Example (VB.NET)

This example shows how to fully define an under defined sketch.

```
'---------------------------------------------------------------------------
' Preconditions: Open a part document containing an under defined sketch.
'
' Postconditions:
' 1. Fully defines the under defined sketch.
' 2. Open the sketch to verify.
'---------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Sub main()

	        Dim swModel As ModelDoc2

	        Dim swFeature As Feature

	        Dim bValue As Boolean

	        Dim swSketchManager As SketchManager

	        Dim swModelExtension As ModelDocExtension

	        Dim lStatus As Integer

	        Dim lMarkHorizontal As Integer

	        Dim lMarkVertical As Integer

	        Dim swSelectionManager As SelectionMgr

	        swModel = swApp.ActiveDoc

	        swModelExtension = swModel.Extension

	        swSketchManager = swModel.SketchManager

	        swSelectionManager = swModel.SelectionManager

	        swModel.ClearSelection2(True)

	        ' These are the marks expected for
	the dimension datums

	        lMarkHorizontal = 2

	        lMarkVertical = 4

	        swFeature = swModel.FirstFeature

	        Do While (Not (swFeature Is Nothing))

	            If (swFeature.GetTypeName = "ProfileFeature") Then

	                Exit Do

	            End If

	            swFeature = swFeature.GetNextFeature

	        Loop

	        If (Not (swFeature Is Nothing)) Then

	            bValue = swFeature.Select2(False,
	0)

	            swSketchManager.InsertSketch(False)

	            ' OR together the marks for the
	vertical and horizontal datums;

	            '
	You cannot select the same point twice with different marks

	            bValue = swModelExtension.SelectByID2("Point1@Origin", "EXTSKETCHPOINT",
	0, 0, 0, False, lMarkHorizontal Or lMarkVertical, Nothing,
	0)
            lStatus = swSketchManager.FullyDefineSketch(True, True, swSketchFullyDefineRelationType_e.swSketchFullyDefineRelationType_Vertical Or swSketchFullyDefineRelationType_e.swSketchFullyDefineRelationType_Horizontal, True, 1, Nothing, 1, Nothing, 1,
	1)

	            swSketchManager.InsertSketch(True)

	        End If

	    End Sub

	    Public swApp As SldWorks

	End Class
```
